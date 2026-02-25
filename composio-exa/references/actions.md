# Exa Search Actions Reference

## Contents

- [EXA_SEARCH](#exa_search)
- [EXA_ANSWER](#exa_answer)
- [EXA_FIND_SIMILAR](#exa_find_similar)
- [EXA_GET_CONTENTS_ACTION](#exa_get_contents_action)
- [Response Format](#response-format)

## Setup

```bash
CONNECTION_ID=$(echo $COMPOSIO_CONNECTIONS | jq -r '.exa')
```

**Required fields for all requests:**
- `connected_account_id`: from `$COMPOSIO_CONNECTIONS`
- `entity_id`: from `$COMPOSIO_USER_ID`
- `arguments`: action-specific parameters

## EXA_SEARCH

Semantic web search with filtering and content categorization.

```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/EXA_SEARCH" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "query": "best practices for building AI agents",
      "numResults": 10,
      "type": "auto"
    }
  }' | jq
```

**Parameters:**
- `query` (required): Natural language search query
- `numResults`: Number of results (default: 10)
- `type`: `"auto"` (default), `"keyword"`, or `"neural"`
- `includeDomains`: List of domains to include
- `excludeDomains`: List of domains to exclude
- `startPublishedDate`: Filter by publish date (ISO format)
- `endPublishedDate`: Filter by publish date (ISO format)
- `category`: Filter by content category

## EXA_ANSWER

Get citation-backed answers to natural language questions. Best for research questions.

```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/EXA_ANSWER" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "query": "What are the key differences between RAG and fine-tuning?"
    }
  }' | jq
```

Returns an answer with citations to source URLs.

## EXA_FIND_SIMILAR

Find pages semantically similar to a given URL using embeddings.

```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/EXA_FIND_SIMILAR" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "url": "https://example.com/article",
      "numResults": 10
    }
  }' | jq
```

## EXA_GET_CONTENTS_ACTION

Retrieve full text and highlights from document IDs or URLs.

```bash
curl -s "https://backend.composio.dev/api/v3/tools/execute/EXA_GET_CONTENTS_ACTION" \
  -H "x-api-key: $COMPOSIO_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$CONNECTION_ID'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "ids": ["url1", "url2"]
    }
  }' | jq
```

## Response Format

```json
{
  "results": [
    {
      "title": "Page Title",
      "url": "https://example.com/page",
      "publishedDate": "2024-01-15",
      "author": "Author Name",
      "score": 0.95,
      "text": "Full page content...",
      "highlights": ["Relevant excerpt..."]
    }
  ]
}
```

## All Actions

| Action | Description |
|--------|-------------|
| EXA_SEARCH | Semantic web search with filtering |
| EXA_ANSWER | Citation-backed answers to questions |
| EXA_FIND_SIMILAR | Find pages similar to a URL |
| EXA_GET_CONTENTS_ACTION | Get full content from results |
