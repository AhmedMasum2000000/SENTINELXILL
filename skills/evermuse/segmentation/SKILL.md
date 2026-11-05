---
name: segmentation
description: 'Segment a market or user base by evidence-based need differences — not demographics — into 3-5 distinct groups, each with its jobs-to-be-done, pains, product fit, and representative customer quotes. Use when the user says ''segment our users'', ''segment the market'', ''who are our target segments'', ''what customer segments do we have'', ''break users into groups'', or wants a needs-based segmentation model. Trigger terms: segmentation, market segments, user segments, customer segments, target audiences, segment the market, needs-based groups. Not for arbitrary demographic buckets with no behavioral difference.'
category: Segmentation & Targeting
tags:
- segmentation
- markets
- analysis
---

# Segmentation (needs-based, from the corpus)

Split the market or user base into groups that **differ in what they need**, not just in what they look like. Real segments earn their keep by pointing at different product bets; demographic buckets that all want the same thing don't. Every segment here is defined by evidence of a distinct need and carries the customers' own voice.

## Step 0 — Relevance & availability
Confirm this is segmentation work and Evermuse is connected (see `using-evermuse` Step 0). If disconnected, produce a framework-only model labeled **⚠ ungrounded** and tell the user to authorize the MCP.

## Two altitudes — pick one
- **User segmentation** (existing users, from feedback) → segments come from the corpus; save **nature=evidence**.
- **Market segments** (the broader addressable market, incl. non-users) → market-level cuts lean on **`context` searches** (industry/analyst signals) *validated* by customer evidence; the customer-derived parts still save as evidence.
State which you're doing up front. Default to **user segmentation** unless the user is clearly exploring a market they don't yet serve.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

Segment **$ARGUMENTS** into 3-5 distinct groups.

1. **Choose segmentation dimensions from the evidence** — behavioral (how they use it), needs-based (the job), workflow context. Reject a demographic dimension unless the evidence shows it maps to a real difference in need.
2. **Define segments** so they're measurable, non-overlapping, and each points at a different product decision.
3. **Characterize each segment** with the structure below, quoting real customers. Where the source method says "if the user provides data" or reaches for market studies, use `evidence` searches (and `context` only for market-size color).
4. **Validate distinctness** — if two segments want the same things, merge them. Fewer real segments beats more fake ones.

### Segment profile (each of 3-5)

**Name & one-line characterization** — memorable, and says what makes it *different*.

**Size / weight** — rough share of the corpus (accounts/mentions), labeled as a corpus estimate, not a market number, unless you have `context` data.

**Jobs-to-be-done** — the primary job, its context, frequency, and success criteria for this group.

**Key pains & unmet needs** — badged with the accounts they came from.

**Representative voice** — 1-2 verbatim quotes:
```markdown
> "[verbatim quote]" — [Name], [Meeting], [Date] [`1`](URL)
```

**Product fit** — how well the product serves this segment today; the sharpest gap.

**Differentiated value / positioning** — what would move this segment most, and the messaging that resonates.

**Priority** — invest / maintain / de-prioritize, with a one-line rationale (growth, revenue, strategic fit vs. effort).

Close with a note flagging any segment that's underrepresented in the corpus. This pairs naturally with `/evermuse:user-personas` (a persona per segment) and market-sizing.

---
### Further reading
- Merges the market-segments and user-segmentation methods from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT); grounding is Evermuse-native. See [Crossing the Chasm for PMs](https://www.productcompass.pm/p/crossing-the-chasm).
