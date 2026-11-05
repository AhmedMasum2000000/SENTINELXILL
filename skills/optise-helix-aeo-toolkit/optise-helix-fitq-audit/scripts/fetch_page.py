#!/usr/bin/env python3
"""
fetch_page.py — Fetch and analyze a webpage for FITq and RACE audits.

Used by:
- optise-helix-fitq-audit
- optise-helix-race-audit (shared via symlink/copy)

Outputs a JSON document containing:
- HTTP status, response headers, redirects
- Raw HTML size, rendered HTML size (best-effort without a real browser)
- Time to first byte (TTFB)
- Detected schema.org markup (counted by type)
- Detected last-updated date (multiple heuristics)
- JS-trapped content detection (raw HTML body length vs total page length)
- Title tag, H1 tags, H2 tags
- Number of tables, lists, FAQ markup
- Word count and average paragraph length
- Outbound link count and source link count for quantitative claims

Usage:
    python fetch_page.py <url>
    python fetch_page.py <url> --json-output  # machine-readable
    python fetch_page.py <url> --html-output  # save raw HTML alongside JSON

Author: Optise + Helix GTM Consulting
"""

import sys
import json
import re
import time
import argparse
import http.client
import ipaddress
import socket
import ssl
from urllib.parse import quote, urljoin, urlsplit
from datetime import datetime, timezone

# These two timeouts are based on real-world observation of B2B SaaS pages.
# Most pages respond in <2s; pages that take longer are usually indicative of
# Findability problems that the FITq audit will catch anyway. 30s is the
# absolute ceiling — beyond this, the page is effectively invisible to AI
# crawlers (per the whitepaper Section 5).
CONNECT_TIMEOUT_SECONDS = 10
READ_TIMEOUT_SECONDS = 30

# Three retries balances reliability vs speed. Most intermittent failures
# resolve by the second retry. Fourth+ retries usually indicate a real outage
# and the audit should report the failure honestly per anti-hallucination rule 3.
MAX_RETRIES = 3

# One honest User-Agent that names this tool. The script never pretends to be
# a browser or an AI crawler (for example ChatGPT-User, GPTBot or ClaudeBot),
# and never switches user agent to get past a block. If a site refuses this
# user agent, that refusal is reported as it is. To check whether AI crawlers
# are allowed, read the site's robots.txt rules for GPTBot, ChatGPT-User,
# ClaudeBot and PerplexityBot instead of impersonating them.
TOOL_VERSION = "1.4.1"
USER_AGENT = (
    f"optise-helix-aeo-toolkit/{TOOL_VERSION} fetch_page.py "
    "(+https://github.com/shashwatgtm/optise-helix-aeo-skills)"
)

# Destination rules. Only web addresses are fetched: file://, ftp:// and other
# schemes are refused. The host name is resolved once, every address must be a
# public internet address (no loopback, private, link-local, reserved, multicast
# or unspecified ranges, no cloud metadata address), and the connection goes to
# that checked address. Every redirect hop is checked the same way. User names
# in the URL, ports other than 80 and 443, and responses that are not HTML are
# refused. Each refusal is reported as an error that starts with "Refused".
ALLOWED_SCHEMES = ("http", "https")
ALLOWED_PORTS = (80, 443)
MAX_REDIRECTS = 5
REDIRECT_STATUSES = (301, 302, 303, 307, 308)
ALLOWED_CONTENT_TYPES = ("text/html", "application/xhtml+xml")

# Largest response body read, in bytes. Bigger pages are cut off and flagged.
MAX_BODY_BYTES = 5 * 1024 * 1024

# Date heuristics, in order of reliability. The first match wins.
DATE_PATTERNS = [
    # ISO datetime in <time datetime="..."> tags — most reliable
    (r'<time[^>]*datetime="([^"]+)"', "time-datetime-attr"),
    # "Last updated: YYYY-MM-DD" or "Updated YYYY-MM-DD"
    (r'(?:last\s*updated|updated\s*on?|last\s*reviewed)\s*[:\-]?\s*'
     r'(\d{4}-\d{2}-\d{2})', "last-updated-iso"),
    # "Last updated: Month DD, YYYY"
    (r'(?:last\s*updated|updated\s*on?|last\s*reviewed)\s*[:\-]?\s*'
     r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{1,2},?\s+\d{4})',
     "last-updated-month"),
    # JSON-LD dateModified field
    (r'"dateModified"\s*:\s*"([^"]+)"', "jsonld-datemodified"),
    # Open Graph article:modified_time
    (r'<meta[^>]+property="article:modified_time"[^>]+content="([^"]+)"',
     "og-modified-time"),
]


