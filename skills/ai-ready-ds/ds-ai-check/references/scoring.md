# Scoring System

## Per-Check Scoring

Each check evaluates to one of three results with a point value:

| Result   | Points |
|----------|--------|
| PASS     | 100    |
| PARTIAL  | 50     |
| FAIL     | 0      |

**Exception:** G1 (Deprecation Signals) scores FAIL as 50 (neutral baseline).

## Per-Category Score

Each category score is a weighted average of its checks:

```
category_score = sum(check_points × check_weight) / sum(check_weights)
```

Round to the nearest integer. Range: 0–100.

## Overall AI Readiness Score

The overall score is a weighted average of all 6 categories:

| Category               | Weight | Rationale                                                |
|------------------------|--------|----------------------------------------------------------|
| Token Architecture     | 25%    | Foundation — tokens are the contract AI reads             |
| Component Contracts    | 25%    | Components are what AI generates — must be well-defined   |
| Design-Code Parity     | 15%    | Bridges design and code — high value but many teams start here at zero |
| Accessibility          | 15%    | AI-generated code defaults are poor — DS must enforce     |
| Documentation Quality  | 10%    | Helps AI understand intent but overlaps with descriptions |
| Governance             | 10%    | Maintenance hygiene — important for long-term readiness   |

```
overall_score = (token × 0.25) + (component × 0.25) + (parity × 0.15) + (a11y × 0.15) + (docs × 0.10) + (governance × 0.10)
```

Round to the nearest integer.

## Grade Scale

| Score  | Grade | Label             | Meaning                                                    |
|--------|-------|-------------------|------------------------------------------------------------|
| 90-100 | A     | AI-Ready          | DS can be confidently used by AI agents for code generation |
| 75-89  | B     | Mostly Ready      | Strong foundation with some gaps to close                   |
| 55-74  | C     | Partially Ready   | Key areas need work before AI can reliably consume the DS    |
| 35-54  | D     | Early Stage       | Significant structural improvements needed                   |
| 0-34   | F     | Not AI-Ready      | Fundamental DS structure missing for AI consumption          |

## Score Improvement Potential

For the Priority Actions section, calculate the **improvement potential** of each failing check:

```
improvement_potential = (100 - check_points) × (check_weight / sum_category_weights) × category_weight
```

This tells the user: "Fixing this one check would raise your overall score by approximately X points."

Rank priority actions by improvement potential, highest first. Show the top 5.
