---
name: ideal-customer-profile
description: 'Build an Ideal Customer Profile from your real won-and-happy customers — firmographics, behaviors, jobs-to-be-done, and pains drawn from actual conversations with the accounts that bought and stayed. Use when the user says ''define our ICP'', ''who is our ideal customer'', ''who are our best customers'', ''who should we sell to'', ''build a customer profile'', or ''who retains and expands''. Trigger terms: ICP, ideal customer profile, best customers, target customer, who to sell to, firmographics, JTBD, disqualification criteria. Not for picking a single first market — use beachhead-segment for that.'
category: Segmentation & Targeting
tags:
- icp
- targeting
- personas
---

# Ideal Customer Profile

Define the customer most likely to find value, retain, and expand — but build it from **real won-and-happy customers in the corpus**, not an idealized composite. The Evermuse twist: you identify the accounts that actually bought and stayed, read *their* conversations for why, and let the patterns across them define the ICP with quotes attached.

## Step 0 — Relevance & availability
Confirm this is an ICP / targeting task and Evermuse is connected. If the tools aren't present, produce a framework-only ICP labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md` Step 0.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

You are defining the ICP for **$ARGUMENTS**. Where the source method reaches for "PMF survey data / win-loss / interviews," use the Evermuse corpus of real customer conversations as the primary source — start from accounts that actually won and stayed, and read their words.

### Step 1 — Find the real best customers
Segment the accounts in the corpus by value signal: bought and renewed, expanded, fastest time-to-value, most enthusiastic, best reference potential. These accounts — not a hypothetical persona — are the raw material.

### Step 2 — Extract the four ICP components (each cited)
For the best-customer cohort, synthesize patterns and attach quotes:

- **Firmographics** — company size, industry/vertical, geography, buyer's role/department, company stage. Note the *actual* common denominators, including non-obvious outliers that are high-value.
- **Behaviors** — how they discovered the product, evaluation process and timeline, who was in the buying committee, adoption speed and breadth, support needs. (Discovery channel is gold for GTM — cite it.)
- **Jobs to Be Done** — the functional job, plus emotional ("how they want to feel") and social dimensions, and their own success metrics — in their words.
- **Needs & pains** — the before-state frustrations and the after-state they got, quantified where the evidence allows (cost/time of the problem).

### Step 3 — Sharpen the edges
- **Ideal-of-the-ideal:** the tightest sub-pattern that predicts the best outcomes.
- **Disqualification criteria:** who is NOT a fit — grounded in accounts that looked similar but churned, stalled, or never activated. This is where evidence prevents an over-broad ICP.
- **GTM implications:** what the ICP means for messaging and channels (hand off to `/evermuse:positioning-and-messaging` or `/evermuse:gtm-strategy`).

## Deliverable format

```markdown
# Ideal Customer Profile — [product]

**Built from:** [N] won-and-happy accounts in the corpus ([examples]).

**Firmographics:** [size / industry / geo / role / stage] — pattern evidenced by [`1`](URL).
**Behaviors:** discovered via [channel] [`2`](URL); buying committee [who]; adoption [speed].
**Jobs to Be Done:** functional — [job]; emotional — [feeling]; social — [status]. > "[JTBD quote]" — [attribution] [`3`](URL)
**Top pains → outcomes:**
| Before (pain) | After (outcome they got) | Evidence |
|---|---|---|
| [pain] | [outcome] | > "[quote]" — [attribution] [`4`](URL) |

**Ideal-of-the-ideal:** [tightest high-value sub-pattern].
**Disqualification (NOT a fit):** [traits] — grounded in [churned/stalled accounts] [`5`](URL).
**GTM implications:** [messaging + channel notes].
```

## Honesty when evidence is thin
If only a handful of happy accounts exist, say so — the ICP is a hypothesis from N accounts, not a law. Flag where more won-customer conversations would sharpen it.

## Save & hand off
After saving, offer: **"Position for this ICP?"** (`/evermuse:positioning-and-messaging`), **"Plan the launch?"** (`/evermuse:gtm-strategy`), or **"Narrow to a first beachhead?"** (`/evermuse:beachhead-segment`).

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) `ideal-customer-profile` (MIT); grounding is Evermuse-native.
- Based on Jobs to Be Done theory (Clayton Christensen).
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
