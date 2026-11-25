# Creating an enchantment

Copy `enchants/_example.yml` (files starting with `_` are not loaded) and rename it. **The file name is
the id**: `life_bolt.yml` becomes `complexenchants:life_bolt`. Use only lowercase letters, numbers and `_`.

```yaml
enabled: true
name: "Life Bolt"                 # the rarity colour is added automatically
description:
  - "<gray>Strikes with the power of life."
rarity: epic                      # from rarities.yml
max-level: 3
applicable: [swords, axes]        # item groups from item-groups.yml
conflicts: [other_enchant, minecraft:sharpness]
mode: INHERIT                     # BOOKS | VANILLA | INHERIT
anvil-cost: 4
sources:                          # VANILLA sources (each also needs its switch in config.yml)
  enchanting-table: true
  villagers: true
  loot: true
  fishing: false
book-chances:                     # BOOKS mode: "50", "40-80" or "random" (destroy = 100 − success)
  success: "40-80"
```

The template documents every option.

> **Never delete an enchantment that players already have.** Set `enabled: false` instead. If you do
> delete a file, ComplexEnchants remembers the enchantment (`data/known-enchants.yml`) and keeps it
> registered, so items that have it are not broken; it shows as "removed" in their lore.

## In-game editor

`/ce editor` (permission `complexenchants.editor`, op) edits the same files without leaving the game: chest menus
to move around and Minecraft's own forms (dialogs, 1.21.6+) to edit. Its start screen has four buttons:

- **Enchantments**: every enchantment (disabled ones in grey, "waiting for a restart" marked), by rarity and id,
  with a rarity filter, a search (id or name) and files that failed to load at the end (click: their problems).
  Click one to open it:
  - **Properties**: name, description, rarity, max level, applicable groups, conflicts, where it is active.
  - **Sources and book**: mode, the four sources, book success chance, weight, anvil cost, grindstone.
  - **Effects**: one item per effect. Click to edit, Shift + left/right click to move it, right click to remove it.
    "Add" asks for the effect, then the trigger (only compatible ones), then its form. Moving or removing an effect
    renumbers the `<value:N:…>` tags of the description.
  - Enable/disable, duplicate (asks for the new id) and its warnings.
  - **Create** (in the list): id, name, description, rarity, max level and groups. The file only has that; the rest
    comes from its rarity.
- **Rarities**, **Item groups** and **Vanilla enchantments**: the same forms for `rarities.yml`, `item-groups.yml`
  and `vanilla-enchants.yml`. A rarity or group in use can't be removed (it says who uses it); "Reset" removes a
  vanilla enchantment's section, so it is like in Minecraft again.

Every change is checked with the real loaders before saving: with errors, the form opens again with them and with
what you wrote. Saving writes the file (a copy of the previous one goes to `backups/editor/`, the last 10 per file)
and applies it like `/ce reload`; what needs a restart is marked ⏻. If someone changed the file since you opened it,
nothing is overwritten and you are told. Nothing is deleted from the editor: to remove an enchantment, use its file.

Advanced parts are shown read-only and kept as they are when you save the rest: effect groups with steps or
delays, `levels:`, `any:`/`not:` conditions, named groups (`use:`), `active-skill` and targets with options. A file
saved from the editor keeps its comments, but its style may change (quotes, lists).

> **The editor is as powerful as the console**: the `command` effect runs console commands. Give
> `complexenchants.editor` only to trusted admins. Bedrock players (Geyser) don't see dialogs properly.
