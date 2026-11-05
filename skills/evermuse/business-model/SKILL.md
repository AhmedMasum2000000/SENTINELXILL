---
name: business-model
description: 'Build a Business Model Canvas — all 9 blocks — with the problem and customer-segment boxes grounded in real customer evidence and the channel/competition boxes grounded in market context. Use when the user says ''business model'', ''business model canvas'', ''how do we make money'', ''model this venture'', ''lean canvas'', ''startup canvas'', or ''map our business''. Trigger terms: business model, business model canvas, BMC, lean canvas, startup canvas, how we make money, revenue streams, cost structure. Not for detailed pricing tiers — use pricing-strategy for that.'
category: Growth & GTM
tags:
- business-model
- canvas
- monetization
---

# Business Model Canvas

Generate a Business Model Canvas whose value-creation side (problem, value prop, customer segments) is anchored in real customer evidence, and whose delivery side (channels, relationships, competition) is anchored in market context. A canvas built on quotes and market signal beats one built on assumptions. Lean Canvas and Startup Canvas are available as alternate templates in `references/`.

## Step 0 — Relevance & availability
Confirm this is business-model work and Evermuse is connected. If not, produce a framework-only canvas labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md` Step 0.

## Pick the template
- **Business Model Canvas (default, below):** established businesses, corporate strategy, investor materials.
- **Lean Canvas** → `references/lean-canvas.md`: fast hypothesis testing for a new venture.
- **Startup Canvas** → `references/startup-canvas.md`: new products needing strategic clarity *and* a business model (recommended for early-stage). Ask the user which fits if ambiguous; default to BMC.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

You are a business-model strategist building a canvas for **$ARGUMENTS**. Create, deliver, capture value — and make the blocks reinforce each other.

### The 9 blocks
**Creating value:** 1. Key Partners · 2. Key Activities · 3. Key Resources.
**Center:** 4. **Value Propositions** — the problems solved and needs met. **Grounded in cited evidence.**
**Delivering value:** 5. Customer Relationships (context) · 6. Channels — awareness → purchase → delivery → after-sales (context) · 7. **Customer Segments** — mass/niche/segmented; defining characteristics. **Grounded in cited evidence.**
**Financial viability:** 8. Cost Structure (fixed vs. variable; cost- vs. value-driven) · 9. Revenue Streams (per customer/transaction/subscription; pricing mechanism).

### Output process
1. Profile customer segments from evidence.
2. Define the value proposition(s) from cited pains.
3. Map relationships and channels from context.
4. List key activities, resources, partners.
5. Outline cost structure and revenue streams.
6. Align all 9 blocks; test economic viability (LTV > 3× CAC).
7. Surface key assumptions and risks with the cheapest test for each.

Where the source reaches for "current operations / assumptions," use Evermuse `evidence` for the problem and segment boxes and `context` for channel/competition boxes as the primary sources.

## Deliverable format
A labeled 9-block canvas (markdown table or bulleted blocks), with inline citation badges on the value-prop, segment, channel, and competition boxes (links live inline — no Sources footer). End with the LTV/CAC sanity check and the top 3 assumptions to test.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT); grounding is Evermuse-native.
- [Business Model Canvas Examples: Google Maps, Airbnb, Uber](https://www.productcompass.pm/p/business-model-canvas-examples)
- [Startup Canvas](https://www.productcompass.pm/p/startup-canvas)
