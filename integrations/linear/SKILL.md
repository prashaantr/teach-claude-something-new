---
name: linear
description: |
  Project management via Linear CLI. Use when:
  (1) Planning and tracking projects
  (2) Breaking projects into tasks (issues)
  (3) Tracking progress, timelines, deadlines
  (4) Figuring out what to work on next
  (5) Inviting people to the workspace
  (6) Creating custom views
---

# Linear Project Management

**Auth:** Uses `$LINEAR_API_KEY` environment variable.

## Core Concept

```
Initiatives (Roadmap)
    └── Projects (main unit of work)
            └── Issues (subtasks)
```

## Decision Tree

### First: Get Team Key
```bash
linear team list
# Use the KEY (e.g., ARS) in all commands
```

### What are you trying to do?

**Start new significant work?**
→ Create Project → Break into Issues → Work through them
→ See: `references/workflows.md`

**Figure out what to work on?**
→ Check projects → View issues → Start one
→ See: `references/workflows.md`

**Create/manage issues?**
→ See: `references/cli-commands.md`

**Work on code with Linear integration?**
→ Start issue → Code → PR → Done
→ See: `references/workflows.md`

**Invite someone to Linear?**
→ You CAN do this via API
→ See: `references/scripts.md`

**Create a custom view?**
→ You CAN do this via API
→ See: `references/scripts.md`

**CLI project commands hanging?**
→ Use GraphQL API directly
→ See: `references/graphql-api.md`

**Look up team members?**
→ `linear team members --team TEAM_KEY`

## Quick Commands

| Task | Command |
|------|---------|
| List teams | `linear team list` |
| List projects | `linear project list --team KEY` |
| List issues | `linear issue list --team KEY` |
| View issue | `linear issue view TEAM-123` |
| Start work | `linear issue start TEAM-123` |
| Mark done | `linear issue update TEAM-123 --state "Done"` |
| Update description | `python3 .../scripts/linear-issue-update.py TEAM-123 --description "text"` |
| Update from file | `python3 .../scripts/linear-issue-update.py TEAM-123 --description-file /tmp/desc.md` |
| **Create view** | `python3 .../scripts/linear-view.py create "View Name" --template urgent` |
| List views | `python3 .../scripts/linear-view.py list` |
| Invite user | `python3 .../scripts/linear-invite.py user@example.com` |

## Custom Views (via script, NOT CLI)

```bash
# Create view with template
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-view.py create "Urgent Issues" --template urgent

# Templates: urgent, high-priority, due-this-week, overdue, unassigned, bugs, in-progress, blocked

# Create for specific team
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-view.py create "ARS Urgent" --template urgent --team TEAM_ID

# List all views
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-view.py list

# Get team IDs
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-view.py teams
```

## ⚠️ CLI Limitation

The `linear issue update` command **ONLY supports `--state`**. To update description, title, or other fields:

```bash
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-issue-update.py TEAM-123 \
  --description "New description here"

# Or from a file:
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-issue-update.py TEAM-123 \
  --description-file /tmp/description.md

# Other options:
  --title "New title"
  --priority 2       # 1=urgent, 2=high, 3=medium, 4=low
  --estimate 3       # story points
```

## References

| File | Content |
|------|---------|
| `references/cli-commands.md` | Full CLI command reference |
| `references/graphql-api.md` | Direct API when CLI hangs |
| `references/workflows.md` | Step-by-step workflow guides |
| `references/scripts.md` | Invite users, create views |

## Tips

- **Projects first**: Create a project for any significant work, then add issues
- **Always use `--project`** when creating issues to link them
- Issue IDs are `TEAM_KEY-123` (e.g., `ARS-42`)
- Priority: 1=urgent, 2=high, 3=medium, 4=low
- States: Backlog, Todo, In Progress, Done, Canceled
