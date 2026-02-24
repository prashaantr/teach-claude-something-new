# Google Drive Actions (Composio)

Connection key: `.googledrive`

## Contents

- [Files](#files)
- [Folders](#folders)
- [Sharing](#sharing)
- [All Actions](#all-actions)

## Setup

```bash
CONNECTION_ID=$(echo $COMPOSIO_CONNECTIONS | jq -r '.googledrive')
```

**Required fields for all requests:**
- `connected_account_id`: from `$COMPOSIO_CONNECTIONS`
- `entity_id`: from `$COMPOSIO_USER_ID`
- `arguments`: action-specific parameters

## Files

### List Files
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_LIST_FILES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {}
  }' | jq
```

### List Files in Folder
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_LIST_FILES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"folder_id": "FOLDER_ID"}
  }' | jq
```

### Search Files
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_SEARCH_FILES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"query": "name contains 'report'"}
  }' | jq
```

Query syntax: `name contains 'x'`, `mimeType = 'application/pdf'`, `modifiedTime > '2024-01-01'`

### Get File Metadata
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_GET_FILE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"file_id": "FILE_ID"}
  }' | jq
```

### Download File
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_DOWNLOAD_FILE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"file_id": "FILE_ID"}
  }' | jq
```

### Upload File
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_UPLOAD_FILE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "name": "filename.pdf",
      "content": "BASE64_ENCODED_CONTENT",
      "mime_type": "application/pdf",
      "parent_folder_id": "FOLDER_ID"
    }
  }' | jq
```

### Delete File
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_DELETE_FILE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {"file_id": "FILE_ID"}
  }' | jq
```

## Folders

### Create Folder
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_CREATE_FOLDER" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "name": "New Folder",
      "parent_folder_id": "PARENT_FOLDER_ID"
    }
  }' | jq
```

## Sharing

### Share File
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_SHARE_FILE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "file_id": "FILE_ID",
      "email": "user@example.com",
      "role": "writer"
    }
  }' | jq
```

Roles: `reader`, `writer`, `commenter`

## All Actions

| Action | Description |
|--------|-------------|
| `GOOGLEDRIVE_LIST_FILES` | List files |
| `GOOGLEDRIVE_SEARCH_FILES` | Search files |
| `GOOGLEDRIVE_GET_FILE` | Get file metadata |
| `GOOGLEDRIVE_DOWNLOAD_FILE` | Download file content |
| `GOOGLEDRIVE_UPLOAD_FILE` | Upload new file |
| `GOOGLEDRIVE_CREATE_FOLDER` | Create folder |
| `GOOGLEDRIVE_DELETE_FILE` | Delete file/folder |
| `GOOGLEDRIVE_SHARE_FILE` | Share with user |
| `GOOGLEDRIVE_COPY_FILE` | Copy file |
| `GOOGLEDRIVE_MOVE_FILE` | Move file |
