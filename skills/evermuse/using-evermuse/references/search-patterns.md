# Search Patterns

How to get sharp, grounded results out of Evermuse without burning credits or drowning in the payload.

## The grounding batch: evidence × 3–4, plus guidance and context

One search finds one facet. Real grounding comes from attacking the topic from several angles in one parallel batch. Word the evidence angles like:

1. **The literal ask** — the user's own phrasing ("bulk export to CSV").
2. **The underlying pain** — the problem behind it ("manual re-keying of data / copy-paste into spreadsheets").
3. **The adjacent workflow** — where it lives ("end-of-month reporting", "handoff to finance").
4. **The objection / negative** — friction and complaints ("export is broken / missing columns / too slow").

Run **3–4 of these as `evidence` searches** (`limit` up to 50 each), plus **one `guidance`** and **one `context`** search. Different wording surfaces different items because retrieval is by vector similarity. Evidence comes back rich and varied — often large. Guidance and context are usually sparse or empty; run them anyway so you know. This whole batch is the required grounding; nothing beyond it is mandatory.

## Declare the nature you want

| You're looking for… | nature | Example query |
|---|---|---|
| What customers said/need/feel | `evidence` | "frustration with onboarding data entry" |
| Market, competitors, news | `context` | "competitor pricing for bulk export" |
| Company strategy/objectives/values | `guidance` | "our stated goals for the reporting area" |

Set `nature` per search so the sets stay clean. Because the param can be silently dropped, **also** triage what comes back by each item's `type` — keep `quote`/`need`/`feedback`/`pain_point` (evidence) apart from competitor/news items (context).

## Results are ranked by relevance, not by type

`search` returns one list ranked purely by semantic relevance. There is no per-type quota, so the makeup of a result set tells you something real: a query that comes back mostly pain points found mostly pain points. Don't read the mix as a system artifact — read it as a finding.

## Read the digest first

Every `search` response opens with a **digest** — a server-computed summary of the *entire* result set, not just the page you were handed. It gives you, for free and correctly counted:

- **Counts by type**, plus two totals that mean different things: **results** are what you page over (a cluster is one row) and **items** are the pieces of evidence inside them. The type counts sum to *items*. When there are no clusters the two are equal and only one is shown.
- **Cluster headlines** — recurring themes, each sized by the full dataset (`total_items`) and the meetings it spans. This is the algorithm's own pattern detection; it is usually the fastest route to "what are customers actually saying".
- **Distinct meetings and speakers**, plus the top speakers by mention count — the raw material for "7 mentions across 5 accounts" claims, already tallied.
- **Date range** of the results.
- **Nature split**, when natures are stamped and you didn't filter to one.
- **Pagination state** — how many you're holding, how many exist, and the `next_offset` to ask for.

Use it. Counting items yourself across a long JSON payload is slower and less accurate than reading the number the server already computed.

## Paginate on judgment, not reflex

`search` accepts `limit` (default 50, max 100) and `offset` (default 0). Ground with `limit` up to 50; then let the **digest decide** whether to go deeper.

- The first page holds the strongest matches. The digest tells you how many more exist — so you can judge, not guess, whether the tail is worth pulling.
- To go deeper, raise `limit` (toward the 100 max) and/or pass the digest's `next_offset` as your next `offset`. `next_offset` reflects what was **actually** returned, so following it never skips or repeats an item.
- `next_offset: null` means you've reached the end.
- Weigh the pull against payload size, remaining context, task complexity, and the value of the data. Rich evidence on a high-stakes deliverable is worth several pages; a quick sanity check is not.
- For large pulls, consider spawning a sub-agent to page through and return the distilled findings — instruct it to carry each citation's tool metadata (`url`, `who_said_it`, `meeting_name`, `created_at`) back so you can still cite.
- Each call re-runs the search, so ordering can shift slightly if new data lands between pages. Harmless in practice; don't rely on offsets across a long session.
- `size_capped: true` means a rare, very large page was trimmed to fit a response-size limit. The trimmed items aren't lost — they're at `next_offset`.

## Quotes: angle the search at verbatim voice

There is no separate quotes tool. To *show* the customer's voice, run a `search` whose `search_query` is worded for verbatim reactions (e.g. "what customers said about X", "how they described the frustration") and keep the `quote`-type items — each carries speaker + meeting + sentiment, ready to cite. Use one search to *map the landscape* (what themes/needs exist) and a quote-angled one to *pull the pull-quotes*.

## Filtering instead of searching

When the question is about a **type** or a **time window** rather than semantics, use `search` in **filters-only mode** — omit `search_query` and pass filters. Results come back recency-ordered (newest first), no relevance score:
- All needs from one source → `search(meeting_id: "<id>", note_types: ["need"])`.
- Sentiment shift this quarter → `search(date_from, date_to, note_types: ["feedback","problem"])`.

(`note_types` only applies in filters-only mode; it's ignored when you pass a `search_query`.)

## The canonical result shape

Each item in `data`:

```
{
  id, type, content, created_at,
  url?,                      // deep link — cite with this
  who_said_it?, meeting_id?, meeting_name?, meeting_type?, project_name?,
  original_transcript_segment?,
  nature?,                   // only when the workspace has the labs flag on
  is_cluster?, total_items?, meetings_count?, children?[]
}
```

**The cluster trap.** A cluster is one item whose members live in `children[]`. Enumerating only top-level items silently skips every member of your fattest themes — exactly the evidence you most wanted. Always include children:

```
.data[], (.data[] | select(.is_cluster) | .children[])
```

On a cluster, `total_items` is its true size in the database and `meetings_count` the meetings it spans; `children` holds only the members *this* search surfaced. `total_items: 9` with two children means the theme is bigger than your slice of it — worth a narrower search or another page.

## When a result lands in a file

Some harnesses save a large tool result to a file and hand you a path instead of inlining it. The digest still reaches you in the response, so you already know what's in the file before you open it — use it to decide what to extract.

Check the envelope before writing a query against it (some harnesses save the whole MCP result, others just the payload):

```
jq 'keys' <file>
```

Then extract only what you need — from `.data[]` if the file is the payload, or `.structuredContent.data[]` if it's the full envelope:

```
# quotes with attribution and the URL you cite with, children included
jq -r '[.data[], (.data[] | select(.is_cluster) | .children[])][]
       | select(.type=="quote") | "\(.url) \(.who_said_it): \(.content)"' <file>
```

Prefer a smaller `limit` over post-filtering a giant file, and pass `project_id` to pre-scope when you already know the project. **Never** paste a raw payload into a deliverable — extract, cite, discard.

## Reuse across a session

Grounding is expensive; reuse it. A spec's evidence pass should feed its dev plan and its gap analysis. Within one session, remember what you already searched and cite it again rather than re-querying.
