---
name: linear
description: |
  Project management via Linear GraphQL API. Use when:
  (1) Planning and tracking projects
  (2) Breaking projects into tasks (issues)
  (3) Tracking progress, timelines, deadlines
  (4) Figuring out what to work on next
  (5) Inviting people to the workspace
---

# Linear Project Management

**Auth:** Uses `$LINEAR_API_KEY` environment variable with Bearer token auth.

## Agent Identification

**CRITICAL**: All issues/comments created by agents MUST include identification:

- **Issue descriptions**: End with `Created by $AGENT_NAME`
- **Comments**: End with `— $AGENT_NAME`

This ensures traceability when multiple agents share the same Linear workspace.

## Core Concept

```
Initiatives (Roadmap)
    └── Projects (main unit of work)
            └── Issues (subtasks)
```

## GraphQL API (Primary Method)

All commands use the Linear GraphQL API with Bearer auth:

```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "YOUR_QUERY_HERE"}'
```

## Quick Commands

### List Teams
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ teams { nodes { id name key } } }"}' | jq '.data.teams.nodes'
```

### List Projects
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ projects(first: 20) { nodes { id name state } } }"}' | jq '.data.projects.nodes'
```

### List Issues (Recent)
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ issues(first: 20, orderBy: updatedAt) { nodes { identifier title state { name } assignee { name } priority dueDate } } }"}' | jq '.data.issues.nodes'
```

### Create Issue (WITH AGENT TAG)
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation CreateIssue($input: IssueCreateInput!) { issueCreate(input: $input) { success issue { identifier title url } } }",
    "variables": {
      "input": {
        "teamId": "TEAM_ID",
        "title": "Issue title",
        "description": "Issue description\n\nCreated by '"$AGENT_NAME"'",
        "priority": 2
      }
    }
  }' | jq '.data.issueCreate'
```

### Add Comment (WITH AGENT TAG)
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation CreateComment($input: CommentCreateInput!) { commentCreate(input: $input) { success comment { id } } }",
    "variables": {
      "input": {
        "issueId": "ISSUE_ID",
        "body": "Your comment here.\n\n— '"$AGENT_NAME"'"
      }
    }
  }' | jq '.data.commentCreate'
```

### Update Issue State
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation UpdateIssue($id: String!, $input: IssueUpdateInput!) { issueUpdate(id: $id, input: $input) { success issue { identifier state { name } } } }",
    "variables": {
      "id": "ISSUE_ID",
      "input": {
        "stateId": "STATE_ID"
      }
    }
  }' | jq '.data.issueUpdate'
```

### Get Issue Details
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ issue(id: \"ISSUE_ID\") { identifier title description state { name } assignee { name } priority estimate dueDate project { name } } }"}' | jq '.data.issue'
```

### Search Issues by Identifier (e.g., ARS-123)
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ issueSearch(query: \"ARS-123\") { nodes { id identifier title state { name } } } }"}' | jq '.data.issueSearch.nodes'
```

### Get Workflow States (for a team)
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ team(id: \"TEAM_ID\") { states { nodes { id name type } } } }"}' | jq '.data.team.states.nodes'
```

### Get My Assigned Issues
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ viewer { assignedIssues(first: 20) { nodes { identifier title state { name } priority dueDate } } } }"}' | jq '.data.viewer.assignedIssues.nodes'
```

## Common Workflows

### Start Working on an Issue
1. Get issue ID from search
2. Update state to "In Progress"
3. Add comment: `Starting work on this. — $AGENT_NAME`

### Complete an Issue
1. Update state to "Done"
2. Add comment: `Completed. — $AGENT_NAME`

## Priority Values
- 0 = No priority
- 1 = Urgent
- 2 = High
- 3 = Medium
- 4 = Low

## Tips

- Use `jq` to parse JSON responses
- Team IDs and State IDs are UUIDs - get them from list queries first
- Issue identifiers (ARS-123) are different from issue IDs (UUIDs)
- Use `issueSearch` to find issues by identifier
- The `viewer` query gets info about the authenticated user
- **Always tag your work** with `$AGENT_NAME` so others know which agent did it
