---
name: review-pr
description: 'Review a pull request against three things at once: code quality, the spec it was meant to satisfy, and the actual customer asks behind it — calling out where the diff diverges from what customers literally requested. Use when the user asks to ''review this PR'', ''review the diff'', ''check this PR against the spec'', or wants a customer-voice-aware code review. Trigger terms: review this PR, review the diff, PR review, check against the spec, does this match what customers asked. Defer to a dedicated code-review tool if the user names one and only wants code quality.'
category: Delivery & Engineering
tags:
- code-review
- pr
- quality
---

# Review a PR (against code, spec, and customer voice)

A normal review asks "is the code good?" This one also asks "does it build what was specified?" and — uniquely — "does it match what customers actually asked for?" That third pass catches the gaps other reviews miss: the export that works but drops the header row a customer explicitly needed.

## Step 0 — Relevance & availability
Confirm this is a customer-facing PR and Evermuse is available. If the user only wants code-quality feedback (or names a dedicated reviewer), do that and skip the customer lens.

## Fetch the PR
Prefer `gh pr view <n>` / `gh pr diff <n>` (or the current branch's diff). Optionally try the Evermuse third-party bridge to GitHub (`find_tool` → `call_tool`); **degrade gracefully** to `gh` if it's blocked (see `third-party-bridge.md`). If neither works, ask the user to paste the diff.

## Find the intent
What was this PR *supposed* to do?
1. **Shaping notes** carry `branch` and `PR number` fields — `get_shaping_notes` and match on the PR/branch, then `read_shaping_note` for the intent and its citations.
2. Else a local `specs/<feature>/spec.md`.
3. Else ask the user for the intended behavior in a sentence.

## Ground in the customer's asks
Run the required grounding batch (see **Evermuse Grounding** below) scoped to this feature area, so you know what customers literally requested about *this* behavior. This is what powers Pass 3.

## Three review passes
1. **Code quality** — correctness, edge cases, error handling, security, tests, style/conventions. Standard, focused review; report only real issues.
2. **Spec conformance** — does the diff satisfy each relevant FR-###? Note requirements that are unmet, partially met, or exceeded (scope creep).
3. **Customer-voice conformance** — does the *behavior* match what customers asked for? Quote-vs-diff mismatches are the headline:
   > Customer asked: "export with the header row, we paste into our template" [`1`](URL). The diff writes rows without a header (`export.ts:41`). ❌ Mismatch.

## Verdict
Lead with a clear recommendation — **Approve / Approve with nits / Request changes** — and the single most important reason. Then the three passes as sections. Keep code nits concise; make the customer-voice findings vivid and cited.

## Save (optional)
Offer to save the review summary: `add_source(nature: "guidance", source_type: "document", tags: ["evermuse-plugin","pr-review","pr-<n>"])`. If the bridge allows and the user wants, offer to post it as a PR comment via `call_tool`.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

---
### Further reading
- Customer-voice review is unique to the Evermuse plugin; see `using-evermuse`.
