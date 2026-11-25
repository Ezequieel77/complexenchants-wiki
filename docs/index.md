# ComplexEnchants

Custom enchantments for Paper, defined in YAML and registered as **real Minecraft enchantments**.
Use them the classic way (drag a book onto an item, with success and destroy chances) or the
vanilla way (enchanting table, anvil, villagers, loot), switchable globally or per enchantment.

Enchantments can also **do things**: damage bonuses, potions, area mining, auto-smelt, permanent speed
and more, with triggers, conditions, chances, cooldowns and per-level formulas. That part has its own
guide: **[Effects](effects/index.md)**.

## Features

- Enchantments are **real registry enchantments**: they show in the vanilla tooltip, make items
  glow, work with `/enchant` and are returned by `ItemStack#getEnchantments()`.
- **Two modes**, global and per enchantment:
  - **BOOKS**: drag books onto items, with success and destroy chances, plus an extractor, a
    catalyst, a transmuter (each of a rarity or generic) and a slot expander.
  - **VANILLA**: enchanting table, anvil, grindstone, librarian trades, chest loot and fishing.
- **Enchantment slots** per item group, with slot expanders.
- **Lore rendered in packets**: players see a formatted list (sorted by rarity, with descriptions)
  while the real item stays clean. An `ITEM` mode writes the lore into items for plugins that read it.
- **Menus** (`menus/`): enchantment lists by rarity (with a button to filter them by item), enchantment details
  and a **shop** selling random books by rarity for money (Vault) or experience. No menu plugin needed;
  PlaceholderAPI works if installed.
- **In-game editor** (`/ce editor`): create and edit enchantments, their effects, rarities, item groups and
  vanilla enchantments with chest menus and Minecraft's dialogs ([more](enchantments/creating.md#in-game-editor)).
- **Ready to play**: 112 enchantments, 7 rarities and their menus come with the plugin (installed on the first
  start; see [Installation](getting-started.md#installation)).
- **Deleted enchantments never break items**: they stay registered as "tombstones".
- **No required dependencies.** Vault (money in menus) and PlaceholderAPI (placeholders in menus, and our own placeholders) are optional.
- **Effects**: 32 triggers, 51 conditions and 55 effects (combat, tools, passives, utility), all reloadable
  with `/ce reload`. See [Effects](effects/index.md).
- **Folia** supported.
- All messages in **MiniMessage**, with English and Spanish included. `/ce help` lists the commands each player
  can use.
- Clear **configuration errors**: file, key, what was expected and what was used instead. A broken
  file never stops the others from loading.
