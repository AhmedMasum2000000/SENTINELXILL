---
name: opportunity-solution-tree
description: 'Build a Teresa Torres Opportunity Solution Tree — outcome → opportunities → solutions → experiments — where every opportunity node is backed by a real customer quote and unsupported nodes are flagged as unproven hypotheses. Use when the user asks to ''build an opportunity solution tree'', ''map opportunities to solutions'', ''structure our discovery'', ''OST'', or ''organize opportunities and solutions''. Trigger terms: opportunity solution tree, OST, discovery tree, map opportunities, outcome to opportunities, Teresa Torres. Not for scoring an existing backlog (that''s prioritize-features).'
category: Prioritization & Planning
tags:
- ost
- discovery
- prioritization
---

# Opportunity Solution Tree (every opportunity quote-backed)

Structure discovery the Teresa Torres way: one measurable **outcome** at the top, the customer **opportunities** (needs/pains) beneath it, **solutions** for the top opportunities, and **experiments** to validate them. The Evermuse discipline: **an opportunity node is only real if a customer said it.** Every opportunity carries a verbatim quote; any node you add from intuition is flagged `hypothesis — no evidence yet` so the tree never launders a guess as a validated need.

## Step 0 — Relevance & availability
Confirm this is discovery structuring and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, you can sketch the tree's skeleton but every opportunity is unverified — label the whole thing **⚠ ungrounded** and tell the user to authorize the MCP.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## The tree (4 levels)

1. **Desired outcome** (top) — one measurable metric (e.g. "increase 7-day retention to 40%"). From OKRs/strategy. One outcome per tree.
2. **Opportunities** — customer needs/pains, framed from *their* perspective ("I struggle to…", "I wish I could…"). **Each must be quote-backed.** Prioritize with Opportunity Score = Importance × (1 − Satisfaction), 0–1.
3. **Solutions** — ≥3 per prioritized opportunity, ideated across PM/Designer/Engineer. Don't commit to the first idea.
4. **Experiments** — fast, cheap tests per promising solution (hypothesis · method · metric · threshold). Prefer skin-in-the-game over opinions.

**Principles:** one outcome at a time · opportunities not features · compare/contrast ≥3 solutions · discovery is non-linear (kill what fails, branch anew) · update the tree continuously.

## Instructions

1. **Define the outcome.** Confirm or help articulate a single measurable metric. Refuse to proceed with a vague, unmeasurable one.
2. **Map opportunities from evidence.** Pull 3–7 real opportunities from the grounded quotes/notes; group related ones; frame each in the customer's words with its quote attached. If you're tempted to add an opportunity with no signal, add it but **flag it** `hypothesis — no evidence yet` and note it needs an interview (`/evermuse:interview`).
3. **Prioritize opportunities.** Rank by Opportunity Score / demand strength (distinct accounts). Focus on the top 2–3.
4. **Generate solutions.** ≥3 per prioritized opportunity, across the three perspectives.
5. **Design experiments** for the most promising solutions (see `/evermuse:assumptions` for the experiment library).
6. **Visualize the tree** hierarchically.

## Deliverable

```markdown
🎯 OUTCOME: [measurable metric]
│
├─ OPPORTUNITY: "I struggle to export my data" — 6 accounts, Opp. Score 0.72
│    > "[verbatim]" — [Name], [Meeting], [Date] [`1`](URL)
│    ├─ SOLUTION: Scheduled export  → EXPERIMENT: fake-door · CTR ≥ 8%
│    ├─ SOLUTION: Email-to-share    → EXPERIMENT: prototype task · success ≥ 70%
│    └─ SOLUTION: Public API        → EXPERIMENT: spike · feasible in budget?
│
├─ OPPORTUNITY: [flag] "unified dashboard" — ⚠ hypothesis — no evidence yet
│    → needs an interview before it earns a place on the tree
```

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) — opportunity-solution-tree. Method: Teresa Torres, *Continuous Discovery Habits*; Opportunity Score: Dan Olsen, *The Lean Product Playbook*.
