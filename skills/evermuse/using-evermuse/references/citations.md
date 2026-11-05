# Citations & Source Badges

IMPORTANT: Citations are **optional but strongly recommended** — the required part of any Evermuse task is the grounding search batch, not the citing. That said, in-line citations are what make customer-derived claims **visibly** backed by real evidence, so cite whenever you reasonably can. When you do cite, follow the format below. Since resource links are not yet supported in many clients, and the citation schema doesn't work properly with external links, this is the best format right now.


## Which citation format applies

**First-party Evermuse chat:** If you are the in-app Evermuse assistant — the surface where the app renders your `[^n]` markers and appends the Sources list for you — so please keep following your system message with the app's own footnote citation instructions. They take precedence.

**Everywhere else** (external MCP clients, Claude Code, Claude Desktop, ChatGPT, Codex or any raw-markdown renderer): use the inline linked-number badge defined below. This is the recommended baseline whenever you cite.


## The rule

Whenever a claim in a deliverable rests on Evermuse input, **prefer an inline citation**. If you wrote "customers want X", a citation lets a reader click straight through to *where they said it* — without it, the claim reads as your opinion. Citations are optional, but they are the whole point of showing the customer's voice, so cite when you can.

The recommended baseline when you cite is the inline linked-number badge below. Fuller treatments — a verbatim quote block, an attribution line — are welcome *in addition* where they sharpen the point, but they never replace the inline badge.


## Recommended format — linked number in a code badge

Cite sources with a bare, linked number rendered as inline code. Put the code span **inside** the link so the number shows as a pink code badge that is still clickable. Do not wrap the number in brackets.

Syntax:

    [`1`](URL)

Where `URL` is the `url` field from the Evermuse result (e.g. `https://dev.evermuse.com/s/<id>`). Number the citations sequentially per answer (1, 2, 3…), in order of first appearance.

Example (raw):
    Discovery is the single biggest unmet need [`1`](https://dev.evermuse.com/s/lHnJP3lDTOo2Vl5KoVqd),
    and finding new shows is manual work [`2`](https://dev.evermuse.com/s/g9A7bQSaVl4QLGIsqfr8).

Rules for external apps:
- The code span goes **inside** the link brackets: `` [`1`](URL) ``. The reverse (a link inside backticks) renders as plain text and will NOT be clickable.
- No square brackets around the number — just the digit, in backticks, inside the link.
- One citation per distinct source; place it immediately after the claim it supports, **before** the punctuation.
- Number sequentially per answer (1, 2, 3…) in order of first appearance. Reuse the same number when you cite the same source again.
- Never invent a URL. If a result has no `url`, fall back to plain attribution (speaker, meeting, date) with no link or citation.
- Reuse the exact Evermuse `url`; do not shorten or edit it.
- There is **no Sources footer** in this format — the links live inline. Do not append a footnote list at the end.

> **Note on `footnote_marker`.** Evermuse results may also carry a `footnote_marker` / `marker_id` field (e.g. `[^7]`). That is the first-party app's own numbering, and it is **not** unique across tool calls in external clients — each call restarts at `[^1]`, so reusing it would render two different sources as the same badge. **Ignore it for this format.** Assign your own sequential numbers (1, 2, 3…) and link them to the result's `url`.


## Occasional richer styles (allowed, never instead of the badge)

The inline badge is the floor, not the ceiling. When showing the customer's actual voice makes the point land harder, add a verbatim quote block and still attach the badge:

```markdown
> "We lose half a day every week re-keying this into the spreadsheet."
> — Dana K., Acme onboarding call, 12 May 2025 [`3`](https://dev.evermuse.com/s/lHnJP3lDTOo2Vl5KoVqd)
```

For a claim summarizing several items, attach a badge per distinct source:

    Re-keying data by hand is the most-cited onboarding pain (7 mentions across 5 accounts) [`3`](URL_A) [`4`](URL_B) [`5`](URL_C).

Pull attribution from the result fields: `who_said_it`, `meeting_name`, `created_at` / `meeting_start` (format as a human date). If a field is missing, include what you have (e.g. "— enterprise customer, sales call").

## Fallback when there is no `url`

Some results won't carry a `url` yet. Keep everything except the link and citation badge — the attribution still makes the claim verifiable:

```markdown
> "We lose half a day every week re-keying this into the spreadsheet."
> — Dana K., Acme onboarding call, 12 May 2025
```

Never fabricate a URL to fill the gap. This is a best-effort to provide real grounding for teams to build trust in your conclusions.

## What not to cite as customer voice

Shaping notes, research questions, the competitor list, and the updated roadmap are internal/AI-generated assets. If you reference them, label them as such ("per the team's draft roadmap (AI-generated)") — never dress them up as a customer quote.

## Hard rules

- Never fabricate a quote, speaker, meeting, or link. If you don't have a real quote, say the point is a hypothesis and mark it — don't invent evidence.
- Never invent or edit a `url`; reuse exactly what the result gave you, or omit the link.
- Verbatim means verbatim: quote the customer's actual words (light trimming with `…` is fine; paraphrase inside quote marks is not).
