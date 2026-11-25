# Primeros pasos

## Requisitos

| Servidor | Java |
|---|---|
| Paper **1.21.11** (o derivados como Purpur) | 21 |
| Paper **26.3** | 25 |
| Folia (mismas versiones) | igual |

**No** funciona en Spigot: no tiene una forma soportada de registrar encantamientos.

Opcional: **Vault** con un plugin de economía (EssentialsX, CMI…), solo para los ítems de menú que cobran
dinero; **PlaceholderAPI**, para sus marcadores en los menús y para [los placeholders propios de ComplexEnchants](placeholders.md).

## Instalación

1. Copia `ComplexEnchants.jar` en `plugins/` y arranca el servidor una vez.
2. Se crean los archivos por defecto en `plugins/ComplexEnchants/`. Los que ya existen nunca se sobrescriben.
3. Añade tus encantamientos en `plugins/ComplexEnchants/enchants/` (ver abajo) y **reinicia**.

**Lo que trae el plugin.** En el primer arranque (cuando todavía no hay carpeta `enchants/`) se instalan
**112 encantamientos** listos (combate, herramientas, armadura, arcos, tridentes, mazas, lanzas, elytras, tótems,
pesca…), **7 rarezas** (`simple`, `special`, `rare`, `epic` y `legendary`, `mythic`, `abyssal`), los grupos de
objetos, los objetos auxiliares y los menús, en inglés (`language: en`). Las rarezas hasta `epic` usan el modo
VANILLA (mesa, yunque, aldeanos, botín, pesca); `legendary` y las de arriba son solo de LIBROS: salen de la tienda,
de comandos o de recompensas. Cambia o borra lo que quieras: un encantamiento o un menú que borras no vuelve
(solo `enchants/_example.yml`, la plantilla, se repone si falta). Nunca borres un encantamiento que ya tienen los
jugadores: ponle `enabled: false`.

## ¿Recargar o reiniciar?

Minecraft solo acepta encantamientos nuevos mientras arranca el servidor. Por eso:

- **`/ce reload`** aplica: nombres, descripciones, colores, formato del lore, rarezas (visualización),
  probabilidades de los libros, interruptores de fuentes, ranuras, objetos auxiliares, lo visual de `vanilla-enchants.yml`, los menús (salvo su
  `command:` propio) y los mensajes.
- **Hace falta reiniciar** para: añadir un encantamiento o cambiar su nivel máximo, su peso, los objetos
  a los que se aplica, sus incompatibilidades, su coste en yunque o mesa, o si aparece en la mesa, en los
  aldeanos o en el botín.

`/ce reload` dice exactamente qué cambios quedan pendientes de reinicio. En los archivos por defecto,
cada opción lleva ⟳ (recarga) o ⏻ (reinicio).

## Archivos de configuración

Los archivos y sus claves están en inglés (es un plugin para publicar); los mensajes para los jugadores
están traducidos en `lang/es.yml` (`language: es` en `config.yml`).

| Archivo | Contenido |
|---|---|
| `config.yml` | Modo, interruptores de mecánicas vanilla, fallo de libros, ranuras, visualización, idioma, cómo se combinan los efectos de daño (`damage`), límites de herramientas (`tools`) |
| `rarities.yml` | Rarezas: nombre, color, peso, orden en el lore, probabilidades por defecto de los libros |
| `vanilla-enchants.yml` | Los encantamientos de Minecraft: nombre, rareza, descripción y opciones de juego ([más](enchantments/vanilla.md)) |
| `item-groups.yml` | Grupos de objetos (`swords`, `armor`…) con objetos, etiquetas (`#minecraft:swords`) u otros grupos (`@tools`) |
| `items.yml` | Extractor, catalizador, ampliador de ranuras y transmutador (aspecto de los de rareza y de los genéricos), y el aspecto de los libros |
| `menus/*.yml` | Menús: la tienda, listas e información de encantamientos, o los tuyos ([más](menus.md)) |
| `enchants/*.yml` | Un archivo por encantamiento |
| `lang/en.yml`, `lang/es.yml` | Todos los mensajes (MiniMessage). Si falta una clave se usa el texto en inglés incluido |
| `data/known-enchants.yml` | Lista interna de todos los encantamientos registrados alguna vez. **No se edita** |
| `backups/` | Copias de tus archivos de antes de añadirles opciones nuevas (las 5 últimas de cada uno) |

**Opciones nuevas tras actualizar.** Al arrancar y con `/ce reload`, las opciones que trae una versión nueva en
`config.yml`, `items.yml` y `lang/*.yml` se añaden a tus archivos, con sus comentarios y en su sitio. No cambia
nada de lo que ya tienes (valores, comentarios, orden); una copia del archivo anterior va a `backups/`. No se
añade una opción si cambiaría lo que hace el plugin (por ejemplo, un interruptor de `vanilla-mechanics` cuyo
valor por defecto depende del modo), ni dentro de una sección escrita en una línea (`display: {mode: ITEM}`):
la consola lo dice una vez. Tus archivos de contenido (rarezas, grupos de objetos, `vanilla-enchants.yml`,
encantamientos, menús) nunca se tocan. Se apaga con `update-files: false`.
