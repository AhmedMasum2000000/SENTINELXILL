<!-- Adapted from phuryn/pm-skills (MIT) -->
# Experiment Templates

A library of low-effort experiments for de-risking assumptions. Pick the **cheapest** method that would actually change your mind. Core principles across all of them:

- **Measure behavior, not opinions.** "Would you use this?" is useless — watch what people *do*.
- **Skin in the game** (Alberto Savoia, *The Right It*): real commitment — time, money, reputation — is the only reliable demand signal.
- **Your Own Data (YODA)**: collect your own experimental data over Others' Data (market reports, analogies). "The market for your idea does not care about the market for someone else's idea."
- Every experiment needs a **clear metric and a pre-committed success threshold**. Decide the threshold *before* running it.
- **Test responsibly** — never put users or the business at material risk; for production tests, state the risk mitigation.

Before designing any experiment, remember the Evermuse twist: if the corpus already answers the assumption, you don't need an experiment — cite the quote and cross it off.

## Existing-product experiments

| Method | Best for validating | What you do | Metric · threshold example |
|--------|--------------------|-------------|----------------------------|
| **First-click / task-completion prototype test** | Usability | Give 5–8 users a clickable prototype and a task; watch where they click and whether they finish. | Task success ≥ 70%; first click correct ≥ 60% |
| **Fake door / feature stub** | Value / demand | Add an entry point (button, menu item) for the not-yet-built feature; count clicks, then show a "coming soon / tell us more" capture. | CTR ≥ 8% of exposed users |
| **Technical spike** | Feasibility | Timeboxed engineering investigation of the riskiest technical unknown (integration, performance, scale). | Spike answers "can we build it in budget?" yes/no |
| **A/B test in production** | Value / Impact | Ship the change to a small % of traffic; compare against control. Mitigate risk with a small exposure %, a kill switch, and guardrail metrics. | Target metric lift ≥ X% at significance |
| **Wizard of Oz** | Value / Feasibility | Users experience the feature; humans perform the "automated" work behind the curtain. | Repeat-usage / satisfaction among the cohort |
| **Behavioral survey** | Value (weak) | Survey that asks about *past behavior and money already spent*, not future intent. | % who already pay for / built a workaround |

## New-product experiments (pretotypes)

Start with an **XYZ hypothesis**: *"At least **X%** of **Y** will do **Z**."* (X = expected engagement %, Y = the specific target market, Z = the concrete action). Then test the smallest thing that produces real behavior:

| Pretotype | Signal it tests | Metric · threshold example |
|-----------|-----------------|----------------------------|
| **Landing page** | Interest | Sign-up / click-through rate ≥ X% of visitors |
| **Explainer video** | Understanding + appeal | Watch-through + waitlist conversion |
| **Email campaign** | Demand | Reply / click-through rate |
| **Pre-order / waitlist (with a deposit)** | Willingness to pay (skin in the game) | % who commit money or a deposit |
| **Concierge / manual MVP** | Value delivery | Deliver the service by hand to a few customers; do they come back and pay? |

## Filling in an experiment
For each true-unknown assumption, specify:
- **Assumption** — the belief being tested.
- **Experiment** — exactly what you'll do.
- **Metric** — the single behavior you'll measure.
- **Success threshold** — the value you'd need to see to proceed (committed in advance).
