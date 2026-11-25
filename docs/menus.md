# Menus and shop

Menus are files in `menus/` (the file name is the menu id). They know about enchantments, so you need
no menu plugin and no placeholders per slot: a list of enchantments fills its slots and pages by itself.
Everything is applied with `/ce reload`, except adding or changing a menu's own `command:` (restart).

Four menus are installed with a new `menus/` folder (a menu you delete never comes back):

| Menu | What it is |
|---|---|
| `shop` | The shop: random books by rarity. `/ce shop` opens it |
| `enchants` | Categories: one item per rarity |
| `enchant_list` | Enchantments of a rarity, page by page |
| `enchant_info` | Details of one enchantment |

## A menu

```yaml
title: "<dark_gray>Enchantments » <rarity> (<page>/<pages>)"
rows: 6                       # 1–6
command: [enchantlist, el]    # optional, own command + aliases (needs a restart)
argument: rarity              # none | rarity | enchant (what the menu receives)
permission: ""                # optional, to open it
disabled-worlds: []
items:
  border:
    slots: [0-9, 17-18, 26-27, 35-36, 44-53]   # or slot: 4
    priority: 10                               # lower wins when items share a slot
    material: black_stained_glass_pane         # or "head:<base64 texture>"
    name: " "                                  # blank name + no lore = no tooltip
  back:
    slot: 49
    material: arrow
    name: "<gray>Back"
    actions: ["[back]"]
```

Item options: `slot`/`slots`, `priority`, `show-if`, `material`, `name`, `lore`, `amount`, `item-model`,
`custom-model-data`, `glint`, the click options below. Attributes (damage of a sword…) are never shown.

- **`show-if`**: all must be true for the item to show: `previous-page`, `next-page`,
  `permission:<permission>`; `!` in front negates. If it doesn't show, the next item in that slot does.
- **`argument`**: `rarity` → opened with a rarity or `all` (default `all`); `enchant` → opened with an
  enchantment: its id or its name without colours or accents, with spaces or `_` (`life_bolt`, `Life Bolt`).
  Own commands take it: `/enchantlist [rarity] [page]`, `/enchantinfo <enchantment>` (with tab-complete).

## Enchantment list

```yaml
  enchants:
    type: enchant-list
    slots: [10-16, 19-25, 28-34, 37-43]   # filled in this order; one page = this many
    filter: argument          # argument (the menu's rarity) | all | a rarity id
    sort: RARITY              # RARITY (rarities.yml order, like the lore) | NAME
    vanilla: false            # false | true (ours and vanilla) | only (only vanilla)
    material: enchanted_book
    name: "<name>"
    lore: ["<gray> <description>", "<gray>Max level: <max-level>"]
    overrides:                # only what you write changes
      rarity:
        legendary: { material: nether_star }
      enchant:
        life_bolt: { material: "head:eyJ0ZXh0dXJlcyI6..." }
        "minecraft:mending": { material: experience_bottle }
    actions: ["[open] enchant_info <id>"]
```

Disabled enchantments are not listed. A list slot without an enchantment (last page) shows what is under it.

**Filter by item.** `filters:` in the list is the order of item groups (`item-groups.yml`) a button goes through
with `[filter] next` / `[filter] previous`; `all` = no filter. An enchantment shows up if it can go on **any** item
of the group, so "Helmets" also shows the armour ones, and "Armor" the helmet-only ones. It combines with the
menu's rarity, goes back to page 1, and is kept when changing page or coming back with `[back]`. `<filter>` (the
group's `name:`, or "All") and `<filter-id>` work in every item of the menu.

```yaml
  enchants:
    type: enchant-list
    slots: [10-16, 19-25, 28-34, 37-43]
    filters: [all, helmets, chestplates, leggings, boots, swords, axes, pickaxes, bows]
  filter:
    slot: 46
    material: hopper
    name: "<yellow>Item: <white><filter>"
    left-actions: ["[filter] next"]
    right-actions: ["[filter] previous"]
```

## Click actions

`actions` run with any click; `left-actions`, `right-actions` and `shift-actions` replace them for that click.
They run in order:

| Action | Does |
|---|---|
| `[player] <command>` | The player runs the command (with their permissions) |
| `[console] <command>` | The console runs it |
| `[open] <menu> [argument] [page]` | Opens another menu |
| `[back]` | Back to the previous menu, with its argument and page (closes if there is none) |
| `[page] next` / `[page] previous` | Page of the enchantment list |
| `[filter] next` / `[filter] previous` | Item filter of the enchantment list (its `filters:`) |
| `[close]`, `[refresh]` | Close; draw the menu again |
| `[message] <text>`, `[actionbar] <text>` | Text to the player |
| `[sound] <sound> [volume] [pitch]` | `ui.button.click 1 1.5` |
| `[buy] <rarity>` | Buys a random book of that rarity (the shop) |

Opening a menu from another one remembers it for `[back]`; changing page doesn't. Opening a menu with none
open starts again.

## Cost, permission and confirmation

```yaml
  rare_book:
    slot: 13
    material: enchanted_book
    name: "<rarity> <gray>Book"
    lore: ["<gray>Enchantments: <white><books>", "<gray>Price: <white><cost>"]
    cost: { currency: LEVELS, price: 20 }   # LEVELS, EXP (points) or MONEY (Vault)
    permission: ""                           # optional, to use it
    confirm: false                           # true = confirm first
    deny-actions: ["[message] <red>You need <cost>.", "[sound] entity.villager.no"]
    actions: ["[buy] rare", "[message] <green>Enjoy!"]
confirm:                                     # look of the confirmation (menu level)
  title: "<dark_gray>Confirm purchase"
  accept: { material: lime_stained_glass_pane, name: "<green>Buy for <cost>" }
  cancel: { material: red_stained_glass_pane, name: "<red>Cancel" }
```

- The cost is checked and charged by the plugin, before the actions run, so nobody is charged without
  getting what they paid for. With `[buy]`, the inventory must have a free slot and `BookPurchaseEvent`
  can cancel or change the price.
- If the player can't pay (or lacks the `permission`), `deny-actions` run instead; without them, a message.
- Without Vault or an economy plugin, `MONEY` can't be paid and the console says so.

## Placeholders

| Where | Placeholders |
|---|---|
| Everywhere | `<player>`, `<menu>`, `<page>`, `<pages>`, `<count>` (enchantments in the list), `<argument>`, `<filter>`, `<filter-id>` |
| Rarity menus | `<rarity>` (name, "All" for `all`), `<rarity-id>` |
| List items and enchantment menus | `<name>`, `<id>`, `<slug>` (name to type), `<rarity>`, `<rarity-id>`, `<max-level>` (roman), `<max-level-number>`, `<applicable>`, `<conflicts>`, `<description>` |
| Items with `cost` / `[buy]` | `<cost>`; `<rarity>` and `<books>` (enchantments it can give) |

A lore line containing `<description>` is repeated for each description line, keeping its format
(`"<gray> » <description>"`); descriptions use the values of the maximum level. With
**PlaceholderAPI** installed (optional), its `%placeholders%` work in every text and command. Their values are
inserted as plain text (a player's nickname can't add formatting), and in `[console]` commands spaces become
`_` so a value can't add extra arguments.

## Opening menus

- `/ce shop` (permission `complexenchants.shop`), `/ce shop <player>`.
- `/ce menu open <menu> [player] [argument] [page]`, `/ce menu list` (staff, console, NPCs; skips the
  menu's permission).
- A menu's own `command:`, or `[open]` from another menu (they check the menu's permission).
- API: `api.openMenu(player, "enchant_list", "epic")`, `api.openShop(player)`.
