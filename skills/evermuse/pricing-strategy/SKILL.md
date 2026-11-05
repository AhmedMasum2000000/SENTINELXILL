---
name: pricing-strategy
description: 'Design pricing and monetization grounded in real willingness-to-pay signals, pricing objections, and value language from customer evidence — with competitor pricing as a labeled secondary input. Use when the user says ''how should we price this'', ''pricing strategy'', ''what should we charge'', ''pricing tiers'', ''how do we monetize'', ''freemium vs paid'', or ''raise our prices''. Trigger terms: pricing, pricing strategy, monetization, willingness to pay, price point, tiers, freemium, revenue model, what to charge. Not for full business-model canvases.'
category: Growth & GTM
tags:
- pricing
- monetization
- packaging
---

# Pricing & Monetization Strategy

Recommend a pricing model and structure, or brainstorm 3–5 monetization options, anchored in what customers actually said about price — their willingness-to-pay signals, objections, and the value they name. Competitor pricing is a secondary check, not the anchor. Value-based pricing built on customer quotes beats guessing from competitor screenshots.

## Step 0 — Relevance & availability
Confirm this is pricing/monetization work and Evermuse is connected. If not, produce a framework-only recommendation labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md` Step 0.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

You are a pricing strategist for **$ARGUMENTS**. Ground everything in value delivered and evidenced willingness to pay.

### A) Pricing strategy (default)
1. **Value delivered** — core value prop; the customer's alternative and its cost; quantifiable outcome (time saved, revenue gained, cost cut); **WTP from evidence, quoted**.
2. **Pick a model** — Flat-rate · Per-seat · Usage-based · Tiered · Freemium · Freemium+usage · Value-based. Recommend the best fit and say why, in terms of the value metric customers care about.
3. **Competitive pricing (secondary)** — map competitor tiers via `list_competitors`/`get_competitor_capabilities` + `context`; place your product (premium / mid / budget); find gaps. Label secondary.
4. **Structure** — 2–4 tiers with clear differentiation; feature-gate on value metrics (not arbitrary limits); pick the value metric (seats, events, storage, API calls); anchor the popular tier; ~15–20% annual discount.
5. **Price sensitivity** — Van Westendorp if survey data exists; otherwise estimate from evidenced WTP + competitor pricing. Surface pricing objections from evidence as the sensitivity signal.
6. **Experiments** — pricing-page A/Bs, founder-led sales conversations, landing-page anchor tests, conversion cohort analysis.

### B) Monetization brainstorm (when the user wants options, not one answer)
Generate 3–5 distinct models (Freemium, Subscription, Usage-based, Seat-based, One-time, Marketplace fee, Ads). For each: how it works for *this* product · audience fit (grounded in evidence) · unit economics (CAC/LTV/break-even) · risks · competitive position (context, secondary) · a low-cost validation experiment with a success metric. Recommend 1–2 to test first.

Where the source method reaches for "web search / competitor pricing / survey files," use Evermuse `evidence` (WTP, objections, value language) as the **primary** source; competitor pricing and market context are **secondary**.

## Deliverable format

```markdown
# Pricing Recommendation — [product]

**Recommended model:** [model] · **Value metric:** [unit]
*Grounded in WTP:* > "[quote about price/value]" — [attribution] [`1`](URL)

| Tier | Price | Target segment | Key features | Positioning |
|---|---|---|---|---|

**Objections heard (sensitivity signal):** [cited [`2`](URL)]
**Competitor pricing (secondary):** [table] — via list_competitors/context
**Assumptions → tests:** [assumption] → [experiment]
**Risks → mitigations:** …
```

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT), merging its `pricing-strategy` and `monetization-strategy` skills; grounding is Evermuse-native.
- [Product Pricing Strategies 101](https://www.productcompass.pm/p/product-pricing-strategies-101)
