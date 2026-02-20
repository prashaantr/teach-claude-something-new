# Linear CLI Commands Reference

## Teams

```bash
# List all teams (do this first!)
linear team list

# Output shows: KEY, NAME, ID
# Use the KEY (e.g., ARS, ENG, OPS) in commands

# View team details
linear team view TEAM_KEY

# List team members (names, emails, roles)
linear team members --team TEAM_KEY

# Create new team
linear team create --name "New Team" --key NTN
```

**Looking up team members:** Use `linear team members --team TEAM_KEY` to see who's on a team. Check there first before asking for emails/usernames.

## Projects

```bash
# List all projects
linear project list --team TEAM_KEY

# View project details (shows progress, dates, issues)
linear project view PROJECT_ID

# Create a new project
linear project create --name "Build Authentication System" --team TEAM_KEY

# Post project status update
linear project-update create PROJECT_ID \
  --body "Completed login flow. Starting password reset next."
```

**Note:** If CLI hangs on project commands, use GraphQL API (see graphql-api.md).

## Issues

```bash
# List issues for a project
linear issue list --team TEAM_KEY --project "Project Name"

# List all your issues
linear issue list --team TEAM_KEY

# View issue details
linear issue view TEAM-123

# Create issue AS PART OF A PROJECT
linear issue create \
  --team TEAM_KEY \
  --project "Project Name" \
  --title "Implement login endpoint" \
  --description "Create POST /auth/login with JWT" \
  --priority 2 \
  --due-date "2024-03-15" \
  --estimate 3

# Create multiple issues to break down a project
linear issue create --team TEAM_KEY --project "Auth System" --title "Design database schema"
linear issue create --team TEAM_KEY --project "Auth System" --title "Implement login endpoint"
linear issue create --team TEAM_KEY --project "Auth System" --title "Implement logout endpoint"
linear issue create --team TEAM_KEY --project "Auth System" --title "Add password reset flow"
linear issue create --team TEAM_KEY --project "Auth System" --title "Write tests"

# Update issue state (ONLY --state is supported by CLI!)
linear issue update TEAM-123 --state "Done"

# ⚠️ CLI LIMITATION: To update description, title, or other fields, use the script:
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-issue-update.py TEAM-123 \
  --description "New description here"
# Or from a file:
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-issue-update.py TEAM-123 \
  --description-file /tmp/description.md

# Start working (moves to In Progress, creates git branch)
linear issue start TEAM-123

# Add comment with progress
linear issue comment TEAM-123 "Completed the basic flow, need to add validation"

# Create sub-issue for complex tasks
linear issue create --team TEAM_KEY --title "Add input validation" --parent TEAM-123

# Add dependencies between issues
linear issue relation TEAM-123 --blocks TEAM-456
linear issue relation TEAM-123 --blocked-by TEAM-789
```

## Initiatives (Roadmap)

```bash
# List initiatives (roadmap items)
linear initiative list

# View initiative details
linear initiative view INITIATIVE_ID

# Create initiative
linear initiative create --name "Platform Expansion"

# Link project to initiative
linear initiative add-project INITIATIVE_ID PROJECT_ID

# Post initiative status update (timeline post)
linear initiative-update create INITIATIVE_ID \
  --body "Q1 milestone complete. Moving to phase 2."

# Archive completed initiative
linear initiative archive INITIATIVE_ID
```

## Milestones

```bash
# List milestones
linear milestone list --team TEAM_KEY

# View milestone
linear milestone view MILESTONE_ID
```

## Labels

```bash
# List labels
linear label list --team TEAM_KEY

# Create label
linear label create --team TEAM_KEY --name "urgent" --color "#ff0000"
```

## Documents

```bash
# List documents
linear document list

# View document
linear document view DOC_ID
```

## Inviting Users

**You can invite people to Linear directly.** No need to ask permission.

```bash
# Invite a user (default role: user)
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-invite.py user@example.com

# Invite as admin
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-invite.py user@example.com admin

# List pending invites
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-invite.py list

# Resend an invite (if needed)
python3 /home/node/.openclaw/workspace/skills/linear/scripts/linear-invite.py user@example.com
```

## Quick Reference

- Issue IDs are `TEAM_KEY-123` (e.g., `ARS-42`)
- Due dates: `--due-date "YYYY-MM-DD"`
- Estimates: `--estimate N` (story points)
- Priority: 1=urgent, 2=high, 3=medium, 4=low
- States: Backlog, Todo, In Progress, Done, Canceled
