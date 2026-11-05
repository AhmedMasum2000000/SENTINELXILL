---
name: using-evermuse
description: 'Foundational doctrine and mechanics for grounding product work in real customer evidence via the Evermuse MCP — loaded by every other Evermuse skill. Use when you need the shared rules for how to search Evermuse, cite customer quotes with source links, resolve the active Product/Project, or save deliverables back via add_source. Trigger terms: Evermuse doctrine, Evermuse MCP, ground this in Evermuse, how to use Evermuse, save to Evermuse. (For an actual customer question, use customer-research; this skill supplies the mechanics other skills reuse.)'
category: Customer Voice & Feedback
tags:
- evermuse
- grounding
- evidence
---

# Using Evermuse

This is the shared foundation for every skill in the Evermuse plugin. It defines **how** to reach into a company's real customer evidence — recorded calls, interviews, feedback, needs, pain points, quotes — and turn any product deliverable from a generic, plausible-sounding answer into one grounded in what customers actually said, with clickable source links.

**The promise this plugin makes:** after it is installed, the agent's product answers should visibly change. They stop being generic best-practice and start carrying the customer's own voice, with quotes and citations. If your output looks the same as it would without Evermuse, you have not used this skill correctly.

## The Loop: Ground → Work → (optionally) Cite & Save

Every Evermuse skill follows the same beats. **Grounding is the one required beat** — the skill supplies the *Work*, and the rest are optional, applied with judgment.

1. **Ground (required).** Before producing anything, run the grounding search batch below. Never answer a customer-related question from memory when the evidence is one tool call away.
2. **Work.** Apply the skill's own method (spec template, prioritization framework, journey map, etc.), shaped by what the evidence actually says.
3. **Cite (optional, recommended).** When a claim rests on customer input, an inline source badge makes it verifiable. See `references/citations.md`. Citations are encouraged, never required.
4. **Save (optional).** Offer to persist important research and deliverables back into Evermuse via `add_source`, so the corpus compounds. See `references/saving-to-evermuse.md`.

### The required grounding batch — fire it in parallel

Grounding is a batch of `search` calls and nothing more is required. Once you know the `product_id` (from the first-run context), issue the whole batch as **one parallel set of tool calls**, not one-at-a-time:

- **3–4 `evidence` searches**, each worded from a different angle (the literal ask, the underlying pain, the adjacent workflow, the objection), `limit` up to 50. Evidence is the voice of the customer — it comes back rich and varied, often large.
- **one `guidance` search** and **one `context` search**, `limit` up to 50. These are usually sparse or empty; run them anyway and note when they're thin.

Read each response's **digest** first — it reports, pre-counted, how many more results exist. Use judgment on whether a query is worth pulling deeper: raise `limit` (toward the 100 max) and/or page with `next_offset` to avoid repeats, weighing payload size, remaining context, task complexity, and the value of the data. For deep pulls, consider spawning sub-agents — instruct them to return every citation with the **same metadata the tools return** (`url`, `who_said_it`, `meeting_name`, `created_at`) so you can still cite from their results.

Everything past this batch — quote-angled searches, `find_sources`, `read_source`, citing, saving — is **optional considered use**. When a skill loops over items (per feature, per competitor, per segment), batch each round's searches together; the only reads that must stay serial are genuinely dependent ones (`find_sources` → `read_source` on what it found). Passing `product_id` explicitly on every call (rather than switching sessions) is what makes this batching safe.

## The Seven Rules (read once, apply always)

**1. Product first, always.** Every product-scoped Evermuse call **requires** a `product_id` — you pass it on every call rather than switching sessions. Your `find_skills` first-run context hands you `current_product.id` (your default scope) and `other_products[].id`; use those. If you don't have that context, call `get_products` to list them. If exactly one product exists (or one obviously matches the repo/context), use its id and mention which one you picked. If several plausibly match, **ask the user** which product before searching — grounding against the wrong product is worse than not grounding at all. A Project (e.g. "Discovery", "Support", "Sales") is optional; pass `project_id` on a call only when the task is scoped to one research effort, otherwise omit it for full-product scope. If no product exists, tell the user to set one up in Evermuse and proceed with a clearly-labeled **⚠ ungrounded** deliverable.

**2. Grounding is the search batch — nothing beyond `search` is required.** The required grounding for any customer question is the parallel batch above: **3–4 `evidence` searches** worded from different angles (the literal ask, the underlying pain, the adjacent workflow, the objection), plus **one `guidance`** and **one `context`** search. Each `search` response opens with a **digest** — counts by type, the recurring-theme clusters, top speakers, date range, and how many results remain. Read it before the items: it hands you the patterns pre-counted, and tells you how deep the tail goes. Set `nature` per search so the sets stay clean:
   - `evidence` — direct customer signal: needs, feedback, quotes, pain points, Q&A from real conversations. **This is the voice of the customer, and it is where the volume is.**
   - `context` — market/industry: competitor capabilities, news, external signals. Usually sparse.
   - `guidance` — the company's own internal direction: strategy, objectives, values, positioning. Usually sparse or empty.
   
   Keep the natures separate in your output — don't blend a competitor's press release with a customer's complaint. (The `nature` parameter may be silently ignored on some workspaces; regardless, triage results by their `type` field yourself so the separation always holds.) Quotes, full sources, citations, and saving are optional follow-ons — never a requirement for grounding.

