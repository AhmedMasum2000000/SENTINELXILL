# Specialist Actor input contracts

Verified against public default-build input schemas on 2026-10-03. Recheck before live execution. These examples are unpaid templates; use the project's actual settings and approved allocation. AI citation fields remain governed by the [visibility contract](../../ai-visibility-tracker/references/actor-contract.md).

## similarweb-alternative

Actor: `khadinakbar/similarweb-alternative`; CLI API identifier: `khadinakbar~similarweb-alternative`. [Store listing](https://apify.com/khadinakbar/similarweb-alternative).

Capped domain batch; estimated organicEtv is separate from optional Similarweb visits. NO_DATA remains unknown.

```json
{
  "domains": [
    "example.com"
  ],
  "mode": "free_tier",
  "countryName": "United States",
  "languageCode": "en",
  "includeCompetitors": true,
  "includeKeywords": true,
  "includeTechnologies": false,
  "includeSimilarweb": false,
  "keywordLimit": 10,
  "competitorLimit": 5
}
```

## google-serp-all-in-one-scraper

Actor: `khadinakbar/google-serp-all-in-one-scraper`; CLI API identifier: `khadinakbar~google-serp-all-in-one-scraper`. [Store listing](https://apify.com/khadinakbar/google-serp-all-in-one-scraper).

countryCode is lowercase and restricted by enum. One structured query record contains organic and selected features; missing features are not zero keyword demand.

```json
{
  "queries": [
    "project management software"
  ],
  "countryCode": "us",
  "languageCode": "en",
  "device": "desktop",
  "extractFeatures": [
    "organic",
    "aiOverview",
    "peopleAlsoAsk"
  ],
  "maxOrganicResults": 10
}
```

## keyword-rank-tracker

Actor: `khadinakbar/keyword-rank-tracker`; CLI API identifier: `khadinakbar~keyword-rank-tracker`. [Store listing](https://apify.com/khadinakbar/keyword-rank-tracker).

One targetDomain per run. Choose OS compatible with device. found:false is outside depth; null ranks remain null.

```json
{
  "targetDomain": "example.com",
  "keywords": [
    "project management software"
  ],
  "locationCode": 2840,
  "languageCode": "en",
  "device": "desktop",
  "os": "windows",
  "depth": 10,
  "maxKeywords": 1
}
```

## dataforseo-keyword-research

Actor: `khadinakbar/dataforseo-keyword-research`; CLI API identifier: `khadinakbar~dataforseo-keyword-research`. [Store listing](https://apify.com/khadinakbar/dataforseo-keyword-research).

Use at most ten seeds for keyword_ideas. search_volume uses the same seedKeywords field for a known list. SEO difficulty/intent may be absent, especially in search_volume.

```json
{
  "mode": "keyword_ideas",
  "seedKeywords": [
    "project management software"
  ],
  "locationCode": 2840,
  "languageCode": "en",
  "maxResults": 25,
  "minSearchVolume": 100
}
```

## google-trends-scraper

Actor: `khadinakbar/google-trends-scraper`; CLI API identifier: `khadinakbar~google-trends-scraper`. [Store listing](https://apify.com/khadinakbar/google-trends-scraper).

Compare at most five terms. geo is uppercase country or empty worldwide; property froogle means shopping. trending_searches uses trendingSearchesGeo. Interest is relative and batch-normalized.

```json
{
  "keywords": [
    "project management software"
  ],
  "geo": "US",
  "timeframe": "today 12-m",
  "property": "web",
  "dataTypes": [
    "interest_over_time",
    "related_queries"
  ],
  "maxResults": 100,
  "outputFormat": "flat"
}
```

## website-backlink-checker

Actor: `khadinakbar/website-backlink-checker`; CLI API identifier: `khadinakbar~website-backlink-checker`. [Store listing](https://apify.com/khadinakbar/website-backlink-checker).

At most ten targets; maxResults is per target. Modes backlinks/referring_domains/anchors/summary differ. Sample absence is not proof of no link.

```json
{
  "targets": [
    "example.com",
    "competitor.example"
  ],
  "mode": "backlinks",
  "maxResults": 5,
  "dofollowOnly": false,
  "excludeLost": true,
  "includeSubdomains": true,
  "excludeInternalBacklinks": true
}
```

## backlink-opportunity-finder

Actor: `khadinakbar/backlink-opportunity-finder`; CLI API identifier: `khadinakbar~backlink-opportunity-finder`. [Store listing](https://apify.com/khadinakbar/backlink-opportunity-finder).

At most ten keywords. Supported types: resource_page, guest_post, listicle, directory, podcast, expert_roundup. relevanceScore is a heuristic; snippets do not verify acceptance or current links.

```json
{
  "keywords": [
    "project management software"
  ],
  "targetDomain": "example.com",
  "opportunityTypes": [
    "resource_page",
    "guest_post",
    "listicle"
  ],
  "countryCode": "US",
  "languageCode": "en",
  "maxResultsPerKeyword": 10,
  "maxPagesPerQuery": 1,
  "minimumRelevanceScore": 35
}
```
