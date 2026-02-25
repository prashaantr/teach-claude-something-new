# Linear Workflows

## Starting New Work

When given a significant task:

1. **Create a Project** for the work:
   ```bash
   linear project create --name "Build Feature X" --team TEAM_KEY
   ```

2. **Break it into issues** (subtasks):
   ```bash
   linear issue create --team TEAM_KEY --project "Build Feature X" --title "Research approach"
   linear issue create --team TEAM_KEY --project "Build Feature X" --title "Implement core logic"
   linear issue create --team TEAM_KEY --project "Build Feature X" --title "Add tests"
   linear issue create --team TEAM_KEY --project "Build Feature X" --title "Documentation"
   ```

3. **Work through issues** one by one:
   ```bash
   linear issue start TEAM-123
   # ... do the work ...
   linear issue update TEAM-123 --state "Done"
   ```

4. **Post status updates** on the project:
   ```bash
   linear project-update create PROJECT_ID --body "Completed research, starting implementation"
   ```

## What Should I Work On?

1. Check active projects: `linear project list --team TEAM_KEY`
2. View project to see remaining issues: `linear project view PROJECT_ID`
3. Pick next issue: `linear issue list --team TEAM_KEY --project "Project Name"`
4. Start work: `linear issue start TEAM-123`

## Project Status Check

1. List projects: `linear project list --team TEAM_KEY`
2. View project: `linear project view PROJECT_ID`
3. Check issue progress within project
4. Post update: `linear project-update create PROJECT_ID --body "Status..."`

## Integration with GitHub

```bash
# Start issue (creates git branch)
linear issue start TEAM-123

# Make changes, commit...

# Create PR with issue details auto-filled
linear issue pr TEAM-123

# Or manually: gh pr create
# Linear auto-links via branch name

# When PR merges, update Linear
linear issue update TEAM-123 --state "Done"
```
