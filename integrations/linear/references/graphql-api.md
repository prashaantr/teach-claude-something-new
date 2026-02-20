# Linear GraphQL API

Use when CLI project commands hang. The issue CLI commands work fine.

## Get Team ID

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ teams { nodes { id key name } } }"}'
```

## List Projects

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ projects(first: 50) { nodes { id name state } } }"}'
```

## Create Project

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { projectCreate(input: { name: \"Project Name\", teamIds: [\"TEAM_ID_HERE\"] }) { success project { id name } } }"}'
```

## View Project with Issues

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ project(id: \"PROJECT_ID\") { name state issues { nodes { identifier title } } } }"}'
```

## Create Issue in Project

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { issueCreate(input: { title: \"Task title\", teamId: \"TEAM_ID\", projectId: \"PROJECT_ID\" }) { success issue { identifier title } } }"}'
```

## List Project Milestones

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ project(id: \"PROJECT_ID\") { projectMilestones { nodes { id name targetDate } } } }"}'
```

## Link Issue to Milestone

**You CAN link issues to milestones.** Use `projectMilestoneId`:

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { issueUpdate(id: \"ISSUE_ID\", input: { projectMilestoneId: \"MILESTONE_ID\" }) { success issue { identifier projectMilestone { name } } } }"}'
```

## Create Milestone

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { projectMilestoneCreate(input: { projectId: \"PROJECT_ID\", name: \"Phase 1\", targetDate: \"2024-03-01\" }) { success projectMilestone { id name } } }"}'
```
