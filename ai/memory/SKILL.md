---
name: memory
description: |
  Persistent memory via Supabase for logging interactions, facts, preferences, and tasks.
  Use when: (1) Starting a session - load recent context, (2) After any interaction - log it,
  (3) Learning new information - store as fact, (4) Tracking tasks - record status,
  (5) Recalling past conversations - search memories. CRITICAL: Log EVERY interaction.
---

# Memory

Persistent memory stored in Supabase. **Log every interaction** to build context over time.

## Environment Variables

These are available to you:
- `SUPABASE_URL` - Your Supabase project URL
- `SUPABASE_ANON_KEY` - Supabase anon key for auth
- `AGENT_API_KEY` - Your unique API key (pass as `x-agent-key` header)
- `AGENT_ID` - Your agent UUID

## Memory Table Schema

```sql
agent_memories (
  id UUID,
  agent_id UUID,
  key TEXT,           -- Unique identifier for this memory
  value TEXT,         -- The actual content (plain text, greppable)
  memory_type TEXT,   -- 'interaction', 'fact', 'preference', 'task', 'general'
  source TEXT,        -- Where it came from: 'telegram', 'email', 'api'
  tags TEXT[],        -- Array of tags for filtering
  created_at TIMESTAMPTZ,
  updated_at TIMESTAMPTZ
)
```

## CRITICAL: Log Every Interaction

For EVERY message you receive or send, log it immediately:

```bash
# Log an incoming message
curl -X POST "$SUPABASE_URL/rest/v1/agent_memories" \
  -H "apikey: $SUPABASE_ANON_KEY" \
  -H "Authorization: Bearer $SUPABASE_ANON_KEY" \
  -H "x-agent-key: $AGENT_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=minimal" \
  -d '{
    "agent_id": "'"$AGENT_ID"'",
    "key": "interaction:'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'",
    "value": "User John asked about project deadlines. I responded with the Q2 timeline.",
    "memory_type": "interaction",
    "source": "telegram",
    "tags": ["user:john", "project:alpha"]
  }'
```

## What to Log

### 1. Interactions (memory_type: 'interaction')
Log every conversation exchange:
- Who said what
- What you responded
- The outcome

Key format: `interaction:<timestamp>`

### 2. Facts (memory_type: 'fact')
When you learn something new, store it:
- User preferences
- Project details
- Important dates
- Technical decisions

Key format: `fact:<topic>:<subtopic>` (e.g., `fact:user:john:timezone`)

### 3. Preferences (memory_type: 'preference')
User communication preferences:
- Preferred times to contact
- Communication style
- Topics they care about

Key format: `preference:<user>:<type>`

### 4. Tasks (memory_type: 'task')
Track ongoing work:
- What was requested
- Current status
- Blockers

Key format: `task:<task_id>` or `task:<description_slug>`

## Reading Your Memory

### Get all recent memories
```bash
curl -X GET "$SUPABASE_URL/rest/v1/agent_memories?agent_id=eq.$AGENT_ID&order=created_at.desc&limit=50" \
  -H "apikey: $SUPABASE_ANON_KEY" \
  -H "Authorization: Bearer $SUPABASE_ANON_KEY" \
  -H "x-agent-key: $AGENT_API_KEY"
```

### Search memories (full-text)
```bash
curl -X POST "$SUPABASE_URL/rest/v1/rpc/search_memories" \
  -H "apikey: $SUPABASE_ANON_KEY" \
  -H "Authorization: Bearer $SUPABASE_ANON_KEY" \
  -H "x-agent-key: $AGENT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_query": "project deadline", "filter_type": "fact"}'
```

### Get memories by type
```bash
curl -X GET "$SUPABASE_URL/rest/v1/agent_memories?agent_id=eq.$AGENT_ID&memory_type=eq.fact" \
  -H "apikey: $SUPABASE_ANON_KEY" \
  -H "Authorization: Bearer $SUPABASE_ANON_KEY" \
  -H "x-agent-key: $AGENT_API_KEY"
```

### Get memories by tag
```bash
curl -X GET "$SUPABASE_URL/rest/v1/agent_memories?agent_id=eq.$AGENT_ID&tags=cs.{user:john}" \
  -H "apikey: $SUPABASE_ANON_KEY" \
  -H "Authorization: Bearer $SUPABASE_ANON_KEY" \
  -H "x-agent-key: $AGENT_API_KEY"
```

## Updating Memories

Update a fact when it changes (upsert by key):
```bash
curl -X POST "$SUPABASE_URL/rest/v1/agent_memories" \
  -H "apikey: $SUPABASE_ANON_KEY" \
  -H "Authorization: Bearer $SUPABASE_ANON_KEY" \
  -H "x-agent-key: $AGENT_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Prefer: resolution=merge-duplicates" \
  -d '{
    "agent_id": "'"$AGENT_ID"'",
    "key": "fact:user:john:location",
    "value": "John now lives in Berlin (moved from Stockholm in Feb 2024)",
    "memory_type": "fact",
    "tags": ["user:john", "location"]
  }'
```

## Session Workflow

### On Session Start
1. Load recent interactions to restore context
2. Check for any pending tasks
3. Review relevant facts for current user

### During Conversation
1. **Before responding**: Check if you have relevant memories
2. **After each exchange**: Log the interaction immediately
3. **When learning new info**: Store it as a fact

### On Session End
1. Summarize the session if significant
2. Update any task statuses
3. Store any deferred items

## Example: Full Interaction Flow

```bash
# 1. User sends message via Telegram
# 2. Before responding, check relevant memories:
curl -X POST "$SUPABASE_URL/rest/v1/rpc/search_memories" \
  -H "apikey: $SUPABASE_ANON_KEY" \
  -H "x-agent-key: $AGENT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_query": "project alpha deadline"}'

# 3. Formulate response using context
# 4. Send response to user
# 5. Log the interaction:
curl -X POST "$SUPABASE_URL/rest/v1/agent_memories" \
  -H "apikey: $SUPABASE_ANON_KEY" \
  -H "x-agent-key: $AGENT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "'"$AGENT_ID"'",
    "key": "interaction:2024-02-21T15:30:00Z",
    "value": "John asked: When is the alpha release? I responded: Based on our last discussion, alpha release is scheduled for March 15th. He confirmed this works for his team.",
    "memory_type": "interaction",
    "source": "telegram",
    "tags": ["user:john", "project:alpha", "release"]
  }'

# 6. If a new fact was learned, store it:
curl -X POST "$SUPABASE_URL/rest/v1/agent_memories" \
  -H "apikey: $SUPABASE_ANON_KEY" \
  -H "x-agent-key: $AGENT_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Prefer: resolution=merge-duplicates" \
  -d '{
    "agent_id": "'"$AGENT_ID"'",
    "key": "fact:project:alpha:team_confirmation",
    "value": "John confirmed March 15 alpha release works for his team (confirmed 2024-02-21)",
    "memory_type": "fact",
    "tags": ["project:alpha", "user:john", "confirmed"]
  }'
```

## Memory Hygiene

- Use descriptive, searchable keys
- Include timestamps in interaction keys
- Tag liberally for easy filtering
- Update facts rather than creating duplicates
- Summarize long conversations periodically
