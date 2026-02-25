# Google Calendar Actions (Composio)

Connection key: `.googlecalendar`

## Setup

```bash
CONNECTION_ID=$(echo $COMPOSIO_CONNECTIONS | jq -r '.googlecalendar')
```

## Create Event

```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLECALENDAR_CREATE_EVENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "summary": "Meeting title",
      "start_datetime": "2026-02-25T10:00:00Z",
      "end_datetime": "2026-02-25T11:00:00Z",
      "description": "Meeting description",
      "attendees": ["email@example.com"]
    }
  }' | jq
```

## Find Events

```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLECALENDAR_FIND_EVENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "query": "search term",
      "time_min": "2026-02-24T00:00:00Z",
      "time_max": "2026-02-28T00:00:00Z"
    }
  }' | jq
```

## Check Free/Busy

```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLECALENDAR_FREE_BUSY" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "time_min": "2026-02-24T00:00:00Z",
      "time_max": "2026-02-28T00:00:00Z"
    }
  }' | jq
```

## All Actions

| Action | Description |
|--------|-------------|
| GOOGLECALENDAR_CREATE_EVENT | Create calendar event |
| GOOGLECALENDAR_FIND_EVENT | Search events |
| GOOGLECALENDAR_FREE_BUSY | Check availability |
| GOOGLECALENDAR_DELETE_EVENT | Delete event |
| GOOGLECALENDAR_UPDATE_EVENT | Update event |
