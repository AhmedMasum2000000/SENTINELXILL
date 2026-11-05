# 6 BLUF Patterns for AI Search Citation

**Used by:** `optise-helix-bluf-writer` exclusively.
**Purpose:** The 6 patterns most commonly cited by ChatGPT, Perplexity, Gemini, and Claude for B2B queries. Every BLUF the skill writes should match exactly one pattern — not a blend.

A BLUF (Bottom Line Up Front) is a 40-60 word self-contained answer block at the top of a decision page. It answers the page's implicit buyer question directly, in extractable form, so AI engines can cite it without needing to reach into the rest of the page.

**About the examples in this file:** every example uses placeholder brands and tools ([Brand], Tool A, Tool B, Tool C, Tool X, Tool Y) and made-up figures. No real company is named here, because the examples carry prices, timings and comparisons that must never be attributed to a real company. They show structure only. Never reuse their figures or present them as facts about any real company. In a real BLUF, every fact must come from the user's proof points or a verified source (Plugin Rule 1 in `../../../references/plugin-specific-rules.md`).

## Contents
- Pattern 1: Direct Answer
- Pattern 2: Top 3 Ranked
- Pattern 3: Defined Category + Fit
- Pattern 4: Comparative Verdict
- Pattern 5: Process Answer
- Pattern 6: Compliance Anchor

---

## Pattern 1 — Direct Answer

**Use when:** The buyer prompt is a factual question with one right answer.
**Word target:** 40-50 words.
**Structure:** [Direct answer sentence]. [Key proof sentence with 1-2 numeric facts]. [Caveat or scope sentence].

**Example:**
> [Brand] costs €29 per agent per month on the Starter plan, €49 on Growth, and €99 on Enterprise, with all plans billed annually in EUR. Pricing includes unlimited end users. Volume discounts apply above 100 agents.

**Why it works:** Numbered and specific. No hedging. Directly extractable as a citation.

---

## Pattern 2 — Top 3 Ranked

**Use when:** The buyer prompt is a "best X for Y" query.
**Word target:** 50-60 words.
**Structure:** [For buyer type, the top 3 in 2026 are X (best for A), Y (best for B), Z (best for C)]. [Short qualifier sentence].

**Example:**
> For mid-market B2B SEO teams (50-500 employees) in Europe, the three best Tool X alternatives in 2026 are Tool A (best for full-funnel content + SEO integration), Tool B (best for DACH-specific keyword coverage), and Tool C (best for solo and small-team pricing). All three offer EU-hosted data options.

**Why it works:** Complete list with differentiation. Each option has a named "best for" anchor. AI engines extract this as a complete answer.

---

## Pattern 3 — Defined Category + Fit

