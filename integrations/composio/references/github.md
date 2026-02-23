# GitHub Actions (Composio)

> **⚠️ DO NOT USE `gh` CLI** - It will fail with "gh auth login" error.
> Use the Composio HTTP API (curl commands) below instead.

Connection key: `.github`

**Note:** All requests must include `entity_id` and use `arguments` (not `input`).

## Repository Contents

### Get File/Directory Contents (BASE64 encoded)
```bash
CONNECTION_ID=$(echo $COMPOSIO_CONNECTIONS | jq -r '.github')

curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_GET_REPOSITORY_CONTENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"owner": "OWNER", "repo": "REPO", "path": "path/to/file.md"}
  }' | jq
```

**Note:** Content is base64 encoded. To decode:
```bash
# Extract and decode content
echo "BASE64_CONTENT" | base64 -d
```

### Get Repository README
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_GET_A_REPOSITORY_README" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"owner": "OWNER", "repo": "REPO"}
  }' | jq
```

### Download Repository (ZIP)
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_DOWNLOAD_A_REPOSITORY_ARCHIVE_ZIP" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"owner": "OWNER", "repo": "REPO", "ref": "main"}
  }' | jq
```

## Issues

### List Repository Issues
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_LIST_REPOSITORY_ISSUES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"owner": "OWNER", "repo": "REPO", "state": "open"}
  }' | jq
```

### Create Issue (WITH AGENT TAG)
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_CREATE_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "owner": "OWNER",
      "repo": "REPO",
      "title": "Issue title",
      "body": "Issue description\n\nCreated by '"$AGENT_NAME"'"
    }
  }' | jq
```

### Update Issue
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_UPDATE_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "owner": "OWNER",
      "repo": "REPO",
      "issue_number": 123,
      "state": "closed"
    }
  }' | jq
```

### Add Issue Comment (WITH AGENT TAG)
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_CREATE_ISSUE_COMMENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "owner": "OWNER",
      "repo": "REPO",
      "issue_number": 123,
      "body": "Comment text\n\n— '"$AGENT_NAME"'"
    }
  }' | jq
```

## Pull Requests

### List Pull Requests
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_LIST_PULL_REQUESTS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"owner": "OWNER", "repo": "REPO", "state": "open"}
  }' | jq
```

### Create Pull Request (WITH AGENT TAG)
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_CREATE_PULL_REQUEST" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "owner": "OWNER",
      "repo": "REPO",
      "title": "PR title",
      "body": "PR description\n\nCreated by '"$AGENT_NAME"'",
      "head": "feature-branch",
      "base": "main"
    }
  }' | jq
```

### Merge Pull Request
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_MERGE_PULL_REQUEST" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "owner": "OWNER",
      "repo": "REPO",
      "pull_number": 123,
      "merge_method": "squash"
    }
  }' | jq
```

## Repositories

### List Your Repos (Public + Private)
```bash
# Use GITHUB_LIST_REPOSITORIES_FOR_THE_AUTHENTICATED_USER for ALL repos
# NOT GITHUB_LIST_REPOSITORIES_FOR_A_USER (that only returns public repos)
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_LIST_REPOSITORIES_FOR_THE_AUTHENTICATED_USER" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "visibility": "all",
      "affiliation": "owner,collaborator,organization_member"
    }
  }' | jq '.data.repositories'
```

### Get Repository Info
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_GET_REPOSITORY" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"owner": "OWNER", "repo": "REPO"}
  }' | jq
```

## Branches

### List Branches
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_LIST_BRANCHES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"owner": "OWNER", "repo": "REPO"}
  }' | jq
```

## Common Actions Reference

| Action | Description |
|--------|-------------|
| `GITHUB_GET_REPOSITORY_CONTENT` | Get file/dir contents (base64) |
| `GITHUB_GET_A_REPOSITORY_README` | Get repo README |
| `GITHUB_DOWNLOAD_A_REPOSITORY_ARCHIVE_ZIP` | Download repo as ZIP |
| `GITHUB_LIST_REPOSITORY_ISSUES` | List repo issues |
| `GITHUB_CREATE_ISSUE` | Create issue |
| `GITHUB_UPDATE_ISSUE` | Update issue |
| `GITHUB_CREATE_ISSUE_COMMENT` | Add comment |
| `GITHUB_LIST_PULL_REQUESTS` | List PRs |
| `GITHUB_CREATE_PULL_REQUEST` | Create PR |
| `GITHUB_MERGE_PULL_REQUEST` | Merge PR |
| `GITHUB_LIST_REPOSITORIES_FOR_THE_AUTHENTICATED_USER` | List ALL repos (public+private) |
| `GITHUB_GET_REPOSITORY` | Get repo info |
| `GITHUB_LIST_BRANCHES` | List branches |
| `GITHUB_LIST_COMMITS` | List commits |

## Troubleshooting

If requests fail:
1. Check `$COMPOSIO_CONNECTIONS` has `.github` key
2. Verify `entity_id` is included in request
3. Use `arguments` not `input`
4. Check action name spelling (use discover endpoint below)

### Discover Available Actions
```bash
curl -s "https://backend.composio.dev/api/v2/actions?apps=github" \
  -H "x-api-key: $COMPOSIO_API_KEY" | jq '.items[] | {name, description}'
```
