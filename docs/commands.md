# Commands and permissions

Main command `/complexenchants`, alias `/ce`. Players only see the subcommands they have permission for.

| Command | Permission | Default |
|---|---|---|
| `/ce help` (or `/ce`): the commands **you** can use, clickable; menus' own commands included | `complexenchants.command.help` | everyone |
| `/ce shop` | `complexenchants.shop` | everyone |
| `/ce shop <player>` | `complexenchants.shop.others` | op |
| `/ce menu open <menu> [player] [argument] [page]`, `/ce menu list` | `complexenchants.command.menu` | op |
| `/ce debug` (see which of your effects run, or why not) | `complexenchants.command.debug` | op |
| `/ce give skillbook <players> [amount]` (the active skills book) | `complexenchants.command.give` | op |
| `/ce list [page]` | `complexenchants.command.list` | op |
| `/ce info <enchant>` (also `minecraft:sharpness`) | `complexenchants.command.info` | op |
| `/ce reload` | `complexenchants.command.reload` | op |
| `/ce enchant <enchant> [level]` | `complexenchants.command.enchant` | op |
| `/ce unenchant <enchant>` | `complexenchants.command.enchant` | op |
| `/ce item` (slots and enchantments of the held item) | `complexenchants.command.item` | op |
| `/ce give book <players> <enchant> [level] [success]` | `complexenchants.command.give` | op |
| `/ce give random <players> [rarity\|any]` (without a rarity: any enchantment, by weight) | `complexenchants.command.give` | op |
| `/ce give extractor\|catalyst\|transmuter <players> [amount] [rarity\|any] [value]` | `complexenchants.command.give` | op |
| `/ce give slot-expander <players> [amount]` | `complexenchants.command.give` | op |
| `/ce editor` (create and edit enchantments, rarities, item groups and vanilla enchantments in game) | `complexenchants.editor` | op |

`complexenchants.admin` grants every permission above. The texts of `/ce help` are in the lang files
(`command.help`).
`/ce enchant` and `/ce unenchant` act on the item in the main hand and follow the same rules as
everything else (applicable items, conflicts, slots).
