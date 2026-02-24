---
name: discord
description: Discord bot development and CLI operations. Use when building Discord bots, managing servers, or working with Discord API directly. For Composio-based Discord messaging and bot-to-bot communication, see composio skill references/discord.md.
---

# Discord

## Discord CLI (discord-cli)

```bash
# Install
npm install -g discord-cli

# Login
discord login

# Send message
discord send --channel <channel_id> "Hello world"

# List servers
discord servers

# List channels
discord channels --server <server_id>
```

## Discord.js Bot Development

```javascript
const { Client, GatewayIntentBits } = require('discord.js');

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ]
});

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.on('messageCreate', message => {
  if (message.content === '!ping') {
    message.reply('Pong!');
  }
});

client.login(process.env.DISCORD_BOT_TOKEN);
```

## Mention Formats

```
<@USER_ID>      → User mention
<@&ROLE_ID>     → Role mention
<#CHANNEL_ID>   → Channel mention
```

## Bot Permissions

Common permission flags:
- `SendMessages` - Send messages in channels
- `ReadMessageHistory` - Read message history
- `MentionEveryone` - Mention @everyone/@here
- `ManageMessages` - Delete/pin messages

## See Also

For Composio-based Discord operations (bot-to-bot messaging, agent directory):
→ See `composio` skill `references/discord.md`
