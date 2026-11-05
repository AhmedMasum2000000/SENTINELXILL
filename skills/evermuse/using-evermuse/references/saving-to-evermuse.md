# Saving Back to Evermuse

Assume that **every important piece of research or every deliverable worth keeping should be saved back into Evermuse**, so the corpus compounds over time. Use `add_source`. Always offer the save and let the user confirm before writing — but do offer it; don't quietly skip it.

## The nature-of-save rule

Pick `nature` by *what the artifact is*:

| Artifact | nature |
|----------|--------|
| Customer-voice synthesis (research brief, VoC summary, persona, journey map, sentiment analysis, feature-request triage) | `evidence` |
| Market / competitor output (competitive analysis, battlecard, market sizing) | `context` |
| Company direction (feature spec, dev plan, PRD, strategy, roadmap, OKRs, pricing, positioning, gap analysis, red-team) | `guidance` |

Rationale: a spec is the company telling itself what to build (guidance); a research brief is the customer's voice captured (evidence); a competitor teardown is external market context.

## Project resolution (add_source requires a project_id)

1. Call `get_projects`.
2. **One project** → use it.
3. **Several** → ask the user once which project this belongs to (Discovery for research, Sales for deal insights, Support for tickets, or a named research project), then pass that project's id as `add_source`'s `project_id` (and as `project_id` on any scoped calls that should stay in it).
4. **None** → don't invent an ID. Skip the save and tell the user: "I couldn't save this to Evermuse — there's no project to attach it to. Create one in Evermuse and I'll save it next time."

Projects live under a product, so make sure the `project_id` you save to belongs to the same `product_id` you grounded in.

## Recipes

**Markdown deliverable (specs, plans, research briefs, most outputs):**
```
add_source(
  project_id: "<resolved>",
  nature: "guidance",              // per the table above
  source_type: "document",
  title: "Spec: CSV export with headers",
  subtitle: "Grounded in 7 customer mentions across 5 accounts",
  content: "<the full markdown deliverable, including its inline citations>",
  tags: ["evermuse-plugin", "feature-spec", "csv-export"]
)
```

**Meeting/interview summary:**
```
add_source(
  project_id: "<resolved>",
  nature: "evidence",
  source_type: "meeting_notes",
  title: "Interview summary: Dana K. (Acme)",
  content: "<summary markdown>",
  tags: ["evermuse-plugin", "interview-summary"]
)
```

**Binary document the user hands you (PDF/DOCX/XLSX):** use `file_base64` + `filename` (title/tags are ignored in binary mode; `spreadsheet` source_type is binary-only). Max ~50 MB.

**A real meeting you fetched from a vendor MCP (Gong, Zoom, Fireflies, Granola…):** use `source_type: "meeting"` — not `call_transcription`. It preserves who said what, creates participants, links the recording for playback and citation clips, and dedupes on the vendor's own id.

```
add_source(
  project_id: "<resolved>",
  nature: "evidence",
  source_type: "meeting",
  title: "Acme QBR",
  external_source: "gong",
  external_id: "<the vendor's call id>",
  occurred_at: "2026-07-29T14:00:00Z",
  participants: [
    { name: "Alice Smith", email: "alice@us.test", is_internal: true },
    { name: "Bob Jones", email: "bob@acme.test" }
  ],
  transcript_turns: [
    { speaker: "Alice Smith", text: "How is onboarding going?", start_ms: 0 },
    { speaker: "Bob Jones", text: "The pricing page confuses my team.", start_ms: 42000 }
  ],
  media: { url: "<direct-GET recording URL>", type: "video" }
)
```

Rules that matter: every turn needs a `speaker` (aggregate sentence- or word-level vendor output into turns rather than dropping attribution); `start_ms` is an offset from the start of the recording, and supplying it is what makes seek-to-quote and clips work; `media.url` must serve the bytes on a plain GET, and pre-signed vendor URLs expire, so submit promptly. If the vendor has a server-side parser (today only `gong`), passing its raw payload as `vendor_payload` beats hand-building turns.

**A Slack thread, Zendesk ticket, Intercom conversation or email chain:** use `conversation` / `message` / `email` / `email_thread` with structured `messages`:

```
add_source(
  project_id: "<resolved>",
  nature: "evidence",
  source_type: "conversation",
  title: "Slack #support — export timeouts",
  external_source: "slack",
  external_id: "<thread ts>",
  messages: [
    { author: "Bob Jones", text: "Exports keep timing out.", sent_at: "2026-07-29T14:00:00Z" },
    { author: "Alice Smith", text: "How large is the export?" }
  ]
)
```

**Dedup:** whenever the source came from another system, pass `external_source` + `external_id` together (one without the other is rejected). Resubmitting a known `external_id` returns `already_exists: true` and the existing `meeting_id` — nothing is re-ingested and nothing is re-billed, so a re-run of a backfill is safe.

## Tagging convention

Every save includes `"evermuse-plugin"` plus the skill's own tag (e.g. `"feature-spec"`, `"research"`, `"gap-analysis"`) plus a slug for the subject (`"csv-export"`). Consistent tags make the saved artifacts findable later.

## Don't double-save

Within a chained workflow (spec → dev-plan → gap-analysis), each step saves its own distinct artifact. Don't re-save the same content. When a deliverable is a minor iteration on one you already saved this session, offer to update rather than create a second copy.
