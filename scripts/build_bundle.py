#!/usr/bin/env python3
"""
Build the SENTINELXILL universal skill bundle from a Claude Code installation.

Collects EVERY skill (plugin skills, marketplace skills, Anthropic built-in
skills, user/local skills), plus plugin slash-commands and agents, into a flat,
portable tree inside this repository, and regenerates manifest.json, INDEX.md
and UNIVERSAL_SKILL.md.

Usage:  python3 scripts/build_bundle.py [--repo PATH] [--home PATH]
"""
import argparse, json, os, re, shutil, sys, hashlib
from pathlib import Path

UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
MAX_FILE = 1_000_000  # bytes; bigger files are skipped (noted in manifest)
SKIP_DIRS = {"node_modules", ".git", "__pycache__", ".venv", "venv", "dist", "build", ".next"}
SKIP_FILES = {"package-lock.json", "yarn.lock", "pnpm-lock.yaml", ".DS_Store"}
SKIP_SUFFIX = {".pyc", ".map", ".skill", ".zip", ".tar", ".gz", ".7z", ".whl", ".so", ".dylib", ".dll", ".exe", ".bin", ".wasm"}

def frontmatter(path: Path):
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}, ""
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("\n---", 2)
        if len(parts) >= 2:
            fm = parts[0][3:]
            body = parts[-1] if len(parts) == 3 else ""
            for line in fm.splitlines():
                m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
                if m:
                    v = m.group(2).strip()
                    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                        v = v[1:-1]
                    meta[m.group(1)] = v
    if "name" not in meta:
        meta["name"] = path.parent.name
    if "description" not in meta:
        # first non-empty, non-heading line of body
        for line in body.splitlines():
            s = line.strip()
            if s and not s.startswith("#") and not s.startswith("---"):
                meta["description"] = s[:300]
                break
    return meta, body

def plugin_name(plugin_dir: Path) -> str:
    pj = plugin_dir / ".claude-plugin" / "plugin.json"
    if pj.exists():
        try:
            n = json.loads(pj.read_text()).get("name")
            if n:
                return n
        except Exception:
            pass
    pj2 = plugin_dir / "plugin.json"
    if pj2.exists():
        try:
            n = json.loads(pj2.read_text()).get("name")
            if n:
                return n
        except Exception:
            pass
    if not UUID_RE.match(plugin_dir.name):
        return plugin_dir.name
    # last resort: derive from the first skill's name
    for s in sorted(plugin_dir.rglob("SKILL.md")):
        return "plugin-" + plugin_dir.name[:8] + "-" + s.parent.name
    return "plugin-" + plugin_dir.name[:8]

