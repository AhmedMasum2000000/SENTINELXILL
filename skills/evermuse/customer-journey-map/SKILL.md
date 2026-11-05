---
name: customer-journey-map
description: 'Map the end-to-end customer journey — awareness through advocacy — with the real pain point, emotion, and a verbatim customer quote at each stage, plus prioritized fixes. Use when the user says ''map the customer journey'', ''map the user journey'', ''where do users drop off'', ''improve onboarding'', ''what does the customer experience look like'', or wants a journey/experience map grounded in real feedback. Trigger terms: customer journey, journey map, user journey, drop-off, onboarding friction, moments of truth, experience map. Not for internal process/workflow diagrams with no customer involved.'
category: Discovery & Research
tags:
- journey-map
- ux
- customer-experience
---

# Customer Journey Map (evidence at every stage)

Map the journey from first awareness to advocacy — and make each stage carry a real customer's words about the friction there. A journey map with plausible-but-invented pains is just a diagram; this one shows, stage by stage, where real users actually struggle and what they said about it.

## Step 0 — Relevance & availability
Confirm this is a customer-experience question and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, produce the framework labeled **⚠ ungrounded** and tell the user to authorize the MCP.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

Build the journey map for **$ARGUMENTS**.

1. **Name the traveler.** Use a specific persona with a JTBD, not a generic user — reuse one from `/evermuse:user-personas` if it exists in the session.
2. **Map the stages** (adapt to the product): Awareness → Consideration → Acquisition → Onboarding → Engagement → Retention → Advocacy.
3. **For each stage, document** — grounding each pain in the notes/quotes you pulled, not in intuition:
   - **Touchpoints** — where they interact (site, email, in-app, support).
   - **User actions** — what they do here.
   - **Thoughts & questions** — what's on their mind.
   - **Emotion** — how they feel (emoji or –2…+2 scale), inferred from the sentiment of real feedback where available.
   - **Pain point** — the real friction, **badged with a quote**.
   - **Opportunity** — how to fix it.
4. **Mark the critical moments:** the **aha moment** (first real value), **moments of truth** (commit/abandon), and **churn triggers** — anchor each to evidence.

### The map

```markdown
| Stage | Touchpoint | Action | Emotion | Pain (evidence) | Opportunity |
|---|---|---|---|---|---|
| Onboarding | in-app setup | connects data source | 😣 –1 | "I gave up wiring it in on day one" — [Name], [Mtg], [Date] [`1`](URL) | guided setup wizard |
```

Under the table, put a **stage-by-stage quote reel** — the sharpest verbatim line per painful stage — then **prioritized improvements** (highest impact on conversion/retention first; quick wins vs. deeper bets). Every quote carries its inline badge.

If a stage has no evidence in the corpus, say so explicitly ("no feedback captured for Advocacy") rather than inventing a pain — that gap is itself a finding. For a visual map, suggest recreating this in FigJam/Miro.

---
### Further reading
- Journey-map structure adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT); grounding is Evermuse-native. See [User Journey Mapping 101](https://www.productcompass.pm/p/user-journey-mapping-101).
