# Third-Party Bridge (find_tool / call_tool)

Evermuse can relay calls to other MCP servers connected to the workspace — Linear, Jira, GitHub, Notion, Attio, Intercom, Fireflies. This lets a skill, say, pull a PR from GitHub or post a follow-up in Intercom without leaving the flow. It is **optional and often unavailable**, so treat it as enrichment, never as a dependency.

## The pattern: try once, then fall back

```
1. find_tool(query: "get a pull request", server: "GitHub")   // discover
2. call_tool(connection_id, tool_name, arguments)             // invoke
```

- `find_tool` returns candidates with `connection_id`, `server_name`, `tool_name`, `description`, `input_schema`, plus pagination (`has_more`, `next_offset`). If you pass only `server`, you get all its tools; with a `query` you get a semantic-ranked short list.
- `call_tool` needs the `connection_id` and `tool_name` from `find_tool`, and `arguments` matching that tool's `input_schema`. Costs ~2 credits.

## Graceful degradation (required)

Third-party access needs the `mcp:thirdparty` scope and a connected server. Either may be missing. **Try once; on any permission/scope/empty error, fall back and keep going** — never fail the deliverable because enrichment was unavailable.

| Wanted via bridge | If blocked, fall back to |
|---|---|
| GitHub PR / diff / issues | `gh` CLI (`gh pr view`, `gh pr diff`), or ask the user to paste |
| Linear / Jira ticket | ask the user for the ticket text, or skip |
| Intercom / email follow-up | list the customers to contact and let the user send |
| Notion doc | ask for the content, or skip |

Say what happened in one line ("GitHub isn't reachable through Evermuse here, so I used the `gh` CLI instead") — don't silently drop capability.

## When to even try

Only reach for the bridge when it materially improves the deliverable (e.g. `review-pr` fetching the actual diff, `release-notes` notifying the customers who asked). For everything else, the native Evermuse evidence tools are the point — don't detour through third-party tools you don't need.
