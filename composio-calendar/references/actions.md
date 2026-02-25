# Google Calendar Actions Reference

## Contents

- [Create Event](#create-event)
- [Find Events](#find-events)
- [Update Event](#update-event)
- [Delete Event](#delete-event)
- [Free/Busy](#freebusy)
- [All Actions](#all-actions)

## Setup

```bash
CONNECTION_ID=$(echo $COMPOSIO_CONNECTIONS | jq -r '.googlecalendar')
```

**Required fields for all requests:**
- `connected_account_id`: from `$COMPOSIO_CONNECTIONS`
- `entity_id`: from `$COMPOSIO_USER_ID`
- `arguments`: action-specific parameters

## Create Event

**IMPORTANT:** Use `event_duration_hour` + `event_duration_minutes`, NOT `end_datetime`!

```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLECALENDAR_CREATE_EVENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "title": "Meeting title",
      "start_datetime": "2026-02-25T10:00:00",
      "event_duration_hour": 1,
      "event_duration_minutes": 0,
      "timezone": "America/Los_Angeles",
      "description": "Meeting description",
      "attendees": ["email@example.com"],
      "calendar_id": "primary"
    }
  }' | jq
```

**Parameters:**
- `title` (required): Event title
- `start_datetime` (required): ISO 8601 format
- `event_duration_hour`: Hours (0+)
- `event_duration_minutes`: Minutes (0-59 ONLY, never 60+)
- `timezone`: IANA timezone (default: UTC)
- `calendar_id`: Calendar ID (default: "primary")
- `description`: Event description
- `attendees`: Array of email addresses
- `create_meeting_room`: Add Google Meet link (default: true)

## Find Events

```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLECALENDAR_FIND_EVENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "text_query": "search term",
      "time_min": "2026-02-24T00:00:00Z",
      "time_max": "2026-02-28T00:00:00Z",
      "calendar_id": "primary"
    }
  }' | jq
```

## Update Event

**IMPORTANT:** Use `end_datetime` to change duration, NOT `event_duration_*`!

### PATCH (Partial Update - Preferred)
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLECALENDAR_PATCH_EVENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "event_id": "EVENT_ID",
      "calendar_id": "primary",
      "end_datetime": "2026-02-24T11:00:00"
    }
  }' | jq
```

### UPDATE (Full Replacement)
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLECALENDAR_UPDATE_EVENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "event_id": "EVENT_ID",
      "calendar_id": "primary",
      "title": "Updated title",
      "start_datetime": "2026-02-24T09:00:00",
      "end_datetime": "2026-02-24T11:00:00"
    }
  }' | jq
```

**Note:** UPDATE replaces the entire event. Unspecified fields may be cleared.

## Delete Event

```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLECALENDAR_DELETE_EVENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "event_id": "EVENT_ID",
      "calendar_id": "primary"
    }
  }' | jq
```

## Free/Busy

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
| GOOGLECALENDAR_CREATE_EVENT | Create calendar event (use duration params) |
| GOOGLECALENDAR_FIND_EVENT | Search events |
| GOOGLECALENDAR_FREE_BUSY | Check availability |
| GOOGLECALENDAR_DELETE_EVENT | Delete event |
| GOOGLECALENDAR_UPDATE_EVENT | Full event replacement (use end_datetime) |
| GOOGLECALENDAR_PATCH_EVENT | Partial event update (use end_datetime) |
