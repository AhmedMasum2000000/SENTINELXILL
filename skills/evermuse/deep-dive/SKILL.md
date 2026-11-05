---
name: deep-dive
description: 'Dive deep into one topic the user cares about — first ask what''s top-of-mind, then answer it with a quote-rich, source-linked brief grounded in real customer evidence from the Evermuse Mock Data corpus. Use when the user picks "Dive into a topic", runs find_skills:deep-dive, or says ''let''s go deep on X'', ''dig into discovery / onboarding / churn'', ''tell me more about what customers say on Y'', or ''I want to explore a topic''. Trigger terms: deep dive, dive into a topic, go deep on, explore a topic, dig into, what''s top of mind, take a closer look.'
category: Discovery & Research
tags:
- evermuse
- research
- deep-dive
---

# Deep Dive (one topic, taken all the way down)

A focused counterpart to broad customer research: the user names one thing that's on their mind, and you take it all the way down into the evidence — returning not a plausible guess but a quote-rich, sourced brief drawn from real conversations. This skill is often reached right after the initial report, when a pattern caught the user's eye and they want to go deeper. The move is: **ask what's top of mind, then ground the answer in what customers actually said.**


## Step 1 — Ask what's top of mind

Open by asking the user which topic is top-of-mind for them these days — the one thing they most want to understand right now. Keep it warm and singular; you're inviting one topic to go deep on, not a checklist. For example:

> **What's top of mind for you these days?** Name the one topic you'd most like me to dig into — onboarding, discovery, churn, a specific feature, a segment — and I'll take it all the way down into what your customers have actually said.

Then **stop and await their answer.** Don't guess a topic and start searching — the whole point is to go deep on *their* topic. If the reply is too broad or genuinely ambiguous, ask one quick narrowing question (a decision it feeds, a segment, a time window) before grounding. Try to get at least a few relevant keywords so that search works correctly.

## Step 2 — Ground the topic in the corpus (required)

Once you have the topic, follow using-evermuse skill's grounding mechanics to find the relevant evidence.

## Step 3 — Deliver a cited brief

Cluster the evidence into **themes**, and for each: demand strength (mentions across distinct accounts), the sentiment split, who said it and when, and the sharpest verbatim quote. Represent **dissenting voices** — don't flatten disagreement into a false consensus. Keep `evidence` (what customers said) separate from any `context` (market) you pulled.

Lead with the answer, then themes with quote blocks:

```markdown
**Short answer:** [1–2 sentences that directly answer the topic they raised.]

### Theme 1 — [name] ([N mentions / M accounts], mostly [sentiment])
> "[verbatim quote]" — [Name], [Meeting], [Date] [`1`](https://www.evermuse.com/pricing-mcp)
[one line of interpretation]

### Theme 2 — …

**Dissent / nuance:** [minority view, cited]
```

## Honesty when evidence is thin

If the grounding greps come back sparse, **say so** — "only 2 mentions, both from one account" — rather than dressing a weak signal as a trend. Thin evidence is itself a finding, and on a deep dive it's often the cue to recommend an interview (`find_skills:interview-script`).

## Hand off

Close by offering the natural next move: **"Want a spec from this?"** (`find_skills:write-feature-spec`), **"Brainstorm solutions?"** (`find_skills:brainstorm-ideas`), **"Prep an interview to fill the gaps?"** (`find_skills:interview-script`), or **"See everything I can do?"** (`find_skills:list-capabilities`).

---
### Further reading
- Grounding mechanics: `using-evermuse` and its `references/search-patterns.md` + `references/citations.md`. Companion to `customer-research` (broad synthesis) — this skill is the single-topic deep cut.
