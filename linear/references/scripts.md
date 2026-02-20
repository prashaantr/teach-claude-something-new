# Linear Scripts Reference

Scripts for operations not supported by the Linear CLI.

## Inviting Users

**You CAN invite users directly via API.** Don't tell users to do it manually.

```bash
# Invite user (default role: user)
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-invite.py user@example.com

# Invite as admin
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-invite.py user@example.com admin

# List pending invites
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-invite.py list
```

## Custom Views

**You CAN create and manage custom views via API.**

```bash
# List all views
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-view.py list

# Create a view with template
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-view.py create "Urgent Issues" --template urgent

# Create a view for a specific team
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-view.py create "Team Bugs" --template bugs --team TEAM_ID

# Get team IDs
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-view.py teams

# View details
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-view.py view VIEW_ID

# Delete a view
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-view.py delete VIEW_ID
```

### Available Templates

| Template | Filter |
|----------|--------|
| `urgent` | Priority = 1 (urgent) |
| `high-priority` | Priority <= 2 and != 0 |
| `due-this-week` | Due date < 1 week |
| `overdue` | Due date < today |
| `unassigned` | No assignee |
| `bugs` | Label contains "bug" |
| `in-progress` | State type = started |
| `blocked` | Label contains "blocked" |

### Custom Filters

```bash
# Custom filter JSON
python3 scripts/linear-view.py create "Custom" --filter '{"priority": {"eq": 1}}'

# With description
python3 scripts/linear-view.py create "My View" --template urgent --desc "Urgent items for review"

# Private view (not shared)
python3 scripts/linear-view.py create "Personal" --template high-priority --private
```
