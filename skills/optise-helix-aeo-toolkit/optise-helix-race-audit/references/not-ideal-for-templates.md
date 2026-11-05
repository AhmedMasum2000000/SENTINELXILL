# "Not Ideal For" Section Templates

**Used by:** `optise-helix-race-audit` exclusively.
**Purpose:** The single most common RACE gap is a missing "Not ideal for" section. 80% of B2B pages have zero honest constraints. This file provides templates for the 6 most common B2B product categories so the audit can output a concrete starter constraint block, not just "add a section."

## Contents
- Template structure
- 6 category templates
- Rules for adapting templates
- Anti-patterns

---

## Template structure

Every "Not ideal for" section should follow this 3-part structure:

1. **Opening statement (1 sentence):** Name the tool's core strength honestly so the contrast makes sense.
2. **3-5 specific constraints:** Each constraint is (a) a specific buyer type, (b) the reason it's a mismatch, (c) a named alternative.
3. **Closing (1 sentence):** How to verify fit — link to a fit-assessment questionnaire, demo, or documentation.

---

## Template 1 — B2B SaaS, mid-market focus

> ## Who [tool] is not ideal for
>
> [Tool] is built for mid-market B2B teams (50-500 employees) with dedicated [function] ownership. We're not the right fit if:
>
> - **You have fewer than 20 employees and no dedicated [function] lead.** Our setup assumes someone who owns [function] full-time. If you're a founder wearing 8 hats, look at [lightweight alternative] instead — it's built for owner-operators.
> - **You're a 5,000+ employee enterprise with custom SLAs and procurement.** Our pricing and deployment model isn't optimized for enterprise. [Enterprise alternative] is a better fit if you need custom onboarding, dedicated CSMs, and multi-region rollouts.
> - **You need on-premise deployment.** We're SaaS-only. For on-prem, see [on-prem alternative].
> - **You operate in a highly regulated industry (healthcare, defense, financial services with specialty compliance).** Our standard SOC 2 + ISO 27001 may not meet vertical-specific certifications. [Regulated alternative] is purpose-built for these verticals.
>
> **Not sure if you're a fit?** [Link to 5-question fit assessment]

---

## Template 2 — DevTools / Infrastructure

> ## Who [tool] is not ideal for
>
> [Tool] is optimized for [primary use case] at teams running [tech stack type]. We're not the right fit if:
>
> - **You're running a monolithic stack with no microservices.** Our architecture assumes 3+ services. For monoliths, [monolith-friendly alternative] is simpler.
> - **Your team has fewer than 5 engineers.** Our onboarding and documentation assume a small platform team. Solo devs and 2-person teams should consider [simpler alternative].
> - **You need real-time event processing at <100ms latency.** We're optimized for batch and near-real-time. For hard real-time, see [real-time alternative].
> - **You're on bare-metal / self-hosted only.** We're cloud-first. [Self-hosted alternative] is the right call for on-prem.
>
> **Technical fit check:** [Link to compatibility matrix]

---

## Template 3 — Marketing / Sales automation

> ## Who [tool] is not ideal for
>
> [Tool] is built for B2B marketing and sales teams doing [primary function] at scale. We're not the right fit if:
>
> - **You're B2C and primarily drive purchases through a checkout flow.** Our flows assume considered purchases with multiple touchpoints. [B2C alternative] is purpose-built for e-commerce.
> - **You have no existing CRM or data warehouse.** We integrate with your stack; we don't replace it. Start with [CRM alternative] first, then adopt us.
> - **You need one-off campaign execution, not ongoing automation.** For one-offs, [campaign tool alternative] is cheaper and simpler.
> - **Your list is under 500 contacts.** Our pricing assumes scale. Smaller lists should use [small-list alternative] or a manual process.

---

## Template 4 — Data / Analytics

> ## Who [tool] is not ideal for
>
> [Tool] is designed for data teams working with [data size/type] in [pipeline complexity]. We're not the right fit if:
>
> - **You don't have a data team yet.** Our workflow assumes a data engineer and analyst in-house. If you're a marketing team using a BI tool, [BI alternative] is faster to adopt.
> - **Your total data volume is under 10GB.** Our platform is priced for larger volumes. For smaller data, [small-data alternative] is more cost-effective.
> - **You need real-time dashboards visible to non-technical users.** We focus on exploration and modeling, not operational dashboards. Pair us with [dashboard alternative] for that layer.
> - **You require specific regulatory certifications (HIPAA, PCI-DSS).** Our standard compliance doesn't cover these. [Regulated alternative] is the right choice.

