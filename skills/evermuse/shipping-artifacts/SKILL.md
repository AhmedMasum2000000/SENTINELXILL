---
name: shipping-artifacts
description: 'Generate the ship-readiness documentation set for an AI-built (vibe-coded) feature — architecture, flows, permissions, variables, and a tests coverage map, plus conditional docs — and reconstruct the missing ''intent'' section from Evermuse shaping notes, the local spec, and customer evidence so a reviewer can judge whether the code matches what was meant. Use when the user wants to ''document this app for review'', ''prep for a security/perf audit'', ''create shipping docs'', ''map the flows and permissions'', or ''get this ready to ship''. Trigger terms: shipping artifacts, ship readiness, document the app, review docs, pre-ship documentation, flows and permissions map. Not for user-facing docs — this is reviewer/auditor documentation.'
category: Delivery & Engineering
tags:
- shipping
- artifacts
- launch
---

# Shipping Artifacts (intent reconstructed from customer evidence)

AI agents write code fast but leave no durable record of **intent** — what the system was *supposed* to do and why. This skill produces the small set of reviewer-facing docs that restore reviewability for $ARGUMENTS, and fills the intent gap by reconstructing it from **Evermuse shaping notes + the local spec + customer evidence**. Without that intent layer, an audit has nothing to compare the code against.

> **Pairs with the gap-analysis flagship.** These docs are the *intended-state* half; `gap-analysis` is the *audit* that compares intent ↔ code ↔ customer need. Produce shipping artifacts first, then run `gap-analysis` against them.

## Step 0 — Relevance & availability
Confirm there's a built feature to document and Evermuse is present. The code-derived docs work ungrounded, but the **intent reconstruction** needs the MCP — if it's not connected, produce the doc set and label the intent sections **⚠ ungrounded — intent not reconstructed from evidence**; tell the user to authorize the MCP. (See `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`, Step 0.)

## Evermuse Grounding (required)
Follow `${CLAUDE_PLUGIN_ROOT}/skills/using-evermuse/SKILL.md`.

**Required — one parallel batch of searches.** Verify the product (Rule 1), then fire in a single parallel batch:
- **3–4 `evidence` searches**, each worded from a different angle (`limit` up to 50). Evidence comes back rich and varied — expect large, useful result sets.
- **one `guidance` search** and **one `context` search** (`limit` up to 50). These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** — it reports how many more results exist. Use judgment on whether a query is worth pulling deeper (raise `limit` toward the 100 max and/or page with `next_offset` to avoid repeats), weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite.

**Optional — considered use.** Once grounded, reach for the other tools only when they add value: a quote-angled `search` for verbatim voice, `read_source` for a single deep dive, inline citations (`references/citations.md`), and `add_source` to save the deliverable. Sources, citations, and saving are optional — not required.

## The doc set (core + conditional)

Write into `/documentation/`. Core docs always; conditional docs only when the capability exists — if it doesn't, write one honest line in `architecture.md` ("No scheduled work — no `cron.md`.") rather than an empty file. Be an accurate map, not a clean bill of health.

**Core**
1. **`architecture.md`** — product overview + **key assumptions** (grounded in reconstructed intent [`1`](URL)); tech stack; how auth/sessions/claims flow; trust boundaries; a **Known risks / assumptions** list (each backed by where it shows up in code); a "Related Documents" index.
2. **`flows.md`** — each load-bearing flow as actor + precondition + success outcome; the UI→server→data→jobs→providers→agents sequence; the **authz check at each protected step** (claim/role/scope, resource, expected *deny*); **trust-boundary crossings**; side effects. *Anti-PRD rule: only flows touching permissions, data integrity, external side effects, money, privacy, or safety belong here.*
3. **`permissions.md`** — roles/claims; where scope is derived (token vs DB); a resource × operation × role matrix; which tables use RLS vs code-enforced checks.
4. **`variables.md`** — table of Name · used-by · scope · source · rotation · risk; explicit "no secret bundled client-side" confirmation; a pre-go-live checklist.
5. **`tests.md`** — the verification map in three separated sections so it can't read falsely green: **Existing coverage** (tests in the repo today, each tied to the rule it pins) · **Proposed tests** (marked by type) · **Gaps** (documented rules verified by nothing, ranked by exposure). Note CI-required checks. *(In the source method this is derived separately from the other docs — treat it as the "documented == implemented" check.)*

**Conditional (include only if the capability exists)**
6. **`emails.md`** — queue→processor→provider path, templates + inputs, retry, where sends fail. *(if it sends email)*
7. **`cron.md`** — job inventory (schedule · function · secrets · limits · retry), idempotency, internal-call auth. *(if scheduled/background jobs exist)*
8. **`seo.md`** — preview approach, route→needs-SEO→public-data-only table, metadata sanitization, bot-vs-human routing. *(if public/indexable routes exist)*
9. **`automation.md`** — per embedded agent/automation: trigger + owner + auto-vs-approval; inputs it reads + **exact tools/APIs it may call**; steering (prompt) vs hard guardrails; output contract; app-owned side effects vs agent-owned suggestions; controls (approval gates, audit logging, rate limits, kill switch). *(if the app embeds agents/LLM workflows/webhooks)*

## Notes
- Each doc registers itself in `architecture.md` under "Related Documents".
- Keep templates/examples out — these describe *this* system.
- The customer-evidence layer is what makes intent real: a "Known risk" like "assumes one workspace per user" should trace to code **and**, where relevant, to a customer who hit the multi-workspace case [`1`](URL).

---
### Further reading
- Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT), `pm-ai-shipping/shipping-artifacts`.
- Pairs with `${CLAUDE_PLUGIN_ROOT}/skills/gap-analysis/SKILL.md`.
