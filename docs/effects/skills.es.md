# Habilidades activas

Un encantamiento con efectos `trigger: active_skill` es una **habilidad**: no se activa sola, la activa el
jugador.

```yaml
# enchants/dominio.yml
active-skill:
  cooldown: "65 - 5 * level"         # segundos (solo puede depender de level)
  requirements:                      # opcional; se comprueban en orden
    - condition: { health_above: 50% }
      message: "<red>Necesitas más de la mitad de la vida."
effects:
  - effect: zone
    trigger: active_skill
    name: dominio
    radius: 16
    duration: 8
```

- **Cómo se activan**:
  - con el **libro de habilidades** (`/ce give skillbook <jugadores> [cantidad]`):
    clic derecho y se abre un menú con tus habilidades, su nivel y su enfriamiento;
  - con la **tecla** de `skills.keybind` en `config.yml`: `sneak_swap` (agachado + la tecla de cambiar de mano,
    F), `swap` (solo F) o `none`. Con una sola habilidad disponible, la activa; con varias, abre el menú.
    `skills.keybind-requires-book` puede hacer que la tecla también pida el libro: `false` (funciona siempre),
    `hotbar` (el libro en la barra rápida o en la otra mano: el mismo espacio que pagan los jugadores de Bedrock,
    que no pueden usar las teclas) o `inventory` (en cualquier parte del inventario). Sin el libro, la tecla hace lo
    normal. La configuración de fábrica del plugin usa `hotbar`.
- **Qué habilidades tienes**: las de los objetos en la mano, la armadura y la **barra rápida** (con el libro en la
  mano, la espada sigue contando). Fuera de su casilla, los efectos que tocan "el objeto encantado" (`repair`,
  `damage_item`, `remove_enchant`) actúan sobre lo que tengas en la mano.
- **Antes de activarse**, en este orden: silencio, enfriamiento de la habilidad y requisitos. Si algo falla, el
  jugador recibe el mensaje y no pasa nada más (ni gasta el enfriamiento).
- **Silencio**: quien tenga la marca `skills.silence-mark` (por defecto `silenced`, la que pone un efecto
  `mark`) no puede usar habilidades.
- Los efectos de una habilidad pueden tener además sus propias condiciones, probabilidad y enfriamiento, como
  cualquier otro efecto.

```yaml
# config.yml
skills:
  keybind: sneak_swap
  keybind-requires-book: hotbar   # false | hotbar | inventory
  silence-mark: silenced
  book:
    material: book
    name: "<gold><bold>Libro de habilidades"
    lore: ["<gray>Clic derecho para ver tus habilidades."]
  menu-title: "<dark_gray>⚔ Habilidades"
```
