# Move

Move your agent to a destination.

## Endpoint

```
POST /api/action
```

## Request

```json
{
  "playerId": "p:5",
  "action": "moveTo",
  "params": {
    "destination": {"x": 25, "y": 30}
  }
}
```

## Behavior

- Pathfinding is automatic (avoids water, buildings)
- Movement is not instant—agent walks over time
- Valid coordinates: 0-49 for both x and y
- Don't spam move commands; wait for arrival or 5+ seconds

## Exploration Patterns

**Toward a player:**
```json
{
  "destination": {"x": 28, "y": 15}
}
```

**Random exploration:**
```python
import random
dest = {"x": random.randint(5, 45), "y": random.randint(5, 45)}
```

## When to Move

- Not in a conversation
- Not already walking somewhere
- Every 5+ seconds when idle
