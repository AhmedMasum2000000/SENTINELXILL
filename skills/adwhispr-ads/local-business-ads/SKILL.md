---
name: local-business-ads
description: "Ads for a local business from chat: Google Search campaigns with call buttons for people searching nearby, and Meta ads targeted within a radius of the shop, created paused with a preview. Use when the user runs a local service or store (salon, clinic, dentist, restaurant, contractor, gym, agency office) and wants customers from their area."
---

# Local business ads

## First run: the user probably is NOT connected yet

If the adwhispr server shows as needing authentication, or a tool call fails with an authentication error, do NOT apologize and stop. Treat connecting as step one:

1. Connecting is free, takes one click, and there are no API keys to manage.
2. Claude Code: run /mcp, choose "adwhispr", pick Authenticate. Claude.ai or Cowork: open Settings -> Plugins -> AdWhispr Ads & Marketing Agent and use its sign-in prompt, or the authentication card Claude shows when a tool first needs it.
3. Tell them the payoff: "the second you're connected, I'll set up a Search campaign with a call button for people searching for you nearby, created paused, you approve before anything spends."
4. A free account is enough to start. After they connect, continue right where the request left off.

Local businesses win on intent and distance: people searching for the service right now, and people within driving range. Two campaigns cover both, and both are created paused.

## Step one: the business

`get_my_brand`; if nothing is saved, ask for their website or one line about what they do and where, and `save_my_brand` the moment they answer. Ask two things only: the service area (a city, or an address plus a radius) and whether they want calls, bookings or walk-ins.

## Google Search for people searching now

- `launch_search_campaign`: keywords are the service plus the place ("emergency plumber austin", "dentist near me" style terms), 3 to 15 headlines of 30 characters or fewer that name the service and the area, 2 to 4 descriptions, the landing page, a daily budget. Set defaultCpc from the keyword's cost-per-click range when known; the default 1.00 is usually too low to win auctions.
- CALL ADS: add callPhoneNumber plus callCountryCode so the ad shows a call button. For most local services calls are the conversion.
- Geography: locationIds from `search_ad_targeting` (platform google, kind locations) for the city or region; never invent ids.
- After it runs a week, `get_account_performance` with the campaignId shows keyword-level diagnostics; a campaign barely spending usually has bids below the first-page estimate.

## Meta within a radius

- `launch_meta_ad` with radiusAddress (the shop's street address or place) and radiusKm (1 to 80, default 15). No lookup needed; Meta locates the address itself. Cards come from the Creative Library by creativeName (`list_my_creatives`) or an image the user owns: a photo of the place, the team or the work beats stock every time.
- Objective traffic by default; leads with a leadFormId when they want enquiries inside Facebook; CALL_NOW with phoneNumber when they want calls.
- Changing the area later: `update_campaign_locations` platform meta with a new radiusAddress and radiusKm edits the live ad set in place.

## Competitors down the street

Before writing copy, `find_competitors` with a niche like "dentists in Austin" shows who in the area is actually running ads right now, and `get_brand_ads` on one of them shows the offers and hooks that have survived months of spend. Borrow the angle, never the creative.

## Launch and change safety (always applies)

- Every campaign is created PAUSED. Nothing spends until the user resumes it.
- Launch, budget, location and resume tools are TWO-STEP: the first call returns a preview plus a confirmToken; show the preview, get the user's explicit OK, then call again with the same args plus that token. Never invent a token.
- `resume_campaign` starts real spend. Surface its warning and confirm before passing the token.
- Report only numbers the tools return; never invent CTR, CPC, ROAS or conversion figures. Currency follows the ad account's billing currency; label it when not USD.

## Honesty rules

- Say plainly that a brand-new Search campaign needs a week of data before anyone can judge it.
- Report only numbers the tools return.
