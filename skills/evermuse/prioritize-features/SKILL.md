---
name: prioritize-features
description: 'Rank a backlog of feature ideas using real demand counts from customer evidence — Reach and Impact come from how many distinct accounts actually asked, not a gut number — and return a top-5 with the quotes behind each score. Use when the user asks to ''prioritize features'', ''what should we build next'', ''rank this backlog'', ''score these ideas'', ''RICE this'', ''make scope decisions'', or ''which feature first''. Trigger terms: prioritize, prioritization, rank features, backlog, RICE, ICE, what to build next, scope decision, score features. Not for open-ended ideation (that''s brainstorm-ideas).'
category: Prioritization & Planning
tags:
- prioritization
- rice
- frameworks
---

# Prioritize Features (scored on real demand)

Rank a backlog to find the top 5 to pursue. The Evermuse difference: **Reach and Impact aren't gut numbers** — they come from counting how many distinct accounts actually asked, and how sharply, in real conversations. A backlog scored on evidence looks different from one scored on the loudest stakeholder.

## Step 0 — Relevance & availability
Confirm this is backlog prioritization and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, you can still apply the frameworks, but every Reach/Impact number is a guess — label the output **⚠ ungrounded** and say the scores are unvalidated.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

1. **Confirm the objective and success metric.** Prioritization is meaningless without the outcome you're ranking against. Ask if it's not stated.

2. **Ground each item in demand.** For every feature, pull its real signal: how many distinct accounts asked, the sentiment, and one verbatim quote. Prioritize **problems (opportunities), not solutions** — "never allow customers to design solutions."

3. **Score with an evidence-fed framework** (details in `references/prioritization-frameworks.md`):
   - **Reach** = number of distinct accounts affected — **from the evidence count**, not a guess.
   - **Impact** = Opportunity Score (Importance × (1 − Satisfaction)) where the corpus reveals importance and dissatisfaction — value per customer.
   - **Confidence** = how sure are we? Higher when the evidence is thick and consistent, lower when it's one account.
   - **Effort** = dev/design/coordination cost.
   RICE = (R × I × C) / E · ICE = I × C × E · Opportunity Score for problem-ranking.

4. **`get_opportunities` is a labeled cross-check only.** You may pull Evermuse's machine-suggested opportunities to sanity-check your ranking, but present them explicitly as **"AI-generated cross-check (not customer ground truth)"** — never let them override the evidence-backed scores.

5. **Recommend the top 5** with ranking, rationale naming the evidence, key trade-offs, and **what was deprioritized and why**.

## Deliverable

```markdown
**Objective:** [outcome being ranked against]

| # | Feature | Reach (accounts) | Impact (Opp. Score) | Conf | Effort | Score | Evidence |
|---|---------|------------------|---------------------|------|--------|-------|----------|
| 1 | Scheduled export | 6 | 0.72 | High | M | … | > "[quote]" [`1`](URL) |
| 2 | … | 3 | 0.55 | Med | S | … | [`2`](URL) |

**Deprioritized:** [feature] — [why, e.g. "only 1 account, low importance"].

**AI-generated cross-check (not ground truth):** roadmap suggests … — [agrees/differs with evidence ranking].
```

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) — prioritize-features; frameworks reference adapted from pm-execution/prioritization-frameworks. Opportunity Score: Dan Olsen, *The Lean Product Playbook*.
