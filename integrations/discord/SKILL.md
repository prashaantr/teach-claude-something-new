---
name: discord
description: Discord bot messaging and multi-agent communication. Use when: (1) Sending messages to Discord channels, (2) Mentioning other bots or users, (3) Bot-to-bot conversations, (4) Replying to Discord messages. Critical for proper mention format to ensure bots receive notifications.
---

# Discord Bot Communication

## Mention Format (CRITICAL)

```
CORRECT: <@USER_ID>     → User mention (works for bots)
WRONG:   <@&ID>         → Role mention (NOT for users/bots)
WRONG:   @Name          → Plain text (no notification)
```

## Known Agents

| Agent | Discord User ID | Mention Format |
|-------|-----------------|----------------|
| Opal/Opalite | 1474918306535309322 | `<@1474918306535309322>` |
| Alan Turing | 1475051850297376882 | `<@1475051850297376882>` |

## Replying to Another Bot

1. Extract sender's user ID from incoming message metadata
2. Use `<@their_user_id>` in your reply (NO `&` symbol)
3. Or use known agent IDs above

Without proper `<@ID>` mentions, bots won't see your response.

## Composio Discord Actions

### Send Message

```bash
curl -X POST "https://backend.composio.dev/api/v2/actions/DISCORD_SEND_MESSAGE/execute" \
  -H "X-API-KEY: $COMPOSIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connectedAccountId": "'$DISCORD_CONNECTION_ID'",
    "input": {
      "channel_id": "CHANNEL_ID",
      "content": "Hello <@1475051850297376882>!"
    }
  }'
```

### Get Guild Members (to find user IDs)

```bash
curl -X POST "https://backend.composio.dev/api/v2/actions/DISCORD_LIST_GUILD_MEMBERS/execute" \
  -H "X-API-KEY: $COMPOSIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connectedAccountId": "'$DISCORD_CONNECTION_ID'",
    "input": {
      "guild_id": "GUILD_ID"
    }
  }'
```

## Config Requirements

For bot-to-bot communication, ensure OpenClaw config has:

```json
{
  "channels": {
    "discord": {
      "allowBots": true,
      "requireMention": true
    }
  }
}
```

- `allowBots: true` - Required to receive messages from other bots
- `requireMention: true` - Bot only responds when properly mentioned with `<@ID>`
