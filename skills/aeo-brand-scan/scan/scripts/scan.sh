#!/usr/bin/env bash
# AEO Brand Scan — calls api.genpicked.com/api/lite-scan
# Usage:
#   scan.sh "Brand Name" "Comp1,Comp2,Comp3" "category"
#   scan.sh "Brand Name" "Comp1,Comp2" "category" "brand.com" "comp1.com,comp2.com"
# Domains are optional; provide them to enable brand logo rendering.
set -euo pipefail

BRAND="${1:?brand required}"
COMPETITORS_CSV="${2:?competitors required}"
CATEGORY="${3:?category required}"
BRAND_DOMAIN="${4:-}"
COMPETITOR_DOMAINS_CSV="${5:-}"

# Convert CSV competitors to JSON array
IFS=',' read -ra COMPS <<< "$COMPETITORS_CSV"
COMP_JSON=$(printf '%s\n' "${COMPS[@]}" | jq -R . | jq -s .)

# Build base payload
PAYLOAD=$(jq -n \
  --arg brand "$BRAND" \
  --argjson competitors "$COMP_JSON" \
  --arg category "$CATEGORY" \
  --arg source "claude-skill" \
  '{brand: $brand, competitors: $competitors, category: $category, source: $source}')

# Optionally add domains
if [ -n "$BRAND_DOMAIN" ]; then
  PAYLOAD=$(echo "$PAYLOAD" | jq --arg d "$BRAND_DOMAIN" '. + {brand_domain: $d}')
fi

if [ -n "$COMPETITOR_DOMAINS_CSV" ]; then
  IFS=',' read -ra COMP_DOMS <<< "$COMPETITOR_DOMAINS_CSV"
  COMP_DOM_JSON=$(printf '%s\n' "${COMP_DOMS[@]}" | jq -R . | jq -s .)
  PAYLOAD=$(echo "$PAYLOAD" | jq --argjson d "$COMP_DOM_JSON" '. + {competitor_domains: $d}')
fi

ENDPOINT="${LITE_SCAN_ENDPOINT:-https://api.genpicked.com/api/lite-scan}"

curl -sS -X POST "$ENDPOINT" \
  -H 'content-type: application/json' \
  --max-time 60 \
  -d "$PAYLOAD"
