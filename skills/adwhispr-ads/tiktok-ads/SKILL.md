---
name: tiktok-ads
description: "Launch and manage TikTok ads from chat, and clone proven TikTok ads into shoot-ready scripts. Use when the user wants to run TikTok ads, launch a TikTok campaign, research TikTok ads, or turn a winning TikTok ad into their own."
---

# TikTok ads

## First run: the user probably is NOT connected yet

If the adwhispr server shows as needing authentication, or a tool call fails with an authentication error, do NOT apologize and stop — treat connecting as step one:

1. Connecting is free, takes one click, and there are no API keys to manage.
2. Claude Code: run /mcp, choose "adwhispr", pick Authenticate. Claude.ai or Cowork: open Settings -> Plugins -> AdWhispr Ads & Marketing Agent and use its sign-in prompt, or the authentication card Claude shows when a tool first needs it.
3. Tell them the payoff: "the second you're connected, I'll find proven TikTok ads in your niche and get your own campaign staged."
4. A free account is enough to start. After they connect, continue right where the request left off.


## Connect once

`connect_ad_account` platform tiktok returns a browser link. Never ask for tokens in chat.

## Research and clone

- `research_tiktok_ads` with a competitor's name: their live TikTok ads, longest-running first (no spend/impressions exist in that data; longevity is the proxy; coverage skews EU).
- `clone_tiktok_ad` (advertiser + adId) produces a SHOOT-READY SCRIPT BRIEF — not a finished video: real frames sampled, hook/structure/pacing analyzed, shot-by-shot script adapted to the user's product and voice. Free, text output.

## Launching

- `launch_tiktok_campaign` takes the user's own video live (created paused) by creativeName from the Creative Library (`list_my_creatives`); uploads happen at https://adwhispr.com/dashboard/creatives.
- Objectives include video_views (TikTok only) plus the standard set; sales/conversion campaigns need a TikTok pixel — `search_ad_targeting` kind pixels lists them with their conversion events.
- Targeting: interests/locations/audiences via `search_ad_targeting` platform tiktok.

## Launch safety (always applies)

- Every campaign is created PAUSED. Nothing spends until the user resumes it.
- Launch, budget, and resume tools are TWO-STEP: the first call returns a preview plus a confirmToken; show the preview, get the user's explicit OK, then call again with the same args plus that token. Never invent a token.
- `resume_campaign` starts real spend. Surface its warning and confirm before passing the token.
- If the user has not clearly stated the campaign objective, ask them to pick from the valid list instead of guessing.
- Targeting is opt-in: only set what the user asked for, resolve real ids with `search_ad_targeting` first, and never invent ids.
