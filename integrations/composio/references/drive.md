# Google Drive Actions

Connection key: `.google`

## Files

### List Files
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_LIST_FILES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{"connected_account_id": "'$CONNECTION_ID'", "input": {}}' | jq
```

### List Files in Folder
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_LIST_FILES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"folder_id": "FOLDER_ID"}
  }' | jq
```

### Search Files
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_SEARCH_FILES" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"query": "name contains 'report'"}
  }' | jq
```

Query syntax: `name contains 'x'`, `mimeType = 'application/pdf'`, `modifiedTime > '2024-01-01'`

### Get File Metadata
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_GET_FILE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"file_id": "FILE_ID"}
  }' | jq
```

### Download File
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_DOWNLOAD_FILE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {"file_id": "FILE_ID"}
  }' | jq
```

### Upload File
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_UPLOAD_FILE" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {
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
    "input": {"file_id": "FILE_ID"}
  }' | jq
```

## Folders

### Create Folder
```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/GOOGLEDRIVE_CREATE_FOLDER" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "input": {
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
    "input": {
      "file_id": "FILE_ID",
      "email": "user@example.com",
      "role": "writer"
    }
  }' | jq
```

Roles: `reader`, `writer`, `commenter`

## Common Actions

| Action | Description |
|--------|-------------|
| GOOGLEDRIVE_LIST_FILES | List files |
| GOOGLEDRIVE_SEARCH_FILES | Search files |
| GOOGLEDRIVE_GET_FILE | Get file metadata |
| GOOGLEDRIVE_DOWNLOAD_FILE | Download file content |
| GOOGLEDRIVE_UPLOAD_FILE | Upload new file |
| GOOGLEDRIVE_CREATE_FOLDER | Create folder |
| GOOGLEDRIVE_DELETE_FILE | Delete file/folder |
| GOOGLEDRIVE_SHARE_FILE | Share with user |
| GOOGLEDRIVE_COPY_FILE | Copy file |
| GOOGLEDRIVE_MOVE_FILE | Move file |
