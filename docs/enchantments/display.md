# How enchantments are displayed

- **`display.mode: PACKETS`** (recommended): the formatted enchantment list is added only to what players
  see. Real items stay clean, so nothing is saved into them. Creative mode is handled: lore sent back by
  the client is removed before it is saved.
- **`display.mode: ITEM`**: the lore is written into items. Use it only if another plugin must read
  the lore. It is also used automatically if this Minecraft version has no packet support.

Other options: `sort-by` (`RARITY`, `NAME`, `LEVEL`), `descriptions` (`items` / `books`: show each
enchantment's description on enchanted items and on books; the old `show-descriptions` still works for
both; `vanilla`: also the descriptions of `vanilla-enchants.yml`, off by default) and
`hide-vanilla-enchant-lines`. Line formats are in `lang/*.yml` under `display`.

**Enchantment books** (BOOKS mode) take their name and lore from `enchanted-book:` in `items.yml`, with
these placeholders: `<name>`, `<level>` (in the same colour as the name; empty for one-level
enchantments), `<max-level>`, `<rarity>`, `<applicable>`, `<conflicts>`, `<success>`, `<destroy>`, and a line that
is just `<description>`. `<applicable>` lists the enchantment's item groups by their `name:` in
`item-groups.yml` (without one, the id: `fishing_rods` → "Fishing Rods"), joined with
`applicable-separator`.

```yaml
enchanted-book:
  name: "<name> <level>"
  lore:
    - "<description>"
    - "<gray>Applies to: <white><applicable>"
    - "<gray>Incompatible with: <conflicts>"
    - ""
    - "<green>Success: <success>%"
    - "<red>Destroy: <destroy>%"
  applicable-separator: ", "
```

**`<conflicts>`** lists the enchantments it is incompatible with, by name and in their colour: the ones in its
`conflicts:` plus the ones that name it (vanilla ones as Minecraft says, unless `vanilla-enchants.yml` changes
them); disabled or missing ones are left out. A line with `<conflicts>` and nothing to list is removed. It also
works in descriptions, in menus and in the `books.info` text.
