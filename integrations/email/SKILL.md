---
name: email
description: |
  Read, send, and respond to emails via Himalaya CLI. Use when:
  (1) New email notification arrives (triggered automatically)
  (2) Need to send an email to someone
  (3) Need to check inbox or find past emails
  (4) Responding to or acknowledging received emails
---

# Email

Account: `$GMAIL_ADDRESS` (from environment)

## Agent Identification

**CRITICAL**: All outgoing emails MUST include the agent signature footer:

```
--
Sent by $AGENT_NAME
```

This ensures traceability across multiple agents sharing the same email account.

## Commands

```bash
# List emails
himalaya envelope list

# Read email
himalaya message read <ID>

# Send email (ALWAYS include agent signature)
himalaya message send << EOF
From: $AGENT_NAME <$GMAIL_ADDRESS>
To: recipient@example.com
Subject: Your subject

Your message here.

--
Sent by $AGENT_NAME
EOF
```

## Response Policy

When triggered with a new email:

1. Read it: `himalaya message read <ID>`
2. Check memory for duplicate handling (search `email:<ID>`)
3. Decide action:
   - `reply` — question asked, action requested, confirmation expected
   - `ack` — quick "got it, will follow up"
   - `no_reply` — newsletters, automated alerts, spam
4. Send reply if needed (**include agent signature**)
5. Log to memory:
   ```bash
   curl -X POST "$SUPABASE_URL/rest/v1/agent_memories" \
     -H "apikey: $SUPABASE_ANON_KEY" \
     -H "x-agent-key: $AGENT_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "agent_id": "'"$AGENT_ID"'",
       "key": "email:'"$EMAIL_ID"'",
       "value": "FROM: <sender> | ACTION: <action> | SUMMARY: <brief>",
       "memory_type": "interaction",
       "source": "email"
     }'
   ```

## Rules

- **Write in plain text** — No markdown, no formatting symbols. Gmail doesn't render markdown.
- **Always include agent signature** — Never send without the `Sent by $AGENT_NAME` footer
- Prefer short, direct replies
- If promising action, include a specific time
- Never ignore human emails silently (unless spam)

## Example: Full Send with Signature

```bash
himalaya message send << EOF
From: $AGENT_NAME <$GMAIL_ADDRESS>
To: john@example.com
Subject: Re: Project timeline question

Hi John,

The project deadline is March 15th as we discussed.

Let me know if you need any other details.

--
Sent by $AGENT_NAME
EOF
```
