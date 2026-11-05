---
name: initial-report
description: 'Present the first Evermuse report after the initial source scan - Use right after ingestion completes, when the user picks "Get my initial report", runs find_skills:initial-report, or asks ''show me my initial report'', ''what did you learn from my sources'', ''give me the first report'', or ''what patterns did you find''. Trigger terms: initial report, first report, what did you learn, show me the report, post-scan report, patterns across my sources.'
category: Discovery & Research
tags:
- evermuse
- report
- onboarding
---

# Initial Report (first report after the first scan)

The first thing Evermuse shows a user once it has scanned and processed their sources: a report of the patterns it has learned across everything it ingested. This skill is almost always reached right after setup — from the post-ingestion view's "Get my initial report" option, or via `find_skills:initial-report`. The job here is small and precise: land the framing in chat, then hand the moment over to the interactive report UI.

# How to run the initial report

Run a few 'search' queries to get a good sense of what's in the ingested sources. Other tools can be helpful but search should be your primary method. Use find_skills and read_skills as needed. Since this report might run right after ingestion, there might not be sufficient clustering or even signals yet. If there aren't - please inform the user that the ingestion is still ongoing and it's advisable to wait.

If there are a few hundred signals at least, then it's OK to proceed. Write a report of the patterns and insights found across the sources, with a focus on new, surprising, and actionable insights. The user is probably aware of the number 1 and 2 top patterns, so state them casually as the clear pattern but focus more on the 3rd, 4th, and 5th patterns, or any clear quick wins emerging from the data. If there are no patterns yet, please inform the user that the ingestion is still ongoing and it's advisable to wait.

