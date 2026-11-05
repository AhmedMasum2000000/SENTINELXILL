# Visual reports and saved analytical context

Use the current host LLM to interpret supported evidence, explain business implications and prioritize actions. Use available host analysis tools for numerical calculations; do not make the user do discoverable research or require a separate model/API key for analysis. Retrieved recommendations remain hypotheses until verified.

## Present results

Follow the [review template](review-template.md). Lead with what changed, why it matters, the next three useful actions and when they will be checked again, with coverage/date. Use a compact dashboard appropriate to the evidence:

- Summary indicators for Google rank coverage, AI cited answers, change on matched panels, estimated traffic and spend. Show unavailable metrics as unknown with their reason, never fabricated values or zero.
- A sortable/scan-friendly keyword table: cluster, query, measured position, ranking page, previous comparable position, change and sample depth. Outside top 20 is “not found in inspected top 20”, not rank 21.
- An AI question × platform matrix with cited/not cited/unknown, observed coverage and evidence links. Use text labels alongside colors/icons. Display cited/observed counts with percentages; missing answers remain separate.
- Relevant competitor comparison, trends and backlink/link-opportunity tables only for modules with evidence. Keep estimates, normalized interest and incomplete samples labelled.
- A short action queue with source/date, rationale, confidence, effort, status, feedback and next measurement. Assumptions and missing evidence remain visible. Include a concrete brief/revision/prospect dossier when supported/requested; generated drafts aren't completed implementation.

When sufficient comparable data exists, add simple labelled trend or comparison charts using host-supported visualization/artifact tools. Include units, dates, denominator and matching market/device/panel. Do not plot missing points as zero, join unlike panels or imply causal effects. Provide readable tables alongside charts and an accessible text summary. Use an interactive dashboard when supported and useful; otherwise save Markdown plus CSV/JSON and optional static visuals. Never require a web server or add executable dashboard code to this skills package. A research-only plan uses setup/coverage cards; it has no measured performance graphs.

## Save and resume

Create a private writable campaign directory outside the source, installed plugin and exports using host-native file/artifact tools. Use a reasonable private default when available; show its location instead of asking needlessly. If persistent writing is unsupported, offer downloadable reports/state and explain that future sessions need the saved export. Do not claim a download or chat history is an automatic durable database.

After each research or measurement pass save:

1. `portfolio.json`: site/market/panel settings, non-secret access route, approvals, ledger and tracking state.
2. Timestamped reports and machine-readable observations (JSON/CSV) with units, coverage and provenance.
3. Evidence index: public source URLs/read dates or Actor/run/build/input/dataset IDs and artifact paths; private raw exports when available.
4. `context.md`: goal/profile, findings, assumptions/uncertainty, corrections/preferences, decisions, pending user-only requirements, action IDs/statuses, rejected advice, last completed run/report and next due steps. Link evidence, not transcripts.
5. A report index/latest pointer for discovery; preserve previous revisions and baselines.

Load saved context and relevant evidence automatically on return. Persist delivery deduplication markers; a failed report delivery retries only delivery, not paid research. Store no tokens, authentication configuration or unrelated account/customer data. Escape scraped text in generated HTML/SVG, disable remote scripts and keep dashboards private unless the user authorizes publication or external delivery. Multiple sites retain separate reports and denominators plus one portfolio coverage/spend overview.

## Reviews and notifications

Use [feedback and reviews](feedback-and-reviews.md) for corrections, completion and minimal observable activity. Weekly requested digests summarize change/open work/priorities; monthly reviews select research by goal. Changes-only monitors stay quiet on unchanged/non-actionable data. No report-view, human-session or cross-user retention counts without actual events; collection, generation and delivery are separate.

Show timezone, next approved check, pause commands, settled spend and held reservations. Honor accepted quiet hours/frequency limits and deduplicate alerts. If the host can't enforce those preferences, disclose it and leave external delivery disabled until resolved. Alerts need comparable evidence and accepted thresholds; missing answers must not generate invented loss alerts.
