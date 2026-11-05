---
name: ansight-install-cordova
description: Install @ansight/capacitor with automatic simulator or emulator registration and one-shot CLI QR enrollment for physical devices. Add and sync the Capacitor bridge, initialize native defaults, expose enrollFromQrCode from a developer-only surface, keep remote tools development-only, verify web and native builds, and inspect the app through the Ansight CLI.
---

## Claude Code plugin integration

Run Ansight CLI commands with Claude Code’s Bash tool on the machine that owns the resident host. If this session cannot execute commands or reach that host, explain the missing prerequisite and do not claim a live inspection succeeded. The plugin’s session-start note reports the CLI, host, and connected-session state it found; re-check with the commands below before acting on it. These skills describe the latest public Ansight CLI: if the session-start note or `ansight update check --json` reports an available update, offer `ansight update apply` with the user’s approval before relying on newer options, and treat `ansight <command> help` as the authority wherever it disagrees with this skill. A remote workspace or cloud agent does not automatically have access to the developer’s local host. Resolve relative helper paths from this skill’s directory. When this workflow references another bundled skill, read its local SKILL.md completely before following it.

Use these bundled files for the canonical skill URLs referenced below; keep public URLs when writing documentation for the user’s app:

- https://www.ansight.ai/skills/agents/ansight-app-inspection.md → [ansight-app-inspection](../ansight-app-inspection/SKILL.md)
- https://www.ansight.ai/skills/cordova/ansight-app-inspection-cordova.md → [ansight-app-inspection-cordova](../ansight-app-inspection-cordova/SKILL.md)


# Ansight Cordova / Capacitor Install Skill

Use this skill for Capacitor 8 apps. Classic Apache Cordova is not currently a
drop-in target for `@ansight/capacitor`.

## Workflow

1. Inspect `package.json`, Capacitor config, web bootstrap, native projects,
   debug guard, and existing developer menu.
2. Install and sync:

```shell
npm install @ansight/capacitor
npx cap sync
```

3. Initialize from development-only bootstrap:

```ts
if (isDevelopmentBuild) {
  await Ansight.initializeAndActivate(
    Ansight.createOptionsBuilder()
      .withAnsightDefaults()
      .withReadOnlyToolAccess()
      .build(),
  );
}
```

   Replace `isDevelopmentBuild` with the app's existing explicit development
   variant flag; do not hard-code it to `true`.

4. Add a developer-only scanner action:

```ts
await Ansight.enrollFromQrCode({
  clientName: "My Capacitor App",
});
```

5. `scanPairingQrCode(...)` is an API alias. Use `connect(payload, ...)` when
   the app already owns a scanner.
6. Keep DOM and native tools behind the app's local-development guard. Prefer
   read-only DOM and native inspection; leave actions, reflection, secure
   storage, writes, and deletes off unless required.
7. Android requires no app camera permission for the SDK scanner. On iOS, add
   `NSCameraUsageDescription` and `NSLocalNetworkUsageDescription`. Add no ATS
   exception or unrelated permissions.
8. Create or update `ansight-readme.md` with the scanner location, selected
   tools, build checks, and CLI enrollment commands. Do not include an enrollment payload.
9. Run package checks, `npx cap sync`, and practical native debug builds.
10. Start or reuse the resident CLI host. A simulator or emulator registers
    automatically. For a physical device, issue one generic host QR and scan it
    from the developer-only surface:

```sh
ansight host run
ansight pairing issue --qr
ansight session list --connected --app-id <app-id> --json
ansight app tools <session-id> --detail summary --include-unavailable --max-results 50 --json
```

    Do not require `ansight app register` before the first connection. After
    the SDK supplies its real App ID, optionally link the discovered app to the
    repository with `ansight app register <app-id> --codebase <repository-path>`.

Simulator and emulator builds register automatically through native loopback.
The first physical-device scan registers the native app installation. Its random installation
id and enrollment state remain in app-private storage, so later developer
launches reconnect automatically.

## Recommended Inspection Skills

Use the main router to select the core inspection workflow. Add the Capacitor
companion only when DOM, bridge, or native-platform semantics are material:

```text
https://www.ansight.ai/skills/agents/ansight-app-inspection.md
https://www.ansight.ai/skills/cordova/ansight-app-inspection-cordova.md
```
