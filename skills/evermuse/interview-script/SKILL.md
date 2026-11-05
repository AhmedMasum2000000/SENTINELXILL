---
name: interview-script
description: 'Write a Mom-Test customer interview guide — warm-up, JTBD exploration, wrap-up — but first check the evidence for what''s ALREADY known so the questions target the open gaps instead of re-asking answered questions. Use when the user asks to ''write an interview script'', ''prep for a user interview'', ''discovery interview questions'', ''interview guide'', ''what should I ask customers'', or ''plan a research call''. Trigger terms: interview script, interview guide, user interview, discovery interview, customer interview questions, Mom Test, research questions to ask. Not for summarizing an interview already done (that''s summarize-conversation).'
category: Discovery & Research
tags:
- interviews
- research
- scripts
---

# Customer Interview Script (targeted at the gaps)

A Mom-Test interview guide — ask about their life, not your idea; the past, not the future. The Evermuse difference: **before writing a single question, check what the corpus already answers.** No point spending a scarce interview slot re-asking what six customers already told you. The script targets the *open* gaps, so each call buys new knowledge instead of confirming old.

## Step 0 — Relevance & availability
Confirm this is interview prep and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, you can still produce a solid Mom-Test script from the framework — label it **⚠ ungrounded** and note you couldn't check what's already known, so it may re-ask settled questions.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

1. **Clarify research objectives.** What decision will this research inform? What assumptions need validating?

2. **Split known vs. open (the key step).** From the grounded evidence, list what the corpus **already answers** (with quotes) and what remains **genuinely open**. Write questions only for the open set; briefly show the user what you cut and why.

3. **Build the script** — Mom-Test throughout:

   **Opening (2–3 min):** purpose is learning not selling; no right/wrong answers; permission to record; confirm time.

   **Warm-up (5 min):** role, typical day/week, how long they've done the relevant activity. Build rapport, understand context.

   **Core exploration — JTBD (15–20 min), weighted to the open gaps:**
   - *Current behavior (past tense, specific):* "Walk me through the last time you [did the thing]. What happened? What tools? How long? Who else?"
   - *Pain points (observe, don't lead):* "What was the hardest part? What have you tried? What happened?"
   - *Desired outcomes (their words):* "What does 'good' look like? How would you know it's working?"
   - *Willingness to pay (skin in the game):* "How much time/money does this cost you today? Have you looked for a better solution?"

   **Probing:** "Tell me more about that" · gentle "Why?" ×2–3 · "Can you give a specific example?" · "What happened next?" · "How did that make you feel?"

   **Mom-Test rules:** ask about their life not your idea · the past not the future · talk less (80/20) · never pitch · hunt for strong emotion · compliments are noise.

   **Wrap-up (3–5 min):** "Anything I didn't ask that matters?" · "Who else should I talk to?" · thanks · next steps.

4. **Note-taking template** (include it):
   ```
   Participant: [Name / ID]   Date: [Date]
   Key Jobs: […]   Current Solution: […]
   Biggest Pain: […]   Desired Outcome: […]
   Willingness to Pay: […]   Surprise Finding: […]   Follow-up: […]
   ```

## Deliverable
The script (with an up-front **"Already known — not asking"** box citing the corpus, and a **"Targeting these gaps"** list) plus the note-taking template. After the interview, hand off to `/evermuse:summarize` to feed the summary back into the corpus.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) — interview-script. Method: *The Mom Test* (Rob Fitzpatrick); Product Trio: Teresa Torres, *Continuous Discovery Habits*.
