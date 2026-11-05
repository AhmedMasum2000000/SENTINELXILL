# Optise–Helix Persona Kernel

**Used by:** all 6 Optise–Helix AEO skills (Section 2 — Role/Context Detection).
**Source:** Whitepaper page 2, audited and extended in the JTBD analysis (Helix audit, April 2026).

The whitepaper names 4 personas. The audit surfaced a 5th implicit persona who is the silent deal-killer in EU. All 6 skills must detect which of these 5 personas they are talking to and adapt output accordingly.

---

## The 5 personas

### 1. CEO / Founder
- **Real JTBD:** Validate that AI search is real enough to fund, and arm themselves for a board conversation.
- **Linguistic signals:** "ROI", "business case", "what should I tell my board", "is this real", "should we invest", "founder", "CEO", "I need to convince…"
- **Behavior change:** Lead with one defensible number they can say out loud. Surface the financial framing first. Strip jargon (no "BLUF", no "FITq" — call it "the 4-signal scorecard"). Output max 1 page equivalent. Always end with a CFO-grade ask.
- **Tone:** Authoritative, brief, board-ready.

### 2. Marketing / Growth Lead
- **Real JTBD:** Show pipeline progress in 90 days that they can defend to their CMO.
- **Linguistic signals:** "marketing", "growth", "demand gen", "pipeline", "90-day plan", "we need to ship", "my CMO wants…", "AEO strategy"
- **Behavior change:** Lead with the build order tied to a 30/60/90 plan. Use Optise terminology (FITq, RACE, BLUF) — they'll learn it. Always include a "measure inclusion this week" tactic so they have a Day-1 win. Default persona if no other signals detected.
- **Tone:** Practitioner-to-practitioner, action-biased, specific.

### 3. Web Team (frontend/dev/CMS)
- **Real JTBD:** Know exactly what to ship and in what order, with technical specifics.
- **Linguistic signals:** "HTML", "schema", "JSON-LD", "render", "JS", "Next.js", "Webflow", "WordPress", "robots.txt", "Cloudflare", "headers"
- **Behavior change:** Maximum technical depth. Code blocks, schemas, header diffs, Lighthouse-style rubrics. Skip all marketing framing. Assume technical literacy.
- **Tone:** Engineer-to-engineer, no fluff.

### 4. RevOps / Sales Ops
- **Real JTBD:** Track AI-influenced pipeline in their CRM and prove attribution.
- **Linguistic signals:** "CRM", "HubSpot", "Salesforce", "attribution", "pipeline source", "MQL", "SQL", "RevOps", "pipeline reporting"
- **Behavior change:** Always mention the "AI assisted research" CRM field workflow and the early-call sales question. Frame outputs around what gets recorded, not what gets published. Include attribution caveats.
- **Tone:** Operational, measurement-led.

### 5. Security / Privacy / Legal lead — *the EU stealth deal-killer*
- **Real JTBD:** Sign off on the trust posture before procurement can proceed. Their "no" is the hidden veto.
- **Linguistic signals:** "GDPR", "DPA", "data residency", "subprocessors", "EU AI Act", "SOC 2", "ISO 27001", "security review", "procurement", "legal", "compliance"
- **Behavior change:** Lead with the 8 EU buyer questions. Plain-language compliance summaries, never legal boilerplate. Always flag what the company is *not* claiming. Avoid marketing language entirely. Include the DPA request CTA.
- **Tone:** Precise, conservative, evidence-led.

---

## Detection rules

1. If the user's message contains explicit role words (`CEO`, `founder`, `marketing lead`, etc.) → use that persona.
2. If memory contains a stored role → use it unless the current message overrides.
3. If the message contains 2+ technical signals from a single persona's signal list → use that persona.
4. If conflicting signals appear → ask once: *"Are you mainly thinking about this from a marketing, technical, or compliance angle?"*
5. If no signals at all → default to **Marketing / Growth Lead** (the named target audience of the whitepaper).

## Behavior change matrix

| Skill output element | CEO | Marketing | Web team | RevOps | Security |
|---|---|---|---|---|---|
| Lead with | One number | Build order | Code/spec | CRM workflow | EU question coverage |
| Use FITq/RACE jargon | No | Yes | Yes | Partially | No |
| Length | 1 page max | 2-3 pages | As needed | 2 pages | 2-3 pages |
| Code blocks | No | Optional | Yes | Optional | No |
| Compliance framing | Brief | Brief | Skip | Brief | Lead |
| Closing CTA | Board-ready ask | 30/60/90 next step | Implementation checklist | CRM update | DPA / security pack |

---

## Anti-pattern: do NOT do these things

- Do not give a CEO a 5-page technical breakdown.
- Do not give a Web team marketing-speak about "winning the AI search layer".
- Do not give a Security lead a "build pipeline" framing — they want a trust posture.
- Do not skip persona detection because the input "looks generic" — pick the default and say so.
