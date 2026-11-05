---
name: analyze-feature-requests
description: 'Triage a pile of customer feature requests into themes, merge duplicates, and surface the underlying need behind each ask — pulling the requests straight from Evermuse notes and backing every theme with quotes. Use when the user asks to ''triage feature requests'', ''group these requests'', ''what are customers asking for'', ''find duplicate requests'', ''what''s the real need here'', or ''cluster the feedback''. Trigger terms: feature requests, triage requests, group requests, duplicate requests, underlying need, cluster feedback. Not for scoring a curated backlog (that''s prioritize-features).'
category: Customer Voice & Feedback
tags:
- feature-requests
- feedback
- triage
- analysis
---

# Analyze Feature Requests (theme, dedupe, find the real need)

Turn a messy pile of customer asks into named themes with the duplicates merged and the **underlying need** surfaced behind each one — "never allow customers to design solutions; prioritize the problem." The requests don't come from a spreadsheet the user pastes; they come straight from Evermuse, so the triage reflects the whole corpus, not just what someone remembered to forward.

## Step 0 — Relevance & availability
Confirm this is request triage and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, ask the user to paste the requests and label the output **⚠ ungrounded** — but the point of this skill is pulling them from the corpus, so prefer to fix the connection.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

1. **Confirm the product goal** the triage serves — it decides which themes matter, and strategic alignment can't be judged without it.

2. **Cluster into themes.** Group the notes into named themes. Collapse **duplicates and near-duplicates** (different words, same ask) into one theme with a combined count. Note when the *same* customer asked repeatedly vs. many distinct accounts — distinct accounts is the stronger signal.

3. **Surface the underlying need.** For each theme, look past the requested solution to the job/pain driving it. "Add a CSV button" and "let me email this to my boss" may both be *"I need to get this data out to share it."* Name that need — it's what you'll actually prioritize and build against.

4. **Assess each theme** on demand strength (distinct accounts), sentiment, strategic alignment, and rough effort/risk. Open hot items with `view_item` to get specifics.

5. **Recommend the top 3 themes** to act on, each with: the underlying need, the customer evidence (counts + quotes), alternative solutions worth considering, the highest-risk assumption, and a cheap way to test it (hand off to `/evermuse:assumptions`).

## Deliverable

```markdown
**Goal:** [product objective the triage serves]

### Themes
| Theme | Underlying need | Requests (distinct accounts) | Dupes merged | Sentiment | Aligned? |
|-------|-----------------|------------------------------|--------------|-----------|----------|
| Data export | "get my data out to share it" | 9 (6 accts) | 4 | frustrated | ✓ |

### Top 3 to act on
1. **[Theme]** — need: […]. Evidence: > "[verbatim]" — [Name], [Meeting], [Date] [`1`](LINK) (6 accounts). Alt solutions: … Riskiest assumption: … Test: …
```

Be honest when a "hot" request is really one loud account repeating itself — say so rather than inflating it into a trend.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) — analyze-feature-requests. Opportunity Score for problem-ranking: Dan Olsen, *The Lean Product Playbook*.
