# EU Market Guide (English-language only)

**Used by:** `optise-helix-prompt-pack-builder` (primary), `optise-helix-eu-trust-centre` (secondary), `optise-helix-fitq-audit` (tertiary).
**Source:** Optise EU AEO Playbook, Section 7 (Europe-Specific Reality) + Section 10 Step 1.
**Scope:** English-language prompts only. Multilingual variants are deferred to v2.

## Contents
- Why English-only at v1
- The 5 EU market clusters (DACH, Nordics, France, Benelux, Southern Europe)
- Cross-market English-language patterns
- Regulated vertical terminology (health, fin, legal, energy, public sector)
- Market-specific trust signals

---

## Why English-only at v1

European B2B buyers — especially in DACH, Nordics, Benelux — search predominantly in English when researching tools. Local-language search dominates only in France, Spain, Italy, and Portugal. Building English-only at v1 covers the high-volume use cases without the maintenance cost of validating multilingual prompt quality. Multilingual ships in v2 if there is real demand.

What this means for the prompt-pack-builder: every prompt is generated in English, even when the target market is DACH. The prompt format uses English regulatory terms (GDPR, not DSGVO) — but always includes the local regulatory acronym buyers actually use as a parenthetical anchor where it adds search value (e.g., "BSI C5 testat" stays as-is because that's how German buyers literally type it).

---

## The 5 EU market clusters

### DACH (Germany, Austria, Switzerland)

**Market characteristics:** Most rigorous compliance market in Europe. Buyers care about subprocessors, data residency, and named legal frameworks. German Mittelstand companies (200-2000 employees) are the highest-value B2B buyer segment in Europe.

**English-language prompt patterns:**
- `best [category] software for German companies`
- `[tool] GDPR compliance Germany`
- `[tool] data centers in Frankfurt`
- `[tool] BDSG compliance` (Bundesdatenschutzgesetz — Germany's federal data protection act)
- `is [tool] used by German Mittelstand`
- `[tool] for Mittelstand IT`
- `[tool] SOC 2 ISO 27001 Germany`
- `[tool] BSI C5 testat` (German federal cloud security catalogue)

**Trust signals DACH buyers look for:** ISO 27001, BSI C5 (for regulated industries), hosting in Germany or EU, explicit DPA/AVV available, named subprocessors with locations.

**Decides-deal weighting:** Compliance prompts score 5/5 universally. ISO 27001 is table stakes — its absence is disqualifying.

### Nordics (Sweden, Norway, Denmark, Finland)

**Market characteristics:** Highest EU AI adoption per Eurostat 2025 (Denmark 42%, Finland 38%, Sweden 35%). English-language search is the norm. Buyers care about sustainability, accessibility, and public-sector references.

**English-language prompt patterns:**
- `best [category] for Nordic B2B`
- `best [category] software used by Swedish companies`
- `[tool] WCAG 2.1 AA compliance`
- `[tool] sustainability report`
- `[tool] EU data center options`
- `best AI tool for Danish startups`
- `[tool] Nordic public sector references`

**Trust signals Nordic buyers look for:** EU hosting, WCAG 2.1 AA accessibility compliance, sustainability disclosures, public-sector customer references, transparent pricing.

**Decides-deal weighting:** Compliance prompts score 5/5 but accessibility (WCAG) is uniquely high-stakes here — score 4/5 minimum, often 5/5 for public-sector buyers.

### France

**Market characteristics:** Sovereignty-conscious. Buyers prefer hosting in France or in EU clouds with explicit data residency commitments. French regulatory framing (CNIL) is more salient than generic GDPR framing.

**English-language prompt patterns:** French buyers search in English for technical comparisons:
- `best [category] software French enterprise`
- `[tool] CNIL compliance`
- `[tool] hosted in France`
- `[tool] French data sovereignty`
- `[tool] HDS certification` (Hébergeur de Données de Santé — mandatory for health data hosting in France)
- `[tool] alternative to [US competitor]`
- `[tool] ANSSI security visa`

**Trust signals French buyers look for:** CNIL alignment statement, French or EU hosting, ANSSI visa for sensitive industries, explicit data sovereignty commitment, French-language customer support availability.

**Decides-deal weighting:** Sovereignty prompts score 5/5 in France. The "is [tool] hosted in France" question is a hard filter for many French enterprises.

### Benelux (Netherlands, Belgium, Luxembourg)

**Market characteristics:** Highest English-language search rate in Europe (especially Netherlands). Heavily multinational B2B markets. Buyers care about cross-border data flows because their customers span multiple jurisdictions.

**English-language prompt patterns:**
- `best [category] for Dutch B2B`
- `[tool] GDPR compliance Netherlands`
- `[tool] EU cross-border data transfer`
- `[tool] multinational compliance`
- `[tool] SCC implementation` (Standard Contractual Clauses)
- `[tool] used by Belgian enterprises`

**Trust signals Benelux buyers look for:** SCCs in DPA, data transfer impact assessments, EU hosting, multilingual customer support availability (English at minimum).

**Decides-deal weighting:** SCC and DPA prompts score 5/5. Multinational deployment prompts score 4/5.

### Southern Europe (Spain, Italy, Portugal)

**Market characteristics:** Lower AI adoption than Northern Europe but growing fast. Local-language search dominates more here than in DACH/Nordics — meaning English-language prompts cover a smaller share of total intent. Price sensitivity is higher than Northern Europe.

**English-language prompt patterns:**
- `best [category] software for Spanish enterprises`
- `[tool] pricing Europe in euros`
- `[tool] EU hosting`
- `[tool] used by Italian companies`
- `[tool] GDPR compliance Spain`
- `best [category] for Portuguese B2B`

**Trust signals Southern European buyers look for:** Local-language support availability, EU pricing transparency in EUR, EU hosting, references from local market leaders.

**Decides-deal weighting:** Pricing prompts score 5/5 here (price sensitivity higher than Northern Europe). Compliance prompts still 5/5 but secondary in importance.

**v2 note:** Southern Europe is the highest-value addition for v2 multilingual support, because English-language search captures less of the intent here than in other markets.

---

## Cross-market English-language patterns

Use these regardless of which specific EU markets the user targets. They are universally relevant across all 5 clusters.

1. **The "in Europe" qualifier** — Add `in Europe` or `for European companies` to any shortlist prompt. This signals the buyer is filtering for EU compliance and EU residency.
2. **The "alternative to [US tool]" pattern** — EU buyers actively search for EU alternatives to dominant US tools. Always generate one of these if the user has a US competitor.
3. **The DPA / data residency double** — Always include both "does [tool] offer a DPA" AND "where is [tool]'s data hosted". They are different searches with different intents.
4. **The EU AI Act question**: the EU AI Act applies in stages (check the current dates on the official EU pages before citing any), and prompts about "is [tool] EU AI Act compliant" are growing in volume. Include at least one.
5. **The subprocessor question** — "Who are [tool]'s subprocessors" is a uniquely European prompt — US buyers don't ask this. Include it.
6. **The certification stack** — "[tool] SOC 2 ISO 27001" is a single combined prompt, not two separate ones. EU buyers expect to see both.

---

## Regulated vertical terminology

When the user is in a regulated vertical, generic GDPR/DPA prompts are necessary but not sufficient. Include vertical-specific compliance prompts using the exact regulatory acronyms buyers in that vertical search for.

### Health-tech (DACH primary, all EU secondary)

- `[tool] BfArM certification` — German Federal Institute for Drugs and Medical Devices
- `[tool] DiGA approval` — German Digital Health Applications directory
- `[tool] KHZG eligible` — German Hospital Future Act funding
- `[tool] MDR conformity assessment` — EU Medical Device Regulation
- `[tool] IVDR compliant` — EU In Vitro Diagnostic Regulation
- `[tool] HDS certified` — French Hébergeur de Données de Santé
- `[tool] EHDS compliant` — European Health Data Space (effective 2026)
- `[tool] FHIR compatible` — health interoperability standard

### Fin-tech (all EU markets)

- `[tool] DORA compliance` — Digital Operational Resilience Act
- `[tool] MiCA compliance` — Markets in Crypto-Assets regulation
- `[tool] PSD2 compliant` / `[tool] PSD3 ready`
- `[tool] AML5 / AML6 compliance`
- `[tool] EBA guidelines alignment`
- `[tool] BaFin licensed` — German financial regulator
- `[tool] ACPR approved` — French banking authority

### Legal-tech / privacy-tech

- `[tool] eIDAS qualified` — Electronic identification and trust services
- `[tool] eIDAS 2.0 ready` — EU Digital Identity Wallet
- `[tool] qualified electronic signature`
- `[tool] EU AI Act high-risk classification`

### Energy / utilities (DACH especially)

- `[tool] BSI C5 testat`
- `[tool] KRITIS compliance` — German critical infrastructure regulation
- `[tool] §8a BSIG compliance`

### Public sector (all EU)

- `[tool] EVB-IT compliant` — German public sector IT contract framework
- `[tool] OpenPEPPOL compliant` — EU public procurement

---

## How the prompt-pack-builder uses this section

When the user's category indicates a regulated vertical (e.g., "EHR", "patient management", "trading platform", "lending", "compliance management"), the skill should:

1. Include 4-6 vertical-specific compliance prompts in addition to the standard 8 EU buyer questions
2. Score all vertical-specific compliance prompts 5/5 (these are universal disqualifiers in regulated verticals)
3. Add a callout: *"This pack is for a regulated vertical. Compliance prompts dominate. Your Trust Centre is the highest-leverage page in this pack — recommend running `optise-helix-eu-trust-centre` immediately."*

---

## Output formatting rule

When the prompt-pack-builder generates a prompt for a specific EU market, present it with the Market column visible:

```
| Prompt | Category | Decides | Target page | Market |
|---|---|---|---|---|
| best [category] software for German companies | Shortlist | 4/5 | /alternatives | DACH |
| [tool] BSI C5 testat | EU Privacy | 5/5 | /trust | DACH |
| best [category] for Nordic B2B | Shortlist | 4/5 | /nordics | Nordics |
```

Always include the Market column when the pack covers more than one EU market cluster.
