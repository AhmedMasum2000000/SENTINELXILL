---
name: test-scenarios
description: 'Create QA test scenarios in Given/When/Then form from a spec''s acceptance criteria AND from the real edge cases customers actually hit — failure stories and complaints pulled from Evermuse so the test plan covers reality, not just the happy path. Use when the user wants to ''write test scenarios'', ''create test cases'', ''build a test plan'', ''define acceptance tests'', or ''QA scenarios for [feature]''. Trigger terms: test scenarios, test cases, QA test plan, acceptance tests, Given/When/Then, edge cases. Not for unit-test code generation with no customer-facing behavior.'
category: Delivery & Engineering
tags:
- testing
- scenarios
- qa
---

# Test Scenarios (grounded in real customer edge cases)

Build a QA test plan for $ARGUMENTS that covers two sources: the **acceptance criteria** in the spec/stories, *and* the **edge cases customers actually hit** — the failure stories, complaints, and "it broke when…" moments in the corpus. Most test plans over-test the happy path and miss the failures customers already reported; this one closes that gap.

## Step 0 — Relevance & availability
Confirm this is customer-facing feature validation and Evermuse is present. If the MCP isn't connected, derive scenarios from the acceptance criteria alone and label the plan **⚠ ungrounded — edge-case coverage from evidence unavailable**; tell the user to authorize the MCP. (See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`, Step 0.)

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

1. **Two sources, clearly separated:**
   - **From acceptance criteria** — for each AC, one positive scenario (the AC holds) and its negative/deny counterpart.
   - **From evidenced edge cases** — for each real failure story in the corpus, a scenario reproducing that condition and asserting the fixed behavior. These are the high-value tests. Replace the source skill's generic "consider edge cases" with **actual customer-reported failures** as the primary edge-case source.
2. **Write each scenario in Given/When/Then** (with the fuller template for hand-off to QA):
   - **Given** starting conditions (system state, data, permissions).
   - **When** the user action / trigger.
   - **Then** the expected, observable outcome — including the negative/deny case.
3. **Tag each scenario** with its source — an acceptance criterion (`AC-##`) or an evidence citation badge [`1`](URL) — and priority. Edge cases customers *actually hit* rank **High** by default — they've already caused real pain.
4. **Cover the boundaries** the evidence reveals: bad input, concurrency, permission edges, limits customers bumped into.
5. **Chain from stories.** If `user-stories` ran this session, reuse its ACs and grounding rather than re-searching (credits — Rule 7).

## Scenario template
```
Test Scenario: [name]            Source: [AC-## | evidence [`1`](URL)]    Priority: [High/Med/Low]
Objective: [what this validates]
Given: [system state / data / permissions]
When:  [action / trigger]
Then:  [observable outcome — include the deny/negative case]
```
Group by source (AC-derived, then evidence-derived), with inline citations.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT).
- Pairs with `${CLAUDE_PLUGIN_ROOT}/skills/user-stories/SKILL.md` and `${CLAUDE_PLUGIN_ROOT}/skills/write-feature-spec/SKILL.md`.
