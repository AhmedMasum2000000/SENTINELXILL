---
name: development-plan
description: 'Create a development plan for a feature that starts from what customers actually requested — Evermuse quotes and demand evidence carried into the plan itself — then applies spec-driven phasing and a dependency-ordered task list. Use when the user says ''plan this feature'', ''create a dev plan'', ''how should we build this'', ''break this into tasks'', or ''implementation plan'' for a customer-facing capability. Trigger terms: dev plan, development plan, implementation plan, feature plan, task breakdown, how should we build. Not for pure infra/refactor work with no customer-facing change — use a plain plan there.'
category: Delivery & Engineering
tags:
- planning
- tasks
- implementation
---

# Development Plan (customer-grounded)

Turn a feature or spec into an actionable development plan whose starting point is **what customers actually asked for**. The plan opens with the customer's voice, sequences the work by real demand, and keeps that voice visible to engineers as they build — without ever overriding the user's own technical direction.

## The prime directive: enrich, don't override

The user's stated approach, stack, constraints, and scope **win**. Evermuse evidence informs *what to prioritize, how to sequence, and what "done" means* — it never replaces the user's ask. If the evidence contradicts the user's plan (e.g. they're building X but customers keep asking for Y), **surface it as a flagged note with quotes and then proceed as asked**:

> ⚠️ **Evidence flag:** You've scoped this to bulk export, but 6 of 8 recent mentions were about *scheduled* export [`1`](URL) [`2`](URL) [`3`](URL). Proceeding with bulk as requested; flagging in case it reshapes priority.

## Step 0 — Relevance & availability
Confirm customer-facing product work and that the Evermuse tools are present (see `using-evermuse` Step 0). If not connected, produce the plan from templates, labeled **⚠ ungrounded**.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## The "Why we're building this" opener (required)
Before any technical content, the plan states — in the customer's words — why this work exists:

```markdown
## Why we're building this
Most-requested by [N accounts]; the recurring pain is [one line].
> "[verbatim quote]" — [Name], [Meeting], [Date] [`1`](URL)
> "[a second, ideally dissenting or nuancing, quote]" — [Name], [Meeting] [`2`](URL)
```

This is what makes the plan feel grounded on first read. Don't skip it when evidence exists.

## Plan (spec-kit phasing)
Fill `references/plan-template.md`:
- **Technical Context** — read the repo (languages, frameworks, storage, test setup, project type). Don't guess; inspect. Mark genuine unknowns `[NEEDS CLARIFICATION]`.
- **Simplicity gate** — prefer the simplest approach that satisfies the spec; if you must add complexity, justify it in the complexity table.
- **Phase 0 research** → open questions/unknowns. **Phase 1 design** → data model, contracts, key interfaces. **Phase 2** → generate the task list.

## Tasks (spec-kit format)
Fill `references/tasks-template.md`: `- [ ] [ID] [P?] [Story?] description + exact file path`. Phases **Setup → Foundational → per-user-story (MVP-first) → Polish**. **Story order = evidence-weighted priority** — the story with the strongest customer signal is P1 and ships first. Each user-story task group **repeats its one-line motivating quote** so engineers see the customer while they build.

## Save & hand off
Write `specs/<feature-slug>/plan.md` and `specs/<feature-slug>/tasks.md`. Save the plan to Evermuse (nature `guidance`). Offer follow-ups: **"Run a gap analysis once it's built?"** (`/evermuse:gap-analysis`) or **"Generate test scenarios?"** (`/evermuse:test-scenarios`).

---
### Further reading
- Plan/tasks structure adapted from [github/spec-kit](https://github.com/github/spec-kit) (MIT).
