---
name: user-stories
description: 'Break a feature into user stories (or job stories) — INVEST-shaped, 3-C''s structure, each story citing the motivating customer quote and acceptance criteria that reflect what customers actually expect, grounded in Evermuse evidence. Use when the user wants to ''write user stories'', ''break this into stories'', ''create backlog items'', ''define acceptance criteria'', or ''write job stories''. Trigger terms: user stories, job stories, backlog items, acceptance criteria, story breakdown, JTBD stories. Not for a full spec or PRD — use write-feature-spec or create-prd for those.'
category: Specs & Requirements
tags:
- user-stories
- agile
- requirements
---

# User Stories & Job Stories (grounded in customer evidence)

Turn a feature ($ARGUMENTS) into a set of independent, testable stories where **each story cites the customer quote that motivates it**, and every acceptance criterion reflects a *stated* customer expectation — not an invented one. This is the difference between a backlog of guesses and a backlog you can defend.

## Step 0 — Relevance & availability
Confirm this is customer-facing product work and Evermuse is present. If the MCP isn't connected, produce the stories from the templates but label them **⚠ ungrounded** and tell the user to authorize the MCP. (See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`, Step 0.)

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

1. **Pick the format that fits.** Both are valid; choose per the user's ask (offer to switch):
   - **User story** — role-centric: *"As a [role], I want [action], so that [benefit]."* Follows the **3 C's** (Card / Conversation / Confirmation).
   - **Job story** — situation-centric (JTBD): *"When [situation], I want to [motivation], so I can [outcome]."* Reach for this when the *trigger/context* matters more than the role, which the evidence often reveals.
2. **Derive stories from the evidence, not the design alone.** Group quotes and needs by distinct user situations/jobs; each cluster becomes one story. Replace the source skill's reliance on "$DESIGN + $ASSUMPTIONS" with **evidence as the primary driver** — designs and assumptions refine stories, but the corpus decides which stories exist and how they rank.
3. **Respect INVEST.** Independent, Negotiable, Valuable, Estimable, Small, Testable. Split any story too big for one sprint.
4. **Write acceptance criteria that mirror stated expectations.** Each AC should trace to something a customer expressed — a needed behavior, an edge case they hit, a performance bar they complained about. 4–6 criteria per story; observable and testable.
5. **Rank by demand.** Order stories by how strongly the evidence backs them (mentions across accounts). Flag any story that's a guess (no evidence) as **assumption — validate**.
6. **Chain onward.** Stories feed `test-scenarios` (Given/When/Then from these ACs) and `write-feature-spec`. Reuse this grounding rather than re-searching (credits — Rule 7).

## Story templates

**User story**
> **Title:** [feature name]
> **As a** [role], **I want** [action], **so that** [benefit]. [`1`](URL)
> **Design:** [link]
> **Acceptance Criteria:** 1–6 observable, testable criteria — each tracing to a stated expectation.

**Job story**
> **Title:** [job outcome]
> **When** [situation], **I want to** [motivation], **so I can** [outcome]. [`1`](URL)
> **Design:** [link]
> **Acceptance Criteria:** 6–8 outcome-focused criteria (situation recognized, motivation enabled, feedback visible, edge cases handled).

Each story block ends with its inline citation.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) — merges `user-stories` + `job-stories`.
- [How to Write User Stories](https://www.productcompass.pm/p/how-to-write-user-stories) · [JTBD Masterclass](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with)
