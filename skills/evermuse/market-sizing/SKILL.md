---
name: market-sizing
description: 'Estimate market size (TAM, SAM, SOM) with top-down and bottom-up approaches, grounded in market/industry signals and validated against a real customer beachhead. Use when the user says ''how big is the market'', ''what''s our TAM'', ''size this opportunity'', ''estimate the addressable market'', ''prep market size for the pitch'', or is evaluating market entry. Trigger terms: market size, TAM, SAM, SOM, addressable market, market opportunity, market sizing, beachhead. Not for internal usage/revenue analytics of an existing product.'
category: Market & Competition
tags:
- tam-sam-som
- market-sizing
- analysis
---

# Market Sizing (TAM / SAM / SOM)

Estimate the opportunity with defensible top-down and bottom-up numbers — and, crucially, ground the **wedge** (which slice you actually win first) in real customer evidence. Most market-sizing decks are context-only guesses; the Evermuse edge is proving the beachhead is real with customers who already want it.

This is the showcase skill for **nature=context**: the market numbers come from external/industry signals, and customer evidence is used to *validate the wedge*, not to size the whole market.

## Step 0 — Relevance & availability
Confirm this is a market-opportunity question and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, produce the sizing framework labeled **⚠ ungrounded** (external numbers still possible via web research, but the wedge won't be evidence-validated) and tell the user to authorize the MCP.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

Size the market for **$ARGUMENTS** within the stated constraints (geography, vertical, customer type).

1. **Market definition** — the problem space, segment boundaries, geography, scoping decisions.
2. **TAM** — top-down (industry total → relevant slice, cite sources) *and* bottom-up (customers × price × frequency) to cross-validate; reconcile the two.
3. **SAM** — the portion realistically serviceable given product, channels, language, pricing tier; as a % of TAM with reasoning.
4. **SOM** — achievable share in 1-3 years given competitive position and GTM capacity; **this is where the customer wedge validates the number** — if evidence shows a hot beachhead, cite it as the basis for near-term obtainability.
5. **Growth projection** — 2-3 year evolution and the drivers/trends behind it.
6. **Assumptions & risks** — numbered, each with a confidence level (high/med/low) and how to validate it.

### Summary table

```markdown
| Metric | Current estimate | 2-3 yr projection | Basis |
|--------|------------------|-------------------|-------|
| TAM | | | [external source] |
| SAM | | | product/channel constraints |
| SOM | | | GTM capacity + evidenced wedge [`1`](URL) |
```

### Wedge validation (the Evermuse differentiator)
A short block: **which slice do we win first, and who in the corpus already wants it?** 1-2 verbatim quotes proving urgency:
```markdown
> "[verbatim quote showing pull/urgency]" — [Name], [Meeting], [Date] [`1`](URL)
```

Close with **key assumptions & risks**, keeping market sources and customer evidence clearly separated via inline citations. Be explicit about what's data vs. estimate, and where confidence intervals are wide.

---
### Further reading
- TAM/SAM/SOM method adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT); wedge-validation grounding is Evermuse-native. See [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques).