class RefusedDestination(ValueError):
    """The URL, or a redirect target, was refused by the destination checks."""


def _refuse(message):
    return RefusedDestination("Refused: " + message)


_NUMERIC_HOST_LABEL = re.compile(r"^(0[xX][0-9a-fA-F]*|[0-9]+)$")
_NAT64_PREFIX = ipaddress.ip_network("64:ff9b::/96")


def build_ssl_context():
    """TLS context that checks the certificate chain and the host name."""
    return ssl.create_default_context()


def _looks_like_numeric_host(host):
    """True for host names made only of numbers, such as 2130706433, 0177.0.0.1,
    0x7f.0.0.1 or 127.1. Some resolvers read these as IPv4 addresses."""
    labels = host.rstrip(".").split(".")
    return all(_NUMERIC_HOST_LABEL.match(label) for label in labels)


def _check_public_ip(ip, host):
    """Raise RefusedDestination unless ip is a public unicast address."""
    candidates = [ip]
    if ip.version == 6:
        if ip.ipv4_mapped is not None:
            candidates = [ip.ipv4_mapped]
        else:
            if ip.sixtofour is not None:
                candidates.append(ip.sixtofour)
            if ip in _NAT64_PREFIX:
                candidates.append(ipaddress.IPv4Address(int(ip) & 0xFFFFFFFF))
    for candidate in candidates:
        if (not candidate.is_global
                or candidate.is_private
                or candidate.is_loopback
                or candidate.is_link_local
                or candidate.is_multicast
                or candidate.is_reserved
                or candidate.is_unspecified):
            who = f"{host} resolves to {ip}, which" if host != str(ip) else f"{host}"
            raise _refuse(
                f"{who} is not a public internet address (loopback, private, "
                "link-local, reserved, multicast or unspecified). Only public "
                "web servers are fetched."
            )


def parse_destination(url):
    """Check one URL (the first one or a redirect target) before any connection.
    Returns (scheme, host, port, request_target)."""
    if any(ord(ch) <= 0x20 or ord(ch) == 0x7F for ch in url):
        raise _refuse("the URL contains spaces or control characters")
    parts = urlsplit(url)
    scheme = parts.scheme.lower()
    if not scheme:
        raise ValueError(f"Invalid URL (missing scheme or host): {url}")
    if scheme not in ALLOWED_SCHEMES:
        raise _refuse(f"only http and https URLs are supported, not {scheme}: {url}")
    if not parts.netloc:
        raise ValueError(f"Invalid URL (missing scheme or host): {url}")
    if "@" in parts.netloc:
        raise _refuse(
            "URLs with a user name or password (user@host) are not allowed: "
            f"{url}"
        )
    try:
        port = parts.port
    except ValueError:
        raise _refuse(f"the port in the URL is not valid: {url}")
    if port is None:
        port = 443 if scheme == "https" else 80
    elif port not in ALLOWED_PORTS:
        raise _refuse(f"port {port} is not allowed, only 80 and 443: {url}")
    host = parts.hostname
    if not host:
        raise ValueError(f"Invalid URL (missing scheme or host): {url}")
    if "%" in host:
        raise _refuse(f"host names with a zone or escape ('%') are not allowed: {url}")
    target = parts.path or "/"
    if parts.query:
        target += "?" + parts.query
    target = quote(target, safe="!#$%&'()*+,/:;=?@[]~")
    return scheme, host, port, target


def resolve_public_addresses(host):
    """Resolve host once and return its addresses (as strings), all checked to be
    public. Raises RefusedDestination if any address is not public."""
    try:
        literal = ipaddress.ip_address(host)
    except ValueError:
        literal = None
    if literal is not None:
        _check_public_ip(literal, host)
        return [str(literal)]
    if _looks_like_numeric_host(host):
        raise _refuse(
            f"{host} is a numeric host in a non-standard form (integer, octal, "
            "hex or short). Use a normal host name or a dotted IPv4 address."
        )
    infos = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)
    addresses = []
    for info in infos:
        text = info[4][0].split("%", 1)[0]
        _check_public_ip(ipaddress.ip_address(text), host)
        if text not in addresses:
            addresses.append(text)
    if not addresses:
        raise socket.gaierror(-2, "Name or service not known")
    return addresses


