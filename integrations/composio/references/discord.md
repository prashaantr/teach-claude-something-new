# Discord Cross-Channel Messaging

When you need to send Discord messages from another channel (Telegram, Slack, web).

**Native OpenClaw channel commands are SESSION-BOUND.** If you're on Telegram, you'll get "Cross-context messaging denied" trying to use native Discord send.

Use direct Discord API instead:

## Send Message

```bash
curl -X POST "https://discord.com/api/v10/channels/CHANNEL_ID/messages" \
  -H "Authorization: Bot $DISCORD_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"content": "<@USER_ID> your message"}'
```

## Find Channel ID

```bash
# List guild channels
curl "https://discord.com/api/v10/guilds/GUILD_ID/channels" \
  -H "Authorization: Bot $DISCORD_BOT_TOKEN" | jq '.[] | {id, name}'
```

## Find User ID

```bash
# List guild members
curl "https://discord.com/api/v10/guilds/GUILD_ID/members?limit=100" \
  -H "Authorization: Bot $DISCORD_BOT_TOKEN" | jq '.[] | {user_id: .user.id, username: .user.username}'
```

## Mention Format

| Format | Result |
|--------|--------|
| `<@USER_ID>` | User notified |
| `@Name` | No notification |

## When on Discord Natively

If you're already in a Discord session (message came from Discord), use OpenClaw's native channel - it's simpler.

Only use direct API for **cross-channel** scenarios (Telegram → Discord, etc).
