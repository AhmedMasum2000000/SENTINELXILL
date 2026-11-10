"""Virality scraper: ranks short-form videos for given keywords by views and engagement.

Source: YouTube search via yt-dlp (no API key needed). TikTok and Instagram data come from
Claude's Firecrawl connector (scrapecreators provider) and are saved to research_tiktok_*.json.

Usage:
  pip install yt-dlp
  python3 scripts/scrape_virality.py "afro house" "down in bossa" "bossa nova house" --limit 25
Output: research_youtube_<date>.json and a printed top-20 leaderboard.
"""
import argparse
import datetime as dt
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def yt_search(query: str, limit: int) -> list[dict]:
    raw = subprocess.run(
        ["yt-dlp", "--flat-playlist", "-J", f"ytsearch{limit}:{query} shorts"],
        capture_output=True, text=True, timeout=180, check=True,
    ).stdout
    rows = []
    for e in json.loads(raw).get("entries") or []:
        rows.append({
            "query": query,
            "title": e.get("title"),
            "channel": e.get("channel") or e.get("uploader"),
            "views": e.get("view_count") or 0,
            "duration_s": e.get("duration"),
            "is_short": "/shorts/" in (e.get("url") or ""),
            "url": e.get("url"),
        })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("queries", nargs="+")
    ap.add_argument("--limit", type=int, default=25)
    a = ap.parse_args()

    rows = []
    for q in a.queries:
        try:
            rows += yt_search(q, a.limit)
        except Exception as exc:  # keep going if one query fails
            print(f"[warn] {q}: {exc}")
    rows = list({r["url"]: r for r in rows}.values())  # same video can match several queries
    rows.sort(key=lambda r: -r["views"])
    out = ROOT / f"research_youtube_{dt.date.today()}.json"
    out.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(f"Saved {len(rows)} rows -> {out}\n")
    for r in rows[:20]:
        print(f"{r['views']:>12,}  {str(r['duration_s']):>6}s  {r['title'][:80]}")


if __name__ == "__main__":
    main()
