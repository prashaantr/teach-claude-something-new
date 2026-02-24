---
name: find-skills
description: Search and discover external skills from skills.sh and GitHub. Use when you need a capability you don't have, want to find best practices for a technology, or need specialized workflows. Search by keyword, browse popular skills, or fetch specific skills by repo.
---

# Find Skills

Search for skills when you need capabilities beyond your current toolkit.

## When to Search

- Need a capability you don't have
- Working with unfamiliar technology
- Want best practices for a framework/library
- Need specialized workflows (testing, deployment, etc.)

## Search skills.sh

Browse popular skills at https://skills.sh or search by keyword.

### Top Skills (most installed)

| Skill | Installs | Use For |
|-------|----------|---------|
| find-skills | 300K+ | Skill discovery |
| vercel-react-best-practices | 160K+ | React patterns |
| web-design-guidelines | 120K+ | Web design |
| frontend-design | 90K+ | UI/UX |
| agent-browser | 50K+ | Web automation |

## Fetch a Skill

```bash
# List skills in a repo without installing
npx skills add <owner/repo> --list

# Fetch skill content directly
curl -s "https://raw.githubusercontent.com/<owner>/<repo>/main/SKILL.md"
# or for nested skills
curl -s "https://raw.githubusercontent.com/<owner>/<repo>/main/skills/<name>/SKILL.md"
```

## Skill Format

Valid skills have YAML frontmatter:

```markdown
---
name: my-skill
description: What it does and when to use it
---

# Instructions here
```

## Using Found Skills

1. Fetch the SKILL.md content
2. Read and understand the instructions
3. If non-standard, use **skill-creator** to normalize it
4. Apply the skill's guidance to your task

## Popular Skill Repos

- `vercel-labs/skills` - Official Vercel skills
- `anthropics/courses` - Claude best practices
- `cursor-ai/cursor-config` - Cursor IDE skills
