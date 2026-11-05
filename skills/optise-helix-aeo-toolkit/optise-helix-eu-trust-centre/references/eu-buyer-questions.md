# The 8 EU Buyer Questions

**Used by:** `optise-helix-eu-trust-centre` (primary), `optise-helix-prompt-pack-builder` (secondary, Category 4 prompts).
**Source:** Optise EU AEO Playbook, page 12 ("Winning AI Search in Europe — The questions EU buyers ask AI engines about your tool").

These 8 questions are the canonical EU buyer compliance taxonomy. Every B2B SaaS site selling into Europe needs answers to all 8 in plain language, in extractable form, with the answers verifiable by Security/Privacy/Legal personas.

A site missing answers to 4+ of these questions is functionally invisible to EU buyer procurement processes — even if the company is technically compliant.

---

## The 8 questions (verbatim from page 12)

1. **Is [tool] GDPR compliant?**
2. **Is customer data stored in the EU?**
3. **Does [tool] offer EU data residency?**
4. **Can I get a DPA for [tool]?**
5. **Who are the subprocessors and where?**
6. **What data is collected and for how long?**
7. **Does [tool] use third-party AI providers?**
8. **What security standards does [tool] meet?**

---

## Why these 8 (not more, not fewer)

- They map 1:1 to the procurement intake forms used by mid-market and enterprise EU buyers (Germany Mittelstand, French ETI, Dutch corporate, Nordic enterprise).
- They cover the entire GDPR Article 28 + Article 30 compliance surface a buyer's DPO will check before approving a vendor.
- They are the prompts buyers actually type into ChatGPT, Perplexity, and Gemini when evaluating tools — not the prompts vendors *think* they ask.
- Adding more questions creates page bloat that hurts FITq Quoteability scores. Removing any of them creates a procurement gap.

---

## Answer block templates

Each question has a recommended answer block structure: a 1-sentence direct answer, a 1-paragraph plain-language expansion, and a "where to verify" link. Templates below — fill in `[User to add: …]` placeholders with actual company data, never invent.

**Template rule (mandatory):** every factual statement in these templates is a placeholder until the user confirms it. Keep a sentence only if the user supplied that fact in this session; otherwise output the `[User to add: ...]` version. Never output a compliance claim (GDPR status, DPA terms, notice periods, certifications, retention periods, AI data flows) that the user did not state.

### Question 1 — Is [tool] GDPR compliant?

**Direct answer (1 sentence):**
> [User to add: Yes / In progress / No]. [Tool name] [User to add: GDPR status exactly as the user states it] and acts as [User to add: Data Processor, Data Controller, or both] under EU Regulation 2016/679.

**Plain-language expansion (3-5 sentences):**
> [Use each sentence only if the user confirms it.] We meet our obligations under GDPR Articles 28 (processor obligations), 30 (records of processing), 32 (security of processing), and 33 (breach notification) [User to add: confirm which of these apply]. Our Data Processing Agreement is [User to add: how and when customers can sign it]. We maintain a record of processing activities [User to add: confirm]. [User to add: name of DPO if appointed] is our designated Data Protection Officer.

**Where to verify:**
> [link to DPA page] · [link to Records of Processing summary] · [link to GDPR compliance page]

---

### Question 2 — Is customer data stored in the EU?

**Direct answer:**
> [Yes, customer data is stored exclusively in the EU.] OR [Customer data is stored in [region], with EU-only options available on [plan name].] — DO NOT INVENT THIS. Use [User to add: actual data residency status].

**Plain-language expansion:**
> Our primary data centers are located in [User to add: city, country, region, e.g., "Frankfurt, Germany (AWS eu-central-1)"]. Customer content (defined in our DPA) is stored in those regions. [User to add: does customer content ever leave those regions, for example for support, backups or AI features, and under what conditions?] Backups are held in [User to add: backup region].

**Where to verify:**
> [link to data residency page] · [link to subprocessor list with regions]

**Anti-hallucination note:** This is the question most likely to get a vendor sued if answered incorrectly. NEVER assume EU residency. Always require the user to confirm.

---

### Question 3 — Does [tool] offer EU data residency?

**Direct answer:**
> [Yes, EU data residency is available on [plan tier] and is the default for [customer segment]. ] — Use [User to add: actual residency offering].

**Plain-language expansion:**
> EU data residency means all customer content, processing, and backups stay within the EU. We offer this through [User to add: cloud provider + region, e.g., "AWS Frankfurt and AWS Dublin"]. Customers on [User to add: plan name] can request it [User to add: how and when]. [User to add: exceptions, if any, for support, analytics, or AI processing, and whether customer consent is required].

**Where to verify:**
> [link to data residency page] · [link to plan comparison page showing residency by tier]

---

### Question 4 — Can I get a DPA for [tool]?

**Direct answer:**
> [User to add: Yes / No / Enterprise only]. [User to add: who can get the DPA and at what stage it can be signed].

**Plain-language expansion:**
> [Use each sentence only if the user confirms it.] The [Tool name] DPA [User to add: does it incorporate the EU Standard Contractual Clauses for transfers outside the EU?]. It is [User to add: pre-signed by [Tool name], or signed by both parties]. It covers [User to add: what the DPA covers, for example processing instructions, security measures, subprocessor list, data subject rights]. Negotiated DPAs are available for [User to add: enterprise tier or threshold, or "not offered"].