def copy_tree(src: Path, dst: Path, skipped: list):
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        r = Path(root)
        rel = r.relative_to(src)
        for f in files:
            if f in SKIP_FILES or Path(f).suffix.lower() in SKIP_SUFFIX:
                continue
            sp = r / f
            try:
                if sp.is_symlink():
                    continue
                size = sp.stat().st_size
            except Exception:
                continue
            if size > MAX_FILE:
                skipped.append(str((rel / f)))
                continue
            dp = dst / rel / f
            dp.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(sp, dp)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--home", default=str(Path.home()))
    args = ap.parse_args()
    repo = Path(args.repo)
    home = Path(args.home)
    claude = home / ".claude"

    out_skills = repo / "skills"
    out_cmds = repo / "commands"
    out_agents = repo / "agents"
    for d in (out_skills, out_cmds, out_agents):
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)

    manifest = {"generated_by": "scripts/build_bundle.py", "skills": [], "commands": [], "agents": [], "skipped_large_files": []}
    seen = set()  # (collection, skill)

    def add_skill(collection: str, skill_dir: Path, source: str):
        key = (collection, skill_dir.name)
        if key in seen:
            return
        seen.add(key)
        meta, _ = frontmatter(skill_dir / "SKILL.md")
        dst = out_skills / collection / skill_dir.name
        skipped = []
        copy_tree(skill_dir, dst, skipped)
        for s in skipped:
            manifest["skipped_large_files"].append(f"skills/{collection}/{skill_dir.name}/{s}")
        manifest["skills"].append({
            "collection": collection,
            "name": meta.get("name", skill_dir.name),
            "description": meta.get("description", ""),
            "path": f"skills/{collection}/{skill_dir.name}",
            "source": source,
        })

    def add_md_set(kind: str, collection: str, src_dir: Path, out_root: Path):
        for f in sorted(src_dir.rglob("*.md")):
            if any(p in SKIP_DIRS for p in f.parts):
                continue
            rel = f.relative_to(src_dir)
            dst = out_root / collection / rel
            if dst.exists():
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dst)
            meta, _ = frontmatter(f)
            manifest[kind].append({
                "collection": collection,
                "name": meta.get("name", f.stem),
                "description": meta.get("description", ""),
                "path": f"{out_root.name}/{collection}/{rel.as_posix()}",
            })

    # 1) Plugins (marketplace / installed) -------------------------------
    for synced in sorted((claude / "plugins" / "synced").glob("*/*/")) + sorted((claude / "plugins" / "cache").glob("*/*/*/")):
        pdir = Path(str(synced).rstrip("/"))
        if not pdir.is_dir() or pdir.name.endswith(".meta.json"):
            continue
        skills = sorted(pdir.rglob("SKILL.md"))
        cmds = pdir / "commands"
        agents = pdir / "agents"
        if not skills and not cmds.exists() and not agents.exists():
            continue
        coll = plugin_name(pdir)
        # Prefer canonical <plugin>/skills/<name> over nested mirrors
        skills.sort(key=lambda p: (0 if p.parent.parent == pdir / "skills" else 1, len(p.parts)))
        for s in skills:
            add_skill(coll, s.parent, f"plugin:{coll}")
        if cmds.is_dir():
            add_md_set("commands", coll, cmds, out_cmds)
        if agents.is_dir():
            add_md_set("agents", coll, agents, out_agents)

    # 2) Anthropic marketplace skills synced to ~/.claude/skills/synced ----
    for s in sorted((claude / "skills" / "synced").rglob("SKILL.md")):
        add_skill("anthropic-skills", s.parent, "claude-skills-marketplace")

    # 3) Local user skills (~/.claude/skills/<name>) -----------------------
    for s in sorted((claude / "skills").glob("*/SKILL.md")):
        add_skill("local", s.parent, "user-local")

    # 4) Anthropic built-in skills shipped with the runtime ----------------
    for base, coll in ((Path("/mnt/skills/public"), "anthropic-builtin"), (Path("/mnt/skills/examples"), "anthropic-examples")):
        if base.is_dir():
            for s in sorted(base.glob("*/SKILL.md")):
                add_skill(coll, s.parent, str(base))
    for extra in (Path("/home/claude/.claude/skills"), Path("/opt/cu-desktop/skill")):
        if extra.is_dir():
            for s in sorted(extra.rglob("SKILL.md")):
                add_skill("anthropic-builtin", s.parent, str(extra))

    # 5) Project-level skills in the current repo (if any pre-existed) -----
    for s in sorted((repo / ".claude" / "skills").glob("*/SKILL.md")):
        add_skill("project", s.parent, "repo:.claude/skills")

    manifest["skills"].sort(key=lambda x: (x["collection"].lower(), x["name"].lower()))
    manifest["counts"] = {
        "skills": len(manifest["skills"]),
        "collections": len({s["collection"] for s in manifest["skills"]}),
        "commands": len(manifest["commands"]),
        "agents": len(manifest["agents"]),
    }
    (repo / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")

    # INDEX.md -------------------------------------------------------------
    lines = ["# SENTINELXILL Skill Index", "",
             f"**{manifest['counts']['skills']} skills** across **{manifest['counts']['collections']} collections**, "
             f"plus {manifest['counts']['commands']} slash-commands and {manifest['counts']['agents']} agents.", "",
             "Each skill lives at `skills/<collection>/<name>/SKILL.md`. Read the SKILL.md (and anything it references) when a task matches its description.", ""]
    by_coll = {}
    for s in manifest["skills"]:
        by_coll.setdefault(s["collection"], []).append(s)
    for coll in sorted(by_coll, key=str.lower):
        lines.append(f"## {coll} ({len(by_coll[coll])})")
        lines.append("")
        for s in by_coll[coll]:
            d = s["description"].replace("\n", " ").strip()
            if len(d) > 220:
                d = d[:217] + "..."
            lines.append(f"- **{s['name']}** — {d}  \n  `{s['path']}/SKILL.md`")
        lines.append("")
    (repo / "INDEX.md").write_text("\n".join(lines))

    # Compact index embedded in UNIVERSAL_SKILL.md ---------------------------
    compact = []
    for coll in sorted(by_coll, key=str.lower):
        names = ", ".join(s["name"] for s in by_coll[coll])
        compact.append(f"- **{coll}**: {names}")
    tpl = (repo / "scripts" / "UNIVERSAL_SKILL.template.md").read_text()
    out = (tpl.replace("{{SKILL_COUNT}}", str(manifest["counts"]["skills"]))
              .replace("{{COLLECTION_COUNT}}", str(manifest["counts"]["collections"]))
              .replace("{{COMMAND_COUNT}}", str(manifest["counts"]["commands"]))
              .replace("{{AGENT_COUNT}}", str(manifest["counts"]["agents"]))
              .replace("{{COMPACT_INDEX}}", "\n".join(compact)))
    (repo / "UNIVERSAL_SKILL.md").write_text(out)

    print(json.dumps(manifest["counts"]))
    print(f"skipped large files: {len(manifest['skipped_large_files'])}")

if __name__ == "__main__":
    main()
