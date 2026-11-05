#!/usr/bin/env bash
# SENTINELXILL universal skill installer.
# Usage: curl -fsSL https://raw.githubusercontent.com/AhmedMasum2000000/SENTINELXILL/HEAD/install.sh | bash
# Env:   SENTINELXILL_HOME (default ~/.sentinelxill)   SENTINELXILL_REF (default main)
#        SENTINELXILL_COPY=1 to copy instead of symlink   SENTINELXILL_NO_PROJECT=1 to skip ./.claude
set -euo pipefail

REPO_URL="https://github.com/AhmedMasum2000000/SENTINELXILL.git"
HOME_DIR="${SENTINELXILL_HOME:-$HOME/.sentinelxill}"
REF="${SENTINELXILL_REF:-}"  # empty = repository default branch

log() { printf '\033[1;36m[sentinelxill]\033[0m %s\n' "$*"; }

if [ -d "$HOME_DIR/.git" ]; then
  log "updating existing clone at $HOME_DIR"
  if [ -n "$REF" ]; then git -C "$HOME_DIR" fetch --depth 1 origin "$REF"; else git -C "$HOME_DIR" fetch --depth 1 origin; fi
  git -C "$HOME_DIR" reset -q --hard FETCH_HEAD
else
  log "cloning $REPO_URL (${REF:-default branch}) to $HOME_DIR"
  rm -rf "$HOME_DIR"
  if [ -n "$REF" ]; then git clone --depth 1 --branch "$REF" "$REPO_URL" "$HOME_DIR"; else git clone --depth 1 "$REPO_URL" "$HOME_DIR"; fi
fi

SKILLS_SRC="$HOME_DIR/skills"
[ -d "$SKILLS_SRC" ] || { echo "no skills/ directory in bundle" >&2; exit 1; }

link_or_copy() { # src dst
  local src="$1" dst="$2"
  mkdir -p "$(dirname "$dst")"
  rm -rf "$dst"
  if [ "${SENTINELXILL_COPY:-0}" = "1" ]; then cp -R "$src" "$dst"; else ln -s "$src" "$dst"; fi
}

install_skills_into() { # target skills dir
  local target="$1" n=0
  mkdir -p "$target"
  for coll in "$SKILLS_SRC"/*/; do
    coll="${coll%/}"
    for skill in "$coll"/*/; do
      skill="${skill%/}"
      [ -f "$skill/SKILL.md" ] || continue
      local name
      name="$(basename "$skill")"
      # avoid name collisions across collections by prefixing when needed
      if [ -e "$target/$name" ] && [ "$(readlink -f "$target/$name" 2>/dev/null || true)" != "$(readlink -f "$skill")" ]; then
        name="$(basename "$coll")--$name"
      fi
      link_or_copy "$skill" "$target/$name"
      n=$((n+1))
    done
  done
  log "installed $n skills into $target"
}

install_md_set_into() { # src-root target
  local src="$1" target="$2" n=0
  [ -d "$src" ] || return 0
  mkdir -p "$target"
  for coll in "$src"/*/; do
    coll="${coll%/}"
    link_or_copy "$coll" "$target/$(basename "$coll")"
    n=$((n+1))
  done
  log "installed $n collections into $target"
}

# --- Claude Code (user level) ---
install_skills_into "$HOME/.claude/skills"
install_md_set_into "$HOME_DIR/commands" "$HOME/.claude/commands/sentinelxill"
install_md_set_into "$HOME_DIR/agents"   "$HOME/.claude/agents/sentinelxill"

# --- Other harnesses: only if they are present on this machine ---
[ -d "$HOME/.codex" ]           && install_skills_into "$HOME/.codex/skills"
[ -d "$HOME/.cursor" ]          && install_skills_into "$HOME/.cursor/skills"
[ -d "$HOME/.gemini" ]          && install_skills_into "$HOME/.gemini/skills"
[ -d "$HOME/.config/opencode" ] && install_skills_into "$HOME/.config/opencode/skills"

# --- Current project (if inside a git repo and not disabled) ---
if [ "${SENTINELXILL_NO_PROJECT:-0}" != "1" ] && git rev-parse --show-toplevel >/dev/null 2>&1; then
  ROOT="$(git rev-parse --show-toplevel)"
  if [ "$ROOT" != "$HOME_DIR" ]; then
    install_skills_into "$ROOT/.claude/skills"
    grep -q 'sentinelxill' "$ROOT/.gitignore" 2>/dev/null || printf '\n# SENTINELXILL skill symlinks\n.claude/skills/\n' >> "$ROOT/.gitignore"
  fi
fi

log "done. Universal manual: $HOME_DIR/UNIVERSAL_SKILL.md  |  Index: $HOME_DIR/INDEX.md"