**3. Pull quotes when you need the customer's actual voice.** To *show* the customer speaking rather than summarize, run a quote-angled `search` — word the `search_query` for verbatim reactions and keep the `quote`-type items it returns (each carries speaker, meeting, and sentiment, ready to cite). When you don't need semantic ranking — a source's quotes, or a window's — use a filters-only `search(note_types: ["quote"])` instead.

**4. Full sources are for deep dives only.** `read_source(source_id)` returns one full source — a long conversation transcript or an entire ingested document. Use it only when analyzing a single specific source in depth, never as a general search. To find things *across* sources, use `search` (the evidence itself) or `find_sources` (which source), then `read_source` on the one that matters.

**5. Treat AI/human-generated assets as secondary.** Shaping notes, the competitor list, and the machine-suggested opportunities (`get_opportunities`) are generated or curated *inside* Evermuse. They are useful context but are **not** ground truth about what customers need. Use them sparingly and only when specifically appropriate (e.g. a shaping note's branch/PR field during a PR review). Never cite them as if they were the customer speaking.

**6. Cite customer-derived claims inline when you cite (optional, recommended).** Citations are not required, but they are what make the customer's voice *visible* — so prefer them whenever you can. When you do cite, use the inline linked-number badge as the baseline — a linked number in a code badge, `` [`1`](URL) ``, using the result's `url` field and numbered sequentially per answer. Fuller styles (a verbatim quote block, an attribution line) are welcome *in addition* where they sharpen the point. When a result has no `url`, fall back to attribution (who said it, which meeting, when) with no link. Full format — and the exact badge syntax — in `references/citations.md`. (Exception: the first-party Usermuse in-app chat keeps its own `[^n]` footnote contract — see the scoping note at the top of `references/citations.md`.)

**7. Saving is optional; reuse grounding across a session.** Important syntheses and deliverables can be offered back to Evermuse via `add_source` so the knowledge base grows — optional, not required. Tool calls cost credits, so reuse grounding across chained skills within a session (a spec's evidence feeds its dev plan) rather than re-running the batch, and pull deeper pages when the digest shows the data is worth it rather than paging reflexively.

## Step 0 for every skill: relevance & availability check

Before grounding, sanity-check two things:
- **Is this actually product/customer work?** If the session is clearly non-product (debugging library internals, CI config, infra plumbing with no customer-facing behavior), don't force Evermuse calls. Say so and offer the plain, ungrounded version of the task.
- **Is the MCP available?** If the `mcp__evermuse__*` (a.k.a. Evermuse) tools are not present, the MCP isn't connected/authenticated. Tell the user to authorize it (via `/mcp` in an interactive session, or their claude.ai connector settings) and produce a framework-only deliverable labeled **⚠ ungrounded — Evermuse not connected**. Never silently skip grounding without telling the user.

## Tool map (full schemas in references/tool-reference.md)

| Need | Tool |
|------|------|
| Confirm / list the product (`product_id` comes from the find_skills first-run context) | `get_products` |
| List research projects | `get_projects` |
| Find customer evidence (declare nature) | `search` |
| List notes by type/date/source, no semantics | `search` filters-only mode (omit `search_query`) |
| Pull verbatim quotes | quote-angled `search` (keep the `quote`-type results) |
| Find conversations / documents / other sources | `find_sources` |
| Read one full source (transcript or document) | `read_source` |
| Inspect one item in detail | `view_item` |
| Save research/deliverables back | `add_source` |
| Secondary/internal assets (use sparingly) | `get_shaping_notes`, `read_shaping_note`, `get_opportunities`, `list_competitors`, `get_competitor_capabilities` |
| Bridge to external tools (Linear/Jira/GitHub/Notion…) | `find_tool`, `call_tool` |

## Reference files (load only the one you need)

- `references/tool-reference.md` — every tool: exact signature, params, enums, return shape, and gotchas.
- `references/citations.md` — the source-badge format and the no-link fallback. **Load this whenever you output customer-derived claims.**
- `references/saving-to-evermuse.md` — `add_source` recipes, project resolution, and the nature-of-save rule.
- `references/search-patterns.md` — how to word the grounding batch (3–4 evidence + guidance + context), the nature-selection table, and how to read the digest and paginate through large result sets on judgment.
- `references/third-party-bridge.md` — using `find_tool`/`call_tool` and degrading gracefully when third-party access is blocked.
