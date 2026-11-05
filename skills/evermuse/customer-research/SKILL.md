---
name: customer-research
description: 'Answer questions about what customers actually think, need, ask for, or complain about — by searching real customer evidence in Evermuse and returning a quote-rich, source-linked brief. Use when the user asks ''what do customers think about X'', ''have customers asked for Y'', ''what are the biggest pain points'', ''who mentioned Z'', ''why are users churning'', or wants voice-of-customer / user-research / feedback synthesis. Trigger terms: what do customers think, customer feedback, user research, voice of customer, pain points, what are customers saying, have customers asked for.'
category: Discovery & Research
tags:
- research
- customers
- insights
---

# Customer Research (voice-of-customer synthesis)

The everyday workhorse: someone asks a question about customers and gets back not a plausible guess but a **quote-rich, sourced brief** drawn from real conversations. This is the skill that most visibly changes the agent's behavior after Evermuse is installed — so lean into the evidence.

## Step 0 — Relevance & availability
Confirm it's a customer question and Evermuse is connected. If not connected, say so plainly and tell the user to authorize the MCP — don't answer a "what do customers think" question from memory and pass it off as grounded.

## Scope the question
Pin down what's really being asked: a topic ("onboarding"), a decision it feeds ("should we build X"), a segment or time window. If a research **project** is clearly implied (e.g. "the audio-listeners study"), pass its `project_id` on your calls; otherwise stay at product scope.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Synthesize
Cluster the evidence into **themes**, and for each: demand strength (mentions across distinct accounts), sentiment split, who said it and when, and the sharpest verbatim quote. Represent **dissenting voices** — don't flatten disagreement into a false consensus. Separate `evidence` (what customers said) from any `context` (market) you pulled; never blend them.

## Deliver
When you cite, use the inline linked-number badge per `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/references/citations.md` — [`1`](URL). Citations are optional, but a voice-of-customer brief is far stronger with them, so prefer them here.

A brief that leads with the answer, then themes with quote blocks and inline citations:

```markdown
**Short answer:** [1–2 sentences that directly answer the question.]

### Theme 1 — [name] ([N mentions / M accounts], mostly [sentiment])
> "[verbatim quote]" — [Name], [Meeting], [Date] [`1`](URL)
[one line of interpretation]

### Theme 2 — …

**Dissent / nuance:** [minority view, cited]
```

## Save & hand off
Offer to save the brief: `add_source(nature: "evidence", source_type: "document", tags: ["evermuse-plugin","research","voice-of-customer","<topic>"])`. Then offer next steps: **"Want a spec from this?"** (`/evermuse:spec`), **"Brainstorm solutions?"** (`/evermuse:brainstorm`), or **"Prioritize against the roadmap?"**

## Honesty when evidence is thin
If searches come back sparse, **say so** — "only 2 mentions, both from one account" — rather than dressing a weak signal as a trend. Thin evidence is itself a finding (maybe it's worth an interview: offer `/evermuse:interview`).

---
### Further reading
- Research method draws on [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT); grounding is Evermuse-native.
