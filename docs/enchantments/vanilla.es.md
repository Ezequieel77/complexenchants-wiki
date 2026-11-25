# Encantamientos vanilla

`vanilla-enchants.yml` configura los encantamientos propios de Minecraft. **Todo es opcional: lo que no
escribas queda exactamente como en Minecraft**, y el archivo por defecto no cambia nada del juego (solo trae
descripciones, que por defecto no se muestran).

```yaml
default:
  rarity: vanilla                 # rareza de los vanilla que no dicen otra

sharpness:
  # Visual (⟳ /ce reload)
  name: "<red>Filo"               # sin él: el nombre de Minecraft en el idioma de cada jugador
  rarity: rare                    # color y posición en el lore
  description: ["<gray>+<calc:level * 0.5 + 0.5> de daño"]
  # Juego (⏻ reinicio; API de registro de Paper, sin reflexión)
  max-level: 7                    # subirlo es seguro; al bajarlo, los objetos conservan el nivel que tienen
  conflicts: [smite, complexenchants:rayo_vital]  # sustituye la lista de Minecraft; siempre en los dos sentidos
  applicable: [swords, axes]      # grupos de objetos; sustituye los objetos que permite Minecraft
  weight: 10
  anvil-cost: 1
  table-cost: { min: {base: 1, per-level: 11}, max: {base: 21, per-level: 11} }
  sources: { enchanting-table: true, villagers: false }   # si falta = como en Minecraft
  grindstone-removes: true

mending:
  enabled: false                  # nunca sale en la mesa, los bibliotecarios, el botín ni la pesca
```

- **Cómo se ven.** La rareza `vanilla` no hace falta que exista en `rarities.yml`: si no está, los vanilla se
  ven exactamente como en Minecraft (grises, las maldiciones en rojo, después de los personalizados, en el orden
  del objeto). Añade una rareza `vanilla:` a `rarities.yml` para elegir su color y su posición, o dale a cada uno
  una `rarity` o un `name`: entonces se muestran como los nuestros (color, nivel del mismo color, ordenados con
  `sort-by`).
- **Las descripciones** se muestran si `display.descriptions.vanilla` es `true` (y `items`/`books` lo
  permiten). `<calc:EXPRESIÓN>` es un número calculado para el nivel (`level`, `+ - * / ^ ( )`, `min`, `max`,
  `round`, `floor`, `ceil`, `abs`); también funciona en las descripciones de tus encantamientos, donde además
  puede leer los valores de sus efectos con `value(N, arg)` ([más](../effects/mechanics.md#valores-en-la-descripcion)).
- **Las fuentes** se comprueban también en tiempo real: apagar una funciona con `/ce reload`; encenderla, y el
  resto de opciones de juego, necesitan reinicio (`/ce reload` dice cuáles).
- `/ce info minecraft:sharpness` muestra la configuración efectiva; los menús pueden listar vanilla
  (`vanilla:` en un `enchant-list`), y `/customenchants sharpness` y el clic derecho con un libro funcionan con
  ellos.
- Los encantamientos de otros plugins o datapacks (`namespace:id`) solo aceptan las opciones visuales.
