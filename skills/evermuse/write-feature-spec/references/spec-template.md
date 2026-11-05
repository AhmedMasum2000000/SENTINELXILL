<!-- Adapted from github/spec-kit (MIT) — extended with an Evermuse Customer Evidence layer. -->
# Feature Specification: [FEATURE NAME]

**Feature slug**: `[###-feature-name]`
**Created**: [DATE]
**Status**: Draft
**Product (Evermuse)**: [product name] · **Grounding**: [N evidence searches, M quotes] or ⚠ ungrounded
**Input**: "$ARGUMENTS"

## Customer Evidence *(Evermuse — mandatory when grounded)*

The voice of the customer behind this feature. Fill from `search` (nature=evidence) + a quote-angled `search`.

**Themes & demand strength**
- **[Theme 1]** — [N mentions across M accounts]. [one-line summary]
  > "[verbatim quote]" — [Name], [Meeting], [Date] [`1`](URL)
- **[Theme 2]** — …

**Dissenting / minority voices** (what a subset wants differently)
- > "[verbatim quote]" — [Name], [Meeting], [Date] [`2`](URL)

**Strategy fit** (nature=guidance) — [how this ladders to a stated company objective, if found] [`3`](URL)

## User Scenarios & Testing *(mandatory)*

<!-- Stories PRIORITIZED as user journeys. Each MUST be INDEPENDENTLY TESTABLE — implementing just one still yields a viable MVP slice. P1 = most critical. -->

### User Story 1 - [Brief Title] (Priority: P1)
[User journey in plain language.]

**Why this priority**: [value + why now]
**Evidence**: > "[quote that motivates this story]" — [Name, Meeting, Date] [`4`](URL)
**Independent Test**: [how this is tested standalone and delivers value]
**Acceptance Scenarios**:
1. **Given** [state], **When** [action], **Then** [outcome]
2. **Given** [state], **When** [action], **Then** [outcome]

---

### User Story 2 - [Brief Title] (Priority: P2)
[…as above, with its own **Evidence:** line where evidence exists…]

---

### User Story 3 - [Brief Title] (Priority: P3)
[…]

### Edge Cases
<!-- Prefer edge cases a real customer actually hit; cite them. -->
- What happens when [boundary]? [customer who hit it, if any] [`5`](URL)
- How does the system handle [error scenario]?

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: System MUST [capability]. [`6`](URL) if it traces to a customer ask
- **FR-002**: System MUST [capability].
- **FR-003**: Users MUST be able to [interaction].
<!-- Mark unresolved items (max 3 across the spec): -->
- **FR-00X**: System MUST [capability] via [NEEDS CLARIFICATION: question — with evidence attached]

### Key Entities *(if the feature involves data)*
- **[Entity]**: [what it represents, key attributes, relationships — no implementation]

## Success Criteria *(mandatory)*

<!-- Measurable AND technology-agnostic. Tie to the magnitude of the observed pain where possible. -->
- **SC-001**: [e.g. "Users complete [task] in under [time]"]
- **SC-002**: [e.g. "Reduce [evidenced pain] — [X]% fewer [complaints/tickets] about [Y]"]
- **SC-003**: [adoption/satisfaction metric]

## Assumptions

**Confirmed (cited)** — backed by evidence:
- [assumption] [`7`](URL)

**Assumed (no signal yet)** — flag for validation:
- [assumption] — *no customer evidence; validate before building.*

## Out of Scope
- [explicitly not doing, and why]
