---
name: create-prd
description: 'Create a business Product Requirements Document from an 8-section template — problem, objectives, segments, value propositions, solution, release — grounded in real customer evidence (verbatim quotes, needs, pains with source links) from Evermuse. Use when the user wants to ''write a PRD'', ''create a PRD'', ''document product requirements'', ''draft a product doc'', or ''prd for [feature]''. Trigger terms: PRD, product requirements document, product doc, requirements doc, business case. Not for low-level API/interface specs — and use write-feature-spec instead when the user wants a rigorous, testable, story-by-story spec.'
category: Specs & Requirements
tags:
- prd
- requirements
- documentation
---

# Create a PRD (grounded in customer evidence)

Produce a comprehensive but readable Product Requirements Document — the business case for $ARGUMENTS — where the problem, the objective, the segments, and the value propositions are each backed by something a real customer actually said, with a source link. A generic PRD reads plausibly; this one reads *true*, because the "why" comes from the corpus.

> **Pick the right sibling.** `create-prd` (this skill) = a lighter **8-section business PRD** for aligning stakeholders and leadership on the what/why. `write-feature-spec` = the **rigorous, spec-driven** sibling with prioritized user stories, Given/When/Then acceptance scenarios, and measurable success criteria for a team to build from. When unsure which the user wants, offer both.

## Step 0 — Relevance & availability
Confirm this is customer-facing product work and the Evermuse tools are present. If the MCP isn't connected, produce the PRD from the template but label it **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. (See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`, Step 0.)

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

1. **Anchor each section in evidence, not assertion.** Walk the 8 sections in `references/prd-template.md`. For each, ask what the corpus says before you write:
   - **Background / Why now** — what changed for customers? Lead with the pain, quoted. A quote-angled `search` on the problem.
   - **Objective + Key Results** — the objective maps to an *evidenced customer outcome*; the KRs measure *reduction of a stated pain*. (For a full OKR set, chain to `brainstorm-okrs`.)
   - **Market Segment(s)** — segments are defined by the *problem/job* customers described, not demographics. Name the accounts/personas the evidence actually came from.
   - **Value Proposition(s)** — each pain avoided / gain created is a real quote, not a guess. This is where the customer's voice does the most work.
   - **Solution** (UX, key features, tech, assumptions) — flag assumptions explicitly so the team can validate them.
   - **Release** — relative timeframes (now / next / later), never hard dates.
2. **Reuse grounding across the session.** If a spec, OKR set, or research brief already pulled this evidence, carry the quotes and source badges forward instead of re-searching (credits — Rule 7).
3. **Write for a wide audience.** Short sentences, minimal jargon; a PRD is read by leadership and engineers alike.
4. **Working-Backwards variant (optional).** If the user wants an Amazon-style press release / FAQ instead of (or before) the full PRD, use `references/wwas-press-release-template.md`. Its customer-quote sections must use **real customer quotes** from a quote-angled `search`, attributed — never invented testimonials.

## Deliverable
An 8-section PRD (or the Working-Backwards press release) as clean markdown, with a **Customer Evidence** callout near the top summarizing themes + demand strength and inline citation badges throughout (links live inline — no Sources footer). Offer to save it (guidance).

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT).
- [PRD template](https://www.productcompass.pm/p/prd-template) · [AI PRD template](https://www.productcompass.pm/p/ai-prd-template)
- Rigorous sibling: `${CLAUDE_PLUGIN_ROOT}/skills/write-feature-spec/SKILL.md`
