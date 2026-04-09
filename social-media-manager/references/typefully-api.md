# Typefully API Reference

Complete command reference for Typefully CLI.

## Table of Contents

- [Setup](#setup)
- [Social Sets](#social-sets)
- [Drafts](#drafts)
- [Scheduling](#scheduling)
- [Media](#media)
- [Analytics](#analytics)
- [Queue](#queue)
- [Tags](#tags)
- [LinkedIn](#linkedin)

## Setup

```bash
# Interactive setup
setup

# Non-interactive
setup --key <api_key> --location global

# With default social set
setup --key <api_key> --default-social-set <id>

# Show config
config:show

# Set default social set
config:set-default [social_set_id]
```

## Social Sets

A "social set" is an account containing connected platforms.

```bash
# List all social sets
social-sets:list

# Get details (shows connected platforms)
social-sets:get <id>

# Get current user
me:get
```

## Drafts

### Creating Drafts

```bash
# Basic draft (uses default platform)
drafts:create --text "Your post"

# Specific platform
drafts:create --platform x --text "Tweet"
drafts:create --platform linkedin --text "LinkedIn post"

# Multiple platforms (same content)
drafts:create --platform x,linkedin --text "Cross-post"

# All connected platforms
drafts:create --all --text "Everywhere!"

# With explicit social set
drafts:create <social_set_id> --text "..."

# Thread (use --- separator)
drafts:create --platform x --text "First tweet

---

Second tweet

---

Third tweet"

# With media
drafts:create --text "Check this!" --media <media_id>
drafts:create --text "Multiple!" --media id1,id2

# Reply to existing post
drafts:create --platform x --text "Reply" --reply-to "https://x.com/user/status/123"

# Quote post
drafts:create --platform x --text "My take" --quote-post-url "https://x.com/user/status/123"

# With tags
drafts:create --text "..." --tags marketing,product

# With scratchpad notes (internal, not published)
drafts:create --text "..." --scratchpad "Notes for later"

# Generate share URL
drafts:create --text "..." --share

# Post to X community
drafts:create --platform x --text "..." --community <community_id>

# From file
drafts:create --file ./post.txt
```

### Managing Drafts

```bash
# List drafts
drafts:list
drafts:list --status draft
drafts:list --status scheduled
drafts:list --status published
drafts:list --sort created_at
drafts:list --sort -created_at  # descending
drafts:list --sort scheduled_date

# Get specific draft
drafts:get <draft_id> --use-default

# Update draft
drafts:update <draft_id> --text "New text" --use-default
drafts:update <draft_id> --tags "new,tags" --use-default
drafts:update <draft_id> --scratchpad "Updated notes" --use-default

# Append to thread
drafts:update <draft_id> --append --text "New tweet in thread" --use-default

# Add platform to existing draft (different content per platform)
drafts:update <draft_id> --platform x --text "X version" --use-default

# Delete draft
drafts:delete <draft_id> --use-default
```

## Scheduling

```bash
# Schedule for specific time (ISO 8601)
drafts:create --text "..." --schedule "2026-04-10T09:00:00Z"

# Schedule to next free slot
drafts:create --text "..." --schedule next-free-slot

# Schedule existing draft
drafts:schedule <draft_id> --time next-free-slot --use-default
drafts:schedule <draft_id> --time "2026-04-10T09:00:00Z" --use-default

# Publish immediately
drafts:publish <draft_id> --use-default
```

## Media

```bash
# Upload (waits for processing)
media:upload ./image.jpg
media:upload ./video.mp4

# Upload without waiting
media:upload ./image.jpg --no-wait

# Custom timeout
media:upload ./large-video.mp4 --timeout 120

# Check status
media:status <media_id>
```

Supported: Images (JPG, PNG, GIF), Videos (MP4), PDFs

## Analytics

X analytics only (currently).

```bash
# Posts in date range
analytics:posts:list --start-date 2026-04-01 --end-date 2026-04-07

# Include replies
analytics:posts:list --start-date 2026-04-01 --end-date 2026-04-07 --include-replies

# Paginate
analytics:posts:list --start-date 2026-04-01 --end-date 2026-04-30 --limit 100 --offset 100
```

Returns: impressions, likes, comments, shares, quotes, saves, profile_clicks, link_clicks

## Queue

```bash
# Get queue timeline
queue:get --start-date 2026-04-01 --end-date 2026-04-30

# Get schedule rules
queue:schedule:get

# Set schedule rules
queue:schedule:put --rules '[{"h":9,"m":30,"days":["mon","wed","fri"]}]'
```

## Tags

```bash
# List tags
tags:list

# Create tag
tags:create --name "Marketing"
```

Tags are scoped per social set.

## LinkedIn

### Mentions

```bash
# Resolve company URL to mention syntax
linkedin:organizations:resolve --organization-url "https://www.linkedin.com/company/anthropic/"
# Returns: {"mention_text": "@[Anthropic](urn:li:organization:123456)", ...}

# Use in post
drafts:create --platform linkedin --text "Thanks @[Anthropic](urn:li:organization:123456)!"
```

### Character Limit

LinkedIn posts: 3000 characters

## Draft URL Structure

```
https://typefully.com/?a=<social_set_id>&d=<draft_id>
```

## Error Handling

| Status | Meaning |
|--------|---------|
| 400 | Bad request (check parameters) |
| 401 | Invalid API key |
| 403 | Forbidden |
| 404 | Draft/resource not found |
| 429 | Rate limited |

## Platform Constraints

- X: 280 chars, direct URL publishing blocked by X policy
- LinkedIn: 3000 chars
- Threads: 500 chars
- Bluesky: 300 chars
- Mastodon: 500 chars
