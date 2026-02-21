# Linear Actions

Connection key: `.linear`

## Issues

### List Issues
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_LIST_LINEAR_ISSUES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {}}' | jq
```

### Get Issue by ID
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_GET_LINEAR_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {"issue_id": "UUID"}}' | jq
```

### Search Issues
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_SEARCH_ISSUES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {"query": "search term"}}' | jq
```

### Create Issue
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_CREATE_LINEAR_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {
      "title": "Issue title",
      "description": "Description",
      "team_id": "TEAM_UUID",
      "priority": 2
    }
  }' | jq
```

Priority: 0=None, 1=Urgent, 2=High, 3=Medium, 4=Low

### Update Issue
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_UPDATE_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {
      "issue_id": "ISSUE_UUID",
      "state_id": "STATE_UUID",
      "assignee_id": "USER_UUID"
    }
  }' | jq
```

### Archive Issue
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_DELETE_LINEAR_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {"issue_id": "UUID"}}' | jq
```

## Teams & Users

### Get All Teams
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_GET_ALL_LINEAR_TEAMS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {}}' | jq
```

### List Users
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_LIST_LINEAR_USERS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {}}' | jq
```

### Get Current User
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_GET_CURRENT_USER" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {}}' | jq
```

## Workflow States

### List States
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_LIST_LINEAR_STATES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {}}' | jq
```

## Projects

### List Projects
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_LIST_LINEAR_PROJECTS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {}}' | jq
```

### Create Project
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_CREATE_LINEAR_PROJECT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"name": "Project Name", "team_ids": ["TEAM_UUID"]}
  }' | jq
```

## Comments

### Create Comment
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_CREATE_LINEAR_COMMENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"issue_id": "ISSUE_UUID", "body": "Comment text"}
  }' | jq
```

## GraphQL (Advanced)

Run any Linear GraphQL query:
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_RUN_QUERY_OR_MUTATION" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"query": "{ teams { nodes { id name key } } }"}
  }' | jq
```

## All Actions

| Action | Description |
|--------|-------------|
| LINEAR_LIST_LINEAR_ISSUES | List all issues |
| LINEAR_GET_LINEAR_ISSUE | Get issue by ID |
| LINEAR_CREATE_LINEAR_ISSUE | Create new issue |
| LINEAR_UPDATE_ISSUE | Update issue |
| LINEAR_DELETE_LINEAR_ISSUE | Archive issue |
| LINEAR_SEARCH_ISSUES | Search issues |
| LINEAR_GET_ALL_LINEAR_TEAMS | List teams |
| LINEAR_LIST_LINEAR_TEAMS | List teams with members |
| LINEAR_LIST_LINEAR_USERS | List users |
| LINEAR_GET_CURRENT_USER | Get authenticated user |
| LINEAR_LIST_LINEAR_STATES | Get workflow states |
| LINEAR_LIST_LINEAR_PROJECTS | List projects |
| LINEAR_GET_LINEAR_PROJECT | Get project |
| LINEAR_CREATE_LINEAR_PROJECT | Create project |
| LINEAR_UPDATE_LINEAR_PROJECT | Update project |
| LINEAR_CREATE_LINEAR_COMMENT | Add comment |
| LINEAR_UPDATE_LINEAR_COMMENT | Edit comment |
| LINEAR_LIST_LINEAR_LABELS | List labels |
| LINEAR_CREATE_LINEAR_LABEL | Create label |
| LINEAR_REMOVE_ISSUE_LABEL | Remove label |
| LINEAR_LIST_LINEAR_CYCLES | List cycles |
| LINEAR_GET_CYCLES_BY_TEAM_ID | Get team cycles |
| LINEAR_RUN_QUERY_OR_MUTATION | Execute GraphQL |
