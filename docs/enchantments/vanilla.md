# Vanilla enchantments

`vanilla-enchants.yml` configures Minecraft's own enchantments. **Everything is optional: what you don't write
stays exactly as in Minecraft**, and the default file changes nothing in the game (it only has descriptions,
which are hidden by default).

```yaml
default:
  rarity: vanilla                 # rarity of the vanilla enchantments that don't set one

sharpness:
  # Visual (⟳ /ce reload)
  name: "<red>Sharpness"          # without it: Minecraft's name in each player's language
  rarity: rare                    # colour and position in the lore
  description: ["<gray>+<calc:level * 0.5 + 0.5> damage"]
  # Gameplay (⏻ restart; Paper's registry API, no reflection)
  max-level: 7                    # raising it is safe; lowering it keeps the levels items already have
  conflicts: [smite, complexenchants:life_bolt]   # replaces Minecraft's list; always mutual
  applicable: [swords, axes]      # item groups; replaces the items Minecraft allows
  weight: 10
  anvil-cost: 1
  table-cost: { min: {base: 1, per-level: 11}, max: {base: 21, per-level: 11} }
  sources: { enchanting-table: true, villagers: false }   # missing = as in Minecraft
  grindstone-removes: true

mending:
  enabled: false                  # never appears in the table, librarians, loot or fishing
```

- **How they look.** The rarity `vanilla` doesn't need to exist in `rarities.yml`: if it doesn't, vanilla
  enchantments look exactly like in Minecraft (grey, curses red, after the custom ones, in the item's order).
  Add a `vanilla:` rarity to `rarities.yml` to choose their colour and position, or give each one a `rarity`
  or a `name`: then they are shown like ours (colour, level in the same colour, sorted with `sort-by`).
- **Descriptions** are shown when `display.descriptions.vanilla` is `true` (and `items`/`books` allow it).
  `<calc:EXPRESSION>` is a number computed for the level (`level`, `+ - * / ^ ( )`, `min`, `max`, `round`,
  `floor`, `ceil`, `abs`); it also works in your own enchantments' descriptions, where it can also read their
  effects' values with `value(N, arg)` ([more](../effects/mechanics.md#values-in-the-description)).
- **Sources** are checked again at runtime, so turning one off works with `/ce reload`; turning one on, and the
  rest of the gameplay options, need a restart (`/ce reload` says which).
- `/ce info minecraft:sharpness` shows the effective configuration; menus can list vanilla enchantments
  (`vanilla:` in an `enchant-list`), `/customenchants sharpness` and right-clicking a book work with them.
- Enchantments of other plugins or datapacks (`namespace:id`) only accept the visual options.
