---
name: value-proposition
description: 'Design a value proposition on the 6-part JTBD structure, then turn it into ready-to-use marketing/sales/onboarding statements — all in customers'' verbatim language. Use when the user says ''write our value proposition'', ''value prop'', ''why should customers choose us'', ''positioning statement'', or ''articulate our value''. Trigger terms: value proposition, value prop, JTBD, positioning statement, marketing copy, sales messaging, customer value. Not for full pricing or business-model work.'
category: Segmentation & Targeting
tags:
- value-prop
- messaging
- positioning
---

# Value Proposition (JTBD + statements)

Two artifacts in one pass: a rigorous 6-part JTBD value proposition per segment, then the marketing/sales/onboarding **statements** derived from it. The pains and gains are verbatim customer language pulled from Evermuse; the statements reuse the customer's own phrasing, so the copy already sounds like the market.

## Step 0 — Relevance & availability
Confirm this is customer-value/positioning work and Evermuse is connected. If not, produce a framework-only value prop labeled **⚠ ungrounded — Evermuse not connected** and tell the user to authorize the MCP. See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md` Step 0.

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## Instructions

You are a product strategist and growth expert designing the value proposition for **$ARGUMENTS**. Do one segment per pass — value props are segment-specific.

### Part A — 6-Part JTBD Value Proposition (per segment)
1. **Who** — the segment and its constraints.
2. **Why (Problem / JTBD)** — the progress they're trying to make and the desired outcome. Grounded in evidence.
3. **What Before** — current state and friction. **Quote the pain verbatim** from a quote-angled `search` result; cite it.
4. **How (Solution)** — the mechanism/features that change the situation.
5. **What After** — the improved state. **Quote the desired gain verbatim** where evidence provides it; cite it.
6. **Alternatives** — what they use today and why we're better; switching friction. Ground in evidence/context.

This customer-first order (Who/Why → solution) beats solution-first canvases. Section 6 forces you to name real substitutes rather than assume none.

### Part B — Value Proposition Statements (per segment)
From the JTBD above, write 2–3 statements for marketing / sales / onboarding. Each statement:
- addresses one segment/use case directly,
- emphasizes the primary benefit and desired outcome,
- names the capability that makes it possible,
- **reuses the customer's own phrasing** from the quotes — if customers say "re-keying," don't write "manual data entry." The verbatim language is the differentiator.

Where the source method reaches for "user-provided data / brand voice files," use Evermuse `evidence` (the customer's actual words) as the primary source for both pains/gains and copy voice.

## Deliverable format

```markdown
# Value Proposition — [segment]

| Who | Why (JTBD) | What before | How | What after | Alternatives |
|---|---|---|---|---|---|
| … | … | > "[pain quote]" [`1`](URL) | … | > "[gain quote]" [`2`](URL) | … |

### Statements
- **Marketing:** [statement reusing customer phrasing]
- **Sales:** [statement]
- **Onboarding:** [statement]
```

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT), merging its `value-proposition` and `value-prop-statements` skills; grounding is Evermuse-native.
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
