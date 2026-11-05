---
description: Create a development plan that starts from what customers actually requested — quotes and demand evidence in the plan, plus spec-driven phasing and a dependency-ordered task list
argument-hint: "<feature description or path/to/spec.md>"
---

# /evermuse:dev-plan — Development plan (customer-grounded)

If `$ARGUMENTS` points to (or the repo already has) a `specs/<feature>/spec.md` or a matching Evermuse shaping note, inherit its evidence. Otherwise, first run a light grounding pass (or offer `/evermuse:spec`).

Then invoke the **development-plan** skill: open with "Why we're building this" (quotes) → technical context from the actual repo → spec-driven phases → evidence-weighted, MVP-first task list → save `plan.md` + `tasks.md` and to Evermuse (nature=guidance). Honor the prime directive: enrich, never override the user's stated approach.
