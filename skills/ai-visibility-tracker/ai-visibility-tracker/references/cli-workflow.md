# Official Apify CLI workflow

This is the Postiz-style dependency boundary: the plugin ships skills; the independently installed CLI authenticates and executes. Use `apify-cli`, published by Apify, not a custom or invented visibility CLI. Commands and stdin/parameter flags were verified with local CLI 1.8.0 and current official docs on 2026-10-05. Local 1.8.0 reports that a newer version exists; do not silently upgrade. Recheck flags before live use.

For a capable existing MCP/connector or secure API integration, use [Apify access](../../seo-growth-agent/references/apify-access.md) instead of requiring CLI setup. This reference covers the CLI route only.

## Availability and authentication

```sh
apify --version
apify api --help
jq --version
apify info > /dev/null
```

The last command verifies the local logged-in account without printing account details. On an auth failure, the user completes `apify login` in their own terminal. Never run `apify auth token`, inspect auth files or ask for API keys in chat. Existing CLI authentication is sufficient; do not force reauthentication when a read succeeds.

If the CLI is absent, explain the external dependency and use the user's installation policy. The supported npm installation is `npm install -g apify-cli`; Node/npm or an official platform-specific installer is needed. Install/upgrade only that dependency within the user's authorized setup scope. Do not install MCP servers or alter unrelated host settings. If `apify api --help` lacks `--body` or `--params`, update via the official CLI release path or give the user a setup requirement; do not invent flags.

## Inspect the fixed Actor

```sh
apify api GET /v2/actors/CFYLF6fOcyvdofuof/builds/default/openapi.json \
  | jq '.components.schemas.inputSchema'
apify api GET /v2/actors/CFYLF6fOcyvdofuof \
  | jq '.data | {id, name, username, pricingInfos}'
```

Select the effective pricing entry with the latest `startedAt` that is not in the future. The billed check event is `keyword-visibility-checked`. Calculate event estimate from its `eventPriceUsd` and the planned check count. Inspect startup events and `isPPEPlatformUsagePaidByUser`; do not turn an absent field into a claim of free platform usage. Only these selected public metadata fields belong in the report. The convenience `actors info --input --json` command can return broad metadata in the verified CLI; use the narrow API schema command instead.

## Start with a budget

Write `input.json` in a private user-selected work directory. Replace the example charge cap with the amount already authorized by the user. The cap is an API query parameter, separate from Actor input:

```sh
apify api POST /v2/actors/CFYLF6fOcyvdofuof/runs \
  --body - \
  --params '{"maxTotalChargeUsd":2,"timeout":600,"build":"latest"}' \
  < input.json
```

It returns an API envelope with `.data.id` and initial run status. Save that ID immediately. This is a billable action; the example `$2` is not implicit spend authorization or a guarantee that platform/account costs are included. Respect the host's permission flow. A successful POST is submission evidence, not completed result evidence. Do not automatically retry a failed or timed-out POST: it may already have created a run.

Keep user prompts in the JSON file rather than interpolating them into shell commands. Treat run/storage IDs as alphanumeric identifiers returned by Apify, not executable strings. Quote filenames with spaces. Restrict this workflow's API calls to the named Actor and the run/storage identifiers it returns; arbitrary API mutation is outside the workflow.

## Status and resumption

```sh
apify runs info RUN_ID --json
apify runs ls CFYLF6fOcyvdofuof --desc --limit 10 --json
```

Substitute the actual returned ID. The list command is for recovering an uncertain submission; do not publish unrelated runs in the user's report. Match input/start time before deciding whether a fresh run is needed. Default to at most 20 status reads, 30-second intervals and a 10-minute observation window, whichever ends first. Bound each read to 60 seconds through the host command timeout; stop and checkpoint if that control is unavailable or a read hangs. These waiting limits do not cancel or relaunch the external run. Save the run ID/status and next read in the operation receipt; keep active or uncertain budget reservations held. Resume read-only after interruption. Keep the user informed. `apify runs wait` can block; interrupted waiting is not permission to relaunch.

Verify `actId: CFYLF6fOcyvdofuof`. Terminal statuses include `SUCCEEDED`, `FAILED`, `ABORTED`, `TIMED-OUT`. Preserve `buildId`, start/end timestamps, `usageTotalUsd` and charged event counts if returned. Charges are observations, not estimates; state when charge fields are unavailable or still settling.

