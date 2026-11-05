<!-- Adapted from github/spec-kit (MIT) clarify workflow — Evermuse-aware. -->
# Clarification Guide

Reduce ambiguity in a spec *before* drafting the body, the same way spec-kit's `/clarify` does — but check the customer evidence first, because it often answers the question for you.

## The evidence-first rule

Before you ask the user anything, ask the corpus. For each ambiguity, run a quick `evidence` search (keep the `quote`-type results). If customers already answered it (e.g. several described the same default behavior), that's your answer — cite it and don't spend a question on it. Only genuine, unresolved, high-impact ambiguities become questions.

## Ambiguity scan (categories to sweep)

- **Functional scope & behavior** — what's in/out; default vs. configurable.
- **Data & domain model** — entities, states, retention, ownership.
- **Interaction & UX flow** — entry points, steps, empty/error states.
- **Non-functional** — performance, scale, security, compliance the customer implied.
- **Integration & dependencies** — external systems the evidence references.
- **Edge cases & failure** — boundaries customers actually hit.
- **Terminology** — a word the team and customers use differently.

## Asking well (spec-kit constraints)

- **Cap: 3 questions.** Only the highest-impact unresolved items (architecture, data model, scope boundary, compliance).
- **Multiple-choice, evidence-attached.** Present 2–5 concrete options and hang the evidence on them so the user decides with the customer in the room:
  > **Default export scope?** Customers split: 3 want current-project only [`1`](URL) [`2`](URL) [`3`](URL), 1 wants the whole workspace [`4`](URL).
  > (a) Current project (recommended — matches majority) · (b) Whole workspace · (c) User-selectable
- **One at a time or as a short batch**, then fold answers into the spec, replacing each `[NEEDS CLARIFICATION]` marker.

## When evidence conflicts

If customers genuinely disagree, that's not a defect — surface it. Serve the majority in v1, note the minority as a fast-follow in Out of Scope, and cite both sides. Don't paper over the split.
