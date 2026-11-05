---
name: outcome-roadmap
description: 'Transform a feature-list (output) roadmap into an outcome-focused one — each lane rewritten as ''Enable [segment] to [outcome] so that [business impact]'' and citing the demand evidence behind it, grounded in Evermuse. Use when the user wants to ''make the roadmap outcome-focused'', ''rewrite the roadmap'', ''turn features into outcomes'', ''make the roadmap more strategic'', or ''build an outcome roadmap''. Trigger terms: roadmap, outcome roadmap, outcome-based roadmap, strategic roadmap, feature list to outcomes. Not for OKRs (use brainstorm-okrs) or a per-feature spec.'
category: Prioritization & Planning
tags:
- roadmap
- outcomes
- planning
---

# Outcome-Focused Roadmap (grounded in demand evidence)

Shift $ARGUMENTS from an output roadmap (a list of features by quarter) to an **outcome roadmap** (customer/business impact by horizon), where **each outcome lane cites the demand evidence that justifies it**. A feature list says what you'll build; an outcome lane says why it matters and proves customers are asking for it.

## Step 0 — Relevance & availability
Confirm this is product-roadmap work and Evermuse is present. If the MCP isn't connected, transform the roadmap using the framework but label it **⚠ ungrounded** and tell the user to authorize the MCP. (See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`, Step 0.)

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

1. **For each initiative, run the transform:**
   - **Output (old):** the feature/project as currently listed.
   - **Outcome (new):** `Enable [customer segment] to [desired customer outcome] so that [business impact]`.
   - **Demand evidence:** the quotes + mention count proving customers want this outcome. [`1`](URL)
   - **Success metric:** how you'll know the outcome landed (ties to `brainstorm-okrs` KRs if present).
2. **Let evidence reorder, not just relabel.** If a lane has thin demand evidence, flag it (**low-demand — validate or defer**); if a strongly-evidenced outcome has no lane, surface it as a **missing lane**. Replace the source skill's "web search for alignment" with **Evermuse evidence as the primary source** for what customers actually want.
3. **`get_opportunities` is a labeled cross-check ONLY.** You may call `get_opportunities` once to compare your evidence-built lanes against Evermuse's machine-suggested opportunities — but present them explicitly as **"AI-generated cross-check (secondary, not customer ground truth)"** and never let them originate a lane or override the demand evidence. Same for shaping notes.
4. **Keep horizons flexible.** Now / Next / Later (or quarters), never hard dates. Multiple outputs can serve one outcome — focus on the outcome.
5. **Apply the "So what?" test.** For any feature you can't tie to a customer/business outcome, ask "so what?" until you reach real value — or drop it from the roadmap.

## Output
Transformed roadmap grouped by horizon. Per lane: outcome statement · demand evidence (inline badge) · success metric. A short **alignment note** to company strategy [`1`](URL) and an optional **AI cross-check** section.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT).
- [Vision vs Strategy vs Objectives vs Roadmap](https://www.productcompass.pm/p/product-vision-strategy-goals-and) · [OKRs 101](https://www.productcompass.pm/p/okrs-101-advanced-techniques) · [Business vs Product vs Customer Outcomes](https://www.productcompass.pm/p/business-outcomes-vs-product-outcomes)
