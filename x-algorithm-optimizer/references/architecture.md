# X Algorithm Technical Architecture

## Source Repositories

### twitter/the-algorithm (2023)
- **URL**: https://github.com/twitter/the-algorithm
- **Languages**: Scala (66.4%), Java (19.7%), Python (3.5%)
- **License**: AGPL-3.0
- **Stars**: 72.8k+
- **Contents**: Heavy Ranker ML model, candidate retrieval, SimClusters, TwHIN embeddings

### xai-org/x-algorithm (2025)
- **URL**: https://github.com/xai-org/x-algorithm
- **Languages**: Rust (62.9%), Python (37.1%)
- **License**: Apache 2.0
- **Stars**: 15.8k+
- **Contents**: Thunder, Phoenix, Home Mixer, Grok-based transformer

## Pipeline Architecture

```
User Request
    ↓
Home Mixer (Orchestration, Rust)
    ↓
┌─────────────────────────────────────┐
│  Thunder (In-Network)               │
│  - Kafka event consumer             │
│  - In-memory post store             │
│  - Sub-millisecond retrieval        │
│  - Posts from followed accounts     │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  Phoenix (Out-of-Network)           │
│  ┌─────────────────────────────┐   │
│  │ Stage 1: Retrieval          │   │
│  │ - Two-tower model           │   │
│  │ - User tower: history →     │   │
│  │   embeddings                │   │
│  │ - Content tower: post →     │   │
│  │   embeddings                │   │
│  │ - Dot product similarity    │   │
│  │ - Top-K candidate selection │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │ Stage 2: Ranking            │   │
│  │ - Grok-based transformer    │   │
│  │ - Predicts 15 engagement    │   │
│  │   probabilities             │   │
│  │ - Candidate isolation       │   │
│  │   (no cross-attention)      │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
    ↓
Scoring Pipeline:
1. Phoenix Scorer (ML predictions)
2. Weighted Scorer (combines predictions)
3. Author Diversity Scorer (reduces repeated authors)
4. Out-of-Network Scorer (adjusts non-followed accounts)
    ↓
Final Ranked Feed
```

## Heavy Ranker Weight Configuration

From `twitter/the-algorithm-ml` commit `b852108`:

```python
scored_tweets_model_weight_fav: 0.5
scored_tweets_model_weight_retweet: 1.0
scored_tweets_model_weight_reply: 13.5
scored_tweets_model_weight_good_profile_click: 12.0
scored_tweets_model_weight_video_playback50: 0.005
scored_tweets_model_weight_reply_engaged_by_author: 75.0
scored_tweets_model_weight_good_click: 11.0
scored_tweets_model_weight_good_click_v2: 10.0
scored_tweets_model_weight_negative_feedback_v2: -74.0
scored_tweets_model_weight_report: -369.0
```

## 15 Predicted Engagement Types

The Grok transformer predicts probabilities for:

1. Liking
2. Replying
3. Reposting (retweeting)
4. Quote tweeting
5. Clicking (on media/links)
6. Profile visiting
7. Video watching
8. Photo expanding
9. Sharing (externally)
10. Dwelling (time spent)
11. Following
12. "Not interested" clicking
13. Blocking
14. Muting
15. Reporting

## Scoring Formula

```
Final Score = Σ (weight_i × P(action_i))
```

Where:
- `weight_i` = configured weight for action type i
- `P(action_i)` = predicted probability of action i

Positive actions (like, repost, reply) have positive weights.
Negative actions (block, mute, report) have negative weights.

## Candidate Isolation

Key architectural decision: "Each post can only attend to the user's context. It cannot attend to other candidates in the same batch."

This ensures:
- Score consistency regardless of batch composition
- Cacheable scores for efficiency
- Posts compete against "silence", not each other

## Premium/Verified Multipliers

From source code analysis (2023-2024):
- **Blue Verified (X Premium)**: 4x boost (reduced to 2x in some contexts)
- Applied as final multiplier after engagement scoring

## For You Timeline Composition

Approximate split:
- **50% In-Network** (Thunder): Posts from accounts you follow
- **50% Out-of-Network** (Phoenix): Discovered posts from ML retrieval

## Recent Changes (2025)

The xAI release indicates:
- "Eliminated every single hand-engineered feature"
- "Most heuristics" removed from the system
- Grok transformer learns relevance patterns directly from engagement history
- No disclosed specific weights (model learns them)
