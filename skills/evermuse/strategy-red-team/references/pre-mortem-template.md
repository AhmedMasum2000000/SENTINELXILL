<!-- Adapted from phuryn/pm-skills (MIT) -->
# Pre-Mortem Mode

Imagine the launch already failed and work backward. Distinguishes real threats from overblown worries and unspoken concerns, then triages by urgency. Use when the user asks to "run a pre-mortem" or "imagine it failed."

## Grounding (same falsify-the-doc discipline as the parent skill)
Before categorizing, run the grounding batch **worded to contradict the plan's core bets** — 3–4 `evidence` searches aimed at falsifying each bet, plus a `guidance` and a `context` search for internal direction and market threats. Optionally pull opposing quotes with a quote-angled `search`. A **Tiger** backed by a customer quote ("we'd never adopt this if it needs SSO on day one [`1`](URL)") is far stronger than a hunch. Save `nature: "guidance"`, tags `["evermuse-plugin","red-team","pre-mortem"]`.

## Steps
1. **Set the scene.** Imagine it launches in 14 days and fails — no adoption, missed revenue, reputation hit. What went wrong? What did we miss or over-trust?
2. **Categorize each risk:**
   - **Tigers** — real problems you personally see could derail it. Evidence-based; require action.
   - **Paper Tigers** — concerns others raise that you don't buy; document to align stakeholders.
   - **Elephants** — unspoken assumptions nobody is validating; investigate before launch.
3. **Triage Tigers by urgency:**
   - **Launch-blocking** — must fix before launch (broken core, regulatory blocker, unmet key-customer dependency).
   - **Fast-follow** — fix within 30 days (perf, secondary features).
   - **Track** — monitor; fix if it bites (nice-to-haves, edge cases).
4. **Action plan per launch-blocking Tiger:** risk · mitigation · owner · due date.

## Output
```markdown
## Pre-Mortem: [product]

### Tigers (real risks)
- [risk] — [launch-blocking|fast-follow|track] · counter-evidence: > "[quote]" [`1`](URL) · mitigation

### Paper Tigers (overblown)
- [risk] — why it's not real (cite if evidence disconfirms it)

### Elephants (unspoken)
- [assumption] — how to investigate

### Action plans — launch-blocking Tigers
| Risk | Mitigation | Owner | Due |
```

Default to "Tiger" when unsure — better to surface a risk early. Be constructive, not blame-seeking.

---
Adapted from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT).
