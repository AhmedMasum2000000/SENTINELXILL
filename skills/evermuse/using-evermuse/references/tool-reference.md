# Evermuse MCP — Tool Reference

Exact signatures and gotchas for all Evermuse tools. Tool names are prefixed `mcp__evermuse__` (shown here without the prefix). Every product-scoped tool takes a required `product_id` and an optional `project_id`.

> **Global gotchas**
> - **`product_id` is required, per call.** You do not switch sessions — you pass `product_id` on every product-scoped call (`search`, `find_sources`, `get_opportunities`, `list_competitors`, `get_shaping_notes`). Get it from the `find_skills` first-run context (`current_product.id`, or an id from `other_products`), or from `get_products`. Omitting it fails with a "Missing product ID" error. Pass `project_id` only to narrow to one project; omit it for full-product scope.
> - **`search` is paginated and opens with a digest.** Ask for the page size you want (`limit`, default 50) and read the digest for the shape of the whole result set. See `search-patterns.md`. A ~120K-char response cap still exists as a safety net for unusually large pages; when it bites, the digest says `size_capped: true` and the trimmed items wait at `next_offset`. `get_opportunities` is **not** paginated and can return a large payload — prefer `search` for evidence.
> - **Credits are billed per call** (≈1 per own-tool call, ≈2 per third-party `call_tool`). The required grounding batch is 3–4 `evidence` searches plus one `guidance` and one `context` search; each page after that is its own call, so page on judgment (let the digest decide) rather than reflexively. Independent reads can be issued **in parallel** in one batch — parallel calls cost the same as serial ones but finish far faster.

## Product & project context

### `get_products()`
Lists all products in the workspace: `id`, `name`, `tagline`, `description`, `status`, `platform`, `segments`. Your `find_skills` first-run context already carries the current product and the other products' ids, so you usually don't need this — call it only when that context is unavailable or you need the full metadata.

### `get_projects(all_products?)`
Lists projects for a product (`id`, `name`, `description`). `all_products: true` groups projects across every product. Typical projects: Support, Discovery, Sales, plus named research projects. Pass the resulting `project_id` to a product-scoped tool to narrow it; most work stays at full-product scope with no project.

## Customer evidence (the voice of the customer)

### `search(literal_user_question, product_id, search_query?, project_id?, nature?, note_types?, meeting_id?, date_from?, date_to?, limit?, offset?)`
Two modes over the same corpus — needs, feedback, quotes, pain points, custom signal types, transcript sections, competitor capabilities, and news.

- **Semantic mode** — pass `search_query`. Items are **ranked purely by relevance** (each carries `relevance`, absolute 0–100); there is no per-type quota, so one search may return mostly pain points and another mostly needs. That mix is a finding, not an artifact. Vary `search_query` across your 3–4 `evidence` searches.
- **Filters-only browse** — omit `search_query` and pass at least one of `note_types` / `meeting_id` / `date_from` / `date_to`. Returns a **recency-ordered** listing of signal notes (newest first, no relevance score). Use it to page a source's notes or a date window, not to answer a semantic question.

Params:
- `literal_user_question` (required) — the actual user question that triggered the search.
- `product_id` (required) — the product to scope to (from the first-run context).
- `search_query` (optional) — the optimized retrieval query. Present ⇒ semantic mode; absent ⇒ filters-only mode.
- `project_id` (optional) — narrow to one project; overrides the session project.
- `nature` (optional) — `evidence` | `context` | `guidance` | `all`. Declares what you're seeking. **May be silently dropped on workspaces without the lab flag** — always also triage results by their `type`.
- `note_types` (optional, filters-only) — array restricting the listing to these signal types: `need`, `feedback`, `quote`, `problem` (alias for pain point), `qa`, or a custom signal type's name. **Ignored when `search_query` is provided.**
- `meeting_id` (optional, filters-only) — restrict the listing to notes from one source (meeting/document) id.
- `date_from` / `date_to` (optional) — inclusive `created_at` bounds, Unix ms.
- `limit` (optional) — page size. Default 50, max 100.
- `offset` (optional) — how many to skip. Default 0. Use the digest's `next_offset` for the following page.
- **Returns a digest first, then the items.** The digest summarizes the *full* result set — counts by type, cluster headlines (sized by the whole dataset), distinct meetings/speakers and top speakers, date range, optional nature split, and pagination state (`returned`, `offset`, `total`, `next_offset`, `size_capped`). Read it before the items. Note the two totals: `total_results` is what you page over (a cluster is one row), `item_count` is the evidence inside them (what `counts_by_type` sums to).
- Items carry `id`, `type` (`need` | `feedback` | `quote` | `pain_point`/`problem` | `transcript_section` | competitor / news / custom), `content`, `created_at`, `url` (deep link — **cite with this**, see `citations.md`), and often `meeting_name` / `meeting_id` / `who_said_it` / `project_name`. Clusters carry `is_cluster: true`, `children` (only the members this search surfaced), and `total_items` (the cluster's true size). (Items also carry `footnote_marker` (`[^n]`) / `marker_id` — the first-party app's own numbering; **ignore it** and cite via `url`.)
- **Cluster members live in `children[]`** — enumerating only top-level items skips them. See the cluster trap in `search-patterns.md`.

