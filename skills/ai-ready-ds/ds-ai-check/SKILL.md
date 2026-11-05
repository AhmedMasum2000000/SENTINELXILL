---
name: ds-ai-check
description: "Run an AI readiness audit on a Figma design system. Use when the user asks to \"check my design system\", \"audit my DS\", \"is my design system AI ready\", \"run ds-ai-check\", \"check AI readiness\", or provides a Figma file URL and wants to know how AI-ready it is. All checks are deterministic and rule-based.\n"
metadata:
  version: "0.1.0"
  author: "Yeshika Senadeera"
---

# DS AI Readiness Check — Figma Audit

Run a deterministic, rule-based audit on a Figma design system file. Every check uses structured data from Figma MCP tools.

## Input

Require a Figma file URL from the user. Extract the file key from the URL (the segment after `/design/` or `/file/`).

## Step 1: Data Extraction

Gather all structured data using Figma MCP tools. Make these calls (parallelize where possible):

1. **`get_metadata`** with the file URL — returns file name, pages, component counts
2. **`get_variable_defs`** with the file URL — returns all variable collections, modes, and variable definitions (this is the token layer)
3. **`get_design_context`** with the file URL — returns component definitions, properties, variants, descriptions
4. **`get_code_connect_map`** with the file URL — returns Code Connect mappings between Figma components and code

If a tool returns empty or errors, record that category as "no data" (score 0) and continue.

## Step 2: Run Checks

Apply every check from `references/checks.md` against the extracted data. Each check is a deterministic rule that evaluates to PASS, PARTIAL, or FAIL based on pattern matching and counting.

**Critical: Do NOT use LLM judgment for any check.** Every check must resolve from the data alone:
- Count-based: "X out of Y variables have descriptions" → percentage
- Pattern-based: "variable name matches `{category}-{role}-{variant}-{state}`" → regex
- Presence-based: "Code Connect mappings exist" → boolean
- Structural: "variable collections include a semantic layer" → name matching

## Step 3: Score

Apply the scoring formula from `references/scoring.md`. Each category gets a 0-100 score. The overall AI Readiness Score is a weighted average.

## Step 4: Generate Report

Output the report using the template in `references/report-template.md`. The report is a markdown document with:

1. **Header** — file name, date, overall score with grade
2. **Scorecard** — table of all 6 categories with score and status icon
3. **Category Details** — for each category: what passed, what failed, specific recommendations
4. **Priority Actions** — top 5 highest-impact fixes ranked by score improvement potential
5. **Re-run Note** — remind the user they can re-run after making changes to track improvement

## Important Rules

- Never hallucinate data. If a Figma tool returns no variables, the Token Architecture score is 0. Do not guess.
- Never use LLM reasoning to "interpret" whether something passes. Apply the rules literally.
- Count everything. The report must show exact numbers: "14 of 23 components have descriptions (61%)".
- Be specific in recommendations. Not "improve naming" but "12 variables use raw names like `blue-500` — rename to semantic format `color-{role}-{variant}-{state}`".
- The report format must be consistent across runs so users can diff results.
