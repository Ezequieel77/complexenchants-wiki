# Placeholders de PlaceholderAPI

Con PlaceholderAPI instalado, ComplexEnchants añade sus propios placeholders para scoreboards, TAB, hologramas o
cualquier plugin que los lea. Valen `%complexenchants_…%` y el corto `%ce_…%`. Los textos salen con los colores
clásicos (§); añade `_plain` al final para quitarlos (`%ce_hand_list_plain%`). `true`/`false` usan el formato de
PlaceholderAPI.

**Los objetos del jugador** — `<slot>` es `hand`, `offhand`, `helmet`, `chestplate`, `leggings` o `boots`:

| Placeholder | Valor |
|---|---|
| `%ce_<slot>_count%` | encantamientos personalizados de ese objeto |
| `%ce_<slot>_list%` | sus nombres con nivel, separados por comas |
| `%ce_<slot>_slots_used%` / `_slots_max%` / `_slots_free%` | ranuras de encantamiento |
| `%ce_<slot>_level_<encantamiento>%` | nivel de ese encantamiento en el objeto (0 si no lo tiene) |
| `%ce_<slot>_has_<encantamiento>%` | si lo tiene |
| `%ce_book_success%` / `%ce_book_destroy%` | probabilidades del libro en la mano (vacío si no lo es) |
| `%ce_equipped_count%` | encantamientos personalizados de todo lo que lleva en las manos y puesto |

**Encantamientos** (sin jugador): `%ce_enchant_<encantamiento>_name%`, `_rarity%`, `_max_level%`, `_applicable%`,
`_description%` (valores del nivel máximo); `%ce_count%` (encantamientos activos), `%ce_rarity_<rareza>_count%`.

**Efectos**: `%ce_var_<nombre>%` (variable del jugador), `%ce_mark_<nombre>%`, `%ce_cooldown_<encantamiento>%` y
`%ce_skill_cooldown_<encantamiento>%` (segundos que faltan, 0 = listo), `%ce_in_combat%`.

`<encantamiento>` es el id (`rayo_vital`), el nombre escrito (`asesino_feroz`) o uno vanilla
(`minecraft:sharpness`). Con jugadores desconectados, lo que necesita un jugador sale vacío.
