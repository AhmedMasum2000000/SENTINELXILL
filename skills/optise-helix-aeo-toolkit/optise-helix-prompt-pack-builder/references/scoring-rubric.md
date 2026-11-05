# "Decides Deals" Scoring Rubric (1-5)

**Used by:** `optise-helix-prompt-pack-builder` exclusively.
**Purpose:** Make the prompt scoring repeatable across users and runs. Two different users running the skill on the same input should get the same scores within ±1 point.

The score is **NOT search volume**. It is the strength of the link between answering this prompt well and converting a deal.

---

## The 5 levels

### 5/5 — Disqualifier
A buyer who gets a wrong answer here ELIMINATES you from the shortlist. There is no recovery.

**Examples:**
- `is [tool] GDPR compliant` (in any EU market)
- `[tool] pricing` (when your pricing isn't on the page)
- `[competitor X] vs [you]` (when your competitor has the comparison page and you don't)
- `does [tool] offer EU data residency` (in DACH, France)
- `who are [tool]'s subprocessors`
- `can I get a DPA for [tool]`

**Heuristic test:** If a buyer who got a wrong answer would silently move to your competitor without telling you, this is a 5.

### 4/5 — Accelerator
A buyer who gets a good answer here moves SIGNIFICANTLY faster. Saves them 1-2 internal cycles.

**Examples:**
- `how long does [tool] implementation take`
- `does [tool] integrate with [stack the buyer uses]`
- `what data does [tool] collect and for how long`
- `[tool] enterprise pricing`
- `is [tool] used by [similar company / vertical]`

**Heuristic test:** If a buyer who got a good answer would advance to a demo or trial 2 weeks faster, this is a 4.

### 3/5 — Confidence builder
A buyer gains confidence but doesn't change their decision. Useful but not deal-deciding.

**Examples:**
- `best [category] tools 2026`
- `top alternatives to [competitor]` (when there are many alternatives)
- `what is [category]`
- `[tool] reviews`
- `[tool] features`

**Heuristic test:** If a good answer makes the buyer feel safer but they would have advanced anyway, this is a 3.

### 2/5 — Awareness reinforcer
A buyer notices but it doesn't move the deal in any meaningful direction. Brand-building, not pipeline.

**Examples:**
- `[category] tools for [role they're not in]`
- `[tool] history`
- `[tool] founders`
- `is [tool] a good company to work for`

**Heuristic test:** If the buyer would forget the answer 5 minutes later, this is a 2.

### 1/5 — Educational
Pure learning intent. No buyer with budget is asking this.

**Examples:**
- `what is AI` (when you sell AI)
- `how does [category] work`
- `glossary of [category] terms`

**Heuristic test:** If the searcher might be a student or a journalist, this is a 1. Don't waste prompt slots on these.

---

## Tie-breakers

When two prompts feel like the same score, apply in order:

1. **Market specificity wins.** A 5/5 prompt for one market beats a 4/5 prompt that works in 5 markets (because the specific one ships a page; the generic one is harder to win).
2. **Competitor-named beats category-named.** `Salesforce alternatives` beats `best CRM`. Always.
3. **Decision-stage beats awareness-stage.** A pricing prompt at 4/5 beats a "what is" prompt at 5/5 (because pricing converts; "what is" educates).
4. **EU compliance beats everything in EU markets.** A 5/5 GDPR prompt always ranks above any other 5/5 in DACH, France, Benelux. Always.

---

## Worked examples

### Example 1 — B2B revenue intelligence in DACH

| Prompt | Category | Score | Why |
|---|---|---|---|
| `Gong vs [you]` | Shortlist | 5/5 | Competitor named, deal-deciding |
| `is [you] GDPR compliant in Germany` | EU Privacy | 5/5 | Disqualifier in DACH (English only at v1) |
| `does [you] offer a DPA` | EU Privacy | 5/5 | Disqualifier, DPA availability |
| `how long to implement [you]` | Implementation | 4/5 | Accelerator, not disqualifier |
| `does [you] integrate with HubSpot` | Integration | 4/5 | Accelerator if HubSpot is the buyer's stack |
| `best revenue intelligence tools 2026` | Shortlist | 3/5 | Confidence, no specific competitor |
| `what is revenue intelligence` | Shortlist | 1/5 | Educational, drop |

### Example 2 — Tie-breaker in action

Two prompts both score 5/5 in initial ranking:
- `[Salesforce] vs [you]` (competitor-named, shortlist)
- `is [you] GDPR compliant` (compliance, EU)

In a DACH market: GDPR wins (rule 4 — EU compliance beats everything in EU).
In a US market: Salesforce-vs-you wins (rule 2 — competitor-named in non-EU).

---

## What the rubric does NOT score

1. **Search volume.** A prompt with 100 searches/month at 5/5 beats a prompt with 10,000 searches/month at 3/5.
2. **Difficulty to win.** Hard-to-win 5/5 prompts still rank above easy-to-win 3/5 prompts. The skill is for prioritization, not for excuses.
3. **The user's existing rankings.** If the user already has a page that wins a 4/5 prompt, that prompt still scores 4/5 — but the skill marks it `[ALREADY WINNING]` in the target page column instead of `[TO BUILD]`.

---

## Calibration check

If your scoring distribution looks like this for a 25-prompt pack, you've calibrated correctly:

| Score | Count | % |
|---|---|---|
| 5/5 | 6-8 | ~25-30% |
| 4/5 | 8-10 | ~35-40% |
| 3/5 | 5-7 | ~25-30% |
| 2/5 | 1-3 | ~5-10% |
| 1/5 | 0-1 | <5% |

If you have 15+ prompts at 5/5, you're inflating scores — the user will lose trust. Re-rank.
If you have <3 prompts at 5/5, you're missing disqualifier prompts — the pack is too soft. Add competitor-vs-you and EU compliance prompts.
