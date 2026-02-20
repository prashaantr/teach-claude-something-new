---
name: memory
description: Use when saving decisions, tasks, facts, or anything to remember. Also use to recall past context. ALWAYS use Supabase API - NEVER write local files.
---

# Memory Skill

**⚠️ IMPORTANT: Memory is Supabase ONLY. NEVER write to local files.**
- ❌ DO NOT write to `~/.openclaw/workspace/memory/*.md`
- ❌ DO NOT create local memory files
- ✅ ALWAYS use Supabase curl commands below

Headers for all requests:
```
-H "apikey: $SUPABASE_KEY" -H "Authorization: Bearer $SUPABASE_KEY" -H "Content-Type: application/json"
```

## Write to Journal

Just write what happened:

```bash
curl -X POST "$SUPABASE_URL/rest/v1/journal" \
  -d '{"content":"...", "agent_id":"giuseppe"}'
```

Optional fields:
- `tags`: `["order", "instacart"]` - loose labels for filtering
- `status`: `"pending"` or `"done"` - for tracking
- `metadata`: `{"photo": "url"}` - any extra data

## Examples

```bash
# Something needs to happen
{"content": "Need milk and eggs from Instacart", "status": "pending", "tags": ["order"]}

# Update when done
{"content": "Groceries delivered", "tags": ["order"]}

# Meeting happened
{"content": "Standup with Andy - decided on projection mapping", "tags": ["meeting"]}

# Random note
{"content": "Andy's email is andy@example.com"}

# Task with photo
{"content": "Shelf assembled", "status": "done", "metadata": {"photo": "https://..."}}
```

## Query

```bash
# Recent entries
curl "$SUPABASE_URL/rest/v1/journal?agent_id=eq.giuseppe&order=created_at.desc&limit=20"

# Pending things
curl "$SUPABASE_URL/rest/v1/journal?agent_id=eq.giuseppe&status=eq.pending"

# Search content
curl "$SUPABASE_URL/rest/v1/journal?agent_id=eq.giuseppe&content=ilike.*instacart*"
```

## On Session Start

Load recent context:
```bash
curl "$SUPABASE_URL/rest/v1/journal?agent_id=eq.giuseppe&order=created_at.desc&limit=20"
```

That's it. Write what happened. Query when needed.
