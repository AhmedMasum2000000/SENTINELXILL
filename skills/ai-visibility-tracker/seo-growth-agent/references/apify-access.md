# Use the user's available Apify access

The package remains skills-only and registers no MCP server, connector or runtime. The host LLM uses integrations already available to the user. Prefer an existing user-owned connection that can fulfill the task safely; keep the official CLI as the documented Postiz-style fallback. Never reuse the publisher's credentials.

| Route | Capability check | Credentials |
| --- | --- | --- |
| Connected Apify MCP/connector | Discover actual available tools and their schemas; check exact Actor identity, input, supported run options, status, storage, pagination and charges | Reuse the user's authorized connection; no extra key request |
| Official Apify CLI | Verify `apify api`/stdin/parameters and local login with suppressed account output | User's official local `apify login` |
| Existing authenticated API integration | Host must make secure HTTPS requests, inject secrets without exposing values, and support the documented API | User enters their own Apify API key in the host's secure credential setup |
| No usable access | Continue public research or analyze saved exports | Ask to connect Apify or complete secure key/login setup; never paste a key into chat |

For MCP, inspect exposed tool schemas instead of inventing names or flags. The documented `call-actor` response provides status/storage IDs; retrieve actual dataset pages separately. Actor availability and permissions vary. Ensure the route can apply the authorized `maxTotalChargeUsd` as a run option, not Actor input, and retrieve required provenance. If a connector lacks charge-cap or evidence capabilities, use another verified route or explain the missing setup before paid execution. Never silently remove caps to use an easier tool. Do not run paid browser/discovery Actors outside the approved plan.

For direct API access, use only `https://api.apify.com` with the documented `/v2/actors/...`, same-task run/storage endpoints and separately approved schedule endpoints. Use structured JSON and numeric query parameters; the start request is `POST /v2/actors/ACTOR_ID/runs` with Actor input as JSON body and run controls such as `maxTotalChargeUsd`, `timeout` and `build` as documented parameters. Secret injection belongs to the host's credential mechanism using an Authorization header; never place tokens in URLs, commands, tool-visible arguments, files or reports. If the host cannot inject a secret safely, require CLI login or a supported connection. Do not read auth files or echo environment secrets.

Apply [execution](execution.md) identically across routes: mapped Actors, current schema/pricing, shared reservations, no duplicate starts, same-run evidence, pagination, real coverage and charge reconciliation. Switching route does not authorize another run or reset the ledger. Keep a non-secret route/capability label in state. Authenticate only to the user's account; uncertain ownership requires local verification. No installation or host configuration mutation is implied by capability discovery.

Sources verified 2026-10-03: [Apify MCP](https://docs.apify.com/integrations/mcp), [API authentication](https://docs.apify.com/api/v2), [Run Actor](https://docs.apify.com/api/v2/actors-runs-post). Refresh official documentation and exposed schemas when using a connection.
