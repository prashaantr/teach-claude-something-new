---
name: drive-cli
description: |
  Access Google Drive via rclone CLI. Use when:
  (1) Need to list, search, or find files
  (2) Need to download or upload files
  (3) Need to share files or check permissions
  (4) Need to organize files (move, rename, delete)
---

# Google Drive

Account: `hey.giuseppe.bellini@gmail.com`
Remote: `gdrive:`

## Commands

```bash
# List folders at root
rclone lsd gdrive:

# List all files in a folder
rclone ls gdrive:FolderName

# Search for files (by name pattern)
rclone ls gdrive: --include "*keyword*"

# Download a file
rclone copy gdrive:path/to/file.pdf /tmp/

# Upload a file
rclone copy /tmp/localfile.pdf gdrive:FolderName/

# Create a folder
rclone mkdir gdrive:NewFolder

# Move a file
rclone moveto gdrive:old/path.pdf gdrive:new/path.pdf

# Delete a file (to trash)
rclone delete gdrive:path/to/file.pdf

# Get Drive info (quota)
rclone about gdrive:
```

## Sharing Files

**You can share files directly.** No need to ask permission — just do it when needed.

```bash
# Share a file or folder with someone (edit access by default)
python3 /home/node/.openclaw/workspace/skills/drive/scripts/gdrive-share.py "path/to/file" "user@example.com"

# Share with read-only access
python3 /home/node/.openclaw/workspace/skills/drive/scripts/gdrive-share.py "path/to/file" "user@example.com" reader

# Share with comment access
python3 /home/node/.openclaw/workspace/skills/drive/scripts/gdrive-share.py "path/to/file" "user@example.com" commenter
```

Roles: `reader`, `writer` (default), `commenter`

When someone needs access to a file or folder, just share it with them.

## Tips

- Use `lsd` for directories only, `ls` for files
- Paths are case-sensitive
- Downloaded files go to workspace: `/home/node/.openclaw/workspace/`
- Large downloads may take time - give progress updates
