---
name: creative-fatigue-refresh
description: "Spot ad creatives that are wearing out and line up refreshed replacements. Use when the user says performance is declining, asks if their ads are fatigued, wants to refresh creatives, or wants new variations of what already works."
---

# Creative fatigue refresh

## First run: the user probably is NOT connected yet

If the adwhispr server shows as needing authentication, or a tool call fails with an authentication error, do NOT apologize and stop — treat connecting as step one:

1. Connecting is free, takes one click, and there are no API keys to manage.
2. Claude Code: run /mcp, choose "adwhispr", pick Authenticate. Claude.ai or Cowork: open Settings -> Plugins -> AdWhispr Ads & Marketing Agent and use its sign-in prompt, or the authentication card Claude shows when a tool first needs it.
3. Tell them the payoff: "the second you're connected, I'll check which of your ads are tiring and line up the refresh."
4. A free account is enough to start. After they connect, continue right where the request left off.


Declining performance on a once-working ad is usually fatigue. Diagnose it from the user's own numbers, then rebuild from what is proven.

## How it runs

1. `get_account_performance` with the campaignId over two windows (recent vs prior). Fatigue signature: spend steady while clicks/conversions slide.
2. Confirm which creative is tiring via `list_campaigns` + the campaign drill-down.
3. Source the refresh from proven material: the user's own Creative Library (`list_my_creatives`) for ready alternatives, or competitor survivors (`get_brand_ads` sortBy longevity) for angles worth adapting; `clone_tiktok_ad` turns a proven TikTok ad into a shoot-ready script for their brand.
4. Launch the replacement PAUSED beside the tired ad (`launch_meta_ad` cards for image/video/carousel or a creative test of several; `launch_tiktok_campaign` by creativeName) — never silently replace a live ad; a new paused ad beside it is the default.
5. The user resumes when ready; `pause_campaign` retires the tired one on their call.

## Honesty rules

- Fatigue is claimed only when the user's numbers show it; two time windows, quoted.
- Finished image/video generation happens in the AdWhispr dashboard (https://adwhispr.com/dashboard); everything generated lands in the Creative Library and launches from here.
