# Gmail Actions Reference

## Contents

- [Messages](#messages)
- [Labels](#labels)
- [Drafts](#drafts)
- [All Actions](#all-actions)

## Setup

```bash
CONNECTION_ID=$(echo $COMPOSIO_CONNECTIONS | jq -r '.gmail')
```

**Required fields for all requests:**
- `connected_account_id`: from `$COMPOSIO_CONNECTIONS`
- `entity_id`: from `$COMPOSIO_USER_ID`
- `arguments`: action-specific parameters

## Messages

### Send Email (WITH AGENT TAG)
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GMAIL_SEND_EMAIL" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "to": "recipient@example.com",
      "subject": "Subject line",
      "body": "Email body text\n\n--\nSent by '"$AGENT_NAME"'"
    }
  }' | jq
```

### Send Email with CC/BCC
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GMAIL_SEND_EMAIL" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "to": "recipient@example.com",
      "cc": "cc@example.com",
      "bcc": "bcc@example.com",
      "subject": "Subject",
      "body": "Body\n\n--\nSent by '"$AGENT_NAME"'"
    }
  }' | jq
```

### List Messages
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GMAIL_LIST_MESSAGES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"max_results": 10}
  }' | jq
```

### Search Messages
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GMAIL_LIST_MESSAGES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"query": "from:someone@example.com", "max_results": 10}
  }' | jq
```

Query syntax: `from:`, `to:`, `subject:`, `is:unread`, `after:2024/01/01`

### Get Message
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GMAIL_GET_MESSAGE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"message_id": "MESSAGE_ID"}
  }' | jq
```

### Reply to Message (WITH AGENT TAG)
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GMAIL_REPLY_TO_MESSAGE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "message_id": "MESSAGE_ID",
      "body": "Reply text\n\n--\nSent by '"$AGENT_NAME"'"
    }
  }' | jq
```

## Labels

### List Labels
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GMAIL_LIST_LABELS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {}
  }' | jq
```

### Add Label to Message
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GMAIL_MODIFY_MESSAGE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "message_id": "MESSAGE_ID",
      "add_label_ids": ["LABEL_ID"]
    }
  }' | jq
```

## Drafts

### Create Draft
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GMAIL_CREATE_DRAFT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "to": "recipient@example.com",
      "subject": "Draft subject",
      "body": "Draft body"
    }
  }' | jq
```

## All Actions

| Action | Description |
|--------|-------------|
| GMAIL_SEND_EMAIL | Send email |
| GMAIL_LIST_MESSAGES | List inbox messages |
| GMAIL_GET_MESSAGE | Get message by ID |
| GMAIL_REPLY_TO_MESSAGE | Reply to message |
| GMAIL_CREATE_DRAFT | Create draft |
| GMAIL_LIST_LABELS | List all labels |
| GMAIL_MODIFY_MESSAGE | Add/remove labels |
| GMAIL_TRASH_MESSAGE | Move to trash |
| GMAIL_DELETE_MESSAGE | Permanently delete |
