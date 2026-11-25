# Effect groups

Each effect rolls its own chance and has its own cooldown. To make several effects happen **together or not at
all** (+50 % damage **and** slowness on the same roll), or to build **sequences with delays**, group them:

```yaml
effects:
  - effect: group
    trigger: projectile_attack
    chance: "11 + level"       # ONE roll for the whole group
    cooldown: "9 - level"      # ONE cooldown for the whole group
    conditions:                # checked once
      - victim_type: [player]
    effects:
      - effect: damage_bonus
        percent: "40 + 10 * level"
      - effect: potion
        target: victim
        potion: slowness
        amplifier: 4
        duration: "level"
      - effect: sound
        sound: entity.ghast.scream
        delay: 0.5             # wait 0.5 s before this effect and the ones after it
```

- The group has `trigger`, `chance`, `cooldown`, `cooldown-message`, `conditions` and `levels` (and `every` with
  `interval`). Its effects do **not** take `trigger`, `chance`, `cooldown` or `every` (load error).
- Each effect in the group can have its own `target`, `conditions` (they only filter that effect), `levels` and
  a `delay` in seconds. Delays add up: 60 s in total at most.
- Effects that change the event itself (`damage_bonus` and the other damage effects, `cancel_event`, drops,
  experience, mining) **can't come after a delay**: the event is over by then (load error).
- After a delay, if you disconnect or die, the rest doesn't run; if a step's target no longer exists (it died or
  despawned), that step is skipped. `/ce reload` cancels pending delays.
- Formulas use the values from the moment of the trigger (`damage`, `health`…), even after a delay.
- If an effect in the group has an error, the whole group is discarded. A group can't contain another group.
- In `/ce debug` and `<value:…>`, step 3 of group 2 is `2.3`.

## Reusable groups: effect-groups.yml

A group used by several enchantments is written once in `effect-groups.yml` and used with `use:`:

```yaml
# effect-groups.yml
stun:
  - effect: potion
    target: victim
    potion: slowness
    amplifier: 3
    duration: "1 + level"
  - effect: sound
    sound: entity.iron_golem.hurt

# enchants/hammer.yml
effects:
  - effect: group
    trigger: melee_attack
    chance: "5 * level"
    use: stun
```

Each enchantment that uses it compiles it with **its** trigger and **its** levels (`level` is that
enchantment's level). If a group doesn't fit an enchantment's trigger, the error says which one:
`effect-groups.yml (enchants/hammer.yml)`.
