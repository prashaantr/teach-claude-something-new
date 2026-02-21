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

### List Issues by Team
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ team(id: \"TEAM_ID\") { issues(first: 50) { nodes { identifier title state { name } priority } } } }"}' | jq '.data.team.issues.nodes'
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

### Create Issue
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
        "description": "Issue description",
        "priority": 2
      }
    }
  }' | jq '.data.issueCreate'
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

### Get Current User Info
```bash
curl -s https://api.linear.app/graphql \
  -H "Authorization: Bearer $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ viewer { id name email } }"}' | jq '.data.viewer'
```

## Common Workflows

### Start Working on an Issue
1. Get issue ID from search
2. Update state to "In Progress"
3. Assign to self if needed

### Complete an Issue
1. Update state to "Done"
```bash
# First get the "Done" state ID for the team
# Then update the issue with that stateId
```

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
