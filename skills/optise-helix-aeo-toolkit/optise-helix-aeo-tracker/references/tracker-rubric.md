# AEO Tracker Rubric

**Used by:** `optise-helix-aeo-tracker` exclusively.
**Source:** Optise EU AEO Playbook, Section 8 ("Measuring AI Search Visibility — The 3 KPIs That Matter").

The Optise tracker measures 3 KPIs only — not 30. Tracking 30 metrics is what generic AEO tools do; it produces dashboards no one acts on. The 3 KPIs are the minimum that actually drive decisions.

## Contents
- KPI 1: Citation Rate
- KPI 2: Prominence
- KPI 3: Competitor Delta
- Weekly cadence rationale
- 4-engine coverage rule
- The "is the tracker working" diagnostic

---

## KPI 1 — Citation Rate

**Definition:** Of the prompts in your pack, what % triggers an AI engine to mention your brand at all?

**Measurement:** For each prompt, ask the AI engine the prompt verbatim. Record:
- **Mentioned (Y/N):** Did the answer reference your brand by name?
- **Cited with link (Y/N):** Did the answer link to your domain?

**Citation Rate formula:**
```
Citation Rate = (prompts where Mentioned=Y) / (total prompts) × 100
```

**Healthy benchmarks (from Optise customer data):**
- **A grade (>40% citation rate):** You're winning AEO. Most B2B SaaS sites won't reach this in year 1.
- **B grade (20-40%):** You're cited regularly. Defensible, expected for a brand with a working Trust Centre.
- **C grade (10-20%):** You're occasionally cited. Improving from FITq audits will move you here.
- **D grade (5-10%):** Sporadic. You probably need structural fixes (FITq Findability < 15).
- **F grade (<5%):** Functionally invisible. The fixes are usually all 4 FITq signals at once.

**What this KPI does NOT measure:** Whether the citation drove a click, lead, or deal. That's downstream — RevOps tracking.

---

## KPI 2 — Prominence

**Definition:** When your brand IS mentioned, where does it appear in the answer?

**Measurement:** For each Mentioned=Y row, record:
- **First mention (1):** Your brand is the first option named.
- **Top-3 mention (2):** Your brand is in the first 3 options named.
- **Late mention (3):** Your brand is named after the first 3 options.
- **Buried mention (4):** Your brand appears only at the end or in a "see also" line.

**Prominence Score formula:**
```
Prominence = sum of (1 for first, 2 for top-3, 3 for late, 4 for buried)
            / count of mentioned prompts
```

Lower is better. Target: <2.0.

**Why this matters:** Buyers often only read the first 3 options in an AI engine answer. A late mention is worse than a generic mention.

---

## KPI 3 — Competitor Delta

**Definition:** When the same prompt asks about your category, are you mentioned MORE or LESS often than your top 2 competitors?

**Measurement:** For each prompt, record:
- **You mentioned (Y/N)**
- **Competitor 1 mentioned (Y/N)**
- **Competitor 2 mentioned (Y/N)**

**Competitor Delta formula:**
```
Delta = (your citation count) - (avg of competitor citation counts)
```

Positive = you're winning. Negative = you're losing. Zero = parity.

**What this KPI does NOT measure:** Why you're losing. The answer to "why" is in FITq + RACE audits, not in the tracker.

---

## Weekly cadence rationale

The tracker runs weekly, not monthly. Reasons:

1. **AI engine answers shift week-to-week** as their indexes update. Monthly tracking misses fast-moving patterns.
2. **Weekly is the minimum to detect signal vs noise.** With 25 prompts × 4 engines = 100 data points per week, you can detect a 5% change in citation rate within 2 weeks.
3. **Action loop matches.** Weekly tracking → Monday review → Tuesday fix → Wednesday re-publish. Fits a normal sprint cadence.

**Anti-pattern:** Daily tracking. AI engine answers change too slowly for daily resolution to be useful — you'll see noise, not signal.

---

## 4-engine coverage rule

Always check the same prompt across **4 engines**:
1. ChatGPT (most popular)
2. Perplexity (highest B2B research usage)
3. Gemini / Google AI Overviews (highest organic traffic crossover)
4. Claude (growing fast, especially developer/security personas)

**Why all 4:** Different engines have different training data and indexing recency. A prompt that wins ChatGPT might lose Perplexity. The variance IS the data.

**Optional 5th:** You.com and other niche engines for specific verticals.

---

## The "is the tracker working" diagnostic

When a user says "my tracker isn't showing improvements," check these in order:

1. **Are they running the prompts verbatim?** The tracker tests prompts as written, not paraphrases. Buyers type prompts the way they're written in the pack.
2. **Are they checking all 4 engines?** Improvements often show up in 1 engine before the others. Single-engine tracking misses this.
3. **Are they comparing weeks consistently?** Same day of week, same time of day, same logged-in vs anonymous state.
4. **Are they tracking competitor delta or just absolute citation rate?** Absolute can stay flat while delta improves (you're holding ground while competitors lose ground).
5. **Are they accounting for prompt freshness decay?** A prompt that worked 8 weeks ago may be outdated as buyer language shifts.
6. **Are they running the dead-prompt swap?** If 5+ prompts have 0% citation after 4 weeks, swap them via `optise-helix-prompt-pack-builder` refresh mode.

If none of those apply, the tracker IS working — the answer is that the user needs FITq + RACE audits on their target pages.

---

## Output format requirement

Every tracker setup must produce:
1. **CSV column spec** (exact column names + types + example values)
2. **Week-1 instructions** (how to run the first measurement)
3. **Weekly cadence checklist** (what to do every Monday)
4. **The 3 KPI formulas** (citation rate, prominence, delta)
5. **The "is it working" diagnostic** (if user is at week 4+)
6. **Handoff note** (when to refresh pack vs when to run audit)
