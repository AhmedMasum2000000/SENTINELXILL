---
name: strategy-frameworks
description: 'Run a classic strategy framework — SWOT, PESTLE, Porter''s Five Forces, or Ansoff Matrix — where every cell cites a real customer-evidence or market-context result instead of generic filler. Use when the user says ''do a SWOT'', ''PESTLE analysis'', ''Porter''s five forces'', ''Ansoff matrix'', ''strategic assessment'', ''analyze our competitive position'', or ''macro environment''. Trigger terms: SWOT, PESTLE, Porter''s five forces, Ansoff matrix, competitive forces, strategic analysis, macro environment, growth options. Not for product specs or roadmaps.'
category: Strategy & Vision
tags:
- frameworks
- swot
- analysis
---

# Strategy Frameworks (SWOT · PESTLE · Porter's · Ansoff)

Run one of four classic frameworks — but grounded. The failure mode of these frameworks is generic filler ("Strength: strong brand"). Here, **every cell must cite an Evermuse `evidence` or `context` result**, or it doesn't go in the grid. A SWOT where each weakness is a customer complaint with a quote is worth ten brainstormed ones.

## Step 0 — Relevance & availability
Confirm this is strategic-analysis work and Evermuse is connected. If not, produce a framework-only grid labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md` Step 0.

## Pick the framework
Ask the user (or infer from their ask) which to run, and load the matching reference:
- **SWOT** — internal strengths/weaknesses × external opportunities/threats → `references/swot.md`
- **PESTLE** — macro-environment scan (Political/Economic/Social/Technological/Legal/Environmental) → `references/pestle.md`
- **Porter's Five Forces** — industry structural attractiveness → `references/porters-five-forces.md`
- **Ansoff Matrix** — growth options across product × market → `references/ansoff.md`

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

You are a strategic analyst applying the chosen framework to **$ARGUMENTS**. Open the relevant `references/*.md` for the full cell definitions and output process, then:
1. Populate each cell **only** with items you can tie to an evidence or context result — no filler.
2. Mark each customer-derived cell with its quote/source; mark each market cell with its context source.
3. Cross-reference for strategic insight (e.g. SWOT: leverage strengths against opportunities; Porter's: which force is most binding), and end with 3–5 grounded recommendations, each traceable to the cells that motivated it.

Where the source frameworks reach for "market context / competitor data / customer feedback (optional)," use Evermuse `evidence` (customer voice) and `context` (market) as the **primary** sources for every cell.

## Deliverable format
The framework grid (table or quadrants) with an inline citation badge in every populated cell, then the cross-referenced recommendations (links live inline — no Sources footer). If a cell has no supporting evidence or context, leave it explicitly empty and note it as a research gap rather than inventing content.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT), merging its `swot-analysis`, `pestle-analysis`, `porters-five-forces`, and `ansoff-matrix` skills; grounding is Evermuse-native.
- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
