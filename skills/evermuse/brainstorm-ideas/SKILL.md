---
name: brainstorm-ideas
description: 'Generate product ideas from PM, Designer, and Engineer perspectives — seeded by the real unmet needs customers actually voiced — and return an idea→evidencing-quote mapping. Use when the user asks to ''brainstorm ideas'', ''what should we build'', ''come up with feature ideas'', ''ideate solutions'', ''what could solve this problem'', or ''help me think of new features'' for either an existing product or a brand-new concept. Trigger terms: brainstorm, ideate, product ideas, feature ideas, come up with ideas, what should we build, solution ideas. Not for prioritizing an existing backlog (that''s prioritize-features) or writing the spec.'
category: Prioritization & Planning
tags:
- brainstorming
- ideation
- creativity
---

# Brainstorm Product Ideas (multi-perspective, evidence-seeded)

Multi-perspective ideation (PM / Designer / Engineer) for product discovery. The difference from a generic brainstorm: every idea is **seeded by a real unmet need** pulled from Evermuse and mapped back to the customer quote that justifies it. If an idea has no evidencing quote, it's flagged as a pure hypothesis.

## Step 0 — Relevance & availability
Confirm this is product ideation and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, produce framework-only ideas labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP — but say plainly the ideas are guesses, not evidence-seeded.

## Two modes (ask which, or infer)
- **Existing product** — continuous discovery. Lean on **`nature=evidence`**: mine unmet needs, pains, and feature asks from real conversations. This is the default and the strong mode.
- **New product / new concept** — initial discovery. Evidence may be thin, so lean more on **`nature=context`** (market/competitor signals) and **`nature=guidance`** (the company's own strategy/vision), and be honest that ideas rest on hypotheses rather than a customer corpus.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

1. **Understand the opportunity.** Confirm product, objective, target segment, and desired outcome. Ask if ambiguous — don't ideate against the wrong goal.

2. **Extract the unmet needs first.** Before generating anything, distill the grounded evidence into a short list of **customer unmet needs**, each with its sharpest verbatim quote and how many distinct accounts voiced it. These are the seeds. (In new-concept mode where evidence is thin, seed instead from market gaps and strategy, and say so.)

3. **Ideate from three perspectives** — generate ~5 ideas each, each idea explicitly tied to one of the seed needs where possible:
   - **Product Manager** — business value, strategic alignment, customer impact.
   - **Product Designer** — user experience, usability, delight, onboarding.
   - **Software Engineer** — technical possibilities, data leverage, scalable/novel solutions. ("Best ideas often come from engineers." — Teresa Torres.)

4. **Prioritize the top 5** across all perspectives. Weight by: strength of the evidencing signal (how many accounts, how sharp the pain), strategic alignment, impact on the desired outcome, feasibility, and differentiation. For a **new concept**, weight instead toward core value delivery, speed to validate, and differentiation.

5. **For each of the top 5**, give: a name + one-sentence description, why it was selected (naming the evidence), and the key assumption to validate next (hand off to `/evermuse:assumptions`).

## Deliverable — the idea→evidence mapping table

Lead with the top 5, then the full idea→evidence map so nothing is unsourced:

```markdown
### Top 5 ideas
1. **[Name]** — [one-sentence description]. *Selected because:* [reason naming the need].

### Idea → evidencing quote
| Idea | Persona lens | Seed need | Evidencing quote | Accounts |
|------|--------------|-----------|------------------|----------|
| [Idea] | PM/Design/Eng | [unmet need] | > "[verbatim]" — [Name], [Meeting], [Date] [`1`](LINK) | 3 |
| [Idea] | Eng | — | *hypothesis — no evidence yet* | 0 |
```

Be honest about thin evidence: an idea seeded by a single mention is a weaker bet than one seeded by six across distinct accounts — reflect that in the ranking, don't hide it.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) — brainstorm-ideas (existing + new). Product Trio & Opportunity Solution Tree: Teresa Torres, *Continuous Discovery Habits*.
