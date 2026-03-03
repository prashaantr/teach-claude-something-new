---
name: x-algorithm-optimizer
description: Optimize posts for X (Twitter) using verified algorithm weights and architecture from the open-source codebase. Use when writing tweets, planning X content strategy, analyzing why posts underperform, or optimizing posts for reach. Triggers on "tweet", "X post", "Twitter", "viral", "engagement", "algorithm", "reach", "timeline", "For You feed".
---

# X Algorithm Optimizer

Optimize X posts using verified data from the open-source algorithm repositories:
- [twitter/the-algorithm](https://github.com/twitter/the-algorithm) (2023, Scala)
- [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) (2025, Rust/Python, Grok-based)

## Verified Engagement Weights

From the Heavy Ranker source code (relative scoring):

| Signal | Weight | Interpretation |
|--------|--------|----------------|
| Reply engaged by author | **75.0** | Author replies to your reply |
| Reply | **13.5** | You reply to the post |
| Profile click | **12.0** | Visit author's profile |
| Conversation click | **11.0** | Click into thread |
| Conversation dwell (2+ min) | **10.0** | Read thread deeply |
| Retweet | **1.0** | Baseline amplification |
| Like | **0.5** | Passive endorsement |
| Video 50% completion | **0.005** | Watch half the video |
| Negative feedback | **-74.0** | "Show less often" / mute |
| Report | **-369.0** | Report the post |

**Key insight**: One reply-with-author-engagement = 150 likes = 75 retweets.

## Architecture: Thunder + Phoenix

### Thunder (In-Network)
- In-memory post store consuming Kafka events
- Sub-millisecond retrieval of posts from accounts you follow
- ~50% of For You timeline comes from in-network

### Phoenix (Out-of-Network)
- **Retrieval**: Two-tower model matches user embeddings to content embeddings
- **Ranking**: Grok-based transformer predicts 15 engagement types
- Enables viral distribution to non-followers
- ~50% of For You timeline comes from out-of-network

## Post Optimization Checklist

### 1. Hook (First 50 characters)
The transformer model uses early stopping patterns. Optimize for scroll-stop:
- Start with contrarian/unexpected statement
- Use specific numbers over vague claims
- Remove hedging words ("I think", "maybe", "perhaps")

### 2. Trigger Replies (Weight: 13.5-75x)
Replies dominate the scoring formula. End posts with:
- Direct question ("What's your take?")
- Debate frame ("Change my mind")
- Experience prompt ("Drop yours below")
- Unfinished list ("What's #3?")

### 3. Enable Reposts (Weight: 1x, but distribution multiplier)
Include 1-2 standalone quotable lines that work when shared without context.

### 4. Avoid Negative Signals (Weight: -74 to -369)
- Strong opinions invite engagement
- Offensive content triggers blocks/reports
- One report erases ~369 likes in scoring

### 5. Timing
Post when followers are online to maximize initial velocity. Phoenix activation requires strong early signals.

## What the Reddit Post Got Wrong

Common misinformation circulates about X algorithm "weights" using a 1-10 scale. The actual weights from source code are:
- NOT "Reposts 8/10, Replies 7/10, Likes 6/10"
- ACTUAL: Reposts 1.0, Replies 13.5, Likes 0.5 (replies are 27x more valuable than reposts)

The "19 signals" categorization and specific "velocity threshold" formulas are not in the open-source code.

## Premium/Verified Boost

From source code: Blue Verified accounts receive a 2-4x multiplier on their final score, applied after engagement weights.

## References

For detailed technical architecture, see [references/architecture.md](references/architecture.md).
