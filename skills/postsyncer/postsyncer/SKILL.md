---
name: postsyncer
description: Schedule, publish, and analyze social media posts with PostSyncer across 11 platforms — X (Twitter), Instagram, Facebook, LinkedIn, TikTok, YouTube, Threads, Bluesky, Mastodon, Pinterest, and Telegram. Use for creating or scheduling posts, uploading media, managing campaigns and labels, moderating comments, and reading performance analytics.
homepage: https://docs.postsyncer.com
---

# PostSyncer

PostSyncer lets you manage social content the same way the PostSyncer app and API do: workspaces, connected social accounts, posts (publish now, schedule, draft, repeat), media library, media folders, labels, campaigns, comment moderation, and performance analytics.

All functionality is provided by the bundled **PostSyncer MCP server** (`https://postsyncer.com/mcp`). The tools mirror PostSyncer's public REST API v1.

## Authentication

Two options:

1. **OAuth (recommended)** — the bundled MCP server supports the standard MCP OAuth connector flow. On first use, run `/mcp` in Claude Code and authenticate the `postsyncer` server; a browser window opens, you log in to PostSyncer once, and tokens are managed automatically.
2. **Bearer token** — a PostSyncer API token (Settings → API in the PostSyncer app) works exactly like API v1. Token abilities map to tool groups: `workspaces`, `accounts`, `labels`, `campaigns`, `posts`. Posts, comments, and analytics tools all require the `posts` ability.

If a tool returns a 401/permission error, authenticate via `/mcp` or check the token's abilities before retrying.

## Core workflow

1. **Discover** — `list-workspaces`, then `list-accounts` to get workspace IDs and connected account IDs. Always do this first; every other tool needs a `workspace_id`, and posts target account IDs from `list-accounts`.
2. **Prepare media** — for images/videos, either pass a publicly reachable URL directly in the post's `media` array, or import into the media library first with `upload-media-from-url` (list of URLs) / `upload-media-file` (base64) and use the returned media ids.
3. **Post** — `create-post` with `workspace_id`, `schedule_type` (`publish_now` | `schedule` | `draft`), `content` (array of thread items: `{ text, media?, cover_image?, is_first_comment?, first_comment_delay? }`), and optionally `accounts` (`[{ id, settings? }]`), `schedule_for` (`{ date: "Y-m-d", time: "H:i", timezone? }`), `labels`, `campaign_id`, and repeat options (`repeatable`, `repeatable_times`, `repeatable_gap`, `repeatable_gap_unit`, `repeatable_accounts`).
4. **Analyze** — `get-analytics-summary` (all workspaces), `get-analytics-workspace`, `get-analytics-account`, `get-analytics-post`; `sync-post-analytics` refreshes numbers from the platforms.
5. **Engage** — `list-comments`, `create-comment`, `update-comment`, `hide-comment`, `sync-comments-from-platforms`.

## Posting rules

- **Threads**: multiple items in `content` become a thread on X/Twitter, Threads, Bluesky, and Mastodon. On other platforms, extra items are ignored or posted per platform rules — prefer a single item unless the user wants a thread.
- **First comment**: to schedule a first comment (link-in-comment pattern), add a content item with `is_first_comment: true` and optional `first_comment_delay` (minutes, default 1). Only Instagram, Facebook, LinkedIn, and YouTube support this — for other platforms put the link in the main caption. Never use `is_first_comment` for X/Twitter threads.
- **Scheduling**: `schedule_type: "schedule"` requires `schedule_for`. With `publish_now`, the response status `IN_QUEUE` means it is publishing right now — not scheduled for later.
- **Repeat posting**: `repeatable: true` with `repeatable_times`, `repeatable_gap`, and `repeatable_gap_unit` (`minutes`–`months`); `repeatable_accounts` limits repeats to specific account IDs.
- **Targeting**: omit `accounts` to use the workspace default account; otherwise pass explicit account IDs from `list-accounts`. Respect workspace boundaries — an account ID belongs to one workspace.
- **Platform requirements**: TikTok, Instagram, and YouTube require video or image media; text-only posts fail there. Check the account's platform before composing.

## Finding posts

- `get-post` — by internal PostSyncer ID.
- `get-post-by-url` — by public permalink (e.g. a tweet URL).
- `get-post-by-platform-post-id` — by the platform-native post ID.
- `list-posts` — paginated (`per_page` 1–100, `page`); set `include_comments: true` to embed comment summaries.
- `analyze-twitter-post` — fetch any public X/Twitter URL, load replies, and answer a question about it with AI.

## Organization

- **Campaigns** — group posts: `list-campaigns`, `create-campaign`, `get-campaign`, `update-campaign`, `delete-campaign`.
- **Labels** — tag posts: `list-labels`, `create-label`, `get-label`, `update-label`, `delete-label`; attach via `labels` on `create-post`/`update-post`.
- **Media folders** — `list-folders`, `create-folder`, `get-folder`, `update-folder`, `delete-folder`; pass `folder_id` when uploading.
- **Post settings** — `update-post-auto-plug` (auto-promote a post when it hits a like threshold), `update-post-comment-moderation`, `update-post-contact-collection`.

## Safety

- Tools named `delete-*` and `hide-comment` are destructive or outward-facing — only call them when the user clearly asked.
- `create-post` with `publish_now` publishes to real social accounts immediately. When the user's intent is ambiguous, prefer `draft` or `schedule` and confirm before publishing.
- Always echo back what was created: platform(s), account(s), schedule time, and the post ID from the response.

## Example prompts this skill handles

- "Schedule a post to LinkedIn and X for tomorrow 9am announcing our new feature"
- "Upload these 3 product shots and draft an Instagram carousel with a first comment containing the link"
- "How did last week's posts perform across all workspaces?"
- "Repost my top-performing tweet every Monday for the next month"
- "Reply to new comments on yesterday's Facebook post"
