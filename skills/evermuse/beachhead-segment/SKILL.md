---
name: beachhead-segment
description: 'Pick the first beachhead market segment by measuring which segment''s people show up most and most painfully in real customer evidence, then evaluating it on burning pain, willingness to pay, winnable share, and reachability. Use when the user says ''who should we target first'', ''what''s our beachhead'', ''which segment do we start with'', ''where do we focus first'', ''pick a first market'', or ''initial market entry''. Trigger terms: beachhead, first market, initial segment, target first, market entry, where to focus, crossing the chasm. Not for a broad ICP definition — this is the single first wedge.'
category: Segmentation & Targeting
tags:
- beachhead
- segmentation
- gtm
- focus
---

# Beachhead Segment

Pick the smallest winnable, referenceable first market — the wedge that gets you to PMF fastest and opens adjacent expansion. The Evermuse twist: instead of brainstorming segments in the abstract, you **measure demand density in the actual corpus** — which segment's people show up most often and most painfully in real conversations — then pressure-test the front-runner against four criteria, each backed by evidence.

## Step 0 — Relevance & availability
Confirm this is a first-market / segmentation task and Evermuse is connected. If the tools aren't present, produce a framework-only analysis labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md` Step 0.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

You are choosing the beachhead for **$ARGUMENTS**. Where the source method reaches for "customer interviews / market research," use the Evermuse corpus as the primary source: demand density from `find_sources`, pain from `evidence` searches and quotes.

### Step 1 — Read demand density from the corpus
List the candidate segments (verticals, company sizes, roles, use cases). For each, gauge presence in the evidence:
- **Frequency** — how many distinct accounts/meetings feature this segment (`find_sources` by `attendee_domain`).
- **Intensity** — how burning the pain reads in their quotes (quote-angled `search`, filters-only `search`).
The segment with the most people showing up, most strongly, is your demand-density front-runner — it earns the burden of proof, not an automatic win.

### Step 2 — Score the front-runners on four criteria
For the top 2–3 candidates, evaluate each criterion and **back it with evidence**:

1. **Burning pain** — acute, daily, unmet? Cite the sharpest pain quote and count how many accounts echo it. Thin evidence is a finding, not a gap to paper over.
2. **Willingness to pay** — is there budget, clear ROI, and no free workaround that fully satisfies? Cite any quotes about cost of the problem or current spend.
3. **Winnable share** — can you realistically take 60–70% in 3–18 months? Assess competitive saturation (context) and your differentiation; large enough but not owned.
4. **Reachability** — can you actually reach and refer within this segment? Look for professional communities, network effects, and adjacency to segments already in the corpus (a solved beachhead should reference into the next market).

### Step 3 — Select and plan
Choose the segment with the best combined picture: strongest cited pain, clear willingness to pay, winnable, reachable, and a natural bridge to adjacent segments. Then outline a 90-day acquisition plan for the beachhead and a post-beachhead expansion path (which adjacent segment the references unlock next).

## Deliverable format

```markdown
# Beachhead — [product]

**Demand density ranking**
| Segment | Accounts in corpus | Pain intensity | Note |
|---|---|---|---|
| [seg] | [N meetings/domains] | [high/med/low] | [one line] |

**Recommended beachhead: [segment]**

| Criterion | Verdict | Evidence |
|---|---|---|
| Burning pain | [strong/weak] | > "[quote]" — [attribution] [`1`](URL) ([M accounts]) |
| Willingness to pay | … | [cited [`2`](URL)] |
| Winnable share | … | [competitive context, cited [`3`](URL)] |
| Reachability | … | [cited [`4`](URL)] |

**Why first:** [1–2 sentences]. **90-day acquisition plan:** […]. **Expansion path:** [next adjacent segment, why].
```

## Honesty when evidence is thin
If a candidate segment barely appears in the corpus, say so plainly — "only 2 meetings, one account" — rather than inflating it into a market. A segment with no evidence isn't a beachhead; it's a hypothesis worth an interview (`/evermuse:interview` if available).

## Save & hand off
After saving, offer: **"Build the full ICP for this segment?"** (`/evermuse:ideal-customer-profile`), **"Plan the launch into it?"** (`/evermuse:gtm-strategy`), or **"Position for this segment?"** (`/evermuse:positioning-and-messaging`).

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) `beachhead-segment` (MIT); grounding is Evermuse-native.
- Based on Geoffrey Moore's beachhead strategy in *Crossing the Chasm*.
- [5 GTM Principles You Should Know as a PM](https://www.productcompass.pm/p/5-gtm-principles-with-frameworks-templates)
- [How to Achieve Product-Market Fit? Part I](https://www.productcompass.pm/p/how-to-achieve-the-product-market)
