# Optise Prompt Pack Categories

**Used by:** `optise-helix-prompt-pack-builder` (primary), `optise-helix-fitq-audit` (secondary, for "what prompt should this page win"), `optise-helix-aeo-tracker` (secondary, for tracking inputs).
**Source:** Optise EU AEO Playbook, Section 10 ("The Europe First AEO and GEO Playbook"), Step 1.

These 6 categories are the proprietary Optise prompt taxonomy. Generic AEO advice does not use a category structure — competitors mix all prompts together. The category structure is what makes the prompt pack defensible.

---

## Category 1 — Shortlist & Category prompts

**What it is:** The top-of-funnel prompts where buyers ask AI engines for a category overview or comparison set. These prompts decide who gets *into* the consideration set.

**Pattern templates:**
- `best tools to solve [problem]`
- `best tools for [job] in [Germany / Nordics / France / Benelux]`
- `best [category] software for EU companies`
- `top [category] tools for mid-market B2B`
- `[competitor] vs [you]`
- `[competitor] alternatives`
- `alternatives to [competitor] for [ICP segment]`

**Who searches with these:** Marketing, growth, ICs starting research.
**Decides-deal score signal:** 5/5 if competitor name is in the prompt; 4/5 if "best in Europe" framing; 3/5 if generic "best".
**Target page type:** Alternatives page, Competitor-vs-you page, Buyer-led shortlist guide.

---

## Category 2 — Pricing & Buying prompts

**What it is:** Mid-funnel prompts where buyers are building a budget case or comparing pricing models.

**Pattern templates:**
- `how much does [tool] cost`
- `[tool] pricing model and cost drivers`
- `what is included in [plan A] vs [plan B]`
- `does [tool] have annual contracts or monthly`
- `[tool] enterprise pricing`
- `is [tool] worth the price for [ICP]`
- `total cost of ownership for [category] in Europe`

**Who searches with these:** RevOps, Procurement, Finance, Marketing leads building business cases.
**Decides-deal score signal:** 5/5 if your pricing isn't on the page (this is a deal-breaker — invisible pricing kills B2B EU deals).
**Target page type:** Pricing explainer, "Cost of [category]" guide.

---

## Category 3 — Implementation prompts

**What it is:** Mid-funnel prompts where buyers want to understand the actual cost of adopting (time, people, integrations).

**Pattern templates:**
- `how long does it take to implement [tool]`
- `what do we need to set up [tool]`
- `who needs to be involved in [tool] rollout (marketing, IT, RevOps)`
- `common implementation risks for [category]`
- `[tool] onboarding process`
- `[tool] time to value`

**Who searches with these:** RevOps, IT, Engineering, anyone responsible for the rollout.
**Decides-deal score signal:** 4/5 always — these are pages that materially shorten sales cycles.
**Target page type:** Implementation page, Onboarding guide.

---

## Category 4 — Privacy / Security / Compliance (EU buyer language)

**What it is:** The 8 EU buyer questions from Section 7 of the whitepaper. These are the **deal-killer** category in Europe — buyers who get the wrong answer here disqualify vendors silently.

**Pattern templates:**
- `is [tool] GDPR compliant`
- `where is customer data stored for [tool] (EU or US)`
- `does [tool] offer EU data residency`
- `can I get a DPA for [tool]`
- `who are [tool]'s subprocessors and where are they located`
- `what data does [tool] collect and how long is it retained`
- `can we delete data and exports easily`
- `does [tool] use third-party AI providers and what data is shared`
- `what security standards does [tool] meet (SOC 2, ISO 27001)`
- `is [tool] EU AI Act compliant`

**Who searches with these:** Security/Privacy/Legal lead — the stealth deal-killer persona.
**Decides-deal score signal:** 5/5 in EU markets, always. These prompts have higher stakes than any other category.
**Target page type:** Trust centre, DPA page, GDPR FAQ.

**Critical note:** These prompts are why the `optise-helix-eu-trust-centre` skill exists. If the prompt-pack-builder finds the user is missing answers to 4+ of these prompts, it should hand off to that skill.

---

## Category 5 — Integration prompts

**What it is:** Buyers asking whether your product fits their existing stack.

**Pattern templates:**
- `does [tool] integrate with [HubSpot, Salesforce, GA4, Snowflake, Slack, etc.]`
- `best [category] tool that works with [stack]`
- `how does [tool] connect to [system]`
- `[tool] API documentation`
- `[tool] webhooks`
- `can [tool] export data to [warehouse]`

**Who searches with these:** Web team, RevOps, Engineering.
**Decides-deal score signal:** 4/5 if the integration is core to the user's stack, 3/5 if peripheral.
**Target page type:** Integration hub, individual integration pages.

---

## Category 6 — Role-based prompts

**What it is:** Buyers searching with their job title in the query, looking for tools tailored to their role.

**Pattern templates:**
- `best [category] tools for RevOps`
- `best [category] tools for marketing ops`
- `best [category] tools for IT teams`
- `best [category] tools for [function] at [company size]`
- `[category] for [vertical] in Europe`

**Who searches with these:** ICs and managers within a specific function.
**Decides-deal score signal:** 4/5 if the role matches your ICP, 2/5 if it doesn't.
**Target page type:** Role-specific landing pages, Use case pages.

---

## How to score "decides deals" (1-5)

The score is NOT how many people ask the prompt. It's how directly the prompt converts to pipeline.

| Score | Definition |
|---|---|
| **5/5** | A buyer who gets a wrong answer here eliminates you from the shortlist. (Pricing, GDPR, DPA, competitor-vs-you.) |
| **4/5** | A buyer who gets a good answer here moves significantly faster. (Implementation, integrations they care about.) |
| **3/5** | A buyer who gets a good answer here gains confidence but doesn't change their decision. (Generic "best of" lists.) |
| **2/5** | A buyer would notice but it doesn't move the deal. (Aspirational role-based prompts.) |
| **1/5** | Awareness only. (Educational "what is [category]?" prompts.) |

---

## Assignment rule: one prompt → one target page

Every prompt must map to exactly one canonical page on the user's site that should be the page AI engines cite. If the user doesn't have that page yet, the output must mark the page as `[TO BUILD]`. This is how the prompt pack becomes a build order, not just a research artefact.
