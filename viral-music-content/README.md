# Down In Bossa — viral content kit

Campaign kit for **Ash Army & ACND – "Down In Bossa"** (Afro House, out 30 Oct 2026).

| File | What it is |
|---|---|
| `Down_In_Bossa_100_Viral_Ideas.xlsx` | **Hand this to the editor.** 100 ideas with hook, edit recipe, length, on-screen text, platform, virality lever, difficulty and priority. Has a status dropdown, plus Playbook and Scraped Research tabs. |
| `research_tiktok_2026-11-10.json` | 60 TikTok videos scraped for "Down In Bossa" and "afro house" (views, likes, shares, saves, duration). |
| `research_youtube_2026-11-10.json` | YouTube search results for the niche. |
| `scripts/scrape_virality.py` | Re-runs the YouTube research for any keywords. Needs `pip install yt-dlp`. |
| `scripts/build_ideas_sheet.py` | Rebuilds the xlsx after you edit the idea list. |
| `scripts/make_reels.py` | **Auto-renders 9:16 reels** from the track plus the sheet. Templates: cold-open on the drop, 3-2-1 countdown, lyric-pulse spectrum. Each has the idea's hook text and the CTA. `python3 scripts/make_reels.py --audio track.mp4 --drop <seconds> [--cover art.jpg]` |
| `captions/NNN.txt` | Ready-to-post caption for each idea (hook, CTA, hashtags). The scheduler picks these up automatically. |
| `scripts/postiz_schedule.sh` | Batch-schedules finished MP4s to TikTok, IG and YT Shorts through Postiz. |

## Key findings (2026-11-10)
1. **The sound is unclaimed.** TikTok search for "Down In Bossa" returns only bossa nova covers, not the track. Upload it as original audio from the artist account now.
2. **Genre flips win.** "System Of A Down x Bossa Nova" got 5.4M views and 108K saves on TikTok. "Billie Bossa Nova" has 50M on YouTube. Bossa-meets-house fits this track's concept exactly (ideas #21–30).
3. **Short DJ/crowd clips lead Afro House.** The top TikToks are 8–18s booth/crowd POVs (1.8M, 1.3M and 1M views).
4. **Afro House remixes of pop hits** pull 5–36M on YouTube. Future angle: a "Down In Bossa"-style flip of a famous song.

## Workflow
1. Editor filters the sheet by `Priority = 1` and works top-down. That gives ~45 quick wins.
2. Export files as `<idea#>_<name>.mp4` (1080x1920). Optionally add a caption in `captions/<idea#>.txt`.
3. Schedule them:
   ```bash
   npm install -g postiz && postiz auth:login && postiz integrations:list
   TIKTOK_ID=... INSTAGRAM_ID=... YOUTUBE_ID=... DRY_RUN=1 ./scripts/postiz_schedule.sh exports/
   ```
   Remove `DRY_RUN=1` when the dry run looks right.
4. After 48h, fill in `Views 48h` and mark each idea `Winner` or `Flop`. Make 3 variations of every winner.