def _connect_pinned(addresses, port):
    """Connect to one of the already checked addresses. The host name is not
    resolved again, so a changed DNS answer cannot redirect the connection."""
    last_error = None
    for address in addresses:
        try:
            sock = socket.create_connection((address, port), CONNECT_TIMEOUT_SECONDS)
        except OSError as e:
            last_error = e
            continue
        sock.settimeout(READ_TIMEOUT_SECONDS)
        return sock
    raise last_error


class _PinnedHTTPConnection(http.client.HTTPConnection):
    """Connects to a pinned address; the Host header keeps the host name."""

    def __init__(self, host, port, addresses):
        super().__init__(host, port, timeout=READ_TIMEOUT_SECONDS)
        self._pinned_addresses = addresses

    def connect(self):
        self.sock = _connect_pinned(self._pinned_addresses, self.port)


class _PinnedHTTPSConnection(http.client.HTTPSConnection):
    """Connects to a pinned address; TLS SNI and the certificate check use the
    host name from the URL, not the address."""

    def __init__(self, host, port, addresses, context):
        super().__init__(host, port, timeout=READ_TIMEOUT_SECONDS, context=context)
        self._pinned_addresses = addresses
        self._tls_context = context

    def connect(self):
        sock = _connect_pinned(self._pinned_addresses, self.port)
        try:
            self.sock = self._tls_context.wrap_socket(sock, server_hostname=self.host)
        except BaseException:
            sock.close()
            raise


def _fetch_following_redirects(url):
    """One attempt: validate, resolve once, connect to the pinned address, and
    follow at most MAX_REDIRECTS redirects, checking every hop the same way."""
    ua = USER_AGENT
    headers = {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "identity",
        "Connection": "close",
    }
    start_time = time.time()
    current = url
    previous = None
    redirects = 0
    while True:
        try:
            scheme, host, port, target = parse_destination(current)
            addresses = resolve_public_addresses(host)
        except RefusedDestination as e:
            if previous is None:
                raise
            raise RefusedDestination(f"{e} (reached by redirect from {previous})")
        if scheme == "https":
            conn = _PinnedHTTPSConnection(host, port, addresses, build_ssl_context())
        else:
            conn = _PinnedHTTPConnection(host, port, addresses)
        try:
            conn.request("GET", target, headers=headers)
            response = conn.getresponse()
            status = response.status
            location = response.getheader("Location")
            if status in REDIRECT_STATUSES and location and location.strip():
                if redirects >= MAX_REDIRECTS:
                    raise _refuse(
                        f"more than {MAX_REDIRECTS} redirects, stopped at {current}"
                    )
                previous = current
                current = urljoin(current, location.strip())
                redirects += 1
                continue
            if status >= 300:
                # 4xx and 5xx are real responses. Report them as they are. A 401,
                # 403 or 429 can mean the site blocks automated tools; never retry
                # with a different user agent to get around that.
                return {
                    "status": status,
                    "url_final": current,
                    "headers": dict(response.getheaders()),
                    "html": "",
                    "html_size_bytes": 0,
                    "ttfb_ms": int((time.time() - start_time) * 1000),
                    "error": f"HTTPError {status}: {response.reason}",
                    "user_agent_used": ua,
                }
            content_type = response.getheader("Content-Type") or ""
            media_type = content_type.split(";", 1)[0].strip().lower()
            if media_type not in ALLOWED_CONTENT_TYPES:
                shown = content_type if content_type else "missing"
                raise _refuse(
                    f"Content-Type is {shown}, not text/html or "
                    f"application/xhtml+xml, so the response was not read: {current}"
                )
            ttfb_ms = int((time.time() - start_time) * 1000)
            html_bytes = response.read(MAX_BODY_BYTES + 1)
            truncated = len(html_bytes) > MAX_BODY_BYTES
            html_bytes = html_bytes[:MAX_BODY_BYTES]
            return {
                "status": status,
                "url_final": current,  # captures redirects
                "headers": dict(response.getheaders()),
                "html": html_bytes.decode("utf-8", errors="replace"),
                "html_size_bytes": len(html_bytes),
                "ttfb_ms": ttfb_ms,
                "user_agent_used": ua,
                "html_truncated": truncated,
            }
        finally:
            conn.close()


