<!-- Adapted from phuryn/pm-skills (MIT) -->
# Prioritization Frameworks Reference

Select and apply the right framework. **Core principle:** never allow customers to design solutions — prioritize **problems (opportunities)**, not features.

**Evermuse note:** the point of grounding is that the numbers below stop being guesses. **Reach** = distinct accounts that actually asked (from quote-angled and filters-only `search` counts). **Importance** and **Satisfaction** are read off what the corpus says — high demand + loud dissatisfaction = high Opportunity Score. Feed real counts in; cite them.

## Opportunity Score (Dan Olsen, *The Lean Product Playbook*) — recommended for problems

Survey/read customers on **Importance** and **Satisfaction** per need (normalize each to 0–1):
- **Current value** = Importance × Satisfaction
- **Opportunity Score** = Importance × (1 − Satisfaction)
- **Customer value created** = Importance × (S2 − S1)

High Importance + low Satisfaction = highest Opportunity Score = best opportunities. Plot Importance vs Satisfaction; the upper-left quadrant is the sweet spot.

## ICE — quick scoring of initiatives
- **I** (Impact) = Opportunity Score × number of customers affected
- **C** (Confidence) = 1–10 — how sure are we? (accounts for risk; raise it when evidence is thick)
- **E** (Ease) = 1–10 — how easy to implement?

**Score = I × C × E.** Higher = do first.

## RICE — ICE with Reach split out (better at scale)
- **R** (Reach) = number of distinct customers/accounts affected — **the evidence count**
- **I** (Impact) = Opportunity Score (value per customer)
- **C** (Confidence) = 0–100%
- **E** (Effort) = person-months

**Score = (R × I × C) / E.**

## Kano Model — for *understanding* expectations, not ranking
Classify each feature: **Must-be** (absence angers, presence unnoticed), **Performance** (more is better, linear satisfaction), **Attractive** (delighters, unexpected upside), **Indifferent**, **Reverse** (some users dislike it). Use to interpret *why* a need matters — evidence tells you which bucket: repeated angry mentions of a missing basic = Must-be; occasional "it'd be lovely if…" = Attractive. Don't use Kano alone to sequence a backlog.

## The 9 frameworks at a glance

| Framework | Best for | Key insight |
|-----------|----------|-------------|
| Eisenhower Matrix | Personal tasks | Urgent vs Important |
| Impact vs Effort | Quick triage | Simple 2×2; not rigorous for strategy |
| Risk vs Reward | Initiatives | Impact vs Effort + uncertainty |
| **Opportunity Score** | Customer problems | **Recommended.** Importance × (1 − Satisfaction), 0–1 |
| Kano Model | Understanding expectations | Must-be / Performance / Attractive / Indifferent / Reverse |
| Weighted Decision Matrix | Multi-factor calls | Weighted criteria; good for stakeholder buy-in |
| **ICE** | Ideas/initiatives | Impact × Confidence × Ease |
| **RICE** | Ideas at scale | (Reach × Impact × Confidence) / Effort |
| MoSCoW | Requirements | Must/Should/Could/Won't (PM-origin; use with care) |

## Templates
- [Opportunity Score intro (PDF)](https://drive.google.com/file/d/1ENbYPmk1i1AKO7UnfyTuULL5GucTVufW/view)
- [Importance vs Satisfaction — Dan Olsen (Slides)](https://docs.google.com/presentation/d/1jg-LuF_3QHsf6f1nE1f98i4C0aulnRNMOO1jftgti8M/edit)
- [ICE Template (Sheets)](https://docs.google.com/spreadsheets/d/1LUfnsPolhZgm7X2oij-7EUe0CJT-Dwr-/edit)
- [RICE Template (Sheets)](https://docs.google.com/spreadsheets/d/1S-6QpyOz5MCrV7B67LUWdZkAzn38Eahv/edit)

---
### Further reading
- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
