# Modes: BOOKS and VANILLA

## Modes: BOOKS and VANILLA

The mode decides how custom enchantments are **obtained and applied**. It never changes how they
are **stored**, so you can switch modes at any time without converting items.

| | BOOKS | VANILLA |
|---|---|---|
| How it's applied | Drag the book onto the item | Anvil (and enchanting table) |
| Success / destroy chances | Yes, stored in each book | No |
| Extractor, catalyst, transmuter | Yes | — |
| Merging books | Drag a book onto an equal book | Anvil |
| Table, anvil, villagers, loot, fishing | Off by default | On by default |

Set the global mode in `config.yml` (`mode: BOOKS` or `mode: VANILLA`). A rarity can override it with `mode:`
in `rarities.yml`, and an enchantment with `mode: BOOKS | VANILLA | INHERIT` in its own file. The most specific
one wins: enchantment → rarity → `config.yml` (`INHERIT` = take it from the next one). `/ce info <enchant>` says
where the mode comes from. Vanilla enchantments always keep their vanilla behaviour.

## BOOKS mode

- **Books** are enchanted books whose success chance is rolled when the book is created
  (from the enchantment, or from its rarity). The destroy chance is always 100 − success (58% success =
  42% destroy). Players drag a book onto an item in their own inventory. One roll:
  - **Success**: the enchantment is applied (or upgraded).
  - **Failure**: the book is lost. With `books.on-fail: BOOK` (default) only the book is lost; with
    `BOOK_AND_ITEM` the item is destroyed too.
- **Merging**: drag a book onto an identical book (same enchantment and level) to get one level higher,
  with the average of both books' success chance.
- **Extractor**: drag it onto an item to move one random custom enchantment into a new book. It always
  works: the chance it shows is the success chance the new book will have.
- **Catalyst**: drag it onto a book to raise its success chance, up to `max-success`.
- **Transmuter**: drag it onto a ComplexEnchants book: with its chance (shown in its name), the book becomes a
  random **different** enchantment of the **same rarity**; on fail the transmuter is lost and, by default, the
  book too (`destroy-book-on-fail`). Other plugins can cancel it or change the chance with `BookTransmuteEvent`.
- **Slot expander**: drag it onto an item to add enchantment slots, up to `slots.max-extra`.

The extractor, the catalyst and the transmuter are either **of a rarity** or **generic**:

| | Of a rarity (e.g. legendary) | Generic |
|---|---|---|
| Extractor | only takes legendary enchantments from the item | any |
| Catalyst | only works on legendary books | any book |
| Transmuter | only accepts legendary books (and gives another legendary) | any book (gives another of its rarity) |

Used on something of another rarity, they say so and are not used up.
`/ce give extractor|catalyst|transmuter <players> [amount] [rarity|any] [value]`: without a rarity (or with
`any`) you get the generic one; without a value it is rolled from `items.yml`. In `items.yml`, `<rarity>` is the
rarity's name, `generic:` changes only what you write in it for the generic look (name, lore, material, model),
and `any-rarity` is what `<rarity>` shows in the generic one. Items made before 1.1.0: extractors and catalysts
become generic (old extractors no longer fail: their chance goes to the book), transmuters keep their rarity.

**Book information**: right-click with a ComplexEnchants enchanted book in your hand to see its enchantments
in the chat (description, applicable to, max level and, for BOOKS-mode books, success and destroy).
Turn it off or make it Shift-only with `books.right-click-info` / `right-click-info-sneak` in `config.yml`;
the text is `books.info` in the lang file. Right-clicking a chest, door… with the book only shows it while sneaking.

Books in BOOKS mode can never be used in the anvil (that would skip their chances). Stacked items are
never enchanted, and creative mode is left to Minecraft.

Give books and helper items with `/ce give` (see [commands](../commands.md)) or sell them in
the [shop](../menus.md).

## VANILLA mode

Custom enchantments behave like vanilla ones. Each source has a global switch in `config.yml`
(`vanilla-mechanics`) and a per-enchantment switch (`sources:`); both must be on. A rarity can set
`sources:` too (in `rarities.yml`): each source the enchantment does not mention is taken from its rarity,
and if the rarity does not mention it either, it is on.

- **Enchanting table**: respects enchantment slots. If nothing is left to add, the table does not charge.
- **Anvil**: combines books and items like vanilla, respecting slots. `anvil-max-cost` raises the
  "Too expensive!" limit only when custom enchantments are involved. Above 40 the client may still show
  "Too expensive!", but the result can be taken.
- **Grindstone**: `grindstone-removes: false` keeps custom enchantments (like curses). It can also be set per
  rarity (`rarities.yml`) and per enchantment (its own file); the most specific wins: enchantment → rarity →
  `config.yml`. Restart to apply.
- **Villagers, chest loot and fishing**: loot and fishing share one Minecraft tag; ComplexEnchants
  separates them at runtime. Trial chamber vaults count as loot. If an item would be left without
  enchantments, it gets a random allowed one instead.
