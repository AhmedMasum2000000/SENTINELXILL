<!-- Adapted from github/spec-kit (MIT) checklist — plus Evermuse evidence-coverage gates. -->
# Spec Quality Checklist

Run before declaring a spec done. Anything unchecked gets fixed or explicitly flagged.

## Structure & testability (spec-kit)
- [ ] Every user story has an explicit priority (P1, P2, …).
- [ ] Each story is **independently testable** — implementing just one yields a viable slice.
- [ ] **P1 is a true MVP** — the smallest thing that delivers real value.
- [ ] Each story has ≥1 Given/When/Then acceptance scenario.
- [ ] Functional requirements are specific and testable (no "fast", "intuitive", "robust" without a measure).
- [ ] Success criteria are **measurable** and **technology-agnostic** (no framework/API/DB specifics).
- [ ] ≤ 3 `[NEEDS CLARIFICATION]` markers remain, each genuinely unresolved.
- [ ] Edge cases and error scenarios are covered.
- [ ] Out-of-scope items are stated.

## Evidence coverage (Evermuse)
- [ ] The **Customer Evidence** section is present with real themes and demand strength (counts across distinct accounts).
- [ ] Every claim of the form "customers want / need / struggle with X" carries a **source badge** or is explicitly marked a **hypothesis**.
- [ ] At least the P1 story has an **Evidence:** quote (if any evidence exists for the feature at all).
- [ ] Dissenting/minority voices are represented, not smoothed over.
- [ ] Every inline citation badge [`1`](URL) links to a real Evermuse `url`; none are fabricated or renumbered.
- [ ] Secondary assets (shaping notes, roadmap) — if referenced — are labeled as such, not cited as customer voice.

## Honesty
- [ ] No invented quotes, speakers, meetings, or links.
- [ ] Where evidence was thin, the spec says so rather than overclaiming demand.
