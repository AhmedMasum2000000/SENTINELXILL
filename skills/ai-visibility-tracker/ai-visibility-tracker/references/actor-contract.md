# AI Search Visibility Tracker contract

Verified on 2026-10-03 against public live Actor metadata, default-build OpenAPI, Store documentation and the existing Actor implementation. Actor ID: `CFYLF6fOcyvdofuof`. Owner/name: `khadinakbar/ai-search-visibility-tracker`.

## Inputs

| Field | Meaning |
| --- | --- |
| `targetDomain` | Bare website domain; required for a useful live check even though schema `required` is empty. |
| `keywords` | Nonempty array of topics; required for a useful check. |
| `targetUrls` | Optional exact HTTPS pages belonging to the target domain. |
| `competitorDomains` | Optional competing bare domains. |
| `platforms` | `perplexity`, `chatgpt`, `gemini`, `claude`; default first three. |
| `queryTemplates` | Ordered categories: `topic_authority`, `how_to`, `what_is`, `comparison`, `expert_picks`. |
| `customQueries` | Literal questions appended after template-generated questions, repeated unchanged for each keyword. |
| `maxQueriesPerKeyword` | Integer 1–10; limits deduplicated queries per keyword. |
| `responseFormat` | `concise` or `detailed`; controls answer excerpt length. |
| `demoMode` | Health-check mode; diagnostic output is not visibility data. Startup/usage charges can still apply. |

Omit `webhookUrl` in this baseline workflow. It would send the run summary outside Apify; this skill does not configure external delivery.

For exact questions, set `queryTemplates` to an explicit empty array. Templates otherwise run before custom prompts and may exhaust the cap. No `querySelectionMode`, `brandName`, brand aliases, sentiment or mention-rate inputs exist here. Never send the old Brand Monitor input schema. `{keyword}` in a custom prompt stays literal; do not assume interpolation. For different keyword-specific exact panels, prepare separate explicitly scoped runs and account for their total cost.

Example input (illustrative, not a completed check):

```json
{
  "targetDomain": "ahrefs.com",
  "keywords": ["backlink research"],
  "competitorDomains": ["semrush.com", "moz.com"],
  "platforms": ["perplexity", "chatgpt", "gemini"],
  "queryTemplates": [],
  "customQueries": [
    "Which websites offer practical guides to backlink research?",
    "Where can I find an authoritative guide to evaluating backlink quality?"
  ],
  "maxQueriesPerKeyword": 2,
  "responseFormat": "concise",
  "demoMode": false
}
```

Two exact prompts × one keyword × three platforms = six planned checks. The current live public event price was $0.09 per `keyword-visibility-checked`, giving $0.54 in check events on the verification date. Schema prose still mentions $0.096, so refresh metadata before spending. Startup events and platform usage may be additional; a run cap can reduce completed coverage.

## Dataset evidence

Each real row is keyed by `run_id`, `keyword`, `query`, `platform` and `target_domain`. Additional fields:

- `domain_cited`, `domain_citation_count`, `citation_rank`, `cited_page_url`, `cited_pages`.
- `page_from_targets_cited`, `content_gap`, `total_sources_cited`, `ai_coverage_ratio`.
- `competing_domains`, `ai_answer_excerpt`, `query_template`, `model_used`, `checked_at`.

Diagnostic rows have `platform: diagnostic` and may include `diagnostic_status` and `diagnostic_message`. Missing inputs or demo mode can produce these rows in a successful run; exclude them from rates. Validate the row's run, domain and platform against its input. Separate duplicates and malformed data for investigation rather than letting them inflate coverage.

## Interpretation

Count each unique observed `(keyword, query, platform)` once. For an exact panel, planned checks are unique keywords × unique custom prompts × selected platforms. Count missing tuples separately; never use planned checks as the denominator for a citation rate.

- Domain citation rate = observed real checks with `domain_cited: true` / observed real checks.
- Specified-page rate = observed real checks with `page_from_targets_cited: true` / observed real checks; unavailable when no target pages were configured.
- Average citation rank uses positive `citation_rank` values from cited checks only; null/unavailable is not rank zero.
- Content-gap rate = observed real checks with `content_gap: true` / observed real checks. Here a gap means other sources were returned but the target domain was absent. An answer with no sources is a separate condition.
- Competing-domain occurrence = number of observed checks containing that domain, deduplicated within each row. `competing_domains` includes non-target cited domains; `competitorDomains` filters the Actor summary's top-competitor list, not necessarily the row list.
- `ai_coverage_ratio` is source-list concentration, not market share or brand share of voice.

Read `LAST_RUN_SUMMARY` from this run's store; use `OUTPUT`/`RUN_SUMMARY` if present and relevant. Label a returned `visibility_score` as the Actor's composite score. Do not reproduce an undocumented formula or treat it as a universal AI ranking. AI-generated recommendations are hypotheses. A truncated `ai_answer_excerpt` does not prove what the complete answer said. Provider API results differ from consumer-app answers and vary across time, geography and model versions.

## Sources

- [Actor listing](https://apify.com/khadinakbar/ai-search-visibility-tracker)
- [Live input contract](https://api.apify.com/v2/actors/CFYLF6fOcyvdofuof/builds/default/openapi.json)
- [Apify CLI reference](https://docs.apify.com/cli/docs/reference)
