# Report Template

Generate the report in this exact structure. Replace placeholders with actual values.

---

## Report Output Format

```markdown
# AI Readiness Report: {file_name}

**Date:** {YYYY-MM-DD}
**File:** {figma_file_url}
**Overall Score:** {overall_score}/100 — Grade {grade}: {grade_label}

---

## Scorecard

| Category | Score | Status | Checks Passed |
|----------|-------|--------|---------------|
| Token Architecture | {score}/100 | {status_icon} | {passed}/{total} |
| Component Contracts | {score}/100 | {status_icon} | {passed}/{total} |
| Design-Code Parity | {score}/100 | {status_icon} | {passed}/{total} |
| Accessibility | {score}/100 | {status_icon} | {passed}/{total} |
| Documentation Quality | {score}/100 | {status_icon} | {passed}/{total} |
| Governance & Maintenance | {score}/100 | {status_icon} | {passed}/{total} |

---

## Detailed Results

### Token Architecture — {score}/100

{For each check in this category:}

**{check_id}: {check_name}** — {PASS|PARTIAL|FAIL}
{One line with exact data: "23 of 45 variables (51%) have multi-segment names"}
{If FAIL or PARTIAL: one line recommendation}

---

### Component Contracts — {score}/100

{Same format per check}

---

### Design-Code Parity — {score}/100

{Same format per check}

---

### Accessibility Readiness — {score}/100

{Same format per check}

---

### Documentation Quality — {score}/100

{Same format per check}

---

### Governance & Maintenance — {score}/100

{Same format per check}

---

## Priority Actions

Fixing these will have the biggest impact on your score:

| # | Action | Category | Current | Potential Gain |
|---|--------|----------|---------|----------------|
| 1 | {specific action} | {category} | {FAIL/PARTIAL} | +{points} pts |
| 2 | {specific action} | {category} | {FAIL/PARTIAL} | +{points} pts |
| 3 | {specific action} | {category} | {FAIL/PARTIAL} | +{points} pts |
| 4 | {specific action} | {category} | {FAIL/PARTIAL} | +{points} pts |
| 5 | {specific action} | {category} | {FAIL/PARTIAL} | +{points} pts |

---

## Next Steps

Run `/ds-ai-check` again after making changes to track your improvement.
Your design system's AI readiness is a continuous journey — each fix makes AI-generated output more consistent with your brand.
```

## Status Icons

Use these based on category score:

- 80-100: `Pass`
- 50-79: `Partial`
- 0-49: `Needs Work`

## Recommendation Writing Rules

Recommendations must be:
1. **Specific** — reference exact counts and names from the data
2. **Actionable** — tell the user exactly what to do in Figma
3. **Scoped** — one recommendation per failing check, not sweeping overhauls

Good: "Add descriptions to the 18 color variables in your 'Primitives' collection — prioritize semantic tokens like `color/action/primary`"
Bad: "Improve your token documentation"

Good: "Create a 'Semantic' variable collection that aliases your 'Primitives' — start with the 12 color variables used in components"
Bad: "Add a semantic token layer"
