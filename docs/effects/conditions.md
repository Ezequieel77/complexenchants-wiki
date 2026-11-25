# Conditions

Each condition is one line `name: value`. All must be true; use `any:` (at least one) and `not:`
for other logic:

```yaml
conditions:
  - health_below: 30%
  - any:
      - in_water: true
      - y_between: "-64-40"
  - not:
      sneaking: true
```

| Condition | Value | Needs |
|---|---|---|
| `health_below`, `health_above` | amount (`6`) or % of max health (`50%`) | — |
| `victim_health_below`, `victim_health_above` | same | victim |
| `attacker_health_below`, `attacker_health_above` | same | attacker |
| `victim_type`, `attacker_type` | list of entity types, tags (`"#minecraft:undead"`) or `mob`, `monster`, `animal` | victim / attacker |
| `victim_is_boss` | `true` / `false` (Wither, Ender Dragon) | victim |
| `attacker_holding`, `victim_holding` | list of items or tags in the attacker's / victim's main hand | attacker / victim |
| `has_potion`, `victim_has_potion`, `attacker_has_potion` | list of active potion effects (any of them) | — / victim / attacker |
| `potion_type` | list of potion effects: the incoming one is one of them | `potion_gain` trigger |
| `damage_cause` | list of damage causes (`fall`, `lava`, `fly_into_wall`, `projectile`…) or groups: `fire` (fire, lava, magma block, campfire), `explosion` | damage |
| `is_projectile`, `critical`, `headshot` | `true` / `false`: the damage comes from a projectile, is a critical hit, the projectile hit the head | damage |
| `sneaking`, `sprinting`, `on_ground`, `in_water`, `underwater`, `on_fire`, `blocking`, `gliding`, `using_item`, `charging` | `true` / `false` (`underwater` = head under water; `using_item` = holding use on an item: charging a spear, drawing a bow, eating, shield up…; `charging` = charging a spear and the charge is still active: once the spear "gets tired", it stops counting even if you keep holding) | — |
| `in_world` | list of world names; `*` matches any text (`"dungeon_*"`) | — |
| `in_biome` | list of biomes | — |
| `time` | `day` / `night` | — |
| `weather` | `clear` / `rain` / `thunder` | — |
| `y_between` | range: `"0-64"` or `[0, 64]` | — |
| `light_below`, `light_above` | number 0–15 | — |
| `block_type` | list of blocks or tags (`"#minecraft:logs"`) | block |
| `block_natural` | `true` / `false`: no player placed the block (blocks that existed before this version count as natural; pistons and falling sand/gravel keep the mark) | block |
| `crop_grown` | `true` / `false`: the block is a fully grown crop (wheat, carrots, potatoes, beetroots, nether wart, cocoa, sweet berries) | block |
| `holding` | list of item groups (from item-groups.yml) held in the main hand | — |
| `consumed_item` | list of items or tags (`golden_apple`, `"#minecraft:..."`) | `consume` trigger |
| `has_permission` | list of permissions (needs all) | — |
| `level_above`, `food_above` | number | — |
| `in_combat` | `true` / `false` | — |
| `in_zone` | list of zones (from `zone`; any of them) | — |
| `has_mark`, `victim_has_mark`, `attacker_has_mark` | list of marks (any of them) | — / victim / attacker |
| `var_is` | variables and their value: `{ mode: tank, stacks: 3 }` (all must match; unset = 0) | — |
| `expression` | formula; true if it isn't 0 | — |
