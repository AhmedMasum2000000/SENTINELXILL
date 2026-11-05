# FITq™ Scoring Rubric

**Used by:** `optise-helix-fitq-audit` (primary).
**Source:** Optise EU AEO Playbook, Section 5 (FITq™ — How AI Search Selects Sources).
**Trademark:** FITq™ is an Optise framework. Always use the trademark on first mention.

The FITq framework scores a webpage on 4 signals. Each signal is scored 0-25, totalling 100. The rubric below is what makes the scoring repeatable across pages and skills.

---

## Signal 1 — Findability (0-25)

**Definition:** Can AI search engines fetch, render, and read this page reliably?

### Scoring criteria

| Score | Criteria |
|---|---|
| **25 (perfect)** | Page renders fully in HTML on first byte (no JS gating). Mobile load time <1.5s. Page <1MB. Crawler-friendly headers (200 OK, no aggressive rate limiting on bots). Canonical tag present. |
| **20** | Renders in HTML but >2s mobile load time. Or page >1.5MB. Or canonical missing. |
| **15** | Critical content (the BLUF, the answer block, the proof) is in HTML, but some supporting content (FAQs, comparison tables) requires JS to render. |
| **10** | The page loads but key content is JS-gated. Crawlers see a shell. |
| **5** | The page is heavily script-dependent. First-paint is empty. Crawlers see almost nothing. |
| **0** | Page returns an error (4xx, 5xx), is behind auth/paywall, or robots.txt blocks bots. |

### What to detect (technical)
- HTTP status (200 vs others)
- `Content-Type` header
- First-paint HTML content size (raw vs rendered)
- Time to first byte (TTFB)
- `<link rel="canonical">` presence
- Robots.txt or meta robots blocking
- Page total size in MB
- Whether key heading/body content is in raw HTML or only in `<script type="application/json">`

### Common failure modes
- Next.js / React app where everything is `<div id="root"></div>` until JS runs
- Cloudflare aggressive bot challenges that block GPTBot, ClaudeBot, PerplexityBot
- Pages over 5MB (Googlebot crawls only first 15MB but other bots cap lower)
- Login walls on pricing pages

---

## Signal 2 — Intent Match (0-25)

**Definition:** Does this page answer the exact question a buyer would ask AI engines, with the buyer's own phrasing?

### Scoring criteria

| Score | Criteria |
|---|---|
| **25 (perfect)** | Page H1 mirrors a real buyer prompt verbatim. The opening 40-60 words directly answer the question. Page stays on the single decision topic. URL slug matches the prompt intent. Title tag contains the question form. |
| **20** | H1 closely matches a buyer prompt. Opening answers the question within 100 words. Page is on-topic but covers 1-2 adjacent topics. |
| **15** | H1 is descriptive but not in question form. Page is roughly on-topic but the answer is buried below the fold or after marketing fluff. |
| **10** | H1 is generic/brand-led. Page covers the topic but mixes in unrelated content. Answer takes 3+ scrolls to find. |
| **5** | Page is brand-led ("Why we built X") rather than buyer-question-led. The actual buyer question is never explicitly answered. |
| **0** | Page is entirely off-topic. Or it's a homepage trying to answer a specific decision question. |

### What to detect (content)
- H1 text vs target prompt (cosine similarity or exact match)
- Position of the answer to the prompt (first paragraph, first 100 words, first scroll, below fold)
- Whether `<h2>` headings are question-style or descriptive
- Topic drift (does the page wander into adjacent topics?)
- URL slug content
- Title tag content

### Common failure modes
- "About [Tool]" pages trying to answer "best tool for X"
- Blog posts written for SEO with the keyword in the title but the answer 800 words down
- Homepage trying to be every page
- Product pages that lead with positioning instead of the buyer's question

---

## Signal 3 — Trust (0-25)

**Definition:** Does this page have the credibility signals AI engines use to filter risky or stale sources?

### Scoring criteria

