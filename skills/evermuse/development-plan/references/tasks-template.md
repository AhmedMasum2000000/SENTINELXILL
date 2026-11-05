<!-- Adapted from github/spec-kit (MIT) tasks-template — story order is evidence-weighted; each story carries its motivating quote. -->
# Tasks: [FEATURE NAME]

**Input**: `specs/[###-feature-name]/plan.md` (+ spec.md for user stories)

## Format: `[ID] [P?] [Story] Description`
- **[P]**: can run in parallel (different files, no dependencies)
- **[Story]**: which user story (US1, US2, …); omit for Setup/Foundational/Polish
- Include exact file paths.

## Phase 1: Setup (shared infrastructure)
- [ ] T001 Create project structure per plan
- [ ] T002 Initialize dependencies
- [ ] T003 [P] Configure linting/formatting

## Phase 2: Foundational (blocking prerequisites)
**⚠️ No user-story work begins until this phase completes.**
- [ ] T004 [foundational task — schema, auth, routing, base models, error handling…]
- [ ] T005 [P] [...]

## Phase 3: User Story 1 — [Title] (Priority: P1) ← strongest customer signal
> Building this because: "[one-line motivating quote]" — [Name] [`1`](URL)
**Goal**: [story goal] · **Independent test**: [how to verify standalone]
- [ ] T00X [US1] [model/service/endpoint task + file path]
- [ ] T00X [P] [US1] [...]
**Checkpoint**: US1 is fully functional and independently demoable.

## Phase 4: User Story 2 — [Title] (Priority: P2)
> Building this because: "[quote]" — [Name] [`2`](URL)
- [ ] T0XX [US2] [...]
**Checkpoint**: US2 works independently.

## Phase N: Polish & cross-cutting
- [ ] T0XX [P] Docs / cleanup / performance / security pass

## Dependencies
- Setup → Foundational → (US1, US2, … in priority order) → Polish
- `[P]` tasks within a phase can run together.

## Implementation strategy
- **MVP** = Setup + Foundational + US1. Ship, learn, then add US2+.
