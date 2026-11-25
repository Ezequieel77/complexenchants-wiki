# Menús y tienda

Los menús son archivos de `menus/` (el nombre del archivo es el id del menú). Conocen los encantamientos,
así que no hace falta ningún plugin de menús ni un marcador por casilla: una lista de encantamientos llena
sus casillas y pagina sola. Todo se aplica con `/ce reload`, salvo añadir o cambiar el `command:` propio de
un menú (reiniciar).

Con una carpeta `menus/` nueva se instalan cuatro menús (un menú que borres no vuelve a aparecer):

| Menú | Qué es |
|---|---|
| `shop` | La tienda: libros aleatorios por rareza. La abre `/ce shop` |
| `enchants` | Categorías: un ítem por rareza |
| `enchant_list` | Los encantamientos de una rareza, por páginas |
| `enchant_info` | La información de un encantamiento |

## Un menú

```yaml
title: "<dark_gray>Encantamientos » <rarity> (<page>/<pages>)"
rows: 6                       # 1–6
command: [enchantlist, el]    # opcional, comando propio + alias (necesita reiniciar)
argument: rarity              # none | rarity | enchant (qué recibe el menú)
permission: ""                # opcional, para abrirlo
disabled-worlds: []
items:
  borde:
    slots: [0-9, 17-18, 26-27, 35-36, 44-53]   # o slot: 4
    priority: 10                               # si varios ítems comparten casilla, gana el menor
    material: black_stained_glass_pane         # o "head:<textura base64>"
    name: " "                                  # nombre en blanco y sin lore = sin recuadro
  volver:
    slot: 49
    material: arrow
    name: "<gray>Volver"
    actions: ["[back]"]
```

Opciones de un ítem: `slot`/`slots`, `priority`, `show-if`, `material`, `name`, `lore`, `amount`, `item-model`,
`custom-model-data`, `glint` y las del clic (más abajo). Los atributos (el daño de una espada…) nunca se muestran.

- **`show-if`**: todas deben cumplirse para que se vea: `previous-page`, `next-page`,
  `permission:<permiso>`; con `!` delante, al revés. Si no se ve, se ve el siguiente ítem de esa casilla.
- **`argument`**: `rarity` → se abre con una rareza o `all` (por defecto `all`); `enchant` → con un
  encantamiento: su id o su nombre sin colores ni acentos, con espacios o con `_` (`rayo_vital`, `Rayo Vital`).
  Los comandos propios lo reciben: `/enchantlist [rareza] [página]`, `/enchantinfo <encantamiento>` (con
  autocompletado).

## Lista de encantamientos

```yaml
  encantamientos:
    type: enchant-list
    slots: [10-16, 19-25, 28-34, 37-43]   # se llenan en este orden; una página = tantas como casillas
    filter: argument          # argument (la rareza del menú) | all | id de una rareza
    sort: RARITY              # RARITY (orden de rarities.yml, como el lore) | NAME
    vanilla: false            # false | true (los nuestros y los vanilla) | only (solo los vanilla)
    material: enchanted_book
    name: "<name>"
    lore: ["<gray> <description>", "<gray>Nivel máximo: <max-level>"]
    overrides:                # solo cambia lo que escribas
      rarity:
        legendary: { material: nether_star }
      enchant:
        rayo_vital: { material: "head:eyJ0ZXh0dXJlcyI6..." }
        "minecraft:mending": { material: experience_bottle }
    actions: ["[open] enchant_info <id>"]
```

Los encantamientos desactivados no aparecen. Una casilla de la lista sin encantamiento (última página) deja
ver lo que hay debajo.

**Filtro por objeto.** `filters:` en la lista es el orden de grupos de objetos (`item-groups.yml`) que recorre un
botón con `[filter] next` / `[filter] previous`; `all` = sin filtro. Un encantamiento sale si se puede poner en
**algún** objeto del grupo: con "Cascos" salen también los de armadura, y con "Armadura" los que son solo de
casco. Se combina con la rareza del menú, vuelve a la página 1 y se conserva al cambiar de página o al volver con
`[back]`. `<filter>` (el `name:` del grupo, o "Todos") y `<filter-id>` funcionan en todos los ítems del menú.

```yaml
  enchants:
    type: enchant-list
    slots: [10-16, 19-25, 28-34, 37-43]
    filters: [all, helmets, chestplates, leggings, boots, swords, axes, pickaxes, bows]
  filter:
    slot: 46
    material: hopper
    name: "<yellow>Objeto: <white><filter>"
    left-actions: ["[filter] next"]
    right-actions: ["[filter] previous"]
```

