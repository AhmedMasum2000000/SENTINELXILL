---
name: ansight-install-react-native
description: Install @ansight/react-native in React Native or Expo development builds with automatic simulator or emulator registration and one-shot CLI QR enrollment for physical devices. Add and link the package, initialize native defaults, expose enrollFromQrCode from a developer-only surface, keep remote tools development-only, verify JavaScript and native builds, and inspect the app through the Ansight CLI.
---

## Claude Code plugin integration

Run Ansight CLI commands with Claude Code’s Bash tool on the machine that owns the resident host. If this session cannot execute commands or reach that host, explain the missing prerequisite and do not claim a live inspection succeeded. The plugin’s session-start note reports the CLI, host, and connected-session state it found; re-check with the commands below before acting on it. These skills describe the latest public Ansight CLI: if the session-start note or `ansight update check --json` reports an available update, offer `ansight update apply` with the user’s approval before relying on newer options, and treat `ansight <command> help` as the authority wherever it disagrees with this skill. A remote workspace or cloud agent does not automatically have access to the developer’s local host. Resolve relative helper paths from this skill’s directory. When this workflow references another bundled skill, read its local SKILL.md completely before following it.

Use these bundled files for the canonical skill URLs referenced below; keep public URLs when writing documentation for the user’s app:

- https://www.ansight.ai/skills/agents/ansight-app-inspection.md → [ansight-app-inspection](../ansight-app-inspection/SKILL.md)
- https://www.ansight.ai/skills/react-native/ansight-app-inspection-react-native.md → [ansight-app-inspection-react-native](../ansight-app-inspection-react-native/SKILL.md)


# Ansight React Native Install Skill

Use this skill for React Native apps, including Expo development builds, with native Android and iOS projects. Expo Go cannot load the native Ansight bridge.

## Workflow

1. Identify the package manager, bootstrap path, native projects, app ids,
   debug guard, and existing developer menu.
2. Install and link:

```shell
npm install @ansight/react-native
npx pod-install
```

3. Initialize once from app bootstrap:

```ts
if (__DEV__) {
  await Ansight.initializeAndActivate({
    useNativeAllInOneDefaults: true,
    toolGuard: "readOnly",
  });
}
```

4. Add a developer-only scanner action:

```ts
await Ansight.enrollFromQrCode({
  clientName: "React Native App",
});
```

5. `scanPairingQrCode(...)` is an API alias. If the app already owns a scanner,
   pass its result to `connect(...)`.
6. Keep native and React inspection tools behind `__DEV__` or the app's
   equivalent local-development guard. Disable tools outside that guard.
7. Android requires no app camera permission for the SDK scanner. On iOS, add
   `NSCameraUsageDescription` and `NSLocalNetworkUsageDescription`. Add no ATS
   exception or unrelated permissions.
8. Create or update `ansight-readme.md` with the scanner location, selected tool
   profile, build checks, and CLI enrollment commands. Do not include an enrollment payload.
9. Run JavaScript checks and practical Android/iOS debug builds.
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

## Enrollment Behavior

Simulator and emulator builds register automatically through native loopback.
The first physical-device scan registers the native app installation. Its random installation
id and enrollment state remain in app-private native storage, so later
developer launches reconnect automatically.

## Recommended Inspection Skills

Use the main router to select the core inspection workflow. Add the React
Native companion only when React, shadow-tree, or native-rendering semantics
are material:

```text
https://www.ansight.ai/skills/agents/ansight-app-inspection.md
https://www.ansight.ai/skills/react-native/ansight-app-inspection-react-native.md
```
