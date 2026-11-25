# Targets

| `target` | Who |
|---|---|
| `self` | you (default for most effects) |
| `victim` | the entity you hit or killed |
| `attacker` | whoever hit or killed you |
| `nearby` | entities around you (not you), nearest first |
| `block` | the block of the trigger (sounds, particles, lightning) |

`nearby` takes options:

```yaml
target:
  type: nearby
  radius: 6          # blocks, 0.5–32 (default 5)
  max: 5             # entities, 1–64 (default 10)
  entities: [monster]   # optional filter (see victim_type below)
```

If the target doesn't exist in that event (a death with no attacker), the effect doesn't run.
