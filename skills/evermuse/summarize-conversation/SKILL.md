---
name: summarize-conversation
description: 'Summarize one customer interview or team meeting into structured notes — participants, needs/JTBD, verbatim quotes with timestamps, decisions, action items — by locating the conversation in Evermuse and reading its transcript. Use when the user says ''summarize this interview'', ''summarize the meeting'', ''recap the call'', ''meeting notes'', ''meeting minutes'', or ''write up the interview''. Trigger terms: summarize meeting, summarize interview, meeting notes, meeting minutes, recap the call, interview summary. Not for research across many calls (that''s customer-research).'
category: Ops & Meta
tags:
- summary
- handoff
- documentation
---

# Summarize a Conversation (interview or meeting)

Turn one specific conversation into a structured, accessible summary — pulling needs, decisions, and **verbatim quotes with timestamps** out of the actual transcript. This is the **sanctioned place to use `read_source`**: a single-conversation deep dive, not a corpus search. The summary can then be saved back so one call's insights compound into the evidence base.

## Step 0 — Relevance & availability
Confirm the user means a specific conversation (not "what do customers think about X" across many — that's `/evermuse:customer-research`) and Evermuse is connected (see `using-evermuse` Step 0). If disconnected but the user pasted a transcript, summarize that directly and label it **⚠ ungrounded — not from Evermuse** (no source links).

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — locate, then read (this skill is serial, not a corpus batch).** Verify the product (Rule 1), then:
1. **`find_sources`** to locate the one conversation (filter by `title_keyword`, `attendee_email`/`attendee_domain`, or date; or `query` if the user described it by topic). If more than one plausible match, confirm which meeting with the user before reading.
2. **`read_source`** on that source and read it fully before writing — page with `offset`/`next_offset` until `has_more` is false. The transcript IS the grounding for this skill.

Do **not** run the multi-search corpus batch here — that's for research skills across many calls (`/evermuse:customer-research`). One conversation in, one summary out.

**Optional — considered use.** After reading, reach for other tools only when they add value: a single `evidence` search to check whether a need heard here echoes across the corpus, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Citations and saving are optional — not required.

## Two flavors (pick by conversation type)

### A — Customer interview → discovery summary (JTBD-focused)
Tag `interview-summary`. Template:
```markdown
**Date**: […]   **Participants**: [names + roles]
**Background**: [about the customer]
**Current Solution**: [what they use today]

**What They Like** (JTBD · desired outcome · importance · satisfaction):
- …

**Problems With Current Solution** (JTBD · desired outcome · importance · satisfaction):
- …

**Key Insights / Notable Quotes**:
- > "[verbatim]" — [Speaker] [12:340] [`1`](URL)

**Action Items**: [Date · Owner · Action]
```

### B — Team / stakeholder meeting → minutes (decision-focused)
Tag `meeting-summary`. Template:
```markdown
## Meeting Summary
**Date & Time**: […]   **Participants**: [names + roles]   **Topic**: […]

**Summary**
- **Point 1**: [key discussion point or decision]
- **Point 2**: …

**Action Items**
| Due Date | Owner | Action |
|----------|-------|--------|

**Decisions Made**
- …
**Open Questions**
- …
```

## Instructions
1. **Locate, then read** the one conversation (never dump the whole corpus). If ambiguous, confirm which meeting.
2. **Read the full transcript** before writing.
3. **Extract to the right template.** Use "-" where info is missing. Preserve **timestamps** on quotes (they're the transcript's citation). Pull needs and pains as JTBD (interview) or decisions and owners (meeting).
4. **Write for clarity** — plain language a non-attendee understands; be objective, summarize what was said not opinions; use "we" for team meetings.
5. **Offer to save** so the needs/quotes rejoin the evidence base, then offer next steps (`/evermuse:opportunity-solution-tree`, `/evermuse:analyze-feature-requests`).

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) — summarize-interview (pm-product-discovery) + summarize-meeting (pm-execution).
