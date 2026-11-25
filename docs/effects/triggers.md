# Triggers

| Trigger | When | Offers |
|---|---|---|
| `melee_attack` | you hit something in melee | damage, victim, cancellable |
| `projectile_attack` | your arrow/trident hits something. The enchantments of the **weapon that launched it** count (even if it is no longer in your hand, like a thrown trident), plus your armour's | damage, victim, cancellable |
| `take_damage` | you take any damage | damage, cancellable |
| `take_entity_damage` | a mob or player damages you | damage, attacker, cancellable |
| `fall_damage` | you take fall damage | damage, cancellable |
| `kill` | you kill something | victim, drops, experience |
| `death` | you die | attacker (if there is one) |
| `mine_block` | you break a block | block, experience, cancellable |
| `block_drops` | a block you broke drops its items | block, drops |
| `shoot` | you shoot a bow or crossbow | cancellable |
| `shield_block` | you block with a shield | damage (read only: the hit before the shield), attacker, cancellable |
| `item_damage` | the **enchanted item** loses durability | cancellable |
| `fish` | you catch something | experience, cancellable |
| `consume` | you eat or drink | cancellable |
| `sneak` | you start sneaking | — |
| `jump` | you jump | cancellable |
| `right_click` | you right-click with the main hand | clicked block (if any), cancellable |
| `interval` | every `every` seconds while the item is active | — |
| `fatal_damage` | a hit is about to kill you (fully calculated); cancelling it saves you (and no totem is used) | damage (read only), attacker if any, cancellable |
| `totem_use` | a totem is used (cancelling it = it doesn't save you) | cancellable |
| `hunger_loss`, `hunger_gain` | your hunger goes down / up | cancellable |
| `projectile_launch` | you launch any projectile (arrow, trident, pearl, snowball…) | cancellable |
| `combat_enter`, `combat_leave` | you enter / leave combat (see `combat:` in config.yml) | — |
| `world_change` | you change worlds | — |
| `block_place` | you place a block | block, cancellable |
| `projectile_hit_block` | your projectile hits a block (the weapon that launched it counts) | block |
| `shield_disable` | your shield gets disabled (by an axe, for example) | attacker, cancellable |
| `item_break` | the **enchanted item** is about to break with this wear; cancelling it saves it | cancellable |
| `active_skill` | the player activates the skill ([active skills](skills.md)) | — |
| `potion_gain` | a potion effect is about to be applied to you (new, renewed or stronger), from any source; removing it or it running out doesn't count. With `cancel_event` it isn't applied | potion, cancellable |

Effects and conditions that need something the trigger doesn't offer are rejected when loading, with the
list of triggers that would work. Triggers react only if the event wasn't cancelled by another plugin
(protections, claims…).
