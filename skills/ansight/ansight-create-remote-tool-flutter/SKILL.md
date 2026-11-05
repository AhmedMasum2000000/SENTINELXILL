---
name: ansight-create-remote-tool-flutter
description: Use this skill when implementing a custom Ansight remote tool for a Flutter app. Create a narrow Dart registerTool handler with a stable id, explicit read/write/critical policy, structured results, development-only registration, runtime guard access, and CLI verification.
---

## Claude Code plugin integration

Run Ansight CLI commands with Claude Code’s Bash tool on the machine that owns the resident host. If this session cannot execute commands or reach that host, explain the missing prerequisite and do not claim a live inspection succeeded. The plugin’s session-start note reports the CLI, host, and connected-session state it found; re-check with the commands below before acting on it. These skills describe the latest public Ansight CLI: if the session-start note or `ansight update check --json` reports an available update, offer `ansight update apply` with the user’s approval before relying on newer options, and treat `ansight <command> help` as the authority wherever it disagrees with this skill. A remote workspace or cloud agent does not automatically have access to the developer’s local host. Resolve relative helper paths from this skill’s directory. When this workflow references another bundled skill, read its local SKILL.md completely before following it.


# Ansight Flutter Remote Tool Skill

Use this skill to expose app-specific Flutter or Dart state that existing widget, native, artifact, and reflection tools do not answer precisely.

## Workflow

1. Define the narrow question or action and choose a stable namespaced id such as `app.get_sync_state`.
2. Prefer `read`; use `write` for ordinary mutation and `critical` for destructive, secret-bearing, or arbitrary code-invoking operations.
3. Define argument and result schemas where useful.
4. Register after runtime initialization:

```dart
final registration = await Ansight.instance.registerTool(
  const AnsightToolDefinition(
    id: 'app.get_sync_state',
    name: 'Get sync state',
    policy: AnsightToolPolicy.read,
  ),
  (arguments, context) async => const AnsightToolResult.success(
    result: <String, Object?>{'state': 'idle'},
  ),
);
```

5. Keep registration inside `kDebugMode` or the app's explicit developer variant and configure the least-permissive `AnsightToolGuard`.
6. Avoid secrets, unbounded object graphs, raw reflection, and broad arbitrary method invocation.
7. Test handler success, invalid arguments, expected failure, unregistration, denied guard access, and discovery/invocation through `ansight app tools` and `ansight app call`.

Report the tool id, policy, exposed data or mutation, guard, registration location, and verification.
