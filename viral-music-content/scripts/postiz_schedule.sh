#!/usr/bin/env bash
# Batch-schedule finished edits to TikTok / Instagram / YouTube Shorts with the Postiz CLI.
#
# Setup (one time):
#   npm install -g postiz
#   postiz auth:login            # or: export POSTIZ_API_KEY=...
#   postiz integrations:list     # copy your channel IDs below
#
# Usage:  ./scripts/postiz_schedule.sh exports/            # every .mp4 in folder, 1 per slot
#         DRY_RUN=1 ./scripts/postiz_schedule.sh exports/  # print only
#
# File naming: <idea#>_<anything>.mp4  e.g. 021_bossa_guitar_flip.mp4
# The caption is taken from captions/<idea#>.txt if present, else a default.
set -euo pipefail

DIR="${1:?usage: postiz_schedule.sh <folder-with-mp4s>}"
TIKTOK_ID="${TIKTOK_ID:-}"     # set these via env or edit here
INSTAGRAM_ID="${INSTAGRAM_ID:-}"
YOUTUBE_ID="${YOUTUBE_ID:-}"
# Posting slots in UTC (staggered, 3/day). Adjust to your audience's timezone.
SLOTS=("11:00" "17:00" "21:00")
START_DATE="${START_DATE:-$(date -u -d tomorrow +%F)}"
DEFAULT_CAPTION='Down In Bossa 🌴 Ash Army x ACND, out now. Full track in bio. #afrohouse #downinbossa #housemusic #fyp'

[ "${DRY_RUN:-0}" = 1 ] || postiz auth:status >/dev/null || { echo "Not authenticated: run 'postiz auth:login'"; exit 1; }

i=0
for f in "$DIR"/*.mp4; do
  [ -e "$f" ] || { echo "No mp4 files in $DIR"; exit 1; }
  idea=$(basename "$f" | cut -d_ -f1)
  caption="$DEFAULT_CAPTION"
  CAP_DIR="$(dirname "$0")/../captions"
  [ -f "$CAP_DIR/${idea}.txt" ] && caption=$(cat "$CAP_DIR/${idea}.txt")
  day=$(( i / ${#SLOTS[@]} ))
  when="$(date -u -d "$START_DATE + $day day" +%F)T${SLOTS[$(( i % ${#SLOTS[@]} ))]}:00Z"

  if [ "${DRY_RUN:-0}" = 1 ]; then
    echo "[dry] $when  $f  -> \"${caption:0:60}...\""; i=$((i+1)); continue
  fi

  # Rule: every file must be uploaded to Postiz first; raw paths are rejected.
  url=$(postiz upload "$f" | jq -r '.path')

  [ -n "$TIKTOK_ID" ] && postiz posts:create -c "$caption" -m "$url" -s "$when" -i "$TIKTOK_ID" \
    --settings '{"privacy_level":"PUBLIC_TO_EVERYONE","duet":true,"stitch":true,"content_posting_method":"DIRECT_POST"}'
  [ -n "$INSTAGRAM_ID" ] && postiz posts:create -c "$caption" -m "$url" -s "$when" -i "$INSTAGRAM_ID" \
    --settings '{"post_type":"post"}'
  [ -n "$YOUTUBE_ID" ] && postiz posts:create -c "$caption" -m "$url" -s "$when" -i "$YOUTUBE_ID" \
    --settings "{\"title\":\"Down In Bossa #shorts (${idea})\",\"type\":\"public\"}"

  echo "Scheduled $f for $when"
  i=$((i+1))
done
echo "Done: $i videos. Check settings per channel first with: postiz integrations:settings <id>"
