# Teach Claude Something New

A curated collection of **Skills** for Claude - modular, self-contained packages that extend Claude's capabilities with specialized knowledge, workflows, and tool integrations.

## What Are Skills?

Skills transform Claude from a general-purpose AI into a specialized agent equipped with procedural knowledge that no model can fully possess. Each skill provides:

- **Specialized workflows** - Multi-step procedures for specific domains
- **Tool integrations** - Instructions for working with specific file formats or APIs
- **Domain expertise** - Schemas, business logic, and best practices
- **Bundled resources** - Scripts, references, and assets for complex tasks

## Skill Categories

| Category | Skills | Description |
|----------|--------|-------------|
| **academic/** | 4 | Research methodology, paper writing/review, neuro-symbolic reasoning |
| **ai/** | 4 | Coding agents, memory systems, image generation, LLM fine-tuning |
| **business/** | 1 | Negotiation preparation and strategy |
| **creative/** | 2 | World-building, script writing |
| **data-viz/** | 1 | Visualization design (Stanford CS448B), D3.js |
| **design/** | 1 | Mockup generation |
| **documents/** | 5 | PDF, DOCX, XLSX, PPTX, assembly instructions |
| **integrations/** | 6 | Composio (GitHub/Linear/Gmail/Drive/Calendar/Exa), Discord, Telegram |
| **meta/** | 1 | Skill creator (for building new skills) |
| **science/** | 1 | AlphaFold protein structure database |

## Usage

Skills are designed to work with Claude Code. To use a skill:

1. Copy the skill directory to `~/.claude/skills/`
2. The skill will be available based on its trigger conditions in the description

Or use the packaged `.skill` format:

```bash
# Package a skill for distribution
python meta/skill-creator/scripts/package_skill.py <skill-directory>
```

## Skill Structure

Each skill follows a standard structure:

```
skill-name/
├── SKILL.md           # Required: frontmatter + instructions
├── scripts/           # Optional: executable Python/Bash
├── references/        # Optional: documentation loaded as needed
└── assets/            # Optional: templates, images for output
```

## Creating New Skills

Use the `skill-creator` skill in `meta/skill-creator/`:

```bash
# Initialize a new skill
python meta/skill-creator/scripts/init_skill.py <skill-name> --path <output-dir>

# Validate and package
python meta/skill-creator/scripts/package_skill.py <skill-directory>
```

See `meta/skill-creator/SKILL.md` for comprehensive guidance on skill design principles.

## Contributing

When adding or modifying skills:

1. Follow the structure defined in `meta/skill-creator/`
2. Keep SKILL.md concise (<500 lines) - use progressive disclosure
3. Write comprehensive `description` fields with clear triggers
4. Test scripts before committing
5. Use `references/` for detailed documentation, `assets/` for templates

## License

Individual skills may have their own licenses. Check each skill's SKILL.md frontmatter for license information.
