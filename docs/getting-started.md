# Getting started

## Requirements

| Server | Java |
|---|---|
| Paper **1.21.11** (or a fork such as Purpur) | 21 |
| Paper **26.3** | 25 |
| Folia (same versions) | same |

Spigot is **not** supported: it has no supported way to register enchantments.

Optional: **Vault** plus an economy plugin (EssentialsX, CMI…), only for menu items that cost money;
**PlaceholderAPI**, for its placeholders in menus and for [ComplexEnchants' own placeholders](placeholders.md).

## Installation

1. Put `ComplexEnchants.jar` in `plugins/` and start the server once.
2. Default files are created in `plugins/ComplexEnchants/`. Existing files are never overwritten.
3. Add your enchantments to `plugins/ComplexEnchants/enchants/` (see below) and **restart**.

**What comes with the plugin.** On the first start (when there is no `enchants/` folder yet) you get
**112 ready-made enchantments** (combat, tools, armour, bows, tridents, maces, spears, elytra, totems,
fishing…), **7 rarities** (`simple`, `special`, `rare`, `epic` and `legendary`, `mythic`, `abyssal`), item groups,
the helper items and the menus. Rarities up to `epic` use VANILLA mode (table, anvil, villagers, loot, fishing);
`legendary` and above are BOOKS-only, so they come from the shop, commands or rewards. Change or delete
anything: a deleted enchantment or menu never comes back (only `enchants/_example.yml`, the template, is
restored if missing). Never delete an enchantment that players already have: set `enabled: false` instead.

## Reload or restart?

Minecraft only accepts new enchantments while the server is starting. So:

- **`/ce reload`** applies: names, descriptions, colours, lore format, rarities (display), book
  chances, source switches, slots, helper items, the visual options of `vanilla-enchants.yml`, menus and messages (except a menu's own `command:`).
- **A restart** is needed to: add an enchantment, or change its max level, weight, applicable items,
  conflicts, anvil/table cost, or whether it appears in the table/villagers/loot.

`/ce reload` tells you exactly which changes are still waiting for a restart. Every option in the
default files is marked with ⟳ (reload) or ⏻ (restart).

## Configuration files

| File | What it contains |
|---|---|
| `config.yml` | Mode, vanilla mechanics switches, book failure, slots, display, language, how damage effects combine (`damage`), tool limits (`tools`) |
| `rarities.yml` | Rarities: name, colour, weight, lore order, default book chances |
| `vanilla-enchants.yml` | Minecraft's enchantments: name, rarity, description and gameplay options ([more](enchantments/vanilla.md)) |
| `item-groups.yml` | Groups of items (`swords`, `armor`…) using items, tags (`#minecraft:swords`) or other groups (`@tools`) |
| `items.yml` | Extractor, catalyst, slot expander and transmuter (look of the rarity ones and the generic ones), and the look of books |
| `menus/*.yml` | Menus: the shop, enchantment lists and details, or your own ([more](menus.md)) |
| `enchants/*.yml` | One file per enchantment |
| `lang/en.yml`, `lang/es.yml` | Every message (MiniMessage). Missing keys fall back to the bundled English text |
| `data/known-enchants.yml` | Internal list of every enchantment ever registered. **Do not edit** |
| `backups/` | Copies of your files from before new options were added to them (the last 5 of each) |

**New options after an update.** On startup and with `/ce reload`, the options that a new version adds to
`config.yml`, `items.yml` and `lang/*.yml` are added to your files, with their comments and in their place.
Nothing you already have changes (values, comments, order); a copy of the previous file goes to `backups/`.
An option is not added if it would change what the plugin does (for example, a `vanilla-mechanics` switch
whose default depends on the mode), nor inside a section written on one line (`display: {mode: ITEM}`): the
console says so once. Your content files (rarities, item groups, `vanilla-enchants.yml`, enchantments, menus)
are never touched. Turn it off with `update-files: false`.
