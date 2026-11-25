# Effects reference

Arguments with a value in brackets are optional; that's their default.

## Combat

| Effect | Arguments | Target | Notes |
|---|---|---|---|
| `damage_bonus` | `percent` | — | +% damage. Damage triggers. |
| `add_damage` | `amount` | — | + flat damage. |
| `damage_reduction` | `percent` | — | −% damage received. |
| `negate_damage` | `amount` | — | − flat damage received. |
| `lifesteal` | `percent` | — | Heals that % of the **final** damage you deal. `melee_attack`, `projectile_attack`. |
| `heal` | `amount` | self | |
| `damage` | `amount`, [`bypass-armor`: false] | victim | Deals damage (protections and PvP are respected). `bypass-armor: true` = magic damage: armor neither reduces it nor wears out (totems still save). |
| `potion` | `potion`, `duration` (s), [`amplifier`: 0], [`particles`: true] | self | Amplifier 0 = level I. |
| `remove_potion` | `potion` | self | Removes that potion effect from the target. |
| `ignite` | `duration` (s) | victim | |
| `lightning` | [`damage`: false] | victim | Visual only; with `damage: true` it deals 5 damage to the target only (no fire, nobody else). |
| `knockback` | [`strength`: 1] | victim | Pushes away from you; negative pulls. |
| `bleed` | `damage`, [`interval`: 1] (s), [`times`: 3] | victim | Stops if the target dies. |
| `set_damage` | `amount` | — | The base damage becomes this; the other damage effects apply after it. |
| `freeze` | `duration` (s), [`lock`: true] | victim | Frozen like in powder snow: slow and, fully frozen, damage. `lock: true` = maxed for `duration`; `lock: false` = that many seconds of freezing that thaw by themselves (like AE's `SCREEN_FREEZE`). |
| `explode` | [`power`: 2] (TNT = 4, max 8), [`fire`: false], [`break-blocks`: false] | victim | Never hurts you; with `break-blocks`, protections decide. |
| `pumpkin_head` | `duration` (s) | victim | Players only. Their helmet always comes back (when it ends, on quit, on death, after a crash). |

The first five go through the [damage calculation](mechanics.md#how-damage-is-calculated).

## Tools

| Effect | Arguments | Triggers | Notes |
|---|---|---|---|
| `area_mining` | [`radius`: 1], [`depth`: 0], [`blocks`: any] | `mine_block` | A (2r+1)² wall in front of you; looking up/down, a floor. `depth` adds layers. `blocks` limits which blocks it breaks (crops only, for example). |
| `plant_seeds` | [`radius`: 1] (max 5), [`seeds`: any] | triggers with a block | Plants on the free farmland (and nether wart on soul sand) around the block, with the seeds in your inventory. Protections decide each one. |
| `vein_mining` | [`max`: 16], [`blocks`: any] | `mine_block` | Connected blocks of the same type, also diagonally. `blocks` limits which veins (blocks or tags). |
| `autosmelt` | — | `block_drops`, `kill` | Uses the server's furnace recipes (datapacks included). |
| `telekinesis` | — | `block_drops`, `kill` | Drops to your inventory (with `kill`, the experience too). What doesn't fit stays on the ground. |
| `multiply_drops` | [`multiplier`: 2], [`blocks`: any] | `block_drops`, `kill` | Decimals are a chance: ×1.5 on 3 items gives 4 or 5. |
| `xp_multiplier` | `multiplier` | `mine_block`, `kill`, `fish` | |

## Passive (no trigger)

| Effect | Arguments | Notes |
|---|---|---|
| `attribute` | `attribute`, `amount`, [`operation`: add] | `add`, `multiply_base` or `multiply`. Speed, max health, armour, damage, reach… |
| `permanent_potion` | `potion`, [`amplifier`: 0] | Infinite, no particles. |

## Utility

| Effect | Arguments | Target |
|---|---|---|
| `message` | `text` | self |
| `actionbar` | `text` | self |
| `title` | `title`, [`subtitle`: ""], [`fade-in`: 0.5], [`stay`: 2], [`fade-out`: 0.5] (s) | self |
| `sound` | `sound`, [`volume`: 1], [`pitch`: 1] | self |
| `particle` | `particle`, [`count`: 10], [`spread`: 0.5] | self |
| `command` | `command`, [`as`: console] (`console` or `player`) | self (once per target) |
| `cancel_event` | — (cancellable triggers) | — |
| `repair` | `amount` | — (the enchanted item) |
| `damage_item` | `amount` | — (the enchanted item) |
| `give_xp` | `amount` | self |
| `mark` | `name`, `duration` (s) | self |
| `remove_mark` | `name` | self |
| `set_var` | `name`, `value` (formula) **or** `text` (text), [`persistent`: true] | — |
| `add_var` | `name`, `amount`, [`persistent`: true] | — |
| `reset_cooldown` | [`enchant`: this one] | — |
| `temp_attribute` | `attribute`, `amount`, `duration` (s), [`operation`: add] | self | They stack; never saved on the player. |
| `drop_item` | `item`, [`amount`: 1] | self (or `block`, `victim`…) | Dropped at the target. |
| `repair_armor`, `damage_armor` | [`amount`: 0], [`percent`: 0], [`slot`: all] (`all`, `head`, `chest`, `legs`, `feet`) | self | The target's armour (all, or one piece). `percent`: % of the durability each piece has left (damage) or is missing (repair), rounded down, so the % alone never breaks a piece. |
| `cancel_armor_damage` | — | — | Your armour takes no wear from this hit. |
| `remove_enchant` | [`enchant`: this one] | — | Removes it from the item that has it (a Phoenix that gets used up). |
| `velocity` | [`strength`: 1], [`direction`: look] (`look`, `up`, `forward`), [`add`: true], [`no-fall`: false] | self | A push where you look, up, or forward. `add: false` sets the velocity instead of adding to it; `no-fall` spares the next fall (like AE's `BOOST`: `BOOST:10` = `strength: 1`). |
| `temp_block` | `block`, [`radius`: 0] (max 5), `duration` (s) | self | A (2r+1)² square at the target's feet. Air only; can't be broken, moved or blown up; always turns back into air (also after a crash). |
| `jail` | `block`, [`shape`: cuboid] (`cuboid`, `sphere`), [`radius`: 3], [`height`: 3], [`roof`: true], `duration` (s) | victim | A cage around the target, with the same rules as `temp_block`. |
| `zone` | `name`, [`shape`: circle] (`circle`, `square`), `radius`, `duration` (s), [`particle`] | self | Temporary zone for the `in_zone` condition; the particle draws its edge. |
| `launch_projectile` | [`entity`: arrow], [`speed`: 3], [`fuse`: 4], [`break-blocks`: false] | — | Launches a projectile from your eyes (arrow, trident, TNT, fireball, pearl…). Can't be picked up. |
| `replace_projectile` | [`entity`: arrow], [`fuse`: 4], [`break-blocks`: false] | — | `projectile_launch` only: swaps the projectile for another (TNT instead of an arrow; a "ghost" trident that never leaves your hand). |
| `bossbar` | `id`, `text`, [`color`: white], [`style`: solid], [`progress`: 1], [`duration`: 0] | self | Creates or updates the bar with that id. Ask for it every second with `duration: 2` to show it while the item is worn. `duration: 0` = until `bossbar_remove`. |
| `bossbar_remove` | `id` | self | |

- **Text** (`message`, `actionbar`, `title`) is MiniMessage with `<player>`, `<target>`, `<victim>`,
  `<attacker>`, `<level>` and `<var:name>` (one of your variables).
- **`command`** has the same placeholders as plain text. For mobs, `<victim>`, `<attacker>` and `<target>`
  are their UUID, never their name: a custom name can't sneak arguments into a console command.
- **`particle`** only accepts particles without extra data (no `dust` or `block` for now).
- **Unbreaking-like**: `cancel_event` with the `item_damage` trigger and a `chance`. It only protects
  the item that has the enchantment.