def fetch_with_retries(url, retry=0):
    """Fetch a URL with retries on network errors. Returns dict or raises.
    A refused destination is never retried."""
    while True:
        try:
            return _fetch_following_redirects(url)
        except (OSError, http.client.HTTPException) as e:
            if retry < MAX_RETRIES:
                time.sleep(1 + retry)  # backoff: 1s, 2s, 3s
                retry += 1
                continue
            raise RuntimeError(
                f"URLError on {url} after {MAX_RETRIES} retries: {e}"
            )


def detect_last_updated(html):
    """Try multiple heuristics to find a 'last updated' date. Returns dict."""
    for pattern, source_name in DATE_PATTERNS:
        match = re.search(pattern, html, re.IGNORECASE)
        if match:
            return {
                "found": True,
                "raw_value": match.group(1),
                "source": source_name,
            }
    return {"found": False, "raw_value": None, "source": None}


def detect_schema_markup(html):
    """Detect schema.org markup. Returns dict with counts by type."""
    schema_types = {}
    # JSON-LD blocks
    jsonld_blocks = re.findall(
        r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>',
        html, re.DOTALL,
    )
    for block in jsonld_blocks:
        # Find all "@type" values
        type_matches = re.findall(r'"@type"\s*:\s*"([^"]+)"', block)
        for t in type_matches:
            schema_types[t] = schema_types.get(t, 0) + 1
    # Microdata
    microdata_matches = re.findall(
        r'itemtype="https?://schema\.org/(\w+)"', html
    )
    for t in microdata_matches:
        schema_types[t + "_microdata"] = schema_types.get(t + "_microdata", 0) + 1
    return schema_types


def detect_js_gating(html, html_size_bytes):
    """
    Heuristic: if the body of the rendered HTML is mostly empty or contains
    just a root div + script tags, the page is JS-gated. AI crawlers will
    see almost nothing.
    """
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
    if not body_match:
        return {
            "js_gated": True,
            "reason": "no-body-tag",
            "body_text_chars": 0,
        }
    body_html = body_match.group(1)
    # Strip script and style tags
    body_text_only = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
    body_text_only = re.sub(r'<style[^>]*>.*?</style>', '', body_text_only, flags=re.DOTALL)
    # Strip HTML tags
    body_text_only = re.sub(r'<[^>]+>', ' ', body_text_only)
    body_text_only = re.sub(r'\s+', ' ', body_text_only).strip()

    text_chars = len(body_text_only)

    # Heuristic: if the body has <500 visible text chars but the page is >50KB,
    # the content is almost certainly in JS bundles
    if text_chars < 500 and html_size_bytes > 50000:
        return {
            "js_gated": True,
            "reason": "small-body-large-page",
            "body_text_chars": text_chars,
            "html_size_bytes": html_size_bytes,
        }
    if text_chars < 200:
        return {
            "js_gated": True,
            "reason": "very-small-body",
            "body_text_chars": text_chars,
        }
    return {
        "js_gated": False,
        "body_text_chars": text_chars,
    }


def count_quoteability_features(html):
    """Count the structural features that drive FITq Quoteability score."""
    return {
        "tables": len(re.findall(r'<table[^>]*>', html)),
        "uls": len(re.findall(r'<ul[^>]*>', html)),
        "ols": len(re.findall(r'<ol[^>]*>', html)),
        "dls": len(re.findall(r'<dl[^>]*>', html)),
        "h2": len(re.findall(r'<h2[^>]*>', html)),
        "h3": len(re.findall(r'<h3[^>]*>', html)),
        "paragraphs": len(re.findall(r'<p[^>]*>', html)),
    }


def extract_headings(html):
    """Extract H1 and H2 text content."""
    h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    h2_matches = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
    h1_text = [re.sub(r'<[^>]+>', '', h).strip() for h in h1_matches]
    h2_text = [re.sub(r'<[^>]+>', '', h).strip() for h in h2_matches]
    return {"h1": h1_text, "h2": h2_text}