## Collect only this run

Get the IDs from its run metadata. In a private directory, read:

```sh
apify key-value-stores get-value STORE_ID INPUT
apify datasets get-items DATASET_ID --format json --limit 100 --offset 0
apify key-value-stores get-value STORE_ID LAST_RUN_SUMMARY
```

Read dataset metadata first with `apify datasets info DATASET_ID --json`. Default to pages of 100, at most 20 successful pages/2,000 rows and a 10-minute collection window per invocation. Use a 60-second host timeout per read. Save each valid JSON array in a distinct page file before advancing the offset; an invalid response or failed write never advances it. Continue from the saved offset, not zero. Stop at the first bound and record PARTIAL, collected rows, item-count observation/time and nextOffset; never claim the first page or a capped download is complete. A short/empty page only supports completion after the run is terminal and metadata/observed coverage reconcile; an active dataset can still grow. Keep raw page files unchanged, including duplicates and provider-specific fields; deduplicate only derived views using documented tuple identity. Raising read bounds needs an explicit task scope, never increased paid run scope. See [operation receipts](../../seo-growth-agent/references/operation-receipt.md). Check `OUTPUT` and `RUN_SUMMARY` too if those records exist. A missing optional summary record is acceptable only after confirming not-found; auth, quota or server errors must be reported and resolved. Collect failed runs too when useful, but identify incomplete coverage.

Save input, rows, summary and selected run metadata outside the plugin using private permissions and distinct names. In POSIX shells, use `umask 077` and `set -C` before redirection to prevent accidental public permissions and overwriting; on other hosts use equivalent private-file and no-overwrite controls. Check command exit status before reading a redirected file as evidence. Never package user results, auth material or raw logs into a plugin release.

Use local JSON analysis tools already available to the host for formulas in the Actor contract. This plugin does not include an executable analytics script. Read-only analysis of saved exports requires neither a new Actor run nor a fresh API token.

## Bounded read recovery

For read-only 429/transient 5xx/network errors, make at most two retries after the initial attempt, respecting Retry-After within the observation window. If Retry-After exceeds the remaining window, checkpoint and return. Never retry invalid input, 401/403 or conflicting state automatically. Recovery of an unknown POST checks at most ten recent runs first and only matching candidates’ metadata/INPUT; if none is conclusively matched, keep UNKNOWN_EXTERNAL_OUTCOME and the reservation. A larger search is a separate bounded read step, not proof that the launch failed. No idempotency key or safe replay guarantee is claimed.

## Errors

| Condition | Action |
| --- | --- |
| CLI missing / incompatible flags | Set up the official CLI within the user's authorized scope. |
| Auth or authorization error | Have the user complete local login/check Actor access; keep tokens out of chat. |
| Quota/rate limit | Respect the limit and use a delayed read; do not expand paid run scope. |
| Ambiguous submission | Recover recent matching runs before any resubmission. |
| Successful run with diagnostics only | Report a health check or invalid-input result; no visibility metrics. |
| Partial provider failure or charge cap | Report observed checks and missing tuples separately. |
| No sources in an answer | Distinguish no-source evidence from a competitive content gap. |
| Host lacks execution/network | Provide commands or analyze a supplied export; no simulated live result. |

Sources: [official CLI commands](https://docs.apify.com/cli/docs/reference), [Run Actor API](https://docs.apify.com/api/v2/actors-runs-post), [Postiz CLI skill pattern](https://github.com/gitroomhq/postiz-agent/blob/main/skills/postiz/SKILL.md). The Postiz repository also contains other integrations; this plugin adopts only its skill-to-external-CLI pattern.

## User-owned credentials

Every live user authenticates to their own Apify account through an existing authorized connector/MCP connection, official local `apify login`, or secure host API-key setup. Never use, bundle, borrow or distribute publisher credentials. If ownership is uncertain, have the user verify the account locally before billable work. Existing user-owned access is sufficient; ask for connection or secure key setup only when access is missing. Never solicit tokens in ordinary chat or save them in campaign records. Saved-export analysis needs no token.
