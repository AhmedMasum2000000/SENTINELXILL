---
name: strategy-red-team
description: 'Adversarially attack a strategy, PRD, or roadmap by hunting the customer counter-evidence that falsifies its claims — ''you assume X, but three customers said the opposite''. Includes a pre-mortem mode. Use when the user says ''red-team this'', ''poke holes in this'', ''stress-test our strategy'', ''pressure-test this plan'', ''what could go wrong'', or ''run a pre-mortem''. Trigger terms: red team, stress test, pressure test, challenge assumptions, poke holes, pre-mortem, kill criteria. Not for polishing or copy-editing a doc.'
category: Strategy & Vision
tags:
- red-team
- pre-mortem
- risk
---

# Strategy Red-Team (attack the assumptions with counter-evidence)

Be a sharp, fair adversary against a strategy/PRD/roadmap — but a *grounded* one. The differentiator over a generic red-team: every attack points to **real customer counter-evidence** where it exists. Not "this might be risky" but "the doc assumes X; three customers said the opposite [`1`](URL)." Your grounding searches are designed to **falsify** the document's claims, not confirm them.

## Step 0 — Relevance & availability
Confirm there's a concrete document to attack and Evermuse is connected. If not connected, run a framework-only red-team labeled **⚠ ungrounded — Evermuse not connected** (assumption logic only, no counter-evidence) and tell the user to authorize the MCP. See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md` Step 0.

## Mode
- **Red-team (default):** attack load-bearing assumptions *now*, while the cheapest test is still available.
- **Pre-mortem mode:** if the user asks to "run a pre-mortem" or imagine the launch already failed, use `references/pre-mortem-template.md` (Tigers / Paper Tigers / Elephants → launch-blocking / fast-follow / track). Same counter-evidence grounding applies.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

You are a sharp, fair adversary reviewing **$ARGUMENTS**.

1. **Extract every claim.** List what the doc asserts as true. Separate **load-bearing** (if false, the plan dies) from cosmetic. Only load-bearing claims are worth attacking.
2. **Design falsifying searches.** For each load-bearing claim, phrase an Evermuse search that would surface the *opposite* — the customers who'd disagree. This is the core move.
3. **Steelman, then attack.** State the strongest version of the claim; then attack *that*, anchored in the counter-evidence found. No strawmen.
4. **Write each failure mode as "Fails if ___."** Concrete and falsifiable. "Fails if activation isn't actually the constraint" beats "execution risk."
5. **Rank by (impact if wrong) × (likelihood wrong) × (cheapness to test).** Surface the top of the list — the highest-impact, plausibly-wrong, cheap-to-check assumption is what to test *this week*.
6. **For each surviving kill-assumption, give the operator something to do:** *Fails if* · *Counter-evidence* (the opposing quotes, cited) · *Evidence to get this week* · *Kill criterion* (the threshold to stop/change) · *Cheapest test*.
7. **Self-refute, don't fabricate.** Default to "this risk is real" unless a falsifying search comes back empty or the doc already cites evidence against it — then say the claim holds.

Where the source method reaches for "web search / market research," use Evermuse `evidence` (falsifying customer voice) as the primary source and `context` (market) as secondary.

## Deliverable format

```markdown
## Red-Team: [plan in one line]

### Top Kill-Assumptions (ranked)
For each (3–5 max):
- **Claim:** [the load-bearing assertion in the doc]
- **Counter-evidence:** > "[opposing quote]" — [attribution] [`1`](URL)  (you assume X; [N] customers said the opposite)
- **Fails if:** [concrete, falsifiable condition]
- **Evidence to get this week:** [specific]
- **Kill criterion:** [threshold]
- **Cheapest test:** [smallest experiment]

### What's Well-Reasoned
[Claims that survived a falsifying search — state why, cite the confirming evidence.]

### What I Couldn't Assess
[Gaps where neither the doc nor Evermuse gave enough to judge.]
```

End with what to *do*, not just what to fear — the emotional job is relief from shipping the wrong bet.

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT), merging its `strategy-red-team` and `pre-mortem` skills; grounding is Evermuse-native.
- [Assumption Prioritization Canvas](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [How Meta and Instagram Use Pre-Mortems](https://www.productcompass.pm/p/how-to-run-pre-mortem-template)
