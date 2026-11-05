---
name: connect-ad-account
description: "Connect the user's own ad account (Meta, Google, TikTok, X, ChatGPT Ads or LinkedIn) to AdWhispr so Claude can read, launch and manage it. Use when the user says connect my ad account, link my Google Ads or Facebook ads, asks how to give Claude access to their campaigns, or when any account tool says no account is connected."
---

# Connect an ad account

## First run: the user probably is NOT connected yet

If the adwhispr server shows as needing authentication, or a tool call fails with an authentication error, do NOT apologize and stop. Treat connecting as step one:

1. Connecting is free, takes one click, and there are no API keys to manage.
2. Claude Code: run /mcp, choose "adwhispr", pick Authenticate. Claude.ai or Cowork: open Settings -> Plugins -> AdWhispr Ads & Marketing Agent and use its sign-in prompt, or the authentication card Claude shows when a tool first needs it.
3. Tell them the payoff: "connecting takes one click on your ad platform's own sign-in screen, and the moment it is done I can read your real campaigns."
4. A free account is enough to start. After they connect, continue right where the request left off.

Connecting an ad account is free on every plan and is the step that turns research into management. Every platform connects on its own consent screen; AdWhispr never sees the user's password and never asks for keys in chat.

## How it works, per platform

- Meta (Facebook and Instagram), Google Ads, TikTok, X and LinkedIn: `connect_ad_account` with the platform returns a browser link. The user signs in on that platform's own screen and allows access. Google needs a regular Google Ads account the user can access (a manager account alone is not enough). Meta needs a Facebook Page the user can post from; on the consent dialog they choose which ad accounts and Pages to share. LinkedIn needs the ad account linked to a company Page.
- ChatGPT Ads: `connect_ad_account` platform chatgpt returns a link to an AdWhispr page where the user pastes an Ads API key they create in their own ChatGPT Ads Manager (ads.openai.com, Settings). NEVER ask for that key in chat; if the user pastes one anyway, do not use or repeat it, send them to the page and suggest they rotate the key.

## After connecting

1. `list_ad_accounts` shows the connected accounts and the account ids every other tool takes. Google Ads ids are digits; Meta ids start with act_.
2. Deliver the first win immediately: `get_account_performance` on the account they just connected, and tell them what is spending, what is converting, and the one change that matters.
3. Offer exactly one next step: fix the leak (pause or budget, with a preview), or launch something new with the platform skill.

## If connecting fails

- Google: the sign-in used an account without access to a Google Ads account, or only a manager account. Ask them to sign in with the account that owns the ads.
- Meta: no Page was shared, or the person is not an admin of the ad account. Ask them to reconnect and tick the Page and the ad account on Facebook's dialog.
- Any platform: disconnecting in AdWhispr Settings and connecting again resolves most expired or partial connections.

## Honesty rules

- Connecting changes nothing in the ad account. Say so: no campaign is touched until the user asks for a change and approves its preview.
- On free accounts, reading and managing the account may return a one-click upgrade link instead of running; relay it as returned, never pre-judge.