## Acciones al hacer clic

`actions` se ejecutan con cualquier clic; `left-actions`, `right-actions` y `shift-actions` las sustituyen para
ese clic. Se ejecutan en orden:

| Acción | Qué hace |
|---|---|
| `[player] <comando>` | Lo ejecuta el jugador (con sus permisos) |
| `[console] <comando>` | Lo ejecuta la consola |
| `[open] <menú> [argumento] [página]` | Abre otro menú |
| `[back]` | Vuelve al menú anterior, con su argumento y su página (sin anterior, cierra) |
| `[page] next` / `[page] previous` | Página de la lista de encantamientos |
| `[filter] next` / `[filter] previous` | Filtro por objeto de la lista de encantamientos (su `filters:`) |
| `[close]`, `[refresh]` | Cerrar; volver a dibujar el menú |
| `[message] <texto>`, `[actionbar] <texto>` | Texto al jugador |
| `[sound] <sonido> [volumen] [tono]` | `ui.button.click 1 1.5` |
| `[buy] <rareza>` | Compra un libro aleatorio de esa rareza (la tienda) |

Abrir un menú desde otro lo recuerda para `[back]`; cambiar de página no. Abrir un menú sin tener otro
abierto empieza de cero.

## Coste, permiso y confirmación

```yaml
  libro_raro:
    slot: 13
    material: enchanted_book
    name: "<rarity> <gray>Libro"
    lore: ["<gray>Encantamientos: <white><books>", "<gray>Precio: <white><cost>"]
    cost: { currency: LEVELS, price: 20 }   # LEVELS, EXP (puntos) o MONEY (Vault)
    permission: ""                           # opcional, para usarlo
    confirm: false                           # true = confirmar antes
    deny-actions: ["[message] <red>Necesitas <cost>.", "[sound] entity.villager.no"]
    actions: ["[buy] rare", "[message] <green>¡Que lo disfrutes!"]
confirm:                                     # aspecto de la confirmación (del menú)
  title: "<dark_gray>Confirmar compra"
  accept: { material: lime_stained_glass_pane, name: "<green>Comprar por <cost>" }
  cancel: { material: red_stained_glass_pane, name: "<red>Cancelar" }
```

- El coste lo comprueba y lo cobra el plugin antes de las acciones, así que nunca se cobra sin entregar.
  Con `[buy]` hace falta un hueco libre en el inventario, y `BookPurchaseEvent` puede cancelar o cambiar el
  precio.
- Si el jugador no puede pagar (o no tiene el `permission`), se ejecutan las `deny-actions`; sin ellas, un aviso.
- Sin Vault o sin plugin de economía, `MONEY` no se puede pagar y la consola lo avisa.

## Marcadores

| Dónde | Marcadores |
|---|---|
| En todo | `<player>`, `<menu>`, `<page>`, `<pages>`, `<count>` (encantamientos de la lista), `<argument>`, `<filter>`, `<filter-id>` |
| Menús de rareza | `<rarity>` (nombre; "Todas" con `all`), `<rarity-id>` |
| Ítems de la lista y menús de encantamiento | `<name>`, `<id>`, `<slug>` (nombre para escribir), `<rarity>`, `<rarity-id>`, `<max-level>` (romano), `<max-level-number>`, `<applicable>`, `<conflicts>`, `<description>` |
| Ítems con `cost` / `[buy]` | `<cost>`; `<rarity>` y `<books>` (encantamientos que puede dar) |

Una línea de lore que contenga `<description>` se repite por cada línea de la descripción, con su formato
(`"<gray> » <description>"`); las descripciones usan los valores del nivel máximo. Con **PlaceholderAPI**
instalada (opcional), sus `%marcadores%` funcionan en todos los textos y comandos. Sus valores se insertan
como texto (el apodo de un jugador no puede añadir formato), y en los comandos `[console]` los espacios pasan
a ser `_` para que un valor no pueda añadir argumentos.

## Abrir menús

- `/ce shop` (permiso `complexenchants.shop`), `/ce shop <jugador>`.
- `/ce menu open <menú> [jugador] [argumento] [página]`, `/ce menu list` (staff, consola, NPC; no exige el
  permiso del menú).
- El `command:` propio de un menú, o `[open]` desde otro menú (exigen el permiso del menú).
- API: `api.openMenu(player, "enchant_list", "epic")`, `api.openShop(player)`.