def extract_title(html):
    """Extract <title> content."""
    match = re.search(r'<title[^>]*>(.*?)</title>', html, re.DOTALL)
    if match:
        return re.sub(r'\s+', ' ', match.group(1)).strip()
    return None


def detect_canonical(html):
    """Detect <link rel='canonical'>."""
    match = re.search(
        r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
        html,
    )
    if match:
        return match.group(1)
    return None


def detect_meta_robots(html):
    """Detect noindex/nofollow meta robots."""
    match = re.search(
        r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)["\']',
        html,
    )
    if match:
        return match.group(1)
    return None


def analyze(url):
    """Run the full analysis on a URL."""
    # fetch_with_retries checks the URL and every redirect hop before connecting.
    fetch_result = fetch_with_retries(url)

    if "error" in fetch_result and fetch_result["html_size_bytes"] == 0:
        # The fetch failed cleanly (4xx/5xx). Report it honestly.
        return {
            "url": url,
            "url_final": fetch_result.get("url_final", url),
            "fetch_status": "failed",
            "http_status": fetch_result["status"],
            "error": fetch_result.get("error"),
            "ttfb_ms": fetch_result["ttfb_ms"],
            "user_agent_used": fetch_result.get("user_agent_used"),
            "blocked_note": (
                "If the status is 401, 403 or 429, the site may be refusing "
                "automated tools. That is a real result: report it, and do "
                "not retry with a browser or AI-crawler user agent."
            ) if fetch_result["status"] in (401, 403, 429) else None,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "anti_hallucination_note": (
                "fetch_page.py could not retrieve content for this URL. "
                "Per skill anti-hallucination rule: do not score a page that "
                "wasn't fetched. Surface this error to the user and request "
                "a screenshot or HTML paste."
            ),
        }

    html = fetch_result["html"]
    html_size = fetch_result["html_size_bytes"]

    schema_types = detect_schema_markup(html)
    last_updated = detect_last_updated(html)
    js_gating = detect_js_gating(html, html_size)
    quoteability = count_quoteability_features(html)
    headings = extract_headings(html)
    title = extract_title(html)
    canonical = detect_canonical(html)
    meta_robots = detect_meta_robots(html)

    return {
        "url": url,
        "url_final": fetch_result["url_final"],
        "fetch_status": "ok",
        "http_status": fetch_result["status"],
        "ttfb_ms": fetch_result["ttfb_ms"],
        "html_size_bytes": html_size,
        "html_size_kb": round(html_size / 1024, 1),
        "user_agent_used": fetch_result["user_agent_used"],
        "html_truncated": fetch_result.get("html_truncated", False),
        "title": title,
        "headings": headings,
        "canonical": canonical,
        "meta_robots": meta_robots,
        "last_updated": last_updated,
        "schema_markup": schema_types,
        "js_gating": js_gating,
        "quoteability_features": quoteability,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "_raw_html": html,  # removed in main() before printing
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch and analyze a webpage for FITq/RACE audits")
    parser.add_argument("url", help="URL to fetch and analyze")
    parser.add_argument("--json-output", action="store_true",
                        help="Output JSON only (machine-readable)")
    parser.add_argument("--html-output", type=str, default=None,
                        help="Save raw HTML to this file")
    args = parser.parse_args()

    try:
        result = analyze(args.url)
    except Exception as e:
        # Per anti-hallucination rule 9: report real errors, never fake data
        error_result = {
            "url": args.url,
            "fetch_status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "anti_hallucination_note": (
                "fetch_page.py raised an exception. Do not proceed to score "
                "this page. Report the error to the user and ask for an "
                "alternative input (HTML paste, screenshot, or different URL)."
            ),
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)

    raw_html = result.pop("_raw_html", None)
    if args.html_output and result.get("fetch_status") == "ok":
        # Save the HTML already fetched, so the site is not requested twice
        try:
            with open(args.html_output, "w", encoding="utf-8") as f:
                f.write(raw_html or "")
        except Exception as e:
            print(f"Warning: failed to save HTML: {e}", file=sys.stderr)

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
