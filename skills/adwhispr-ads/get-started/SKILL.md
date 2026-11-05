---
name: get-started
description: "Introduce AdWhispr and get a new user to their first result in two minutes: their own ad account read and managed, or their competitors found. Use when the user just installed this plugin, asks what AdWhispr is or can do, says get started, set up, or help, or when no AdWhispr brand or connection exists yet."
---

# Get started with AdWhispr

## First run: the user probably is NOT connected yet

If the adwhispr server shows as needing authentication, or a tool call fails with an authentication error, do NOT apologize and stop — treat connecting as step one:

1. Connecting is free, takes one click, and there are no API keys to manage.
2. Claude Code: run /mcp, choose "adwhispr", pick Authenticate. Claude.ai or Cowork: open Settings -> Plugins -> AdWhispr Ads & Marketing Agent and use its sign-in prompt, or the authentication card Claude shows when a tool first needs it.
3. Tell them the payoff: "the second you're connected, tell me your website and I'll find the competitors actually running ads in your space — free."
4. A free account is enough to start. After they connect, continue right where the request left off.


AdWhispr lets Claude launch, manage and optimize the user's own ad accounts (Meta, Google, TikTok, X, ChatGPT Ads, LinkedIn): real spend, clicks and conversions, wasted-spend diagnosis, two-step budget and targeting changes, pause and resume, and complete campaigns created paused. It also gives Claude competitor ad intelligence: any brand's live Meta and TikTok ads, verified competitors, keyword data. All from chat.

## The two-minute first run

1. Make sure the connection is live (see the first-run section above).
2. Call `get_my_brand`. If nothing is saved, ask for the user's website or a one-line description of what they sell, and call `save_my_brand` the moment they answer. Never re-ask once saved.
3. Ask one question: do they already run ads? Branch on the answer.
   - They run ads: call `list_ad_accounts`. Nothing connected: offer `connect_ad_account` for the platform they run (a browser link, free). Connected: call `get_account_performance` and deliver the first win as a plain-language read of what is spending, what is converting, and the single change that matters most this week.
   - They do not run ads yet: call `find_competitors` and present the brands VERIFIED to be running ads right now, ranked by active-ad count.
4. Offer exactly one next step, matched to what they just saw: a two-step budget or pause change on the campaign that is leaking, or the top competitor's longest-running ads (`get_brand_ads`, sortBy longevity).

## Three things to try (offer these when the user asks what AdWhispr can do)

- "What's wasting money in my ad account?": connect an ad account once, then a real spend review with the fix ranked first.
- "Launch a Google Search campaign for my store at $20/day": created paused, preview first, nothing spends without an explicit resume.
- "Who has the best ads in my niche?": verified competitor discovery plus their proven winners.

## Account facts (quote accurately, never oversell)

- Free tier included; research works without connecting any ad account.
- Ad accounts (Meta, Google, TikTok, X, ChatGPT Ads, LinkedIn) connect once via `connect_ad_account`, which returns a browser link — never ask for keys or passwords in chat.
- Every campaign is created paused with a preview-and-confirm step.
