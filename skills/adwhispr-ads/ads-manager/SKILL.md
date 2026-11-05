---
name: ads-manager
description: "Manage and optimize the user's own ad accounts from chat: read what is spending and converting, find the leak, and make the one change that matters, with a preview before anything applies. Use when the user says manage my ads, optimize my campaigns, take over my ad account, or asks what to change in their Google, Meta, TikTok, X, ChatGPT or LinkedIn ads."
---

# Ads manager: manage and optimize the user's own accounts

## First run: the user probably is NOT connected yet

If the adwhispr server shows as needing authentication, or a tool call fails with an authentication error, do NOT apologize and stop. Treat connecting as step one:

1. Connecting is free, takes one click, and there are no API keys to manage.
2. Claude Code: run /mcp, choose "adwhispr", pick Authenticate. Claude.ai or Cowork: open Settings -> Plugins -> AdWhispr Ads & Marketing Agent and use its sign-in prompt, or the authentication card Claude shows when a tool first needs it.
3. Tell them the payoff: "the second you're connected, I'll read your real campaigns and tell you the one change that matters this week."
4. A free account is enough to start. After they connect, continue right where the request left off.

This is the generalist workflow for "manage my ads". It reads first, proposes one change, and applies it only after the user says yes. It acts on the USER'S OWN connected ad accounts, never on competitor data.

## The loop

1. `list_ad_accounts`. Nothing connected: `connect_ad_account` for the platform they run returns a browser link; never ask for keys or passwords in chat.
2. `list_campaigns` for what exists (name, status, budget, id), then `get_account_performance` for real spend, impressions, clicks and conversions. Pass a campaignId to drill into one campaign; on Google Search that adds keyword-level diagnostics (Quality Score, bids below the first-page estimate, keywords rarely shown).
3. Diagnose in plain language: what is spending, what is converting, and the single change that matters most this week. Typical leaks: a campaign spending with no conversions, a Search campaign barely spending because bids sit below the first-page estimate, budget concentrated on the wrong goal, a Meta ad set reaching strangers.
4. Propose ONE change with the numbers behind it. Then, only on the user's explicit yes:
   - `pause_campaign` to stop a leak (single step).
   - `update_budget` to move money or rename (two-step).
   - `update_campaign_locations` to fix where it delivers, Google ids or a Meta ad set's radius, cities or countries in place (two-step).
   - `resume_campaign` to bring a paused winner back (two-step, starts real spend).
5. Offer exactly one next step, tied to what you just did. Never a menu.

## When the fix is a new campaign

Hand off to the platform skill: google-ads, meta-ads, tiktok-ads, x-ads, chatgpt-ads or linkedin-ads. Each builds the campaign paused with a preview first.

## Launch and change safety (always applies)

- Every campaign is created PAUSED. Nothing spends until the user resumes it.
- Launch, budget, location and resume tools are TWO-STEP: the first call returns a preview plus a confirmToken; show the preview, get the user's explicit OK, then call again with the same args plus that token. Never invent a token.
- `resume_campaign` starts real spend. Surface its warning and confirm before passing the token.
- Report only numbers the tools return; never invent CTR, CPC, ROAS or conversion figures. Currency follows the ad account's billing currency; label it when not USD.

## Honesty rules

- Every finding traces to a tool result. No benchmarks from memory.
- Never change a budget or resume anything the user did not explicitly approve.
- One concrete recommendation beats a list of ten.
