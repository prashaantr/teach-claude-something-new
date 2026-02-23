---
name: composio
description: |
  Execute actions on connected services via Composio API. Use when:
  (1) Working with Linear - list/create/update issues, get teams, search
  (2) Working with GitHub - list/create issues, manage PRs, repos
  (3) Working with Gmail - send/list emails
  (4) Working with Google Drive - list/upload/download files
  Composio handles OAuth automatically. Check COMPOSIO_CONNECTIONS to see which services are connected.
---

# Composio

Execute actions on Linear, GitHub, Gmail, and Google Drive via Composio's API.

> **⚠️ CRITICAL: NEVER USE CLI TOOLS FOR THESE SERVICES**
>
> You MUST use the Composio HTTP API (curl commands below) for ALL operations.
> **DO NOT** use:
> - `gh` (GitHub CLI) - will fail with "gh auth login" error
> - `linear` CLI
> - `gcloud` or `gsutil`
> - Any other CLI tools for these services
>
> The user connected these services via OAuth. CLI tools don't have access to those tokens.
> **ALWAYS use the curl-based Composio API patterns shown in this skill.**

## Environment

```bash
COMPOSIO_API_KEY      # API key
COMPOSIO_USER_ID      # Entity ID (required for all requests)
COMPOSIO_CONNECTIONS  # JSON: {"linear":"ca_xxx","github":"ca_yyy","google":"ca_zzz"}
```

## Core Pattern

```bash
# 1. Get connection ID for the service
CONNECTION_ID=$(echo $COMPOSIO_CONNECTIONS | jq -r '.linear')

# 2. Execute action (note: use "arguments" not "input", and include entity_id)
curl -s "https://backend.composio.dev/api/v3/tools/execute/ACTION_NAME" \
  -H "x-api-key: $COMPOSIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {}
  }' | jq '.data'
```

## Service References

| Service | Connection Key | Reference |
|---------|---------------|-----------|
| Linear | `.linear` | [references/linear.md](references/linear.md) |
| GitHub | `.github` | [references/github.md](references/github.md) |
| Gmail | `.google` | [references/gmail.md](references/gmail.md) |
| Google Drive | `.google` | [references/drive.md](references/drive.md) |

## Quick Examples

### Linear: Get Teams
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_GET_ALL_LINEAR_TEAMS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$(echo $COMPOSIO_CONNECTIONS | jq -r '.linear')'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {}}' | jq
```

### Linear: List Issues
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/LINEAR_LIST_LINEAR_ISSUES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$(echo $COMPOSIO_CONNECTIONS | jq -r '.linear')'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {}}' | jq
```

### GitHub: List All Your Repos
```bash
# First get username, then list repos
USERNAME=$(curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_GET_THE_AUTHENTICATED_USER" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$(echo $COMPOSIO_CONNECTIONS | jq -r '.github')'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {}}' | jq -r '.data.response_data.login')

curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_LIST_REPOSITORIES_FOR_A_USER" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$(echo $COMPOSIO_CONNECTIONS | jq -r '.github')'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {"username": "'$USERNAME'"}}' | jq
```

### GitHub: List Repo Issues
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_LIST_REPOSITORY_ISSUES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$(echo $COMPOSIO_CONNECTIONS | jq -r '.github')'", "entity_id": "'$COMPOSIO_USER_ID'", "arguments": {"owner": "OWNER", "repo": "REPO"}}' | jq
```

## Discover Actions

```bash
# List all actions for a service
curl -s "https://backend.composio.dev/api/v2/actions?apps=linear" \
  -H "x-api-key: $COMPOSIO_API_KEY" | jq '.items[] | {name, description}'
```

Replace `linear` with: `github`, `gmail`, `googledrive`
