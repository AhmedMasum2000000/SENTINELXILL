# Operation receipt and recovery contract

The host creates a private `operation.json` per task outside the plugin. This is structured bookkeeping for the agent, not a bundled executable or proof of behavior. Validate against [the JSON schema](operation-receipt.schema.json) using an available validator when possible; otherwise inspect required fields and state rules and disclose that schema validation was not run. Record raw provider statuses separately from workflow state. Never convert a provider SUCCEEDED alone into completed research.

Required keys: schemaVersion, operationId, capability, scope, state, source, bounds, checkpoint, outputs, verification, error, nextAction. Scope carries stable website/market/panel/revision identifiers (null when genuinely unavailable). Source keeps Actor/run/build/dataset identity and observation time; unavailable values are null, never invented. For saved exports, keep their declared source versus verified identity distinct. Output entries identify private artifact paths, kinds and actual write/readback state; merely proposed files are not saved outputs. Preserve original provider rows/pages and fields; joins use the Actor's documented tuple or stable entity ID, with ambiguous matches unresolved.

| Workflow state | Meaning and next action |
| --- | --- |
| prepared | Input/draft exists; no launch; satisfy the specific missing capability or authorization |
| submitted | Returned run ID saved; poll that run only |
| collecting | Terminal/active run status and downloaded pages recorded; resume nextOffset |
| partial | Usable bounded subset; report coverage and exact continuation without declaring completion |
| completed | Requested scope reconciled and result produced; verification level still distinguishes saved export from live measurement |
| blocked | Required capability/auth/state/budget unavailable; preserve prior work |
| unknown_external_outcome | Submission may have happened; reconcile, hold reservation and never automatically replay POST |

Safe error codes: MISSING_RUNTIME, MISSING_PROJECT, INVALID_INPUT, DENIED_ACCESS, AUTH_REQUIRED, STATE_CONFLICT, PARTIAL_COMPLETION, UNKNOWN_EXTERNAL_OUTCOME, RATE_LIMITED, UPSTREAM_FAILED, STORAGE_UNAVAILABLE. Include a safe explanation, retryability for **reads only**, and one next action. Do not copy tokens, auth headers, raw logs, credential URLs or unrelated runs into errors. Diagnostics stay outside the receipt's JSON; the official CLI's stdout is provider output, not this contract.

Default bounds from the [CLI workflow](../../ai-visibility-tracker/references/cli-workflow.md): 20 polls, 100 rows/page, 20 successful pages, 2,000 rows, 600 seconds per observation/collection window, 60 seconds per read, at most two read retries. Store the actual invocation bounds. Connector/API routes apply equivalent controls. They bound local work, not billing: financial authorization, maxTotalChargeUsd, provider charge caveats and the shared ledger remain separate. A timeout stops observation, not the Actor. Settling charges requires independent readback.

Checkpoint: last observed status/time, successful pages/rows, nextOffset, dataset item-count observation/time, terminal flag and held reservation. Advance offset only after validated page write/readback. When resuming, verify artifact existence/readability and same-run/storage identity; a missing page or changed ID is STATE_CONFLICT. No schema can prove artifact existence, identity, paid authorization or actual execution: check them with the host. Never claim safe replay or auto-release an uncertain reservation.

Example — **synthetic interrupted download**, not a live result:

```json
{
  "schemaVersion": 1,
  "operationId": "synthetic-import-01",
  "capability": "citation-import",
  "scope": {"websiteId": "site-a", "marketId": "market-a", "panelId": "panel-a", "panelRevision": 1},
  "state": "partial",
  "source": {"kind": "synthetic", "actorId": "CFYLF6fOcyvdofuof", "runId": "abc123", "buildId": null, "datasetId": "data123", "observedAt": "2026-10-05T12:00:00Z", "identityVerified": false},
  "bounds": {"maxPolls": 20, "pageSize": 100, "maxPages": 20, "maxRows": 2000, "windowSeconds": 600, "readTimeoutSeconds": 60, "readRetries": 2},
  "checkpoint": {"providerStatus": "SUCCEEDED", "terminal": true, "pagesSaved": 2, "rowsSaved": 200, "nextOffset": 200, "datasetItemCount": null, "itemCountObservedAt": null, "heldReservationUsd": 3},
  "outputs": [],
  "verification": "synthetic_only",
  "error": {"code": "PARTIAL_COMPLETION", "message": "Download interrupted; coverage is incomplete.", "readRetryable": true},
  "nextAction": {"action": "resume_read", "description": "Verify saved pages and same-run dataset, then resume at offset 200 within existing scope.", "requires": ["user-owned Apify access", "private state read/write"]}
}
```

This example intentionally contains no claimed saved output; an actual receipt lists each file only after write/readback. Unknown submission instead has a null runId, UNKNOWN_EXTERNAL_OUTCOME and `reconcile_submission`. No access? Preserve the receipt and deliver existing partial analysis. No storage? Return downloadable JSON and mark persistence unavailable. Keep a compact handoff linked to the receipt and one next action; do not include the full chat.
