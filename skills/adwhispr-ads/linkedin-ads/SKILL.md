---
name: linkedin-ads
description: "Launch and manage LinkedIn ads from chat: Sponsored Content targeted by job title, seniority, function, industry and company size, with budgets, pause, resume and performance. Use when the user wants to run LinkedIn ads, reach a B2B audience by job title or company, or manage LinkedIn campaigns."
---

# LinkedIn ads

## First run: the user probably is NOT connected yet

If the adwhispr server shows as needing authentication, or a tool call fails with an authentication error, do NOT apologize and stop. Treat connecting as step one:

1. Connecting is free, takes one click, and there are no API keys to manage.
2. Claude Code: run /mcp, choose "adwhispr", pick Authenticate. Claude.ai or Cowork: open Settings -> Plugins -> AdWhispr Ads & Marketing Agent and use its sign-in prompt, or the authentication card Claude shows when a tool first needs it.
3. Tell them the payoff: "the second you're connected, I'll set up your LinkedIn campaign targeted by job title and company, created paused, you approve before anything spends."
4. A free account is enough to start. After they connect, continue right where the request left off.

## Connect once

`connect_ad_account` platform linkedin returns a browser link (OAuth on LinkedIn's own consent screen). The ad account must be linked to a company Page the user can post for, with a payment method in Campaign Manager. Never ask for tokens in chat.

## Launching

- `launch_campaign` platform linkedin builds the campaign, its targeting and the Sponsored Content ad together, PAUSED. A daily budget is required (LinkedIn usually asks for at least 10 in the account currency).
- The ad: postText (up to 600 characters, lead with the point, about the first 150 show before "see more"), imageUrl (a JPG or PNG the user owns, or a Creative Library image by name or id from `list_my_creatives`), optional adTitle (the headline under the image). Pass posts for a creative test of 2 or more ads. Write the copy fresh for the user's own product and show it before launching.
- Objectives: traffic, sales, leads (website conversions, not Lead Gen Forms), awareness, engagement. If the goal matters and is unstated, ASK.

## Targeting is LinkedIn's strength

- Pass job titles, seniorities, job functions, industries, company sizes, skills and member interests in `interests` as PLAIN WORDS the way LinkedIn names them, for example {"id":"Marketing Manager"}, {"id":"Director"}, {"id":"51-200 employees"}. Place names go in locationIds, for example "London Area, United Kingdom". The preview names every match LinkedIn made; show it and let the user correct a wrong match before confirming.
- Job titles cannot be combined with seniorities or job functions; specific companies cannot be combined with industries or company sizes. LinkedIn will not run an audience under 300 members, and the preview shows the estimate.
- ageMin and ageMax map to LinkedIn's age buckets. Keywords and audienceIds do not apply on LinkedIn.
- LinkedIn Audience Network and Audience Expansion stay off, so the budget goes to the audience the user picked.

## Managing

- `list_campaigns` and `get_account_performance` (platform linkedin) for what exists and how it performs, down to the ad.
- `pause_campaign`, `resume_campaign`, `update_budget` (budget and rename) as on every platform. The words of a LinkedIn ad cannot be edited after creation; a change means a new ad.
- Sales and leads campaigns may land as a draft with one step left in Campaign Manager (attaching the conversion); the reply names it. Relay that plainly.

## Launch and change safety (always applies)

- Every campaign is created PAUSED. Nothing spends until the user resumes it.
- Launch, budget, location and resume tools are TWO-STEP: the first call returns a preview plus a confirmToken; show the preview, get the user's explicit OK, then call again with the same args plus that token. Never invent a token.
- `resume_campaign` starts real spend. Surface its warning and confirm before passing the token.
- Report only numbers the tools return; never invent CTR, CPC, ROAS or conversion figures. Currency follows the ad account's billing currency; label it when not USD.
