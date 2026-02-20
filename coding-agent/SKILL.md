---
name: coding-agent
description: |
  Delegate coding tasks to external coding agents. Currently not installed.
  This skill documents how to use them if added in the future.
---

# Coding Agents

**Status:** Not currently installed. This documents future capability.

To add coding agents, they would need to be installed in the Dockerfile and have API keys configured.

## If Claude Code Were Installed

```bash
# One-shot task
claude "Add error handling to the login function"

# With auto-approval
claude --dangerously-skip-permissions "Build the authentication module"
```

Requires: `ANTHROPIC_API_KEY` (already configured)

## If Codex CLI Were Installed

```bash
# One-shot execution
codex exec "Your prompt here"

# Full auto mode (sandboxed)
codex exec --full-auto "Build feature X"
```

Requires: `OPENAI_API_KEY` (not configured)

## Alternative: Use OpenClaw's Built-in Capabilities

Giuseppe already has coding capabilities via OpenClaw/Claude. For most tasks, just describe what you need and execute bash commands directly:

```bash
# Read code
cat /path/to/file.py

# Edit code
# Use the file editing capabilities already available

# Run tests
pytest /path/to/tests
```

## Future Installation

To add Claude Code:
```dockerfile
RUN npm install -g @anthropic-ai/claude-code
```

To add Codex:
```dockerfile
RUN npm install -g @openai/codex
```
