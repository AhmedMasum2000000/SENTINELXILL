# SENTINELXILL — Universal Skill Pack

**Every skill from a fully-loaded Claude Code install, bundled once, installable anywhere.**

| | |
|---|---|
| Skills | see `manifest.json` → `counts.skills` (1600+) across 168 collections |
| Slash-commands | 114 |
| Agent personas | 126 |
| Works with | Claude Code, Claude.ai, ChatGPT, Grok, Gemini, Codex CLI, Cursor, OpenCode, any LLM that can read a URL or a pasted file |

## The one-paste install

Copy the contents of [`UNIVERSAL_SKILL.md`](UNIVERSAL_SKILL.md) and paste it into any AI chat, `AGENTS.md`, `GEMINI.md`, `.cursorrules`, or a custom-GPT / Grok system prompt. That file is the entire manual: it tells the model where the skills live, how to fetch them on demand, and how to install them locally if it has a shell.

### If the AI has a shell (Claude Code, Codex, Cursor, OpenCode, Gemini CLI)

```bash
curl -fsSL https://raw.githubusercontent.com/AhmedMasum2000000/SENTINELXILL/HEAD/install.sh | bash
```

This clones the pack to `~/.sentinelxill` and symlinks all skills into `~/.claude/skills` (plus `~/.codex/skills`, `~/.cursor/skills`, `~/.gemini/skills`, `~/.config/opencode/skills` when those harnesses exist, and the current project's `.claude/skills`). Commands land in `~/.claude/commands/sentinelxill/`, agents in `~/.claude/agents/sentinelxill/`. Re-run to update.

Options: `SENTINELXILL_COPY=1` copies instead of symlinking. `SENTINELXILL_NO_PROJECT=1` skips the current project.

### If the AI can only browse (ChatGPT, Grok, Gemini web, Claude.ai)

Paste `UNIVERSAL_SKILL.md`. The model fetches `INDEX.md` once, then fetches `skills/<collection>/<name>/SKILL.md` whenever a task matches.

## Layout

```
UNIVERSAL_SKILL.md   the pasteable master skill / manual
INDEX.md             every skill with its description
manifest.json        machine-readable index (skills, commands, agents, sources)
install.sh           one-shot installer
skills/<collection>/<skill>/SKILL.md   1600+ skill folders (references, scripts, assets included)
commands/<collection>/*.md             plugin slash-commands
agents/<collection>/*.md               plugin agent personas
scripts/build_bundle.py                regenerates everything from a live Claude Code install
```

Collections are named after the plugin or marketplace they came from (`anthropic-skills`, `anthropic-builtin`, `anthropic-examples`, `agentic-council`, `wix`, `twilio-developer-kit`, ...).

## Rebuilding from your own Claude Code install

```bash
python3 scripts/build_bundle.py
git add -A && git commit -m "Rebuild skill bundle" && git push
```

The builder walks `~/.claude/plugins`, `~/.claude/skills`, `/mnt/skills` and project `.claude/skills`, de-duplicates nested mirrors, drops lockfiles, `node_modules`, archives and any file over 1 MB (listed under `skipped_large_files` in the manifest), and regenerates the index files.

## Notes

- Skills that depend on MCP servers or paid connectors still need those connectors on the target machine. The skill text installs; the tool access does not.
- Each skill keeps its original license file where the plugin shipped one.
