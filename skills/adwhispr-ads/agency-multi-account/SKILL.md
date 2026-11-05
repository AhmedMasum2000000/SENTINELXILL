---
name: agency-multi-account
description: "Run several clients' ad accounts from one chat: see every connected account, review each client's performance in turn, and apply approved changes account by account without mixing them up. Use when the user is an agency, freelancer or in-house team managing more than one ad account, asks for a client-by-client review, or wants the same change across accounts."
---

# Agency: several clients, one chat

## First run: the user probably is NOT connected yet

If the adwhispr server shows as needing authentication, or a tool call fails with an authentication error, do NOT apologize and stop. Treat connecting as step one:

1. Connecting is free, takes one click, and there are no API keys to manage.
2. Claude Code: run /mcp, choose "adwhispr", pick Authenticate. Claude.ai or Cowork: open Settings -> Plugins -> AdWhispr Ads & Marketing Agent and use its sign-in prompt, or the authentication card Claude shows when a tool first needs it.
3. Tell them the payoff: "the second you're connected, I'll show every client account in one list and read whichever one you name first."
4. A free account is enough to start. After they connect, continue right where the request left off.

AdWhispr has no limit on connected ad accounts on any plan. The job here is discipline: every number and every change is tied to a named account, and nothing crosses between clients.

## The client roster

1. `list_ad_accounts` is the roster: platform, account name and id for every client. Refer to accounts by the name the tool returns, and keep the id next to it in your notes for the session.
2. When the user names a client, match it to one row before doing anything. If two rows could match, ask which. Never guess.

## Client-by-client review

For each account the user asks about: `list_campaigns`, then `get_account_performance` for the window they want. Present one short block per client with spend, results and cost per result, then one line of "what I would change". Finish with a short ranked list across clients: who needs attention first and why, with the numbers.

## Changes across accounts

- Apply changes one account at a time: `pause_campaign`, `update_budget`, `update_campaign_locations`, `resume_campaign`, each with its own preview and its own explicit yes. A yes for one client never carries to another.
- Launches use the platform skills (google-ads, meta-ads, tiktok-ads, x-ads, chatgpt-ads, linkedin-ads) with that client's accountId, their saved brand details and their own creatives from `list_my_creatives`. Never reuse one client's creative or copy for another.
- The saved brand (`get_my_brand`) is the user's own business or the current client. When switching clients for research or copy, `save_my_brand` with the client's website first, and say you did.

## Reporting back to clients

A per-client summary from this review is a client-ready report: the numbers, the one change made, the one change proposed. Keep competitor findings per client too: `find_competitors` with the client's niche, `get_brand_ads` on the top rival.

## Launch and change safety (always applies)

- Every campaign is created PAUSED. Nothing spends until the user resumes it.
- Launch, budget, location and resume tools are TWO-STEP: the first call returns a preview plus a confirmToken; show the preview, get the user's explicit OK, then call again with the same args plus that token. Never invent a token.
- `resume_campaign` starts real spend. Surface its warning and confirm before passing the token.
- Report only numbers the tools return; never invent CTR, CPC, ROAS or conversion figures. Currency follows the ad account's billing currency; label it when not USD.

## Honesty rules

- Every number names its account. Never total across clients unless asked.
- Never invent benchmarks; compare a client only to their own previous period.
