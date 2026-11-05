---
description: Save the current research, spec, plan, or analysis back into Evermuse so the knowledge base compounds
argument-hint: "[what to save] [evidence|context|guidance]"
---

# /evermuse:save — Persist to Evermuse

Read `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/references/saving-to-evermuse.md`. Determine what to save (the most recent substantial deliverable, or `$ARGUMENTS`), pick the `nature` (customer-voice synthesis → evidence; market/competitor → context; company direction like specs/plans/strategy → guidance), resolve the project (get_projects → ask if several), then `add_source(source_type: "document", tags: ["evermuse-plugin", …])`. Confirm what was saved and where.
