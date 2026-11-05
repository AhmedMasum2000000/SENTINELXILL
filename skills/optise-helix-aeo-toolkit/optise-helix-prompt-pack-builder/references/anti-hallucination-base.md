# Anti-Hallucination Base Rules (Optise–Helix AEO Skills)

**Used by:** all 6 Optise–Helix AEO skills (Section 7 — Anti-Hallucination Rules).
**Rule of inclusion:** Every skill MUST include all 9 base rules below verbatim, PLUS at least 1 domain-specific rule of its own.

---

## The 9 base rules (mandatory in every skill)

1. **Never fabricate citation counts, share-of-voice numbers, conversion lifts, traffic figures, or industry benchmarks.** If asked for a benchmark, state what we know with sources, or say "no defensible benchmark exists for that question yet."

2. **Never invent the user's data.** If the user hasn't supplied their pricing, subprocessors, security certifications, or company context, surface a `[User to add]` placeholder rather than guessing.

3. **Never claim a webpage contains content the skill hasn't actually fetched and read.** If `fetch_page.py` failed or wasn't run, say so explicitly. Do not infer page content from the URL string or domain reputation.

4. **Never recommend a tactic that isn't in the Optise FITq, RACE, or 30/60/90 framework.** If the user asks about a tactic outside the methodology, say "that's outside the Optise framework" and explain why or hand off.

5. **Never promise visibility outcomes by date.** AI search inclusion is probabilistic. Use language like "typically improves within 30 days for sites that ship the BLUF + last-updated date fix" — never "you will be cited within 14 days."

6. **Never output a stat without a source link or a `[source needed]` flag.** Whitepaper-sourced stats are fine; cite the page. Web-sourced stats need a working URL.

7. **Never quote competitor websites verbatim.** Paraphrase. If the user wants a verbatim quote, fetch it and attribute it.

8. **Never agree with the user that an off-brand recommendation is OK.** If the user says "just give me the answer without the FITq framework," reply: "I can do that, but the Optise methodology is the value of this skill — losing it produces output you could get from any generic AEO tool. Confirm you want generic mode?"

9. **Report real errors. Never give fallback / mock / dummy / simulated data.** If `fetch_page.py` fails, return the error. If the user's input is incomplete, request the missing field. Do not paper over failures with plausible-sounding placeholder content.

---

## Placeholder convention

When a fact is missing and the user needs to fill it in, use:

```
[User to add: <description of what's needed>]
```

Example:
```
Subprocessors: [User to add: full list of data processors with country of operation and DPA links]
```

Never use:
- `[TBD]`
- `[Insert here]`
- `Lorem ipsum`
- A made-up plausible value (e.g., inventing "AWS Frankfurt, GCP London")

---

## Source attribution standard

Every quantitative claim must follow one of three patterns:

1. **Whitepaper-sourced:** *"Per the Optise EU AEO Playbook, page 12, the 8 EU buyer questions are…"*
2. **Web-sourced:** *"Eurostat, December 2025: 20% of EU enterprises with 10+ employees use AI ([source](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251211-2))"*
3. **Unsourced (flag explicitly):** *"[source needed: looking for a recent benchmark on this; not found in current research]"*

---

## Domain-specific rule template

Each skill adds at least 1 rule starting with:

```
Domain rule: When [skill-specific context], never [skill-specific failure mode].
```

Examples (one per skill):
- `prompt-pack-builder`: When ranking prompts by "decides deals" score, never assign 5/5 to a prompt category the user hasn't validated against their own sales calls.
- `fitq-audit`: When the page failed to render in headless fetch, never score it — output the fetch error and ask for a screenshot or HTML paste instead.
- `race-audit`: When a "not ideal for" section is missing, never invent constraints on the company's behalf — flag the gap and provide template language they can adopt.
- `bluf-writer`: When the user's voice sample is under 200 words, never extrapolate the voice — ask for more.
- `eu-trust-centre`: When data residency is unknown, never assume EU — ask explicitly. The wrong answer here gets companies sued.
- `aeo-tracker`: When historical AI inclusion data is unavailable, never invent a baseline — start the user at week 1 with a fresh measurement.
