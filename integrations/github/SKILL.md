---
name: github
description: GitHub CLI (gh) for repos, issues, PRs, Actions, projects, releases. Use $GITHUB_TOKEN for auth.
---

# GitHub CLI (gh)

**Auth:** Already configured via `$GITHUB_TOKEN` environment variable.

## Agent Identification

**CRITICAL**: All issues, PRs, and comments created by agents MUST include identification:

- **Issue/PR body**: End with `Created by $AGENT_NAME`
- **Comments**: End with `— $AGENT_NAME`

This ensures traceability when multiple agents share the same GitHub credentials.

## Quick Reference

```bash
# Issues
gh issue list --repo OWNER/REPO
gh issue view 123 --repo OWNER/REPO
gh issue create --repo OWNER/REPO --title "Title" --body "Description

Created by $AGENT_NAME"
gh issue close 123 --repo OWNER/REPO

# Pull Requests
gh pr list --repo OWNER/REPO
gh pr view 123 --repo OWNER/REPO
gh pr create --repo OWNER/REPO --title "Title" --body "Description

Created by $AGENT_NAME"

# Comments (always sign)
gh issue comment 123 --repo OWNER/REPO --body "Comment here.

— $AGENT_NAME"

# Search
gh search issues "label:bug state:open" --repo OWNER/REPO
gh search code "TODO" --repo OWNER/REPO

# Repo info
gh repo view OWNER/REPO
gh repo view OWNER/REPO --json description,defaultBranchRef
```

## Issues

```bash
# List open issues
gh issue list --repo OWNER/REPO

# List with filters
gh issue list --repo OWNER/REPO --state all
gh issue list --repo OWNER/REPO --labels bug,enhancement
gh issue list --repo OWNER/REPO --assignee @me

# View issue
gh issue view 123 --repo OWNER/REPO
gh issue view 123 --repo OWNER/REPO --comments

# Create issue (WITH AGENT TAG)
gh issue create --repo OWNER/REPO \
  --title "Bug: Something broken" \
  --body "Steps to reproduce...

Created by $AGENT_NAME"

# Edit issue
gh issue edit 123 --repo OWNER/REPO --title "New title"
gh issue edit 123 --repo OWNER/REPO --add-label bug

# Close/reopen
gh issue close 123 --repo OWNER/REPO
gh issue reopen 123 --repo OWNER/REPO

# Comment (WITH AGENT TAG)
gh issue comment 123 --repo OWNER/REPO --body "Comment here.

— $AGENT_NAME"
```

## Pull Requests

```bash
# List PRs
gh pr list --repo OWNER/REPO
gh pr list --repo OWNER/REPO --state merged
gh pr list --repo OWNER/REPO --author @me

# View PR
gh pr view 123 --repo OWNER/REPO
gh pr view 123 --repo OWNER/REPO --comments

# Create PR (WITH AGENT TAG)
gh pr create --repo OWNER/REPO \
  --title "Feature: New thing" \
  --body "Description of the change.

Created by $AGENT_NAME" \
  --base main

# Review
gh pr review 123 --repo OWNER/REPO --approve --body "Looks good!

— $AGENT_NAME"
gh pr review 123 --repo OWNER/REPO --request-changes --body "Please fix X.

— $AGENT_NAME"

# Merge
gh pr merge 123 --repo OWNER/REPO --squash
```

## Search

```bash
# Search issues
gh search issues "is:open label:bug" --repo OWNER/REPO

# Search code
gh search code "function_name" --repo OWNER/REPO

# Search PRs
gh search prs "is:open review:required" --repo OWNER/REPO
```

## Repository

```bash
# View repo
gh repo view OWNER/REPO

# List files (via API)
gh api repos/OWNER/REPO/contents/PATH

# Get file content
gh api repos/OWNER/REPO/contents/README.md --jq '.content' | base64 -d
```

## Actions

```bash
# List workflow runs
gh run list --repo OWNER/REPO

# View run
gh run view 123456 --repo OWNER/REPO

# Watch run
gh run watch 123456 --repo OWNER/REPO
```

## JSON Output

Add `--json` for structured data:
```bash
gh issue list --repo OWNER/REPO --json number,title,state,labels
gh pr list --repo OWNER/REPO --json number,title,author,headRefName
```

## Tips

- **Always sign your work** with `$AGENT_NAME` in bodies/comments
- Use `--repo OWNER/REPO` to specify the repository
- Add `--json` for machine-readable output
- Ask Prashaant which repos to check
