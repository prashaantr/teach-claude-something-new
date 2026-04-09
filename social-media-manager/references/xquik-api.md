# Xquik API Reference

Complete endpoint reference for X (Twitter) via Xquik.

## Authentication

```bash
curl -X POST "https://xquik.com/api/v1/..." \
  -H "x-api-key: xq_YOUR_KEY" \
  -H "Content-Type: application/json"
```

## Write Actions (10 credits each)

### Tweet Composer - Post a tweet
```bash
POST /api/v1/x/tweets
{
  "account": "@prashaant_x",
  "text": "Your tweet content",
  "reply_to_tweet_id": "OPTIONAL_TWEET_ID",  # For replies
  "attachment_url": "https://...",            # Optional link card
  "community_id": "COMMUNITY_ID",             # Optional community post
  "media_ids": ["id1", "id2"]                 # Optional media (upload first)
}
```

### Tweet Liker - Like a tweet
```bash
POST /api/v1/x/tweets/{tweet_id}/like
{
  "account": "@prashaant_x"
}
```

### Tweet Unliker - Remove like
```bash
POST /api/v1/x/tweets/{tweet_id}/unlike
{
  "account": "@prashaant_x"
}
```

### Tweet Retweeter - Retweet
```bash
POST /api/v1/x/tweets/{tweet_id}/retweet
{
  "account": "@prashaant_x"
}
```

### Tweet Unretweeter - Remove retweet
```bash
POST /api/v1/x/tweets/{tweet_id}/unretweet
{
  "account": "@prashaant_x"
}
```

### Tweet Deleter - Delete your tweet
```bash
DELETE /api/v1/x/tweets/{tweet_id}
{
  "account": "@prashaant_x"
}
```

### User Follower - Follow a user
```bash
POST /api/v1/x/users/{user_id}/follow
{
  "account": "@prashaant_x"
}
```
Note: Requires numeric user ID, not username. Get ID from user profile endpoint first.

### User Unfollower - Unfollow
```bash
POST /api/v1/x/users/{user_id}/unfollow
{
  "account": "@prashaant_x"
}
```

### DM Sender - Send direct message
```bash
POST /api/v1/x/dm/{user_id}
{
  "account": "@prashaant_x",
  "text": "Your message"
}
```

### Media Uploader - Upload image/video
```bash
POST /api/v1/x/media
Content-Type: multipart/form-data
{
  "account": "@prashaant_x",
  "file": <binary>
}
```
Returns `media_id` to use in tweet.

### Profile Editor - Update profile
```bash
PATCH /api/v1/x/profile
{
  "account": "@prashaant_x",
  "name": "New Name",
  "bio": "New bio",
  "location": "New location",
  "url": "https://..."
}
```

### Avatar Updater
```bash
PATCH /api/v1/x/profile/avatar
Content-Type: multipart/form-data
{
  "account": "@prashaant_x",
  "file": <binary>
}
```

### Banner Updater
```bash
PATCH /api/v1/x/profile/banner
Content-Type: multipart/form-data
{
  "account": "@prashaant_x",
  "file": <binary>
}
```

## Read Actions (1-7 credits)

### Get User Profile
```bash
GET /api/v1/x/users/{username}
```
Returns: id, username, name, followers, following, bio, profile_picture, etc.

### Get User's Tweets
```bash
GET /api/v1/x/users/{user_id}/tweets?limit=20
```

### Get User's Likes
```bash
GET /api/v1/x/users/{user_id}/likes?limit=20
```

### Get User's Media
```bash
GET /api/v1/x/users/{user_id}/media?limit=20
```

### Get Single Tweet
```bash
GET /api/v1/x/tweets/{tweet_id}
```

### Search Tweets
```bash
GET /api/v1/x/tweets/search?query=AI+agents&limit=50
```

### Get Tweet Replies
```bash
GET /api/v1/x/tweets/{tweet_id}/replies?limit=50
```

### Get Quote Tweets
```bash
GET /api/v1/x/tweets/{tweet_id}/quotes?limit=50
```

### Get Tweet Thread
```bash
GET /api/v1/x/tweets/{tweet_id}/thread
```

### Get Home Timeline
```bash
GET /api/v1/x/timeline?limit=30
```

### Get Notifications
```bash
GET /api/v1/x/notifications
```

### Get Followers
```bash
GET /api/v1/x/users/{user_id}/followers?limit=100
```

### Get Following
```bash
GET /api/v1/x/users/{user_id}/following?limit=100
```

## Extraction (Bulk Data)

### Estimate First
```bash
POST /api/v1/extractions/estimate
{
  "type": "follower_explorer",
  "params": {"username": "anthropic"}
}
```

### Create Extraction
```bash
POST /api/v1/extractions
{
  "type": "follower_explorer",
  "params": {"username": "anthropic"}
}
```

Extraction types:
- `follower_explorer` - Account followers
- `following_explorer` - Account following
- `post_extractor` - User's posts
- `reply_extractor` - Tweet replies
- `quote_extractor` - Quote tweets
- `mention_extractor` - Mentions of account
- `tweet_search_extractor` - Bulk search

### Get Extraction Status
```bash
GET /api/v1/extractions/{extraction_id}
```

### Get Results
```bash
GET /api/v1/extractions/{extraction_id}/results?limit=100
```

## Monitoring

### Create Monitor
```bash
POST /api/v1/monitors
{
  "username": "anthropic",
  "events": ["tweet.new", "tweet.reply"]
}
```

### Get Events
```bash
GET /api/v1/events
```

## Response Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Invalid input |
| 401 | Unauthenticated |
| 402 | No subscription / usage limit |
| 500 | Write failed (retry or reauth account) |

## Rate Limits

- Read: 120/minute
- Write: 30/minute
- Delete: 15/minute

## Pricing

- $20/month base
- Write actions: 10 credits
- Read actions: 1-7 credits
- 1 credit = $0.00015
