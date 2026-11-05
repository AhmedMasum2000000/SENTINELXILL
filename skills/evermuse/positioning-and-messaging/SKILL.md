---
name: positioning-and-messaging
description: 'Generate differentiated positioning options and campaign/message ideas written in your customers'' own mined vocabulary, where every message maps to a real quote that proves it resonates. Use when the user says ''how should we position this'', ''position the product'', ''differentiate from competitors'', ''write our messaging'', ''brainstorm marketing campaigns'', ''promote the product'', or ''what''s our positioning''. Trigger terms: positioning, positioning statement, messaging, differentiation, value proposition, marketing ideas, campaign ideas, tagline, how to position. Not for a full launch plan — use gtm-strategy for that.'
category: Market & Competition
tags:
- positioning
- messaging
- marketing
---

# Positioning & Messaging

Produce positioning options and campaign/message ideas — but written in the **customer's own mined vocabulary**, not marketer-speak. The Evermuse twist: every positioning angle and every campaign message maps to a verbatim quote that proves real people talk that way and care about that thing. A message you can't attach to a quote is a guess; cut it.

## Step 0 — Relevance & availability
Confirm this is positioning / marketing work and Evermuse is connected. If the tools aren't present, produce framework-only positioning labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md` Step 0.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

You are developing positioning and messaging for **$ARGUMENTS**. Where the source method reaches for "brainstorm from context," use Evermuse `evidence` as the primary source — the customer's actual words — and `context` (competitor positioning) as secondary.

### Part A — Positioning options (differentiated)

**A1. Competitive landscape.** Identify the top competitors (from `context` + `list_competitors` if useful, labeled secondary). For each: their positioning angle, audience focus, differentiators they emphasize, and the gap they leave open.

**A2. Generate 5 positioning options.** Each must be differentiated from competitors, resonate with the mined customer values/needs, emphasize a capability competitors downplay, and claim unclaimed territory. For each, provide:
1. **Positioning statement** — e.g. "The only [category] for [segment] who want to [outcome]" — using the customer's own words for [outcome].
2. **Strategic rationale** — why it resonates and differentiates.
3. **Supporting messages** — reinforcing lines.
4. **Competitive advantage** — the capability that lets you own this claim.
5. **Proof quote** — > "[verbatim]" — [attribution] [`1`](URL). If no quote supports it, the option is speculative — mark it.

### Part B — Campaign / message ideas

Generate **5 creative, cost-effective campaign ideas** to carry the chosen positioning to the target segment. For each:
1. **Channel** — primary channel (content, social, community, partnerships, email…).
2. **Core message** — in mined customer vocabulary.
3. **Why it works** — grounded in a customer quote about what they care about ([`1`](URL)).
4. **Cost efficiency** — what makes it high-impact on a limited budget.

Prioritize high-impact-low-budget and unconventional angles. Every core message must map to a proof quote — that mapping is the whole point.

## Deliverable format

```markdown
# Positioning & Messaging — [product]

## Positioning options
### Option 1 — [name]
**Statement:** [The only … for … who want to …]
**Rationale:** [why]. **Advantage:** [capability]. **Territory:** [unclaimed gap vs [competitor], [`1`](URL)].
**Proof:** > "[verbatim]" — [attribution] [`2`](URL)
… (options 2–5) …

## Campaign ideas
| # | Channel | Core message (mined) | Why it works | Proof quote |
|---|---|---|---|---|
| 1 | [channel] | "[message]" | [reason] | > "[quote]" — [attribution] [`3`](URL) |
```

## Honesty when evidence is thin
If the corpus doesn't yield distinctive customer language, say so — generic phrasing is a signal the positioning isn't validated yet. Flag which messages rest on real quotes vs. which are hypotheses to test.

## Save & hand off
After saving, offer: **"Fold into the launch plan?"** (`/evermuse:gtm-strategy`), **"Build a battlecard for the top competitor?"** (`/evermuse:competitive-battlecard`), or **"Sharpen the ICP behind this?"** (`/evermuse:ideal-customer-profile`).

---
### Further reading
- Merged and adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) `positioning-ideas` + `marketing-ideas` (MIT); grounding is Evermuse-native.
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
- [Product Management vs. Product Marketing vs. Product Growth 101](https://www.productcompass.pm/p/product-management-vs-product-marketing)
