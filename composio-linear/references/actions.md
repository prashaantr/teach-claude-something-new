# Linear Actions Reference

## Contents

- [Teams & Users](#teams--users)
- [Issues](#issues)
- [Workflow States](#workflow-states)
- [Projects](#projects)
- [Comments](#comments)
- [GraphQL (Advanced)](#graphql-advanced)
- [All Actions](#all-actions)

## Setup

```bash
CONNECTION_ID=$(echo $COMPOSIO_CONNECTIONS | jq -r '.linear')
```

**Required fields for all requests:**
- `connected_account_id`: from `$COMPOSIO_CONNECTIONS`
- `entity_id`: from `$COMPOSIO_USER_ID`
- `arguments`: action-specific parameters

## Teams & Users

### Get All Teams
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_GET_ALL_LINEAR_TEAMS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {}}' | jq
```

### List Users
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_LIST_LINEAR_USERS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {}}' | jq
```

### Get Current User
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_GET_CURRENT_USER" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {}}' | jq
```

## Issues

### List Issues
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_LIST_LINEAR_ISSUES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {}}' | jq
```

### Get Issue by ID
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_GET_LINEAR_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {"issue_id": "UUID"}}' | jq
```

### Search Issues
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_SEARCH_ISSUES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {"query": "search term"}}' | jq
```

### Create Issue
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_CREATE_LINEAR_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
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
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "issue_id": "ISSUE_UUID",
      "state_id": "STATE_UUID"
    }
  }' | jq
```

### Archive Issue
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_DELETE_LINEAR_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {"issue_id": "UUID"}}' | jq
```

## Workflow States

### List States
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_LIST_LINEAR_STATES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {}}' | jq
```

## Projects

### List Projects
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_LIST_LINEAR_PROJECTS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {}}' | jq
```

### Create Project
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_CREATE_LINEAR_PROJECT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"name": "Project Name", "team_ids": ["TEAM_UUID"]}
  }' | jq
```

## Comments

### Create Comment
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_CREATE_LINEAR_COMMENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"issue_id": "ISSUE_UUID", "body": "Comment text"}
  }' | jq
```

## GraphQL (Advanced)

Use `LINEAR_RUN_QUERY_OR_MUTATION` for operations not covered by standard actions.

**CRITICAL**: Arguments must use these exact field names:
- `query_or_mutation`: The GraphQL query or mutation string (NOT `query`)
- `variables`: Variables object (required, use `{}` if none)

### Query Example
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_RUN_QUERY_OR_MUTATION" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "query_or_mutation": "{ teams { nodes { id name key } } }",
      "variables": {}
    }
  }' | jq
```

### Get Labels (needed for filtering)
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_RUN_QUERY_OR_MUTATION" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "query_or_mutation": "{ issueLabels { nodes { id name color } } }",
      "variables": {}
    }
  }' | jq
```

### Create Custom View (filter by label)
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_RUN_QUERY_OR_MUTATION" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "query_or_mutation": "mutation CreateView($input: CustomViewCreateInput!) { customViewCreate(input: $input) { success customView { id name } } }",
      "variables": {
        "input": {
          "name": "Opalite Issues",
          "filterData": {
            "filters": [{"label": {"id": {"in": ["LABEL_UUID_HERE"]}}}]
          }
        }
      }
    }
  }' | jq
```

### List Custom Views
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_RUN_QUERY_OR_MUTATION" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "query_or_mutation": "{ customViews { nodes { id name filterData } } }",
      "variables": {}
    }
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
| LINEAR_LIST_LINEAR_USERS | List users |
| LINEAR_GET_CURRENT_USER | Get authenticated user |
| LINEAR_LIST_LINEAR_STATES | Get workflow states |
| LINEAR_LIST_LINEAR_PROJECTS | List projects |
| LINEAR_CREATE_LINEAR_PROJECT | Create project |
| LINEAR_CREATE_LINEAR_COMMENT | Add comment |
| LINEAR_RUN_QUERY_OR_MUTATION | Execute GraphQL |
