---
name: write-feature-spec
description: 'Write a feature specification grounded in real customer evidence — verbatim quotes, needs, and pain points with source links from Evermuse — using spec-driven-development structure (prioritized user stories, Given/When/Then acceptance scenarios, functional requirements, measurable success criteria). Use when the user wants to write a spec, feature spec, ''spec out'' a feature, or turn an idea into a rigorous specification. Trigger terms: write a spec, feature spec, specify, spec out, user stories with acceptance criteria. Not for low-level API/interface specs with no customer-facing behavior; for a lighter business PRD, use create-prd.'
category: Specs & Requirements
tags:
- spec
- user-stories
- acceptance-criteria
---

# Write a Feature Spec (grounded in customer evidence)

Produce a feature specification that a team can build from — with the rigor of spec-driven development **and** the customer's own voice woven through it. The difference between this and a generic spec is that every "why", every priority, and every edge case is backed by something a real customer actually said, with a source link.

> This is the rigorous, spec-driven sibling of `create-prd`. Use `write-feature-spec` when you want prioritized user stories, testable acceptance scenarios, and measurable success criteria. Use `create-prd` for a lighter 8-section business PRD. When unsure, offer both.

## Step 0 — Relevance & availability
Confirm this is customer-facing product work and the Evermuse tools are present. If the MCP isn't connected, produce the spec from the templates but label it **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. (See `using-evermuse` SKILL.md, Step 0.)

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Clarify before drafting (spec-kit discipline)
Scan for ambiguity using `references/clarification-guide.md`. Two rules:
1. **Check evidence before asking.** Often the corpus already answers the question — if three customers described the same workflow, that's your answer; cite it and move on.
2. **Cap at 3 `[NEEDS CLARIFICATION]` markers.** Present each as a short multiple-choice question, and **attach the evidence** to it: "Customers split on default scope — 3 quotes want per-project export [`1`](URL) [`2`](URL) [`3`](URL), 1 wants everything [`4`](URL). Which do we serve in v1?" Resolve, then draft.

## Draft the spec
Fill `references/spec-template.md`. Beyond the standard spec-kit sections it adds:
- A **Customer Evidence** section up top: the themes you found, demand strength (counts across distinct accounts), and dissenting voices — quote-rich, badged.
- An **Evidence:** line under each prioritized user story (the quote that motivates it).
- An inline linked-number badge [`1`](URL) on functional requirements that trace to a customer ask.
- Success criteria (SC-###) that are technology-agnostic and, where possible, tied to the *magnitude* of the observed pain.
- An **Assumptions** section split into "Confirmed (cited)" vs "Assumed (no signal yet)".

## Quality gate
Run `references/spec-quality-checklist.md` before finishing: every user story independently testable, P1 is a true MVP slice, every claimed customer need is either badged or explicitly marked a hypothesis, ≤3 clarification markers, success criteria measurable and tech-agnostic.

## Save & hand off
Write the spec to `specs/<feature-slug>/spec.md` in the working directory (create the folder). Save it back to Evermuse (nature `guidance`). Then offer the next step: **"Want me to turn this into a development plan?"** (`/evermuse:dev-plan`).

---
### Further reading
- Spec structure adapted from [github/spec-kit](https://github.com/github/spec-kit) (MIT).
- Evidence discipline is the core of the Evermuse plugin — see `using-evermuse`.
