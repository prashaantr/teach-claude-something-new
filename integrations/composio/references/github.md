# GitHub Actions

Connection key: `.github`

## Issues

### List Repository Issues
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_LIST_REPOSITORY_ISSUES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"owner": "OWNER", "repo": "REPO", "state": "open"}
  }' | jq
```

### Create Issue
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_CREATE_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {
      "owner": "OWNER",
      "repo": "REPO",
      "title": "Issue title",
      "body": "Issue description"
    }
  }' | jq
```

### Update Issue
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_UPDATE_ISSUE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {
      "owner": "OWNER",
      "repo": "REPO",
      "issue_number": 123,
      "state": "closed"
    }
  }' | jq
```

### Add Issue Comment
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_CREATE_ISSUE_COMMENT" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {
      "owner": "OWNER",
      "repo": "REPO",
      "issue_number": 123,
      "body": "Comment text"
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
    "input": {"owner": "OWNER", "repo": "REPO", "state": "open"}
  }' | jq
```

### Create Pull Request
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_CREATE_PULL_REQUEST" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {
      "owner": "OWNER",
      "repo": "REPO",
      "title": "PR title",
      "body": "PR description",
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
    "input": {
      "owner": "OWNER",
      "repo": "REPO",
      "pull_number": 123,
      "merge_method": "squash"
    }
  }' | jq
```

## Repositories

### List User Repos
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_LIST_USER_REPOS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {}}' | jq
```

### Get Repository
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_GET_REPOSITORY" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"owner": "OWNER", "repo": "REPO"}
  }' | jq
```

### Get File Contents
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_GET_CONTENTS" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"owner": "OWNER", "repo": "REPO", "path": "README.md"}
  }' | jq
```

## Branches

### List Branches
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_LIST_BRANCHES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"owner": "OWNER", "repo": "REPO"}
  }' | jq
```

### Create Branch
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GITHUB_CREATE_BRANCH" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {
      "owner": "OWNER",
      "repo": "REPO",
      "branch": "new-branch",
      "sha": "BASE_COMMIT_SHA"
    }
  }' | jq
```

## Common Actions

| Action | Description |
|--------|-------------|
| GITHUB_LIST_REPOSITORY_ISSUES | List repo issues |
| GITHUB_CREATE_ISSUE | Create issue |
| GITHUB_UPDATE_ISSUE | Update issue |
| GITHUB_CREATE_ISSUE_COMMENT | Add comment |
| GITHUB_LIST_PULL_REQUESTS | List PRs |
| GITHUB_CREATE_PULL_REQUEST | Create PR |
| GITHUB_MERGE_PULL_REQUEST | Merge PR |
| GITHUB_LIST_USER_REPOS | List user repos |
| GITHUB_GET_REPOSITORY | Get repo info |
| GITHUB_GET_CONTENTS | Get file contents |
| GITHUB_LIST_BRANCHES | List branches |
| GITHUB_CREATE_BRANCH | Create branch |
| GITHUB_LIST_COMMITS | List commits |
| GITHUB_STAR_REPO | Star repo |
| GITHUB_FORK_REPO | Fork repo |