| Score | Criteria |
|---|---|
| **25 (perfect)** | Visible "Last updated" date within 90 days. Named author with bio link. Every quantitative claim has a linked source. Author is a real person with verifiable credentials. Page is consistent with the brand's third-party footprint (G2, Capterra, Wikipedia, Reddit). |
| **20** | Last updated date present and within 90 days. Named author. Most claims sourced. Some third-party consistency. |
| **15** | Date present but stale (>90 days, <365 days). Author present but unnamed or generic ("The X Team"). Claims partially sourced. |
| **10** | No visible date OR no author. Sources missing on key claims. |
| **5** | Stale, anonymous, unsourced. Page reads like marketing copy with no accountability. |
| **0** | Page has factual errors, conflicting claims with the brand's other pages, or makes unverifiable absolute claims ("the #1", "the best", "the only"). |

### What to detect (content)
- Presence and date of "Last updated" / "Updated on" / "Last reviewed"
- Author byline (named person vs "Team" vs none)
- Number of `<a href>` links to sources for quantitative claims
- Schema.org markup for `Article`, `Person`, `Organization`
- E-E-A-T signals (experience, expertise, authoritativeness, trustworthiness)

### Common failure modes
- Pages with no date — the single biggest fixable trust gap
- "By [Brand] Team" instead of a named person
- Stats with no source ("Studies show…")
- Marketing copy that uses "first", "leading", "best" without any data

---

## Signal 4 — Quoteability (0-25)

**Definition:** Is the page structured so AI engines can lift a clean, self-contained block of text and cite it without context?

### Scoring criteria

| Score | Criteria |
|---|---|
| **25 (perfect)** | Page uses tables, bullet lists, short definitions, FAQ schema. Each section is a self-contained answer block (heading + 2-4 sentence answer + optional bullets/proof). The opening 40-60 word BLUF is extractable as a single quote. Schema.org markup present (`FAQPage`, `HowTo`, `Article`). |
| **20** | Tables and bullet lists present. Most sections are quotable but a few are wall-of-text paragraphs. Schema partially implemented. |
| **15** | Some structural elements (headings, occasional bullets). Most content is paragraph prose. No schema. |
| **10** | Long-form prose with minimal structure. AI engines have to reach in and extract sentence-by-sentence. |
| **5** | Wall of text. No headings below H1. No bullets, no tables, no breaks. |
| **0** | Content is in images of text, or in PDFs embedded as objects, or in carousels that JS-gate the content. |

### What to detect (structure)
- Number of `<table>`, `<ul>`, `<ol>`, `<dl>` per page
- Average paragraph length (sentences per `<p>`)
- Presence of schema.org markup (`FAQPage`, `HowTo`, `Article`, `Product`)
- Whether the first 40-60 words form a self-contained answer
- Whether headings have answer content immediately below or just lead into more headings

### Common failure modes
- "Hero" sections with one big sentence and a CTA — nothing for AI to quote
- 1500-word paragraphs without bullets
- Comparison content rendered as JS-only carousels instead of HTML tables
- FAQs that are accordion-collapsed without `FAQPage` schema (AI engines may not see the answers)

---

## Total scoring and grade bands

| Total | Grade | Meaning |
|---|---|---|
| 90-100 | **A** | Citation-ready. Likely already being cited by ChatGPT, Perplexity, Gemini for relevant prompts. |
| 75-89 | **B** | Close. Usually 1-2 fixes (often Trust + Quoteability) away from being cited. |
| 60-74 | **C** | Fixable in 1-2 weeks. Usually missing BLUF, last-updated date, or schema. |
| 40-59 | **D** | Major gaps. Likely needs structural rewrite. Probably not cited at all today. |
| 0-39 | **F** | Page is invisible to AI engines. Often a JS-only render or off-topic content. |

---

## Output format requirement

Every FITq audit must produce:
1. **Total score and grade band**
2. **Per-signal breakdown** (4 numbers, each with 1-line justification)
3. **Top 5 fixes ranked by impact** (each with effort estimate: ship-this-week vs ship-this-month)
4. **Before/after diff for the #1 fix** (show the actual HTML/copy change)
5. **A "what's already strong" section** (so the user knows what NOT to break)

This format is non-negotiable. It maps to the 30/60/90 build order in the whitepaper.
