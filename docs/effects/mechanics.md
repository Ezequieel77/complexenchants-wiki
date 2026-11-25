# How effects work

## How damage is calculated

All damage effects of **one hit** (the attacker's and the victim's) only note their part, and the
damage is calculated **once**, always in this order:

```
base damage
+ add_damage
× (1 + bonus)          sum of damage_bonus
× (1 − reduction)      sum of damage_reduction (capped)
− negate_damage
never below 0
```

Minecraft's armour, Protection and Resistance then apply as usual. The result never depends on the order
of the effects. In `config.yml`:

```yaml
damage:
  bonus-stacking: ADD        # ADD: they add up (15% × 4 = 60%). MULTIPLY: like other plugins.
  reduction-stacking: ADD
  max-bonus: ""              # empty = no cap
  max-reduction: 75%         # the reduction can never go above 100% (damage never heals)
```

Damage dealt by effects (`damage`, `lightning`, `bleed`) is normal Minecraft damage, so protections and
PvP settings see it, but it **never triggers more effects**: two players with "thorns" never bounce damage
back and forth forever.

## Tools: area, vein and drops

- **Which blocks an area or vein breaks**: blocks your tool mines properly, never unbreakable ones
  (bedrock), and at most twice as hard as the one you mined. Mining stone also breaks the ores around it,
  but not obsidian.
- **Protections decide block by block**: each extra block is broken as if you broke it yourself (it
  passes protections, uses durability and drops normally). If a protection cancels the block you mined,
  nothing else breaks.
- **Limit**: at most `tools.max-blocks` blocks per action, counting the one you mined, nearest first
  (`config.yml`, default 64, absolute limit 512). The console warns when loading if a level could go over.
- **Drops are always applied in this order**: multiply → smelt → collect (telekinesis), whatever the order
  you write them in.

## Passive effects

Passive effects (`attribute`, `permanent_potion`) take no trigger: they're on while the item is active.

- Attribute changes are never saved on the player, so a crash can't leave "ghost" bonuses.
- Permanent potions come back after milk, a totem or `/effect clear`, and after respawning. They're removed
  when you log out and cleaned up on join if a crash left one behind. A stronger potion from another
  source (beacon, potion) is never removed.
- Their values can only depend on `level` (no `random`): they're calculated when you equip the item.

## Values in the description

The description can show an effect's values for the item's level, so you never have to write numbers
twice:

```yaml
description:
  - "<gray>+<value:1:percent>% damage (<value:1:chance>% chance)"
```

`<value:N:argument>`: N is the effect's number in the list (from 1, as in `/ce debug`; inside a group,
`<value:1.2:duration>` is the group's second effect); `chance` and `cooldown` also work. If the value depends on
the game (`"damage * 0.1"`) the formula is shown; if the tag is wrong, `?`.

**Calculations with those values**: inside `<calc:…>`, `value(N, argument)` is the same number, so you can do maths
with it:

```yaml
description:
  - "<gray>Up to <white><calc:value(1, percent) * 5>%</white> with 5 stacks"
```

If the value depends on the game, the whole `<calc>` shows `?`.

**Incompatible enchantments**: `<conflicts>` lists them, by name and in their colour (its `conflicts:` plus the
ones that name it). A description line with `<conflicts>` and nothing to list is removed.
