# Campaign continuity

Use a private writable host folder outside the plugin; choose a safe default when available and show the location without an unnecessary question. Save portfolio-wide defaults and separate records for each website, market and accepted panel. Do not store this user state in the source repo, plugin exports or a public issue. Create private directories/files with restricted permissions and preserve old revisions. Load existing settings on return.

Maintain a budget ledger with baseline and monthly portfolio limits, site allocations, per-run allocation/reservation, Actor/run/build IDs, status, observed charges, unresolved charges, platform allowance and remaining available allocation. An unresolved run holds its reservation. Sum every site's reservations before launching; do not reset the budget when switching sites, skills or chats. Native Apify recurrence is projected separately from a host-enforced ledger; do not claim unsupported shared enforcement.

Maintain an evidence index for saved inputs, dataset exports, summaries and timestamps; an action ledger with action ID, supporting observations, owner, priority, suggested work and next matching measurement. Raw credentials, account metadata and private customer data do not belong in campaign records. Avoid overwriting earlier panels/results. A user-provided export lacking provenance can support qualified observations, not a verified historical comparison.

## Portfolio record

Store a readable `portfolio.json` (schema version 2) and reports/evidence in a private host directory. These are host-created data, not packaged runtime files. Minimum structure:

```json
{
  "schemaVersion": 2,
  "portfolioId": "portfolio-a",
  "planRevision": 1,
  "status": "draft",
  "timezone": "UTC",
  "budget": {"baselineCapUsd": null, "monthlyCapUsd": null, "monthlyPolicy": "unconfirmed", "platformAllowanceUsd": null},
  "approvals": [],
  "websites": [{
    "websiteId": "site-a", "domain": "example.com", "label": "Example", "status": "draft",
    "business": "", "audience": "", "goals": [], "monthlyAllocationUsd": null,
    "context": {"claims": [], "constraints": [], "preferences": [], "corrections": [], "priorityPages": [], "pendingDecisions": []},
    "markets": [{"marketId": "market-a", "country": "", "language": "", "device": "desktop", "actorLocations": {}}],
    "panels": [{"panelId": "panel-a", "revision": 1, "marketId": "market-a", "status": "proposed", "modules": [], "competitors": [], "googleKeywords": [], "aiKeywords": [], "aiQuestions": [], "platforms": [], "targetUrls": [], "moduleInputs": {}}]
  }],
  "tracking": [], "runs": [], "budgetLedger": [], "evidence": [], "actions": [],
  "hypotheses": [], "feedback": [], "activity": [],
  "reporting": {"destination": "in-chat", "frequency": "on-demand", "alertRules": [], "lastDelivered": [], "quietHours": null, "maxNotificationsPerPeriod": null}
}
```

Null/empty required settings are unconfigured, never zero-budget authorization. Site IDs are unique and stable; same normalized domain can have multiple market/panel records. Explicitly distinguish separate subdomain/country scope. A run records websiteId, marketId, panelId/revision, module, actorId, run/build ID, occurrence/execution ID, input/evidence paths, coverage, timestamps, charges and reservation. Batch runs map every row to its website(s); count shared charges once and use a recorded allocation rule.

Approval records specify plan revision, baseline/recurrence scope, caps, timing/duration and reporting destination; no raw transcript is needed. A portfolio approval never implicitly authorizes added sites, larger panels or higher frequency. Effective dates and monthly rollover must retain old ledgers and unresolved charges. Tracking records include backend, ownership marker, site/market/module/panel mapping, schedule/action IDs or host task ID, cadence/timezone, accepted caps, end/review date, nextRunAt, configuration readback, last execution/run and verification state.

Status is draft, ready, baseline pending/completed, schedule prepared/configured, verified tracking, paused or blocked as applicable. One site's failure need not mark all sites failed, but unresolved reservations remain held. Pause flags must persist across chats; removing a site requires pausing its schedules first and preserving historical results. A schedule record cannot become verified solely from a successful creation response. A delivered report needs destination/acknowledgement evidence and a deduplication marker; never store credentials there.

Read [scheduling](../../scheduled-visibility-tracking/references/scheduling.md) for recurrence and cost controls. Compare matching windows and panels; observed changes do not establish causation.

## Research and report continuity

Follow [visual reporting](reporting.md). Save inferred settings with source/rationale/confidence, measured observations with provenance, timestamped reports and a concise `context.md` plus report index. Record access route and verified capabilities without secrets. Load known state automatically. If the host cannot persist files, provide exportable state and state the continuity limitation. A research-selected panel under delegated defaults may be ready without per-keyword approval; spend and recurrence remain separately authorized.

## Context, hypothesis and action records

Use [business context](business-context.md), [adaptive research](adaptive-research.md) and [feedback](feedback-and-reviews.md). Claims have IDs, scope, provenance, sources, dates, confidence rationale and superseded/active status. Hypotheses record observation/evidence, alternatives, missing evidence, selected check/cost rationale, status and result. Never save speculation as a measurement.

Actions retain website/market/panel IDs, evidence, target page, work/draft artifact, rationale/effort/confidence, status, feedback IDs, implementation date/verification, follow-up due/panel/evidence and outcome limitations. Append dated transitions; preserve rejected/deferred actions rather than regenerating them as new advice. Feedback is scoped to an action/claim. Activity records observable events with deduplication IDs; absent session/read events remain unknown.

## Safe migration and writes

Read state before writing. Version 1 is supported: retain a private pre-migration snapshot; preserve unknown fields, IDs, plan/panel revisions, approvals, runs, reservations, charges, schedules, pauses, evidence/artifact paths and delivery markers. Add v2 context/feedback/hypothesis/activity fields only where absent; don't reset ledgers or infer approvals. Save a dated migration record. Migration doesn't change accepted plan scope or authorize spending.

Don't overwrite malformed or newer unsupported state with defaults. Recover a verified snapshot or provide a read-only report; block paid starts until reconciled. Use host-supported atomic replacement/locking for concurrent writes; JSON isn't a mutex. If safe writes aren't supported, provide prepared state/export and disclose the limitation. Claim storage only after write/readback.

## Executable handoff for the next session

Keep a compact `handoff.md` beside private state: task/operation ID, accepted goal and scope, current plan/panel revision, last verified artifact, pending run/download offset, held reservation, blocker, one exact next action and the capability/approval it needs. Link the [operation receipt](operation-receipt.md), not raw transcripts. On “continue”, compare the handoff with current files and run identity before writing or collecting. Stale/mismatched state is STATE_CONFLICT; do not reset it or replay a launch. Save a new observation without rewriting historical evidence. Receipts are additive to schema v2; no campaign migration or new approval is implied.
