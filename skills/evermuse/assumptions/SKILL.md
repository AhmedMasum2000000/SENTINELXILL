---
name: assumptions
description: 'Surface the risky assumptions behind a feature or idea, but first check the evidence — if customers already answered it, it''s a finding, not an assumption — then score the rest by Impact × Risk and match each to the cheapest experiment. Use when the user asks to ''identify assumptions'', ''what are we assuming'', ''stress-test this idea'', ''what could go wrong'', ''what should we test first'', or ''design an experiment''. Trigger terms: assumptions, risks, what could go wrong, validate, de-risk, experiment, test this. Not for prioritizing shipped features (that''s prioritize-features).'
category: Specs & Requirements
tags:
- assumptions
- validation
- experiments
- risk
---

# Assumptions (find → cross off what's known → prioritize → experiment)

Devil's-advocate risk analysis with a twist that only Evermuse makes possible: **before you call something an assumption, search the evidence.** If customers already answered the question, it's not an assumption — it's a finding. Cite the quote and cross it off. The remaining true unknowns get scored (Impact × Risk) and matched to the cheapest experiment that would resolve them.

## Step 0 — Relevance & availability
Confirm this is idea/feature stress-testing and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, you can still list candidate assumptions from the framework, but label them **⚠ ungrounded** — you cannot cross any off, because you can't check what customers already said.

## Two scopes
- **Existing product feature** — 4 core risk areas: **Value, Usability, Viability, Feasibility** (Teresa Torres).
- **New product / venture** — extend to 8: add **Ethics, Go-to-Market, Strategy & Objectives, Team** (critical when there's no live product to lean on).

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

1. **Surface candidate assumptions** from three perspectives (PM / Designer / Engineer), across the 4 (or 8) risk areas. Frame each as a falsifiable belief: "We assume [X]."

2. **Check each against the evidence (the key step).** For every candidate, ask: did a real customer already tell us the answer? Search / pull quotes.
   - **Answered by evidence** → reclassify as a **finding**. State the answer, cite the quote, and **cross it off** the assumption list. (This is the visible payoff — a plain brainstorm would have "tested" things customers already settled.)
   - **Contradicted by evidence** → flag as a **red-flag assumption** the idea is currently getting wrong; cite it.
   - **Not addressed** → keep as a **true unknown** to score.

3. **Score the true unknowns** on Impact × Risk:
   - **Impact** = value of validating it × how many customers it touches (use real demand counts from the searches, not a guess).
   - **Risk** = (1 − Confidence) × Effort.
   Then place each in the matrix: High Impact/High Risk → **design an experiment**; High Impact/Low Risk → **just proceed**; Low Impact/High Risk → **drop the idea/branch**; Low Impact/Low Risk → **defer**.

4. **Match each "experiment" cell to the cheapest test** from `references/experiment-templates.md` — maximum validated learning, minimum effort, measures behavior not opinions, with a clear metric and success threshold.

## Deliverable

```markdown
### Already answered by customers (crossed off)
- ~~We assumed users want scheduled export~~ → **Confirmed.** > "[verbatim]" — [Name], [Meeting] [`1`](LINK) (5 accounts)

### Contradicted — the idea currently gets this wrong
- We assumed [X], but customers say [Y]. > "[quote]" [`2`](URL)

### True unknowns — scored & matched
| Assumption | Area | Impact | Risk | Quadrant | Cheapest experiment | Metric · threshold |
|-----------|------|--------|------|----------|---------------------|--------------------|
| We assume … | Value | High | High | Experiment | Fake-door test | CTR ≥ 8% |
```

## References
- `references/experiment-templates.md` — the experiment library (prototype tests, fake doors, spikes, A/B, Wizard of Oz, pretotypes / XYZ hypotheses) with when-to-use and success-metric guidance.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) — identify-assumptions (existing + new), prioritize-assumptions, brainstorm-experiments (existing + new). Risk areas: Teresa Torres, *Continuous Discovery Habits*. Pretotypes: Alberto Savoia, *The Right It*.
