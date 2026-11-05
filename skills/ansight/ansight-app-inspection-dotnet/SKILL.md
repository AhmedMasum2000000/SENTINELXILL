---
name: ansight-app-inspection-dotnet
description: Add .NET MAUI and .NET mobile platform semantics to an Ansight operation. Use alongside a selected core Ansight workflow when MAUI hierarchy, bindings, handlers, native rendering, reflection, or .NET tool behavior affects interpretation; do not use as the primary live-operation, remote-tool, session-investigation, or annotation workflow.
---

## Claude Code plugin integration

Run Ansight CLI commands with Claude Code’s Bash tool on the machine that owns the resident host. If this session cannot execute commands or reach that host, explain the missing prerequisite and do not claim a live inspection succeeded. The plugin’s session-start note reports the CLI, host, and connected-session state it found; re-check with the commands below before acting on it. These skills describe the latest public Ansight CLI: if the session-start note or `ansight update check --json` reports an available update, offer `ansight update apply` with the user’s approval before relying on newer options, and treat `ansight <command> help` as the authority wherever it disagrees with this skill. A remote workspace or cloud agent does not automatically have access to the developer’s local host. Resolve relative helper paths from this skill’s directory. When this workflow references another bundled skill, read its local SKILL.md completely before following it.

Use these bundled files for the canonical skill URLs referenced below; keep public URLs when writing documentation for the user’s app:

- https://www.ansight.ai/skills/agents/ansight-operate-live-app/SKILL.md → [ansight-operate-live-app](../ansight-operate-live-app/SKILL.md)
- https://www.ansight.ai/skills/agents/ansight-use-remote-app-tools/SKILL.md → [ansight-use-remote-app-tools](../ansight-use-remote-app-tools/SKILL.md)
- https://www.ansight.ai/skills/agents/ansight-investigate-session/SKILL.md → [ansight-investigate-session](../ansight-investigate-session/SKILL.md)
- https://www.ansight.ai/skills/agents/ansight-annotate-session/SKILL.md → [ansight-annotate-session](../ansight-annotate-session/SKILL.md)


# Ansight .NET Inspection Semantics

Use this companion skill for .NET MAUI, .NET for Android, .NET for iOS, or .NET Mac Catalyst evidence. Do not use it for native-only iOS or Android, React Native, Flutter, server, console, or web apps.

## Keep The Core Workflow In Charge

Select the skill that owns the requested outcome before applying these .NET semantics:

- live lifecycle or visible UI interaction: `https://www.ansight.ai/skills/agents/ansight-operate-live-app/SKILL.md`
- bundled or app-specific remote tools: `https://www.ansight.ai/skills/agents/ansight-use-remote-app-tools/SKILL.md`
- live or recorded evidence investigation: `https://www.ansight.ai/skills/agents/ansight-investigate-session/SKILL.md`
- annotation writes: `https://www.ansight.ai/skills/agents/ansight-annotate-session/SKILL.md`

The selected core skill owns session selection, authorization, command procedure, verification, reporting, and any relevant workspace reuse. Use this skill only to interpret .NET-specific evidence or choose among cataloged .NET tool families.

## Interpret .NET UI Evidence

- Prefer cataloged `maui.*` tools when the question requires MAUI page, element, bindable-property, binding, resource, layout, handler, navigation, or binding-context semantics that the unified tree does not expose.
- Use cataloged native `ui.*` tools when the issue concerns the rendered UIKit or Android hierarchy, native screenshots, platform widgets, overlays, or native hit testing.
- Treat MAUI, native, and reflection identifiers as separate namespaces unless a returned schema explicitly connects them.
- Correlate screenshots with the relevant MAUI or native tree when layout, visibility, labels, hit targets, or navigation state matter.

## Interpret .NET State And Tools

- Treat `maui.*`, `ui.*`, database, file, preference, secure-storage, artifact, and `reflect.*` families as optional catalog entries rather than guaranteed .NET capabilities.
- Use `reflect.*` only against roots returned by `reflect.list_roots`. It normally comes from `Ansight.Tools.Reflection` or an all-in-one package enabled in a Debug or explicit local-development configuration.
- An absent reflection catalog may mean the development-only suite, runtime policy, or local guard is intentionally unavailable; report that state instead of enabling it automatically.
- MAUI operations such as setting bindable properties, inflating XAML, adding elements, invoking element actions, or invoking binding-context commands are remote mutations. Follow the core remote-tool skill's authorization, baseline, verification, and cleanup rules.

## Platform Fallbacks

Use direct simulator, emulator, device, app-container, or source inspection only after the owning core skill identifies a concrete Ansight capability gap. Report whether the gap was in the MAUI view, native hierarchy, cataloged tools, retained evidence, or device control, and identify the fallback used.

## Report .NET-Specific Evidence

In addition to the core skill's report, name the observed .NET target shape and distinguish evidence from the MAUI tree, native hierarchy, reflection roots, or other cataloged .NET tool families.
