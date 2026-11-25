# PlaceholderAPI placeholders

With PlaceholderAPI installed, ComplexEnchants adds its own placeholders for scoreboards, TAB, holograms or any
plugin that reads them. Both `%complexenchants_…%` and the short `%ce_…%` work. Texts come with classic colours
(§); add `_plain` at the end for no colours (`%ce_hand_list_plain%`). `true`/`false` use PlaceholderAPI's
boolean format.

**The player's items** — `<slot>` is `hand`, `offhand`, `helmet`, `chestplate`, `leggings` or `boots`:

| Placeholder | Value |
|---|---|
| `%ce_<slot>_count%` | custom enchantments on that item |
| `%ce_<slot>_list%` | their names with level, separated by commas |
| `%ce_<slot>_slots_used%` / `_slots_max%` / `_slots_free%` | enchantment slots |
| `%ce_<slot>_level_<enchant>%` | level of that enchantment on the item (0 if it doesn't have it) |
| `%ce_<slot>_has_<enchant>%` | whether it has it |
| `%ce_book_success%` / `%ce_book_destroy%` | chances of the book in hand (empty if it isn't one) |
| `%ce_equipped_count%` | custom enchantments on everything the player holds and wears |

**Enchantments** (no player needed): `%ce_enchant_<enchant>_name%`, `_rarity%`, `_max_level%`, `_applicable%`,
`_description%` (values at the max level); `%ce_count%` (active enchantments), `%ce_rarity_<rarity>_count%`.

**Effects**: `%ce_var_<name>%` (player variable), `%ce_mark_<name>%`, `%ce_cooldown_<enchant>%` and
`%ce_skill_cooldown_<enchant>%` (seconds left, 0 = ready), `%ce_in_combat%`.

`<enchant>` is the id (`life_bolt`), the written name (`asesino_feroz`) or a vanilla one (`minecraft:sharpness`).
Offline players get an empty value for what needs a player.
