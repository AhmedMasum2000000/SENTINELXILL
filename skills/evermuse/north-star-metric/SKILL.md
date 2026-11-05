---
name: north-star-metric
description: 'Define a customer-centric North Star Metric plus a tree of 3-5 input metrics that drive it, where the North Star is anchored to the actual value customers describe getting from the product in real evidence. Use when the user says ''define our north star'', ''what should we measure'', ''pick a key metric'', ''set up a metrics framework'', ''what''s our North Star'', or ''what drives our growth''. Trigger terms: north star, north star metric, NSM, key metric, input metrics, what to measure, metrics framework, OMTM, leading indicator. Not for an ops/health monitoring dashboard — this is the single value metric and its drivers.'
category: Strategy & Vision
tags:
- metrics
- north-star
- kpis
---

# North Star Metric

Define a single, customer-centric North Star Metric and the 3–5 input metrics that drive it (a metrics constellation / input tree). The Evermuse twist: the North Star must reflect the **value customers actually describe getting** in real conversations — not a revenue proxy or a vanity number. You ground the value definition in quotes, then pick the metric that best captures it.

## Step 0 — Relevance & availability
Confirm this is a metrics-definition task and Evermuse is connected. If the tools aren't present, produce a framework-only NSM labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md` Step 0.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

You are a metrics strategist defining the North Star for **$ARGUMENTS**. Where the source method reaches for "business context you provide," use Evermuse `evidence` (how customers describe value) as the primary input.

**NSM is NOT** multiple metrics, a revenue/LTV metric, an OKR, or a strategy. **NSM IS** a single customer-centric KPI reflecting the value customers get and leading long-term business success.

### Step 1 — Classify the business game
Determine which game the product plays; it shapes the North Star family:
- **Attention** — time customers spend (Spotify, YouTube).
- **Transaction** — exchanges between customer and platform (Uber, Airbnb, Amazon).
- **Productivity** — how efficiently someone completes work or reaches a goal (Notion, Canva, Loom).
Ground the pick: which framing matches the value customers actually describe? Cite it.

### Step 2 — Define the North Star from evidenced value
State the single metric that captures the core value customers named. Validate against the **7 criteria**: (1) easy to understand, (2) customer-centric, (3) reflects sustainable value/habit, (4) aligned to vision, (5) quantitative, (6) actionable, (7) leading indicator. Show the metric passing each — and tie criterion (2) directly to a customer quote about value.

### Step 3 — Build the input-metric tree (3–5)
Define the input metrics that most directly drive the North Star. Each input should be easier to move short-term, provably contribute to the North Star outcome, and point to where teams optimize. Draw the tree: **North Star = f(input₁, input₂, …)**. For each input, prefer a good-metric shape — a **ratio or rate**, comparative over time, and behavior-changing ("if it won't change what you do, it's a bad metric"). Distinguish leading from lagging, and note where a qualitative signal (customer complaints, sentiment from the corpus) is the earliest leading indicator.

### Step 4 — Guardrails (brief)
Name 1–2 health guardrails so optimizing the North Star doesn't quietly harm the customer (e.g. quality, latency, churn). This is the useful half of a metrics dashboard — not a full ops dashboard; for that, keep it out of scope.

## Deliverable format

```markdown
# North Star — [product]

**Business game:** [Attention / Transaction / Productivity] — because [evidenced value, [`1`](URL)].

**North Star Metric:** [metric]
**Why it captures value:** > "[customer quote about the value]" — [attribution] [`2`](URL)
**7-criteria check:** [✓ understandable · ✓ customer-centric [`2`](URL) · ✓ sustainable · ✓ vision-aligned [`3`](URL) · ✓ quantitative · ✓ actionable · ✓ leading]

**Input-metric tree**  (North Star = f(inputs))
| Input metric | Shape (ratio/rate) | How it drives NSM | Lead/Lag |
|---|---|---|---|
| [input 1] | [rate] | [link, cited [`4`](URL)] | Leading |

**Guardrails:** [health metric 1], [health metric 2].
```

## Honesty when evidence is thin
If customers don't clearly articulate the value, say so — a North Star built on a guessed value definition is fragile. Flag it as a hypothesis and suggest interviews (`/evermuse:interview` if available) to confirm the value the metric is meant to track.

## Save & hand off
After saving, offer: **"Wire this into the GTM plan's metrics?"** (`/evermuse:gtm-strategy`), or **"Define the ICP whose value this measures?"** (`/evermuse:ideal-customer-profile`).

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) `north-star-metric`, absorbing the input-tree half of `metrics-dashboard` (MIT); grounding is Evermuse-native.
- [The North Star Framework 101](https://www.productcompass.pm/p/the-north-star-framework-101)
- [AARRR (Pirate) Metrics](https://www.productcompass.pm/p/aarrr-pirate-metrics)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