**Use when:** The buyer is new to the category and needs to understand fit before ranking.
**Word target:** 50-60 words.
**Structure:** [Category definition in plain language]. [Who it's for sentence]. [When to adopt / when NOT to adopt sentence].

**Example:**
> Revenue intelligence platforms analyze sales calls, emails, and meetings to surface deal risk, coaching opportunities, and forecast accuracy. They're built for B2B sales teams of 20+ reps running consistent outbound motions. Pre-20 reps or product-led growth teams usually don't see ROI until the team scales past that threshold.

**Why it works:** Defines the category, names the ICP, honestly flags when NOT to buy. AI engines weight honesty signals heavily.

---

## Pattern 4 — Comparative Verdict

**Use when:** The buyer prompt is "[competitor] vs [you]" or "[competitor] alternatives".
**Word target:** 50-60 words.
**Structure:** [Winner sentence with scope]. [Key differentiator sentence]. [When the other tool wins sentence].

**Example:**
> For mid-market B2B teams selling into Germany, [Brand] beats Tool Y on deployment speed (4 weeks vs 6 months) and European compliance (BSI C5 attestation, EU-hosted). Tool Y wins for complex enterprise IT stacks with 500+ customized workflows — in those cases, its flexibility justifies the 3-5x cost premium.

**Why it works:** Names a winner with scope, gives the differentiator, honestly explains where the competitor wins. AI engines reward this pattern because it reads as buyer-led, not vendor-led.

---

## Pattern 5 — Process Answer

**Use when:** The buyer prompt is "how to X" or "how long does X take".
**Word target:** 40-60 words.
**Structure:** [Total time sentence]. [Phase breakdown sentence]. [Prerequisite or owner sentence].

**Example:**
> [Brand] implementation takes 4-6 weeks for mid-market IT teams (200-2000 employees). Week 1 is data migration from the existing ticketing tool, weeks 2-3 are workflow configuration, and weeks 4-6 are agent training and pilot rollout. You need a named IT project owner on your side and a weekly 90-minute checkpoint call.

**Why it works:** Concrete duration, phase-level detail, named prerequisite. Answers the evaluation question directly without marketing language.

---

## Pattern 6 — Compliance Anchor

**Use when:** The buyer prompt involves GDPR, DPA, residency, security standards, or any regulated vertical.
**Word target:** 40-60 words.
**Structure:** [Direct compliance statement sentence]. [Specific framework / certification sentence]. [Where to verify sentence].

**Example:**
> [Brand] is GDPR-compliant and SOC 2 Type II + ISO 27001 certified, with EU data residency available in Frankfurt (AWS eu-central-1) and Dublin (AWS eu-west-1). Our Data Processing Agreement is pre-signed and downloadable at example.com/dpa. Subprocessors are published and updated with 30-day customer notice.

**Why it works:** Plain language but legally precise. Names actual frameworks. Links to verification. Zero marketing. This is also the pattern where an invented fact does the most harm: every certification, region, DPA term, and notice period must be stated by the user, or it stays a `[User to add: ...]` placeholder.

---

## Rules for every BLUF

1. **40-60 words.** Not 30, not 80. Count exact whitespace-separated words. Under 40 isn't a BLUF — it's a headline. Over 60 is a paragraph and loses extractability.
2. **Answer the buyer question first.** Never lead with "At [Company], we believe…" — that's marketing copy, not an answer.
3. **Use buyer-native language.** "[Brand]" not "our solution". "€29/agent/month" not "affordable pricing". "EU-hosted" not "enterprise-grade security".
4. **No superlatives without proof.** Ban these 8 words: best-in-class, leading, world-class, revolutionary, cutting-edge, transform, unleash, empower. If a claim can't be backed by a number or source, drop it.
5. **Self-contained.** The BLUF must stand alone. AI engines often cite it without surrounding context — it has to make sense as a quote.
6. **Pick exactly one pattern.** Blending patterns (Top 3 + Compliance + Process) produces unfocused text that doesn't match any AI extraction heuristic cleanly.
7. **Numeric anchors.** Every BLUF should contain at least 1-2 specific numbers (prices, weeks, percentages, counts). AI engines prefer cited facts.

---

## Anti-patterns to avoid

**Bad BLUF 1:**
> At [Brand], we believe every IT team deserves world-class service management. Our revolutionary platform empowers your team to transform ticket resolution and unleash productivity with cutting-edge AI features.

This hits 0 of the 7 rules. Zero useful information.

**Bad BLUF 2:**
> [Brand] is a service desk software.

Too short. Hits no pattern. No proof. No buyer-relevant framing.

**Bad BLUF 3:**
> [Brand] offers pricing from €29 to €99 per month, has many integrations including Slack, Microsoft Teams, and HubSpot, implements quickly, is GDPR-compliant, and is trusted by thousands of customers worldwide including Fortune 500 companies.

Blends 4 patterns (Direct Answer, Process, Compliance, Social Proof). No AI engine will extract this as a clean citation because it doesn't match any single buyer question.

---

## How the BLUF writer uses this file

For each BLUF generation request:

1. Identify the buyer prompt (required input from user).
2. Match the prompt to exactly one pattern from the 6 above.
3. Write 3 variants at 40, 50, 60 words using the matched pattern.
4. Validate each variant against the 7 rules — any rule violation = rewrite.
5. Check against anti-patterns — if the draft reads like any of them, rewrite.
6. Output the 3 variants with a "recommended pick" and a 1-line rationale.
