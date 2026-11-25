# Debugging and limitations

## Debugging: /ce debug

`/ce debug` (permission `complexenchants.command.debug`, op) shows in your chat every one of **your**
effects that runs, or why it didn't: cooldown (seconds left), the condition that failed, the chance roll,
no target, or another plugin cancelling it. Run it again to turn it off.

To show variables, marks, cooldowns or combat on a scoreboard or TAB, use the PlaceholderAPI placeholders
`%ce_var_<name>%`, `%ce_mark_<name>%`, `%ce_cooldown_<enchant>%`, `%ce_skill_cooldown_<enchant>%` and
`%ce_in_combat%` ([README](../placeholders.md)).

## Limitations

- **Players only**: mobs wearing enchanted items don't run effects (yet).
- **`interval` runs once per second** (`every` 1 at least; a decimal waits for the next whole second). Changes like
  `forward_speed` or a spear getting tired can take up to a second to be noticed.
- **Plugins that change damage after ComplexEnchants** (`HIGHEST`/`MONITOR`) change its result.
  ComplexEnchants applies damage at `HIGH` and never at `MONITOR`, on purpose.
- **Permanent potions** are recognised by their signature (infinite, ambient, no particles). If another
  plugin gives exactly the same kind of potion, removing the item could remove it too. It's unlikely; use
  `attribute` when there is one (speed, health…).
- **Particles that need extra data** (colour, block) aren't supported yet.
- **Folia**: an effect on an entity or place in another region (a `nearby` target far away) is applied
  one tick later, in that region's thread. Area/vein blocks in another region are skipped.
