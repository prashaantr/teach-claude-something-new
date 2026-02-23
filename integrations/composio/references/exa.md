# Exa Search

Exa is an AI-native search engine that understands meaning. Unlike keyword search, Exa finds what you're looking for even if your query doesn't match exact words on the page.

## Available Actions

### EXA_SEARCH

Semantic web search with filtering and content categorization.

```bash
curl -X POST "https://backend.composio.dev/api/v3/tools/execute/EXA_SEARCH" \
  -H "x-api-key: $COMPOSIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$(echo $COMPOSIO_CONNECTIONS | jq -r '.exa')'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "query": "best practices for building AI agents",
      "numResults": 10,
      "type": "auto"
    }
  }'
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

### EXA_ANSWER

Get citation-backed answers to natural language questions. Best for research questions.

```bash
curl -X POST "https://backend.composio.dev/api/v3/tools/execute/EXA_ANSWER" \
  -H "x-api-key: $COMPOSIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$(echo $COMPOSIO_CONNECTIONS | jq -r '.exa')'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "query": "What are the key differences between RAG and fine-tuning?"
    }
  }'
```

Returns an answer with citations to source URLs.

### EXA_FIND_SIMILAR

Find pages semantically similar to a given URL using embeddings.

```bash
curl -X POST "https://backend.composio.dev/api/v3/tools/execute/EXA_FIND_SIMILAR" \
  -H "x-api-key: $COMPOSIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$(echo $COMPOSIO_CONNECTIONS | jq -r '.exa')'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "url": "https://example.com/article",
      "numResults": 10
    }
  }'
```

### EXA_GET_CONTENTS_ACTION

Retrieve full text and highlights from document IDs or URLs.

```bash
curl -X POST "https://backend.composio.dev/api/v3/tools/execute/EXA_GET_CONTENTS_ACTION" \
  -H "x-api-key: $COMPOSIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connected_account_id": "'$(echo $COMPOSIO_CONNECTIONS | jq -r '.exa')'",
    "entity_id": "'$COMPOSIO_USER_ID'",
    "arguments": {
      "ids": ["url1", "url2"]
    }
  }'
```

## Query Tips

Exa understands natural language. Write queries as if asking a knowledgeable person:

| Instead of | Try |
|------------|-----|
| `"LLM fine tuning"` | `"tutorials on how to fine-tune large language models"` |
| `"react hooks"` | `"best practices for using React hooks in production"` |
| `"startup funding"` | `"guides for raising seed funding for AI startups"` |

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

## Best Practices

1. **Use EXA_ANSWER for questions**: When you need a direct answer with citations
2. **Use EXA_SEARCH for exploration**: When you need multiple results to analyze
3. **Be specific**: "Python libraries for PDF text extraction" > "PDF Python"
4. **Use filters**: Narrow by domain or date for recent/authoritative sources
