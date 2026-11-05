---
name: brainstorm-okrs
description: 'Draft team-level OKRs — inspirational objectives with measurable key results — where each objective maps to an evidenced customer outcome and each key result measures reduction of a real, stated customer pain, aligned to company strategy via Evermuse. Use when the user wants to ''set OKRs'', ''draft quarterly objectives'', ''write key results'', ''align team goals with strategy'', or ''brainstorm OKRs for [team]''. Trigger terms: OKRs, objectives and key results, quarterly goals, key results, KPIs, north star metric. Not for a full roadmap — use outcome-roadmap for that.'
category: Ops & Meta
tags:
- okrs
- goals
- planning
---

# Brainstorm Team OKRs (grounded in customer outcomes)

Generate ambitious, measurable OKRs for the team working on $ARGUMENTS. The difference from a generic OKR exercise: each **Objective maps to a customer outcome the evidence actually supports**, and each **Key Result measures the reduction of a stated pain** — not vanity output like "ship 5 features."

## Step 0 — Relevance & availability
Confirm this is product/team-goal work and Evermuse is present. If the MCP isn't connected, produce OKRs from the framework but label them **⚠ ungrounded** and tell the user to authorize the MCP. (See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`, Step 0.)

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

1. **Domain model (keep these distinct).**
   - **Objective** (Why/What/When): qualitative, inspirational, time-bound (usually quarterly), SMART.
   - **Key Results** (How much): ~3 quantitative metrics + target values.
   - **KPIs / NSM** are interconnected, not alternatives — a KR can *be* a KPI; the NSM is a single customer-centric KPI a KR can express expected change in. Never table them as rivals.
2. **Map objectives to evidenced outcomes.** For each candidate objective, point to the customer outcome it delivers and the quotes behind it. Replace the source skill's "web search for benchmarks" with **Evermuse evidence as the primary source** for what outcomes matter; use general benchmarks only to sanity-check target ambition.
3. **Make KRs measure pain reduction.** Prefer outcome metrics tied to a stated pain (e.g. "cut time-to-first-value from 20→8 min" when customers complained onboarding was slow) over output metrics. Each KR independently measurable, 60–70% confidence (ambitious, not safe).
4. **Generate three credible sets.** Present all three with equal weight — none obviously best — to spark strategic discussion. For each: objective, exactly 3 KRs, and a one-line rationale linking it to both the company strategy and the customer evidence.
5. **Flag data gaps.** If a KR's metric isn't currently instrumented, say so.

## Output format
```
Objective: [inspiring, customer-outcome-oriented statement]   [`1`](URL)
Key Results:
- [metric → target]        [`2`](URL)
- [metric → target]
- [metric → target]
Rationale: [ladders up to <company objective> [`3`](URL); addresses <stated pain> [`4`](URL)]
```
Three sets, each with inline citations.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT).
- [OKRs 101](https://www.productcompass.pm/p/okrs-101-advanced-techniques) · [OKR vs KPI](https://www.productcompass.pm/p/okr-vs-kpi-whats-the-difference) · [Business vs Product vs Customer Outcomes](https://www.productcompass.pm/p/business-outcomes-vs-product-outcomes)
