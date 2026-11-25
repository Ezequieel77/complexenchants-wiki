# Effects

What enchantments **do**: damage bonuses, potions, area mining, auto-smelt, permanent speed…
Effects live in each enchantment's file and are applied with `/ce reload` (no restart needed).

## Quick example

```yaml
# enchants/life_bolt.yml (the base options: see Creating an enchantment)
name: "Life Bolt"
rarity: epic
max-level: 5
applicable: [swords]
description:
  - "<gray>+<value:1:percent>% damage against weakened players"

effects:
  # +10% damage per level against players below half health, 15-25% of the time.
  - effect: damage_bonus
    trigger: melee_attack
    percent: "10 * level"
    chance: "15 + 2 * level"
    cooldown: 2
    conditions:
      - victim_type: [player]
      - victim_health_below: 50%

  # Slows the victim down.
  - effect: potion
    trigger: melee_attack
    target: victim
    potion: slowness
    duration: "1 + 0.5 * level"

  # While held: +5% speed per level.
  - effect: attribute
    attribute: movement_speed
    operation: multiply
    amount: "0.05 * level"
```

## Anatomy of an effect

| Key | Meaning |
|---|---|
| `effect` | Which effect ([reference](reference.md)). Required. |
| `trigger` | When it runs ([triggers](triggers.md)). Required, except for [passive effects](mechanics.md#passive-effects), which take none. |
| `target` | Who it applies to ([targets](targets.md)), for effects that use one. |
| `chance` | Chance in % (formula). Default 100. |
| `cooldown` | Seconds before it can run again, per player and per effect. It may only depend on `level`. |
| `cooldown-message` | `true` = show the remaining time in the action bar when it's on cooldown. |
| `conditions` | All must be true ([conditions](conditions.md)). |
| `levels` | Exact values for specific levels: `levels: { 5: { chance: 100 } }`. Any argument, `chance` or `cooldown`. |
| `every` | Only for the `interval` trigger: every how many seconds (minimum 1). |
| *other keys* | The effect's own arguments (`percent`, `potion`…). |

**Errors never half-run an effect.** If an effect has an error (unknown effect, a trigger it can't use,
a wrong formula, a broken condition…), that whole effect is skipped and the console says exactly where
and why; the rest keeps working. Unknown keys and out-of-range values are only warnings.

The order of checks when a trigger happens is: cooldown → conditions → chance → targets → effect. If an
effect does not run, its cooldown is not used up.

## Where an enchantment is active

Effects only work while the item is **worn or held in the right place**. A sword in a chest or in your
backpack does nothing, and enchanted books never do. Set it with `active-in` in the enchantment file:

| `active-in` | Active when the item is in… |
|---|---|
| `MAINHAND` | the main hand |
| `OFFHAND` | the off hand |
| `HANDS` | either hand |
| `ARMOR` | its armour slot |
| `ANY` | a hand or an armour slot |

If you leave it out it's deduced from `applicable`: armour → `ARMOR`, shields → `HANDS`, the rest →
`MAINHAND`. **Each piece counts on its own**: the same enchantment on 4 armour pieces runs 4 times
(so "15% reduction" on each piece = 60%).

## Formulas and levels

Any number can be a formula: `"10 + 5 * level"`, `"min(level, 3)"`, `"victim_health / victim_max_health < 0.3"`.

- **Operators**: `+ - * / % ^`, parentheses, comparisons `< <= > >= == !=`, and `&& || !` (true = 1, false = 0).
- **Functions**: `min`, `max`, `floor`, `ceil`, `round`, `abs`, `sqrt`, `clamp(value, min, max)`, `random(a, b)`,
  `nearby_players(radius)` (players nearby, not you), `nearby_entities(radius)` (living entities nearby, not you) and
  `nearby_enemies(radius)` (players nearby you could hurt right now: protections, PvP zones, factions and teams are
  asked, like a real hit, without hitting anyone); max radius 32; `var("name")` (your variable as a number), `mark_time("name")` (seconds left on one of your marks)
  and `cooldown("enchant")` (cooldown seconds you have left on that enchantment). Random, nearby, variable, mark and
  cooldown functions can't be used in passive effects.
- **Variables**:

| Variable | Available |
|---|---|
| `level` | always |
| `health`, `max_health`, `food`, `player_level`, `y` | every trigger (they are the player's) |
| `damage` | triggers with damage |
| `victim_health`, `victim_max_health` | triggers with a victim |
| `attacker_health`, `attacker_max_health` | triggers with an attacker |
| `distance` | triggers with a victim or an attacker |
| `speed` | always: your real speed in blocks/s (walking ~4.3, sprinting ~5.6, riding, falling…), measured from your positions over the last quarter of a second; standing still = 0 |
| `fall_distance` | always: blocks you have been falling (the mace's smash attack needs more than 1.5) |
| `forward_speed`, `side_speed` | always: your real horizontal speed (like `speed`) towards where you look (negative = backwards) and sideways (positive = to your right), in blocks/s |
| `victim_armor_pieces` | triggers with a victim: armour pieces they wear (0–4; elytra or a pumpkin don't count) |
| `potion_amplifier`, `potion_duration` | `potion_gain`: amplifier (0 = level I) and duration in seconds (infinite: -1) of the incoming effect |

Using a variable the trigger doesn't have is an error when loading, and the message lists the ones that
exist there. A result that isn't a number (division by zero…) counts as 0. Formulas that only use `level`
are calculated once when loading, so in game they cost the same as a plain number.
