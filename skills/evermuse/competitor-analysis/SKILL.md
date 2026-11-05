---
name: competitor-analysis
description: 'Analyze competitors and find differentiation openings by cross-checking capability data against what customers ACTUALLY say about each rival — mentions, win/loss reasons, switching pain — with quotes. Use when the user says ''what do customers say about <competitor>'', ''analyze our competitors'', ''competitive analysis'', ''how do we compare to X'', ''why do we lose to Y'', ''where can we differentiate'', or wants a competitive landscape/brief. Trigger terms: competitor analysis, competitive landscape, competitors, win/loss, differentiation, how do we compare, why we lose deals. Not for internal team/vendor comparisons.'
category: Market & Competition
tags:
- competitors
- analysis
- market
---

# Competitor Analysis (what customers actually say)

Map the competitive landscape — but weight it by the customers' own words, not a feature spec sheet. The sharpest competitive intelligence isn't "Competitor X has feature Y"; it's a prospect saying *why* they picked or dropped a rival. This skill cross-checks the internal competitor data against real customer mentions and win/loss quotes.

## Step 0 — Relevance & availability
Confirm this is competitive/market work and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, produce the framework labeled **⚠ ungrounded** and tell the user to authorize the MCP.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

Analyze the competitive landscape for **$ARGUMENTS**.

1. **Scope the market** and assemble the competitor set: start from `list_competitors`, then add any rival that *customers actually name* in the corpus (evidence often surfaces competitors the DB misses — that's a finding).
2. **For each competitor**, build the profile below, and for every strength/weakness claim mark its source: `[customer]` (a real mention, badged), `[competitor DB]` (secondary, unverified), or `[market]` (external).
3. **Reconcile.** Where the competitor DB and customers disagree, trust the customers and say so.
4. **Find the differentiation openings** — the unmet needs and switching pains customers voice that no competitor solves well.

### Per-competitor profile

**Profile** — focus, segments served, positioning, stage `[market]`.

**Strengths** — what wins them deals. Prefer customer reasons:
```markdown
> "We went with [competitor] because [reason]" — [Name], [Meeting], [Date] [`1`](LINK)
```

**Weaknesses & gaps** — where customers are frustrated or churned away from them, badged. Add `[competitor DB]` capability gaps as secondary.

**Pricing / model** — `[market]`, cite source.

**Threat & win/loss pattern** — how they threaten us; the recurring reason we win or lose against them, from real deals.

### Differentiation opportunities (the payoff)
A ranked list of openings — each an **unmet need or switching pain customers voiced** that we could own — badged with the quote that proves it.

Close with a **competitive positioning recommendation** (differentiators to emphasize, segments to target, threats to monitor), keeping customer evidence visibly separate from competitor-DB and market sources. This feeds `/evermuse:market-sizing` (wedge) and positioning work.

---
### Further reading
- Competitive-analysis structure adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT); customer cross-check is Evermuse-native.
