---
name: ansight-cli-setup
description: Prepare a developer workstation or agent to use the Ansight CLI by verifying the executable and dependencies, starting or reusing the resident host, and proving structured discovery. Use when setup or setup troubleshooting is requested; do not use for ordinary app operation once they work.
---

## Claude Code plugin integration

Run Ansight CLI commands with Claude Code’s Bash tool on the machine that owns the resident host. If this session cannot execute commands or reach that host, explain the missing prerequisite and do not claim a live inspection succeeded. The plugin’s session-start note reports the CLI, host, and connected-session state it found; re-check with the commands below before acting on it. These skills describe the latest public Ansight CLI: if the session-start note or `ansight update check --json` reports an available update, offer `ansight update apply` with the user’s approval before relying on newer options, and treat `ansight <command> help` as the authority wherever it disagrees with this skill. A remote workspace or cloud agent does not automatically have access to the developer’s local host. Resolve relative helper paths from this skill’s directory. When this workflow references another bundled skill, read its local SKILL.md completely before following it.


# Ansight CLI Setup Skill

Use this skill when a user wants an agent or developer workstation prepared for Ansight without modifying an app SDK integration.

## Goal

Make the `ansight` executable the canonical local interface, verify its dependencies, start or reuse its resident host, and prove that structured CLI commands can discover apps and sessions.

## Required Constraints

- Use `ansight` commands directly and do not add a separate client bridge or daemon configuration.
- Prefer `--json` whenever command output will be consumed by an agent or script.
- Preserve any running host and its selected data directory.
- Do not install or modify an app SDK unless the user separately requests it.
- Do not start a second host against the same data directory.
- Keep the resident host on the developer machine and do not expose its local ports publicly.
- Treat macOS Keychain and resident-host IPC denials as execution-sandbox boundaries, not damaged Ansight credentials. Do not delete Keychain items, sign the user out, create a parallel file-backed secret store, or restart a healthy host to work around them.

## Workflow

1. Confirm the executable and command surface:

   ```sh
   ansight help
   ansight version --json
   ansight update check --json
   ansight doctor --json
   ```

2. Check for a resident host:

   ```sh
   ansight host status --json
   ```

3. If no host is running, start one in a persistent terminal:

   ```sh
   ansight host run
   ```

   Use `ansight host run --open` when the user also wants the local browser explorer. Use the same `--data-dir` on status and management commands when a custom data directory is required.

4. From another terminal, verify the host and discovery surface:

   ```sh
   ansight host status --json
   ansight app list --json
   ansight session list --connected --limit 20 --json
   ```

5. A simulator, emulator, Mac Catalyst app, or desktop app registers
   automatically with the local host. To enroll a physical device, issue a
   generic one-use terminal QR and scan it from the app's developer-only Ansight
   surface:

   ```sh
   ansight pairing issue --qr
   ```

   Do not require app registration before this first connection. Once the SDK
   supplies its real App ID, optionally link it to a repository with
   `ansight app register <app-id> --name <name> --codebase <path>`.

6. For agent workflows, prove the machine-readable inspection path with the selected session:

   ```sh
   ansight session show <session-id> --json
   ansight app tools <session-id> \
     --policy read \
     --detail summary \
     --max-results 10 \
     --json
   ```

   This is a compact discovery check. For a real app question, use the
   installed `/ansight:ansight-use-remote-app-tools` skill: search with focused terms,
   then retrieve the selected exact tool with `--tool-id <id> --detail full`.
   Session listing is summary-only and cursor-paginated. Follow `nextCursor`
   with `--cursor` only when the first filtered page does not contain the
   intended session, and preserve the same filters between pages.

7. For fast live interaction, verify `ansight app interact --help`. Once the exact
   session is selected, the live-operation skill can open one persistent process:

   ```sh
   ansight app interact --session <session-id> --repository <repository-root> --jsonl
   ```

   Keep its process handle and send JSON Lines on stdin. This built-in duplex
   connection returns compact fresh UI trees and supports semantic targets,
   coordinate fallback, sequential batches and saved task execution. Screenshot
   and tree evidence capture is automatic. `--repository` is optional for gestures and
   required for `tasks`/`task`. This does not create another host, agent, app
   process or recording session. Setup alone does not authorize live mutations.

8. Report the executable used, doctor result, host state, data directory, discovered app/session identifiers, and any manual pairing or persistent-terminal step that remains.

## Troubleshooting Within Requested Setup

Use the check matching the observed error. If it does not resolve the blocker,
report the result and required next step; do not work through unrelated repairs.

- CLI device launches show simulator/emulator windows by default. Pass `--headless` on each device-launching command when windowless operation is requested; `--json`, `--silent`, and CI do not imply it. This skips Simulator.app on iOS and adds `-no-window` for new Android emulators without closing existing windows or changing physical devices. See [headless device launches](https://www.ansight.ai/docs/cli/commands#headless-device-launches).
- After an update or local build install, compare `ansight version --json` and `ansight host status --json`. A running host keeps its loaded code, so new launch options require an updated host too. Coordinate an authorized restart rather than interrupting a shared host automatically.
- Run `ansight doctor --json` first and use its required/optional capability results instead of guessing at missing dependencies.
- In a sandboxed agent environment, `OSStatus -50` while reading the Ansight macOS Keychain item or `Permission denied` for a `CoreFxPipe_ansight-*` path usually means the sandbox denied Keychain or resident-host IPC access. Retry the exact command outside the sandbox with explicit user approval and the narrowest command permission the client supports. If that succeeds, continue Ansight commands in that approved execution context; do not repair or replace the credential store.
- If the same command also fails outside the sandbox, treat it as a real host or credential problem and preserve both outputs for diagnosis.
- If a command cannot find the resident host, compare the `--data-dir` value and current OS user.
- If no live session appears, confirm the host is running and the app is a development build. Host-local targets should auto-register; a physical device should have scanned a current `ansight pairing issue --qr` invite.
- If multiple sessions match, select one explicitly; never guess.
- Use `ansight help` and `ansight <command> help` as the authoritative syntax for the installed version.

## Done Criteria

- `ansight version --json` reports the expected version string, daily build
  number, and public or preview channel, and any available update is reported.
- `ansight doctor --json` completes and required capabilities are understood.
- Exactly one intended resident host is running or the user has the explicit command needed to start it.
- `ansight host status --json` succeeds.
- App and connected-session discovery has been checked through the CLI.
- No separate client bridge or legacy daemon configuration was added.