**Where to verify / how to get it:**
> Email [User to add: DPA request email, e.g., "dpa@[tool].com"] OR [link to self-serve DPA download page]

**Optise note:** The DPA should be 1-click accessible, not hidden behind a sales call. EU buyers who can't get a DPA quickly assume the vendor doesn't have one.

---

### Question 5 — Who are the subprocessors and where?

**Direct answer:**
> We use [User to add: number] subprocessors, listed below with their location and the data they process. [User to add: how and how far in advance customers are notified of new subprocessors, or "no notice commitment"].

**Plain-language expansion:**
> [User to add: full subprocessor table with: Subprocessor name | Service provided | Data type processed | Location of processing | Country of legal entity]
>
> Example row format:
> | Subprocessor | Service | Data type | Region |
> |---|---|---|---|
> | [Subprocessor name] | [Service, e.g. hosting, email, billing, LLM API] | [Data type processed] | [Region and transfer mechanism] |

**Where to verify:**
> [link to live subprocessor page] · [link to subprocessor change notification policy]

**Critical:** EU buyers will check this list during evaluation. Missing subprocessors or vague entries ("various cloud providers") immediately fail the security review.

---

### Question 6 — What data is collected and for how long?

**Direct answer:**
> We collect [User to add: categories of data, e.g., "account information, usage telemetry, and customer-uploaded content"] and retain it for [User to add: retention rule, for example the contract term plus a stated backup period].

**Plain-language expansion:**
> | Data type | Purpose | Retention | Deletion |
> |---|---|---|---|
> | [User to add: data type] | [User to add: purpose] | [User to add: retention period] | [User to add: deletion method] |
>
> (One row per data type the user lists, for example account info, usage telemetry, customer content, support tickets.)
>
> Customers can export and delete their data through [User to add: self-service mechanism or email].

**Where to verify:**
> [link to privacy policy] · [link to data deletion request flow]

---

### Question 7 — Does [tool] use third-party AI providers?

**Direct answer:**
> [Yes — we use [User to add: AI providers] for specific features, with the data flow described below. Customer content is [User to add: never sent / sent with anonymization / sent with opt-in consent].] — Use [User to add: actual AI usage].

**Plain-language expansion:**
> Our product uses [User to add: e.g., "OpenAI GPT-4 via Azure OpenAI EU endpoint"] for [User to add: feature description]. When this feature is invoked, [User to add: exact data flow — what is sent, what is excluded, retention by the AI provider]. [User to add: is a DPA in place with each AI subprocessor?] [User to add: can customers opt out of AI features, and how? link to opt-out flow].

**Where to verify:**
> [link to AI features page with data flow diagram] · [link to subprocessor list showing AI providers]

**Critical for 2026:** The EU AI Act applies in stages, with many obligations applying from August 2026 (verify the exact dates for the user's use case per operating-principles Rule 5). Buyers will increasingly ask follow-up questions: which AI Act risk category does this use fall into, is the AI provider in the EU, is there a DPIA. Be ready.

---

### Question 8 — What security standards does [tool] meet?

**Direct answer:**
> [Tool name] is certified [User to add: e.g., "SOC 2 Type II, ISO 27001"] and aligns with [User to add: e.g., "GDPR, the NIS2 Directive, and the EU Cyber Resilience Act"].

**Plain-language expansion:**
> | Standard | Status | Verification |
> |---|---|---|
> | SOC 2 Type II | [User to add: Certified / In progress / Not pursuing] | [User to add: what evidence is available and how] |
> | ISO 27001 | [User to add: status] | [User to add: evidence] |
> | GDPR | [User to add: status as the user states it] | [User to add: evidence, for example DPA] |
> | EU AI Act | [User to add: status and risk category] | [User to add: evidence] |
> | NIS2 | [User to add: applicable / not applicable] | — |
>
> [User to add: penetration testing frequency and vendor, or "not stated"]. [User to add: incident notification commitment to customers; GDPR Article 33 sets the 72-hour deadline for notifying the supervisory authority, not customers].

**Where to verify:**
> [link to security page] · [link to trust portal / compliance pack request]

---

## Output assembly rule

The `optise-helix-eu-trust-centre` skill assembles answers in this order on the page:

1. **Page H1:** "Trust & Compliance" (or localised equivalent)
2. **Page BLUF (40-60 words):** Direct summary of the user-confirmed GDPR status, where data lives, how to get the DPA, and the certifications with their exact status. Placeholders for anything not confirmed.
3. **Question 1 — GDPR compliance**
4. **Question 2 — Data location**
5. **Question 3 — EU data residency**
6. **Question 8 — Security standards** (moved up from #8 because it answers the highest-frequency follow-up)
7. **Question 4 — DPA availability**
8. **Question 5 — Subprocessors table**
9. **Question 6 — Data collection and retention**
10. **Question 7 — Third-party AI providers**
11. **DPA request CTA**
12. **JSON-LD schema block** containing all 8 Q&A pairs. Per operating-principles Rule 4, FAQPage is no longer eligible for Google rich results on corporate compliance pages: either use the eligible substitute (`Organization` + `hasCredential` + `WebPage`) or, if FAQPage is kept for other AI parsers, include the Rule 4 disclosure note.

Order rationale: questions 1-3 + 8 are the "go/no-go" filter questions. Questions 4-7 are the deeper-dive questions a security reviewer asks once the company has cleared the filter. Putting them in this order means a reviewer can stop reading at #4 and have everything they need to forward the page to procurement.
