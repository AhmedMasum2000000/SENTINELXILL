---
name: sentiment-analysis
description: 'Analyze the feedback corpus over a time period to surface sentiment, themes, and satisfaction shifts — with a score per theme and verbatim quotes carrying their own sentiment labels. Use when the user says ''how do users feel about X'', ''what''s the sentiment on Y'', ''analyze feedback from last quarter'', ''are customers happy'', ''what are people complaining about'', or wants a satisfaction/theme read across feedback. Trigger terms: sentiment analysis, how do users feel, customer satisfaction, feedback themes, complaints, are customers happy, sentiment over time. Not for analyzing a single conversation (use customer-research).'
category: Customer Voice & Feedback
tags:
- sentiment
- feedback
- analysis
---

# Sentiment Analysis (feedback corpus over a period)

Read the mood of the feedback corpus — for a topic, a segment, or a time window — and turn it into scored themes backed by real quotes. Not a vague "customers seem happy," but "onboarding sentiment is –0.4 this quarter, driven by setup friction, and here are the six people who said so."

## Step 0 — Relevance & availability
Confirm this is a feedback/satisfaction question spanning multiple conversations and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, produce the framework labeled **⚠ ungrounded** and tell the user to authorize the MCP. For a single conversation's sentiment, use `/evermuse:customer-research` instead.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

Analyze sentiment for **$ARGUMENTS** over the specified period (or all-time if none given — state which).

1. **Inventory** the feedback pulled — count of notes, date span, distinct accounts. If the window is thin, say so before scoring.
2. **Cluster into themes** — recurring topics of praise and complaint. Aim for a handful, not one bucket.
3. **Score each theme** — a sentiment score from **–1 to +1**, derived from the `sentiment_analysis` labels on the underlying quotes, not vibes. Note the split (e.g. "mostly negative, 5 of 7 mentions").
4. **Separate drivers** — for each theme, the satisfaction drivers vs. detractors, each with a real example.
5. **Track shift over time** — if the window allows, whether sentiment on a theme is rising or falling, and against what (a release, a change).

### Output

Lead with a one-line **overall read** (net sentiment + the single biggest driver), then per theme:

```markdown
### [Theme] — sentiment [score] ([N mentions / M accounts], mostly [pos/neg])
**Loves:** [driver]
> "[verbatim]" — [Name], [Meeting], [Date] · sentiment: [positive] [`1`](URL)
**Frustrations:** [detractor]
> "[verbatim]" — [Name], [Meeting], [Date] · sentiment: [negative] [`2`](URL)
```

Then **top pain points ranked by frequency × severity** and **2-3 highest-impact recommendations**. Represent minority/dissenting sentiment — don't flatten a split into a false consensus. Flag any theme resting on a small sample. Offer `/evermuse:customer-research` to drill into any single theme.

---
### Further reading
- Sentiment-synthesis method adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT); grounding is Evermuse-native.