**Quotes.** There is no separate quotes tool: to *show* the customer's voice, run a `search` whose `search_query` is worded for verbatim reactions and keep the `quote`-type items (each carries `who_said_it`, `meeting_name`, sentiment, and a `url`). For a source's or window's quotes without semantic ranking, use `search(note_types: ["quote"], …)` in filters-only mode.

### `view_item(item_id, item_type)`
Detail on one item. `item_type`: `need` | `problem` | `pain_point` | `feedback` | `quote` | `opportunity`, or a custom signal-type name. Use to expand a specific hot item surfaced by `search`.

## Sources (conversations, documents, and other ingested records)

### `find_sources(product_id, query?, project_id?, source_types?, date_from?, date_to?, attendee_email?, attendee_domain?, title_keyword?, limit?)`
Find sources — meetings, calls, ingested documents, spreadsheets, and email/communication records — for a product.
- **Query mode** — pass `query` to rank sources by semantic match over their content. Each result carries `relevance`, `match_count`, and `top_snippet`.
- **Browse mode** — omit `query` for the most recent sources, newest first. This includes sources still processing, marked by `processing_status`.
- `source_types` (optional) — filter by category: `meeting`, `call`, `document`, `spreadsheet`, `meeting_notes`, `communication`. Omit for all.
- `date_from` / `date_to` (Unix ms), `attendee_email`, `attendee_domain` (e.g. "acme.com" — great for building personas/ICPs from real accounts), `title_keyword`.
- `limit` (default 20, max 50).
- Each result is a **summary**: `id`, `name`, `type`, `nature?`, `created_at`, `start?`, `attendees`, `duration?`, `origin_ref_type?`, `processing_status?`, and (query mode) `relevance` / `match_count` / `top_snippet`, plus a `url`. Use `read_source` with an `id` for full content.

### `read_source(source_id, offset?, limit?)`
Full content of one source. Documents are returned as **titled markdown sections**; conversations as **speaker-attributed segments**. **Long** — deep dives only. Paginated: `offset` (default 0) and `limit` (default 200 segments, max 500); the response returns `total_segments`, `has_more`, and `next_offset` to page through. Returns `source_type` and a `url`, with per-segment citation markers.

## Secondary / internal assets (use sparingly — not customer ground truth)

### `get_opportunities(product_id)`
The automated product opportunities the system has suggested for a product from its signal clusters. **Machine-generated — treat with a grain of salt** and corroborate against evidence (`search` / `find_sources`) before relying on them. Label as AI-generated when referenced.

### `get_shaping_notes(keyword?, status?, tag?, limit?, product_id)`
Lists collaborative markdown docs in the workspace lifecycle (statuses like Ideas → PRDs → Dev Plans → Build Notes → Revisions → Ready → Done; tags like Prompts, Interview Notes, Research Notes). Response includes the workspace's valid `available_statuses` and `available_tags`. Notes carry **branch** and **PR number** fields — the hook for `review-pr`.

### `read_shaping_note(note_ids)`
Full body of one or more shaping notes by ID: title, subtitle, status, tags, branch, PR number, markdown body.

### `list_competitors(product_id)` / `get_competitor_capabilities(competitor_id)`
Competitor list (with threat level) and a competitor's capabilities. The list is a curated/less-reliable category — cross-check against what customers actually say (`search` for competitor mentions, win/loss quotes).

## Saving back

### `add_source(project_id, nature, source_type, …)`
Persists a note, document, meeting or communication thread into a Project. See `saving-to-evermuse.md` for full recipes. Requires a `project_id`. `nature`: `evidence` | `guidance` | `context`. Four modes:

- **Note** — `source_type` `document` | `meeting_notes` | `call_transcription`, with `content` (markdown) + `title` + optional `subtitle`/`tags`.
- **Document** — `source_type` `document` | `spreadsheet` | `meeting_notes`, with `file_base64` + `filename` (+ optional `mime_type`). Tags are rejected in this mode.
- **Meeting** — `source_type: 'meeting'`, for a real call pulled from a vendor MCP (Gong, Zoom, Fireflies, Granola…). Supply one or more of `transcript_turns` (`[{speaker, text, start_ms?}]` — speaker required on every turn), `vendor_payload` (raw payload; supported vendors only, today `gong`), `media` (`{url, type: 'video'|'audio'}`). Plus optional `participants`, `occurred_at`, `thread_id`. Produces speaker-attributed transcripts, participants, playable media and citation clips — prefer it over `call_transcription`, which only creates a flat unattributed note.
- **Communication** — `source_type` `conversation` (Slack thread / Zendesk ticket / Intercom conversation) | `message` | `email` | `email_thread`, with `messages` (`[{author, text, sent_at?}]`, preferred) or `content`.

Set `external_source` + `external_id` on anything fetched from another system: resubmitting the same `external_id` returns the existing source instead of duplicating or re-billing it.

## Third-party bridge

### `find_tool(query?, server?, offset?)` / `call_tool(connection_id, tool_name, arguments)`
Discover and call tools on workspace-connected external MCPs (Linear, Jira, GitHub, Notion, Attio, Intercom, Fireflies). Requires `mcp:thirdparty` scope — **may be blocked**. See `third-party-bridge.md` for the try-once-then-fallback pattern.

> `run_subagent` exists on some Evermuse deployments but is not available to API-key/plugin sessions — do not rely on it.
