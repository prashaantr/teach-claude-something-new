# Discord Actions (Composio)

Connection key: `.discord`

## Contents

- [Setup](#setup)
- [Guilds & Channels](#guilds--channels)
- [Messages](#messages)
- [Members](#members)
- [Mention Format](#mention-format)
- [All Actions](#all-actions)

## Setup

```bash
CONNECTION_ID=$(echo $COMPOSIO_CONNECTIONS | jq -r '.discord')
```

## Guilds & Channels

### List Guild Channels
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/DISCORD_GET_GUILD_CHANNELS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {"guild_id": "GUILD_ID"}}' | jq
```

### Get Guild Info
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/DISCORD_GET_GUILD" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {"guild_id": "GUILD_ID"}}' | jq
```

## Messages

### Send Message
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/DISCORD_SEND_MESSAGE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "channel_id": "CHANNEL_ID",
      "content": "<@USER_ID> your message"
    }
  }' | jq
```

### Get Channel Messages
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/DISCORD_GET_CHANNEL_MESSAGES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {"channel_id": "CHANNEL_ID"}}' | jq
```

## Members

### List Guild Members
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/DISCORD_LIST_GUILD_MEMBERS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {"guild_id": "GUILD_ID"}}' | jq
```

Use this to find user IDs by username.

## Mention Format

| Format | Result |
|--------|--------|
| `<@USER_ID>` | User notified |
| `@Name` | No notification |

Plain text `@Name` does NOT work. Extract numeric user_id from guild members list.

## All Actions

| Action | Description |
|--------|-------------|
| DISCORD_SEND_MESSAGE | Send message to channel |
| DISCORD_GET_CHANNEL_MESSAGES | Get messages from channel |
| DISCORD_GET_GUILD_CHANNELS | List channels in guild |
| DISCORD_GET_GUILD | Get guild info |
| DISCORD_LIST_GUILD_MEMBERS | List members (to find user IDs) |
