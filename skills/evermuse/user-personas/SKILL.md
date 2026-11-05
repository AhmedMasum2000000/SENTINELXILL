---
name: user-personas
description: 'Build user personas from the real people in a company''s customer corpus — 3 evidence-backed personas with jobs-to-be-done, pains, gains, and an ''in their own words'' verbatim quote block each. Use when the user says ''build personas'', ''create user personas'', ''who are our users'', ''make a persona for X'', ''segment our users into profiles'', or wants research-backed profiles instead of invented archetypes. Trigger terms: personas, user persona, buyer persona, who are our users, JTBD profiles, user archetypes. Not for fictional marketing avatars invented without evidence.'
category: Discovery & Research
tags:
- personas
- users
- research
---

# User Personas (from real people, not archetypes)

Produce 3 personas that a skeptical stakeholder can't dismiss as made up — because every trait, pain, and goal traces to a real person who appears in the Evermuse corpus, and each persona carries a block of that person's own words. A persona nobody in the corpus resembles is a failure of this skill.

## Step 0 — Relevance & availability
Confirm this is user/customer profiling work and Evermuse is connected (see `using-evermuse` Step 0). If the MCP isn't connected, produce framework-only personas labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. Never present invented archetypes as research-backed.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.
- **one `find_sources` browse** (no `query`, `limit` up to 50) to map who actually exists in the corpus — the attendees, accounts, and domains across sources. Personas are composites of these real people; this call is the raw material for Instructions step 1.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

Build **3 refined personas for $ARGUMENTS**, grounded entirely in the corpus.

1. **Map who's really there.** From `find_sources`, list the distinct people/accounts. This is your raw material — personas are composites of these real users, not personas you'd expect the market to have.
2. **Cluster by job and behavior.** Group the real people by shared jobs-to-be-done, workflows, and motivations. Distinct *needs*, not distinct age brackets. Aim for 3 non-overlapping personas; if the corpus only supports 2, say so rather than padding.
3. **Enrich each persona from evidence**, using the structure below. Where the source method would reach for a survey or "if the user provides data", reach for `evidence` searches and a quote-angled `search` instead.
4. **Validate.** Every attribute must trace to something a real person said or did. Flag any trait you're inferring vs. one that's directly evidenced.

### Persona structure (each of the 3)

**Name & snapshot** — a memorable label + role/context (the composite of who this represents in the corpus).

**Primary job-to-be-done** — the core outcome they're trying to achieve, with context and frequency, drawn from what they described.

**Top 3 pains** — each a real obstacle, each badged with the account(s) it came from and severity.

**Top 3 gains** — the outcomes they seek and how they'd measure success.

**One unexpected insight** — a counterintuitive pattern the evidence reveals, and why it matters for the product.

**In their own words** (required) — a block of 2–4 verbatim quotes from real people in this cluster:
```markdown
> "[verbatim quote]" — [Name], [Meeting], [Date] [`1`](URL)
> "[verbatim quote]" — [Name], [Meeting], [Date] [`2`](URL)
```

**Product fit** — how $ARGUMENTS serves (or fails) this persona, with the friction points evidenced.

End with a one-line honesty note if any persona rests on thin evidence (e.g. "Persona C: only 2 accounts — validate with more interviews"). Offer `/evermuse:customer-research` to go deeper on any one persona.

---
### Further reading
- Persona method adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT); grounding is Evermuse-native. See also the [JTBD Masterclass](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with).
