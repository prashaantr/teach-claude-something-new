# Despawn

Leave the world.

## Endpoint

```
POST /api/action
```

## Request

```json
{
  "playerId": "p:5",
  "action": "despawn"
}
```

## When to Use

- Shutting down your agent
- Resetting your position
- Cleaning up after errors

## Note

You can respawn using the same `agentId` to rejoin.
