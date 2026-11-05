---
name: competitive-battlecard
description: 'Create a sales-ready competitive battlecard against a named competitor where the ''they say / we say'' rows are ACTUAL objections and competitor mentions pulled from real customer conversations — not invented talking points. Use when the user says ''build a battlecard'', ''how do we beat competitor X'', ''why not competitor X'', ''competitive comparison'', ''handle this objection'', or ''prep sales against a competitor''. Trigger terms: battlecard, competitor, competitive, objection handling, win/loss, why not X, versus, compete. Not for broad market sizing — this is a one-competitor sales asset.'
category: Market & Competition
tags:
- battlecard
- competitors
- sales-enablement
---

# Competitive Battlecard

Create a concise, sales-ready battlecard against a specific competitor. The Evermuse twist: the objections and competitor claims in the card are **the real ones customers actually raised** in recorded conversations — mined verbatim — so reps counter what prospects genuinely say, not a strawman. Competitor capability data from Evermuse is used only as a labeled secondary source.

## Step 0 — Relevance & availability
Confirm this is competitive / sales-enablement work and Evermuse is connected. If the tools aren't present, produce a framework-only battlecard labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md` Step 0.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

You are creating a battlecard against **$ARGUMENTS**. Where the source method reaches for "web search / G2 / Reddit," use Evermuse `evidence` (real objections and mentions from calls) as the PRIMARY source, and competitor-capability data as clearly-labeled secondary.

Build these sections, keeping it scannable — reps reference this live on calls:

### Company overview
One-sentence positioning, target market/ICP, and what's publicly known (funding/scale). Keep it tight.

### Quick comparison
| Capability | Us | Them | Winner |
|---|---|---|---|
| [area] | [our approach] | [their approach *(secondary)*] | [Us/Them/Tie] |

### Where we win / where they win
- **We win:** [advantage] — proof: > "[customer quote]" — [attribution] [`1`](URL) (real, not asserted).
- **They win:** [their strength, from a real objection [`2`](URL)] → our counter-positioning.

### Common objections & responses — the heart of the card
| Prospect actually said | Respond with |
|---|---|
| > "[verbatim objection]" — [attribution] [`3`](URL) | [grounded counter — reframe, value/ROI, proof quote] |
Only include objections you can trace to a real conversation. If you must add a likely-but-unheard objection, mark it **(anticipated — not yet heard in corpus)**.

### Landmines to plant
Questions that expose the competitor's weaknesses — each tied to a gap customers actually named.

### Win/loss patterns
- We tend to win when: [pattern from evidence].
- We tend to lose when: [pattern from evidence].
- What tips competitive deals: [the differentiator that shows up in wins].

## Deliverable format

```markdown
# Battlecard: Us vs [Competitor]

**Overview:** [one-line positioning · target · scale]

**Quick comparison** — [table]

**Where we win**
- [advantage] — > "[quote]" — [attribution] [`1`](URL)

**Objections & responses**
| Prospect said | Respond with |
|---|---|
| > "[verbatim]" — [attribution] [`2`](URL) | [counter] |

**Win/loss:** win when [pattern [`3`](URL)] · lose when [pattern [`4`](URL)] · tipping point [diff].
```

## Honesty when evidence is thin
If the competitor barely appears in the corpus, say so — "mentioned in 1 deal" — and lean on labeled secondary capability data while flagging that the objection set is unvalidated. Don't manufacture objections and present them as heard.

## Save & hand off
After saving, offer: **"Turn wins into positioning?"** (`/evermuse:positioning-and-messaging`), or **"Fold this into the GTM plan?"** (`/evermuse:gtm-strategy`).

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) `competitive-battlecard` (MIT); grounding is Evermuse-native.
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
