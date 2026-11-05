# Persistent scheduling procedures

Verified against official documentation 2026-10-03. Refresh supported fields/tools when configuring. Use a capable user-owned route from [Apify access](../../seo-growth-agent/references/apify-access.md); the examples below use the official CLI fallback. Keep the credential binding in the scheduler's supported secret mechanism; no token strings, environment secrets or authentication paths in scheduled prompts or inputs. Read [execution rules](../../seo-growth-agent/references/execution.md) for allowlisted Actors and same-run evidence.

## Host recurring agent — complete pipeline

Offer a baseline followed by a small weekly fixed rank/citation panel, a monthly goal-selected opportunity review and a suitable follow-up after acknowledged implementation. These are editable proposals, not default activation. Separate collection cadence from report/digest cadence. An action follow-up isn't an extra paid job unless approved. Preview total occurrence counts/caps across all sites before activation.

Record the selected IANA timezone, next occurrence, start/end or review date, per-site modules, notification mode (requested digest or changes only), approved destination, accepted material-change thresholds/coverage, quiet hours and maximum frequency. Do not invent thresholds or inactive-user reminders. Verify notification preference enforcement; unavailable capability stays disclosed/prepared. An alert-only collection schedule still incurs research costs, which must be included in the plan.

Use the host's purpose-built recurring task tools when available. Discover supported timezone, persistent execution environment, state access, notifications and pause/update operations. Follow that host's recurring-task instructions. Keep the saved prompt human-readable and include:

- Private portfolio location and accepted plan revision; site/market/module selection and due cadences.
- This skill and the entry skill; approved Actor inputs/panels and per-run/site/portfolio caps, valid duration and stop conditions.
- Read and reconcile the durable ledger before each launch. Reserve within remaining allocation, persist returned run IDs, do not duplicate unresolved occurrences, and stop on errors or expired approval.
- Collect evidence, compare matching panels, create site reports and a portfolio rollup, and deliver only to the approved destination. If configured for changes only, stay quiet on unchanged results.
- Honor site/portfolio pause flags and record execution, delivery and charge markers. No outreach, content publication, extra Actors or paid retries.
- Load scoped business context, action status and feedback; select approved exploratory checks by the current goal, keep stable panels unchanged, and save the concise review format. Respect requested quiet hours/frequency limits. Separate run, generated report, confirmed delivery and human review events; no publisher telemetry.

Verify saved task ID, schedule/timezone, execution access and prompt by readback. If the scheduler does not provide a mutex/serial execution guarantee, use an atomic host-supported lock in private state; otherwise leave paid recurring launches disabled until serialization is verified and explain the missing capability. Do not claim a plain JSON file prevents simultaneous launches. A hard monthly cap requires verified serialization, complete reconciled charges and a defined platform-fee allowance; uncertain costs hold reservations. Calendar-month boundaries follow the selected billing timezone.

## Apify cloud — fixed input collection

This runs on Apify while the chat is closed. It collects data only. Use direct RUN_ACTOR schedule actions, not new tasks, to avoid unnecessary persistent resources. Only the schedule endpoints below expand the baseline skill's API scope; actions must target the visibility Actor or seven mapped specialists. Scope inventory to known portfolio resources; never copy unrelated users' inputs into reports.

Prepare one schedule per site/market/module/cadence by default, with a stable unique portfolio ownership marker in its name/description. Compute inputs from the accepted panel and schema. Create disabled after approval, then read back and enable only after all fields and budget projections match. No automatic test call or backfill.

An illustrative **disabled** visibility schedule body, not authorization or a default input, is:

```json
{
  "name": "avt-portfolio-a-site-a-ai-v1",
  "isEnabled": false,
  "isExclusive": true,
  "cronExpression": "0 9 * * 1",
  "timezone": "UTC",
  "description": "AI Search Visibility Tracker portfolio-a / site-a / panel-v1",
  "actions": [{
    "type": "RUN_ACTOR",
    "actorId": "CFYLF6fOcyvdofuof",
    "runInput": {"body": "{\"targetDomain\":\"example.com\",\"keywords\":[\"example topic\"],\"platforms\":[\"perplexity\"],\"queryTemplates\":[],\"customQueries\":[\"Which sources explain example topic?\"],\"maxQueriesPerKeyword\":1,\"demoMode\":false}", "contentType": "application/json"},
    "runOptions": {"build": "latest", "timeoutSecs": 600, "maxTotalChargeUsd": 1, "restartOnError": false}
  }]
}
```

Generate `runInput.body` with a JSON serializer from the actual validated input, rather than manually interpolating prompts. Replace example caps, identifiers, cadence and timezone with the accepted plan. Resolve local time using an IANA timezone; preview future occurrences, DST and short-month behavior with host calendar tools. Use isExclusive to request non-overlap for that schedule, not as a portfolio lock.

Official CLI requests (filenames are private, no-overwrite task files; IDs come from readback):

```sh
apify api POST /v2/schedules --body - < schedule-create.json
apify api GET /v2/schedules/SCHEDULE_ID
apify api PUT /v2/schedules/SCHEDULE_ID --body - < schedule-update.json
apify api GET /v2/schedules/SCHEDULE_ID/log
```

An enable/pause body changes only `isEnabled` to true/false. Never enable on uncertain POST outcome: paginate schedule inventory, match the ownership marker and full configuration, and record/reuse the existing ID. Reject conflicting or multiple matches pending resolution. Validate ID syntax and keep values out of shell code. Persist/read back each action's returned ID before action updates.

Native schedules expose per-action `runOptions.maxTotalChargeUsd`, not a portfolio monthly hard cap or automatic expiry field. A monthly projection sums each schedule's occurrence count × action cap across all websites/modules, plus platform/startup allowance and manual/baseline reservations. Count actual calendar occurrences; weekly is not always four per month. A requested hard limit or end date needs a verified external controller before enablement. Never silently label a projection as enforced or change account-wide limits. Apify's scheduling failure emails concern failure to start; they are not citation-change reports. Inspect actual notification settings in Console if requested; the documented create payload does not expose notification controls. Do not invent a notification API field, add a webhook, or promise digest delivery.

For scheduled execution proof, use its log to associate execution/action and run IDs, then retrieve only those runs and their input/results. Record build/model changes. If the log lacks a usable ID, match exact input, Actor and scheduled time; ambiguous matches remain unverified. An independent on-demand baseline does not prove the schedule fired. A host report job can consume these known runs without starting duplicates.

Sources: [create schedule](https://docs.apify.com/api/v2/schedules-post), [read schedule](https://docs.apify.com/api/v2/schedule-get), [update schedule](https://docs.apify.com/api/v2/schedule-put), [schedule execution log](https://docs.apify.com/api/v2/schedule-log-get), [platform scheduling](https://docs.apify.com/actors/running/schedules).
