<!-- Adapted from github/spec-kit (MIT) plan-template — with an Evermuse "Why we're building this" opener. -->
# Implementation Plan: [FEATURE]

**Feature slug**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link to spec.md if any]
**Product (Evermuse)**: [name] · **Grounding**: [inherited from spec / N searches] or ⚠ ungrounded

## Why we're building this *(Evermuse — mandatory when grounded)*
Most-requested by [N accounts]; the recurring pain is [one line].
> "[verbatim quote]" — [Name], [Meeting], [Date] [`1`](URL)
> "[second quote]" — [Name], [Meeting] [`2`](URL)

[If the user's scope diverges from the evidence, add the ⚠ Evidence flag here.]

## Summary
[Primary requirement + the technical approach in a sentence or two.]

## Technical Context
<!-- Read the actual repo. Don't guess. Mark real unknowns [NEEDS CLARIFICATION]. -->
**Language/Version**: [...]
**Primary Dependencies**: [...]
**Storage**: [... or N/A]
**Testing**: [...]
**Target Platform**: [...]
**Project Type**: [single / web / mobile / cli / service]
**Performance Goals**: [... or N/A]
**Constraints**: [... or N/A]
**Scale/Scope**: [...]

## Simplicity Gate
*Prefer the simplest design that satisfies the spec. Re-check after Phase 1.*
- [ ] No unjustified new services, layers, or abstractions.
- [ ] Complexity that remains is justified in the table below.

**Complexity justification** (only if the gate is not clean):
| Added complexity | Why it's needed | Simpler alternative rejected because |
|---|---|---|
| [...] | [...] | [...] |

## Phase 0 — Research / open questions
- [unknown → how it will be resolved]
- Decisions: | Decision | Rationale | Alternatives considered |

## Phase 1 — Design
- **Data model**: entities, fields, relationships, state transitions.
- **Contracts / interfaces**: API endpoints, events, CLI, or component boundaries.
- **Quickstart**: how to run/validate the feature end-to-end.

## Phase 2 — Tasks
Task generation → `tasks.md` (see tasks-template). Story order = evidence-weighted priority.
