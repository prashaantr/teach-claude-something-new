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

Account: `hey.giuseppe.bellini@gmail.com`

## Commands

```bash
# List emails
himalaya envelope list

# Read email
himalaya message read <ID>

# Send email
himalaya message send << EOF
From: Giuseppe <hey.giuseppe.bellini@gmail.com>
To: recipient@example.com
Subject: Your subject

Your message here.
EOF
```

## Response Policy

When triggered with a new email:

1. Read it: `himalaya message read <ID>`
2. Check journal for duplicate handling (search `EMAIL_ID: <ID>`)
3. Decide action:
   - `reply` — question asked, action requested, confirmation expected
   - `ack` — quick "got it, will follow up"
   - `no_reply` — newsletters, automated alerts, spam
4. Send reply if needed
5. Log to journal: `EMAIL_ID: <ID> | FROM: <sender> | ACTION: <action> | SUMMARY: <brief>`

## Rules

- **Write in plain text** — No markdown, no formatting symbols. Gmail doesn't render markdown.
- Prefer short, direct replies
- If promising action, include a specific time
- Never ignore human emails silently (unless spam)
