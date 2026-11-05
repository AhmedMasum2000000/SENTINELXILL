---
name: ansight-create-remote-tool-cordova
description: Use this skill when implementing a custom Ansight remote tool for a Cordova-family Capacitor app. Create a narrow JavaScript registerTool handler with a stable id, explicit read/write/critical policy, structured results, development-only registration, runtime guard access, and CLI verification.
---

## Claude Code plugin integration

Run Ansight CLI commands with Claude Code’s Bash tool on the machine that owns the resident host. If this session cannot execute commands or reach that host, explain the missing prerequisite and do not claim a live inspection succeeded. The plugin’s session-start note reports the CLI, host, and connected-session state it found; re-check with the commands below before acting on it. These skills describe the latest public Ansight CLI: if the session-start note or `ansight update check --json` reports an available update, offer `ansight update apply` with the user’s approval before relying on newer options, and treat `ansight <command> help` as the authority wherever it disagrees with this skill. A remote workspace or cloud agent does not automatically have access to the developer’s local host. Resolve relative helper paths from this skill’s directory. When this workflow references another bundled skill, read its local SKILL.md completely before following it.


# Ansight Cordova / Capacitor Remote Tool Skill

Use this skill to expose app-specific JavaScript state that existing DOM, native, artifact, and reflection tools do not answer precisely.

## Workflow

1. Define a narrow question or action and choose a stable namespaced id.
2. Prefer `read`; use `write` for ordinary mutation and `critical` for destructive, secret-bearing, or arbitrary code-invoking operations.
3. Register after bridge initialization:

```ts
const registration = Ansight.registerTool(
  {
    id: "app.get_sync_state",
    name: "Get sync state",
    policy: "read",
  },
  async () => ({
    success: true,
    result: { state: "idle" },
  }),
);

await registration.ready;
```

4. Keep registration inside the app's explicit development guard and use the least-permissive tool access.
5. Avoid secrets, full stores, arbitrary JavaScript evaluation, unbounded DOM scraping, and broad method invocation.
6. Test success, invalid inputs, failures, unregistration, denied guard access, and discovery/invocation through `ansight app tools` and `ansight app call`.

Report the tool id, policy, exposed data or mutation, guard, registration location, and verification.
