# Composio Google Calendar Actions Reference

Full reference for all 46 Google Calendar actions via Composio.

## Table of Contents

1. [Event Management](#event-management)
2. [Event Retrieval](#event-retrieval)
3. [Calendar Management](#calendar-management)
4. [Access Control (ACL)](#access-control-acl)
5. [Scheduling & Availability](#scheduling--availability)
6. [Synchronization & Notifications](#synchronization--notifications)

---

## Event Management

### GOOGLECALENDAR_CREATE_EVENT

Creates calendar events with optional attendees, recurrence, and conferencing.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `start_datetime` | Yes | ISO 8601 | `YYYY-MM-DDTHH:MM:SS` |
| `event_duration_hour` | No | Integer | Hours component |
| `event_duration_minutes` | No | Integer | 0-59 ONLY |
| `summary` | No | String | Event title |
| `description` | No | String | Event description |
| `location` | No | String | Location text |
| `attendees` | No | Array | Email addresses |
| `timezone` | No | String | IANA identifier (e.g., "America/Los_Angeles") |
| `recurrence` | No | Array | RRULE/EXRULE/RDATE/EXDATE lines |
| `create_meeting_room` | No | Boolean | Default: true (adds Meet link) |
| `eventType` | No | String | "birthday" \| "default" \| "focusTime" \| "outOfOffice" \| "workingLocation" |
| `visibility` | No | String | "default" \| "public" \| "private" \| "confidential" |
| `send_updates` | No | Boolean | Default: true |
| `calendar_id` | No | String | Default: "primary" |

**Constraints:**
- Natural language dates ("tomorrow") are REJECTED
- `end_datetime` parameter does NOT exist - use duration fields

---

### GOOGLECALENDAR_PATCH_EVENT

Partial updates to existing events (only specified fields modified).

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `event_id` | Yes | String | Use FIND_EVENT to get this |
| `calendar_id` | Yes | String | "primary" or specific ID |
| `start_time` | No | RFC3339 | New start time |
| `end_time` | No | RFC3339 | New end time |
| `timezone` | No | String | IANA identifier |
| `summary` | No | String | New title |
| `description` | No | String | New description |
| `attendees` | No | Array | REPLACES entire list |
| `rsvp_response` | No | String | "needsAction" \| "declined" \| "tentative" \| "accepted" |
| `send_updates` | No | String | "all" \| "externalOnly" \| "none" |

**Note:** For recurring events, use format "baseId_YYYYMMDDTHHMMSSZ" for specific instances.

---

### GOOGLECALENDAR_UPDATE_EVENT

Full replacement PUT operation; unspecified fields may be cleared.

**Parameters:** Same as CREATE_EVENT plus mandatory `event_id`

**Warning:** This replaces the entire event - unspecified fields are cleared.

---

### GOOGLECALENDAR_DELETE_EVENT

Removes events (idempotent; returns 404 if not found).

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `event_id` | Yes | String | Base ID for all occurrences, or instance ID |
| `calendar_id` | No | String | Default: "primary" |

---

### GOOGLECALENDAR_QUICK_ADD

Natural language parsing for rapid event creation (limited features).

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `text` | Yes | String | Natural language description |
| `calendar_id` | No | String | Default: "primary" |
| `send_updates` | No | String | "all" \| "externalOnly" \| "none" |

**Limitations:** No attendee addition, no recurring events.

---

### GOOGLECALENDAR_REMOVE_ATTENDEE

Deletes single attendee from event.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `event_id` | Yes | String | Event identifier |
| `calendar_id` | No | String | Default: "primary" |
| `attendee_email` | Yes | String | Must match existing attendee |

---

## Event Retrieval

### GOOGLECALENDAR_FIND_EVENT

Comprehensive search combining text, time ranges, and modification filters.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `query` | No | String | Searches summary, description, location, attendees |
| `time_min` | No | String | RFC3339 or simple datetime |
| `time_max` | No | String | RFC3339 or simple datetime |
| `updated_min` | No | String | Filter by modification timestamp |
| `order_by` | No | String | "startTime" \| "updated" |
| `single_events` | No | Boolean | Default: false |
| `show_deleted` | No | Boolean | Default: false |
| `max_results` | No | Integer | 1-2500 |
| `calendar_id` | No | String | Default: "primary" |

---

### GOOGLECALENDAR_EVENTS_LIST

Lists events within specified time range.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `calendarId` | No | String | Default: "primary" |
| `timeMin` | No | RFC3339 | With mandatory timezone offset |
| `timeMax` | No | RFC3339 | With mandatory timezone offset |
| `q` | No | String | Free text search |
| `orderBy` | No | String | "startTime" (requires singleEvents=true) \| "updated" |
| `singleEvents` | No | Boolean | Expands recurring events |
| `eventTypes` | No | Array | Filter by event type |
| `maxResults` | No | Integer | 1-2500 (default: 250) |
| `showDeleted` | No | Boolean | Default: false |

**Timezone Warning:** UTC timestamps are interpreted in UTC regardless of calendar timezone.

---

### GOOGLECALENDAR_EVENTS_GET

Fetches single event by ID.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `event_id` | Yes | String | Specific event identifier |
| `calendar_id` | No | String | Default: "primary" |
| `time_zone` | No | String | Response formatting only |
| `max_attendees` | No | Integer | Positive integer |

---

### GOOGLECALENDAR_EVENTS_LIST_ALL_CALENDARS

Unified query across all user calendars.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `time_min` | Yes | RFC3339 | With timezone offset |
| `time_max` | Yes | RFC3339 | With timezone offset |
| `calendar_ids` | No | Array | Queries all if omitted |
| `single_events` | No | Boolean | Default: true |
| `max_results_per_calendar` | No | Integer | Per-calendar limit |

---

### GOOGLECALENDAR_EVENTS_INSTANCES

Returns individual occurrences of recurring events.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `eventId` | Yes | String | Recurring event base ID |
| `calendarId` | Yes | String | "primary" or specific |
| `timeMin` | No | RFC3339 | Filter start |
| `timeMax` | No | RFC3339 | Filter end |
| `maxResults` | No | Integer | 1-2500 (default: 250) |

---

## Calendar Management

### GOOGLECALENDAR_DUPLICATE_CALENDAR

Creates new empty calendar.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `summary` | Yes | String | Non-empty calendar name |

---

### GOOGLECALENDAR_GET_CALENDAR

Retrieves specific calendar metadata.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `calendar_id` | No | String | Default: "primary" |

---

### GOOGLECALENDAR_LIST_CALENDARS

Retrieves user's calendar list.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `max_results` | No | Integer | 1-250 |
| `show_hidden` | No | Boolean | Default: false |
| `show_deleted` | No | Boolean | Default: false |
| `min_access_role` | No | String | "freeBusyReader" \| "owner" \| "reader" \| "writer" |

---

### GOOGLECALENDAR_PATCH_CALENDAR

Partial calendar metadata update.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `calendar_id` | Yes | String | "primary" or specific ID |
| `summary` | No | String | Calendar name |
| `description` | No | String | Empty string clears it |
| `location` | No | String | Geographic location |
| `timezone` | No | String | IANA identifier |

---

### GOOGLECALENDAR_CALENDARS_DELETE

Removes secondary calendar (not primary).

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `calendar_id` | Yes | String | Secondary calendar only |

---

### GOOGLECALENDAR_CLEAR_CALENDAR

Deletes all events from primary calendar.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `calendar_id` | No | String | Default: "primary" |

---

## Scheduling & Availability

### GOOGLECALENDAR_FIND_FREE_SLOTS

Analyzes free/busy periods across calendars.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `items` | No | Array | Calendar IDs (default: ["primary"]) |
| `time_min` | No | String | Default: current timestamp |
| `time_max` | No | String | Default: end of time_min day |
| `timezone` | No | String | IANA identifier (default: UTC) |
| `calendar_expansion_max` | No | Integer | 1-50 |
| `group_expansion_max` | No | Integer | 1-100 |

**Returns:** Busy intervals + calculated free slot gaps

**Limit:** ~90 day span maximum.

---

### GOOGLECALENDAR_FREE_BUSY_QUERY

Low-level free/busy information query.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `items` | Yes | Array | Calendars (strings or {id: ...}) |
| `timeMin` | Yes | RFC3339 | Start time |
| `timeMax` | Yes | RFC3339 | End time |
| `timeZone` | No | String | Default: UTC |

---

## Access Control (ACL)

### GOOGLECALENDAR_ACL_INSERT

Creates sharing permission rule.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `calendar_id` | Yes | String | Calendar to share |
| `role` | Yes | String | "none" \| "freeBusyReader" \| "reader" \| "writer" \| "owner" |
| `scope` | Yes | Object | Recipient specification |
| `send_notifications` | No | Boolean | Default: true |

---

### GOOGLECALENDAR_LIST_ACL_RULES

Retrieves all ACL rules for calendar.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `calendar_id` | Yes | String | Calendar identifier |
| `max_results` | No | Integer | Default: 100 |
| `show_deleted` | No | Boolean | Default: false |

---

### GOOGLECALENDAR_ACL_DELETE

Removes ACL rule (revokes sharing).

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `calendar_id` | Yes | String | Calendar identifier |
| `rule_id` | Yes | String | Rule to delete |

---

## Synchronization & Notifications

### GOOGLECALENDAR_SYNC_EVENTS

Full or incremental event synchronization.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `calendar_id` | No | String | Default: "primary" |
| `sync_token` | No | String | For incremental sync |
| `event_types` | No | Array | Type filters |
| `single_events` | No | Boolean | Expand recurring |
| `max_results` | No | Integer | Limit |

---

### GOOGLECALENDAR_EVENTS_WATCH

Sets up webhook push notifications for event changes.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `id` | Yes | String | Channel UUID |
| `address` | Yes | String | HTTPS webhook URL |
| `type` | No | String | "web_hook" \| "webhook" |
| `calendarId` | Yes | String | Calendar to watch |

---

### GOOGLECALENDAR_CHANNELS_STOP

Terminates notification channel subscription.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `id` | Yes | String | Channel UUID |
| `resourceId` | Yes | String | Opaque resource identifier |

---

## Utility Actions

### GOOGLECALENDAR_GET_CURRENT_DATE_TIME

Returns current datetime in specified timezone.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `timezone` | No | String | IANA, abbreviation (PST/EST), or numeric offset |

---

### GOOGLECALENDAR_GET_CALENDAR_PROFILE

Retrieves primary calendar profile (timezone, settings).

**Parameters:** None

---

### GOOGLECALENDAR_COLORS_GET

Retrieves available color palette for calendars/events.

**Parameters:** None

---

### GOOGLECALENDAR_BATCH_EVENTS

Executes up to 1000 event mutations in single HTTP batch request.

**Parameters:**
| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| `operations` | Yes | Array | Batch operation objects (max 1000) |
| `fail_fast` | No | Boolean | Default: false |

---

## Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "API has not been used in project" | Calendar API not enabled | Enable in Cloud Console |
| "Error 400: invalid_scope" | Wrong scope format | Verify against Google OAuth docs |
| 401 errors | Expired token | Re-authenticate user |
| "App is blocked" | Unverified scopes | Use default scopes or create verified OAuth app |
| Events default to 30 minutes | Used `end_datetime` in CREATE | Use `event_duration_hour` + `event_duration_minutes` |
