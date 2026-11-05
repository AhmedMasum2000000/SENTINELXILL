<!-- Adapted from github/spec-kit (MIT) analyze workflow. Read-only; never modifies artifacts. -->
# Cross-Artifact Analysis Checklist (Lens 1: Spec ↔ Spec)

A read-only pass over spec + plan + tasks. Build a mental inventory first (requirements FR-###/SC-###, user stories, tasks), then run these detection passes. Cap the report at the ~50 highest-signal findings; aggregate trivia.

## Detection passes
- **Duplication** — near-identical requirements stated twice; consolidate.
- **Contradiction** — requirements that can't both hold; flag as Critical.
- **Ambiguity** — vague adjectives ("fast", "secure", "scalable", "intuitive") with no measure; unresolved `[NEEDS CLARIFICATION]`, `TODO`, `TKTK`, `???`.
- **Underspecification** — a requirement missing an object or outcome; a user story with no acceptance criteria; a success criterion with no measure.
- **Coverage gaps** — requirement with zero tasks; task tracing to no requirement; success criterion whose work isn't in the plan.
- **Inconsistency** — terminology drift (same concept, different words); a data entity in the plan but absent from the spec; conflicting priorities.

## Output per finding
`Severity · Location(s) · What's wrong · Suggested fix` — but **suggest only**; this lens never edits the artifacts. Hand fixes to the user.

## Severity guide
- **Critical**: contradiction, or a P1 story with no path to being built.
- **High**: an uncovered requirement or success criterion.
- **Medium**: ambiguity/terminology that could mislead implementation.
- **Low**: cosmetic; aggregate into a single line.