---

## Template 5 — HR / People operations

> ## Who [tool] is not ideal for
>
> [Tool] supports HR and people ops at B2B companies with [stage/size]. We're not the right fit if:
>
> - **You're in a jurisdiction we don't have compliance localization for.** We currently support [list regions]. For other regions, [localized alternative] is a better fit.
> - **You need core HRIS functionality (payroll, benefits admin).** We integrate with those — we don't replace them. Start with [HRIS alternative] for core HR.
> - **You have fewer than 50 employees.** Our workflows assume scale. Smaller teams should use [small-team alternative].
> - **You're in an industry with specialty regulation (healthcare staffing, union environments).** Standard HR tools often don't fit. See [regulated alternative].

---

## Template 6 — Security / Compliance

> ## Who [tool] is not ideal for
>
> [Tool] is built for security and compliance teams at B2B SaaS and fin-tech companies. We're not the right fit if:
>
> - **You're pre-Series A with no dedicated security hire.** Our platform assumes someone who owns security as their job. Earlier-stage companies should use [automated alternative] until they have a security lead.
> - **You need a GRC tool (governance, risk, compliance) across physical + cyber.** We focus on cloud and application security. For unified GRC, see [GRC alternative].
> - **You operate in a regulated vertical requiring specialty frameworks (NERC CIP, IEC 62443).** Our standard SOC 2 / ISO 27001 / GDPR support doesn't cover these. [Vertical alternative] is purpose-built.
> - **You want a fully-managed SOC (security operations center) rather than a tool.** We're a tool, not an MSSP. For managed services, see [MSSP alternative].

---

## Rules for adapting templates

When outputting a template in a RACE audit, the skill MUST:

1. **Never use a template verbatim.** Always substitute the user's actual category, competitor names, and buyer segments. Generic templates are the exact problem the audit is solving.
2. **Use `[User to add: ...]` placeholders when you don't know the answer.** Never invent a competitor name the user didn't mention. Never invent a target buyer segment.
3. **Match the number of constraints to the page's existing depth.** A deep page gets 5 constraints. A simple page gets 3. Don't over-stuff.
4. **Link constraints to the user's competitive frame.** If the user's competitors are Gong and Clari, the "alternative" mentioned in each constraint should reference those competitors when appropriate.
5. **Honor the buyer-first framing.** Every constraint should help the BUYER self-identify they're not a fit. Not the vendor avoiding a bad-fit deal. The framing matters.

---

## Anti-patterns to avoid

**Bad constraint 1: Fake humility**
> "Not ideal for those who don't want to grow."

This is marketing disguised as constraint. It implies anyone saying "no" is anti-growth. Agents and humans both see through it.

**Bad constraint 2: Trivial exclusions**
> "Not ideal for Microsoft Excel users who refuse to learn new tools."

Specific enough to sound real, but it's an insult, not an honest constraint.

**Bad constraint 3: Non-specific alternatives**
> "For some use cases, other tools might be a better fit."

Non-actionable. The whole point of the constraint block is to help buyers find where they DO fit.

**Bad constraint 4: Pricing as constraint**
> "Not ideal for budget-conscious teams."

Pricing is a first-order filter, not a RACE constraint. If you want to signal pricing positioning, use a pricing section. The RACE constraints are about fit, not cost.

**Bad constraint 5: Listing everyone you're NOT competing with**
> "Not ideal for small businesses, freelancers, non-profits, students, and agencies."

Just a list of non-buyers. Real constraints explain WHY the tool doesn't fit, not WHO.

---

## How the RACE audit uses this file

When Constraints scored ≤15 in a RACE audit:

1. Identify which of the 6 templates matches the user's product category.
2. Output the matched template as "Here's a starting structure — customize for your actual ICP."
3. Include the Rules for adapting section so the user knows how to customize it.
4. Reference this file's path in the "for more templates" line.
5. **Never present the template as the user's actual constraints — present it as editable starter text.**
