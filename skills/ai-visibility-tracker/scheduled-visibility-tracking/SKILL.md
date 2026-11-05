---
name: scheduled-visibility-tracking
description: Configure, verify, resume, pause or change recurring AI visibility and SEO tracking for a website portfolio using an available host scheduler or Apify schedules, with approved budgets and reports.
---

# Schedule and manage portfolio tracking

Read the [portfolio state](../seo-growth-agent/references/campaign-state.md) and [scheduler procedures](references/scheduling.md). Use `visibility-onboarding` for missing settings. This skill manages authorized campaign schedules; the baseline visibility skill remains limited to its run. No scheduler, executable, credentials or server is bundled.

## Prepare

Require accepted website/market/panel revisions, user-owned Apify access, module scopes, cadence/timezone, baseline/per-run and portfolio budgets, duration, report destination and alert preferences. Confirm only missing or materially expanded authorization. Building the plugin is not authorization to activate the publisher's own recurring paid jobs.

Check the host's actual scheduling tools and execution environment. Prefer a recurring **agent** job when the user wants the complete pipeline: collect due modules, enforce the portfolio ledger, compare results, generate actions and deliver reports. It must have durable state and user-owned authentication available at execution time. A reminder or wake-up with no execution access does not qualify.

Offer Apify cloud schedules for fixed Actor data collection when a recurring agent is unavailable or the user chooses it. Explain which parts are automatic and which require opening the assistant. Apify native schedules do not execute this plugin's analysis skills or enforce a shared monthly portfolio ledger. If a hard monthly maximum or automatic end date is required, verify a controller that checks/stops launches; otherwise leave the schedule prepared and offer a manual or host-controlled plan.

## Configure and verify

1. Inventory only schedules recorded for this portfolio or matching its confirmed ownership marker. Reuse matching IDs and reconcile any ambiguous prior creation before retry. Never modify unrelated schedules or use a global account spending change as a shortcut.
2. Prepare a readable schedule table and input files: site/market/panel, module, exact actor, input revision, frequency/timezone, per-run cap, monthly occurrence estimate, duration, reports and alerts. Split site and market inputs; batch only where the mapped Actor explicitly supports it and evidence remains attributable.
3. Follow the selected backend procedure. Keep collection and reporting ownership explicit: a report job must not launch modules already collected by Apify schedules. Persist IDs immediately; read back actual configuration, including status, next occurrence, Actor inputs and run caps. A changed site/panel/cadence needs a recalculated portfolio allocation.
4. Collect an authorized substantive baseline and verify the first scheduled execution when due. Link its run/build IDs, actual input, dataset, summaries and charges to the schedule/host execution record. `SUCCEEDED` with diagnostic rows is not tracking coverage. Report **configured, awaiting first scheduled run** until a real scheduled measurement completes. Full report automation additionally requires successful report generation and delivery evidence.
5. Save verification status and last execution/report markers. Return site-level status, next known run with timezone, costs/limits, report location and pause/resume instructions. Never wait in chat indefinitely or launch an unapproved test merely to claim activation.

## Each recurring agent execution

Load state; reconcile known runs/charges before launching anything. Process due site/market/module records sequentially with a durable execution ID and reservation. Skip paused sites and already handled occurrences. If a prior occurrence is pending, resume it instead of relaunching. Check the global and site remaining budget plus provider/schema compatibility. Fail closed on unreadable state, uncertain charges, expired authorization or unavailable login; no automatic paid retries.

Load goals/corrections, feedback/action history and due records. Use [adaptive selection](../seo-growth-agent/references/adaptive-research.md) for approved exploration; never silently change fixed comparison panels.

Collect complete pages and real coverage through the existing specialist skills. Compare only matching site, market and panel revisions; record changed builds/models and partial coverage. Generate separate site reports and one portfolio rollup without blending denominators or treating different businesses as competitors. Deliver approved digests or alerts only to the configured destination; deduplicate using execution/panel/report IDs. If delivery fails, retain the report and retry only delivery, not Actor research.

Use the [review template](../seo-growth-agent/references/review-template.md): what changed, why it matters, next three actions and next check. Generated/delivered reports aren't human reviews. Honor quiet hours/frequency limits; unchanged changes-only monitors stay quiet. A requested digest is a separate policy. No default inactivity reminders, publisher feedback uploads or extra runs to inflate engagement.

## Manage

“Pause website A” disables only A's collection and reporting work, verifying each scheduler readback; already running jobs may continue and must be reported. Do not delete results. Portfolio pause covers all recorded portfolio jobs. If a shared host job cannot be paused per site, persist the site pause flag and verify its execution prompt honors it; confirm other sites remain due. Resume with existing IDs after checking authorization and remaining allocation. Adding/removing a site or changing a panel preserves old baselines, updates reservations and adjusts only matching schedules. Disabling a host report job does not stop Apify collection jobs; pause both when stopping tracking. Treat “stop now” separately from deletion and ask only when scope is unclear.

Use [visual reporting and persistence](../seo-growth-agent/references/reporting.md) for readable tables/charts, machine-readable evidence and saved analytical context. Use the host LLM for synthesis and resume known state automatically.
