---
name: gap-analysis
description: 'Audit an existing spec, plan, or shipped feature for gaps across three lenses — spec-vs-spec consistency, spec-vs-code implementation, and whether the build covers what customers need — with every finding backed by evidence. Use when the user asks to ''do a gap analysis'', ''what''s missing from the spec'', ''did we build what we specced'', ''did we build what customers asked for'', or wants a consistency/coverage check against a spec, plan, or shipped feature. Trigger terms: gap analysis, what''s missing from the spec, coverage check, consistency check, did we build what we planned. Requires an artifact to audit against — for an open-ended customer question with no spec, use customer-research.'
category: Prioritization & Planning
tags:
- gap-analysis
- capabilities
- assessment
---

# Gap Analysis (three lenses)

Find what's missing — not just against the spec, but against reality and against the customer. Most "gap analysis" stops at spec-vs-code. This one adds the lens that matters most: **are the things customers most need actually covered?**

## Step 0 — Relevance & availability
Confirm the product context and Evermuse availability (see `using-evermuse` Step 0). Lens 3 needs the MCP; Lenses 1–2 work ungrounded (label the output accordingly if disconnected).

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Gather the artifacts
- **Spec/plan**: local `specs/<feature>/spec.md` + `plan.md`, and/or shaping notes via `get_shaping_notes` → `read_shaping_note`.
- **Code** (for Lens 2): read the relevant implementation, **read-only**. Don't modify anything.
- **Customer evidence** (for Lens 3): `evidence` searches per major need theme + a quote-angled `search`.

## The three lenses

**Lens 1 — Spec ↔ Spec (internal consistency).** Using `references/analysis-checklist.md` (spec-kit `analyze` method): duplicate/contradictory requirements, ambiguity (vague terms, unresolved `[NEEDS CLARIFICATION]`), coverage gaps (requirements with no task; success criteria needing work not planned), terminology drift.

**Lens 2 — Spec ↔ Code (intended vs. implemented).** For each functional requirement (FR-###), find the implementation evidence in the code and classify: implemented / partial / missing / diverged. Cite both sides — the requirement *and* the file:line. A mismatch only matters when it changes behavior or crosses a trust/permission boundary; note cosmetic drift separately.

**Lens 3 — Spec ↔ Customer (demand coverage).** For each high-signal need in the corpus, check whether the spec/build addresses it. The gaps that hurt are **strongly-evidenced needs that nothing covers**. Rank by demand strength (mentions across accounts), each row badged with a quote.

## Output
When you cite, use the inline linked-number badge per `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/references/citations.md` — [`1`](URL). Citations are optional but recommended.

A severity-ranked table — Critical / High / Medium — where each row names the gap, the lens, and the evidence (a linked-number badge for Lens 3, a file:line for Lens 2, a spec reference for Lens 1):

```markdown
| Sev | Gap | Lens | Evidence |
|-----|-----|------|----------|
| 🔴 Critical | No scheduled export, but it's the top ask | Customer | 6 mentions [`1`](URL) [`2`](URL) [`3`](URL) |
| 🟠 High | FR-004 (audit log) not implemented | Code | spec §FR-004 · not found in src/ |
| 🟡 Medium | "export" vs "download" used interchangeably | Spec | spec §3, §7 |
```

Lead with a one-paragraph verdict (is the build ready / what's the biggest risk), then the table, then a short prioritized fix list.

## Save
`add_source(nature: "guidance", source_type: "document", tags: ["evermuse-plugin","gap-analysis","<slug>"])` after confirmation.

---
### Further reading
- Lens 1 adapts [github/spec-kit](https://github.com/github/spec-kit) `analyze` (MIT); Lens 2 adapts the intended-vs-implemented method from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT).
