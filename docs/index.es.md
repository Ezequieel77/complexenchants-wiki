# ComplexEnchants

Encantamientos personalizados para Paper, definidos en YAML y registrados como **encantamientos reales
de Minecraft**. Se pueden usar al estilo clásico (arrastrar un libro sobre un objeto, con probabilidad
de éxito y de destrucción) o al estilo vanilla (mesa de encantamientos, yunque, aldeanos, botín), y se
elige de forma global o por encantamiento.

Los encantamientos también pueden **hacer cosas**: bonus de daño, pociones, minería en área, autofundir,
velocidad permanente y más, con triggers, condiciones, probabilidades, enfriamientos y fórmulas por nivel.
Esa parte tiene su propia guía: **[Efectos](effects/index.md)**.

## Características

- Los encantamientos son **encantamientos reales del registro**: salen en el tooltip vanilla, hacen
  brillar el objeto, funcionan con `/enchant` y los devuelve `ItemStack#getEnchantments()`.
- **Dos modos**, globales y por encantamiento:
  - **LIBROS** (`BOOKS`): se arrastran libros sobre los objetos, con probabilidad de éxito y de
    destrucción, además de extractor, catalizador, transmutador (cada uno de una rareza o genérico) y
    ampliador de ranuras.
  - **VANILLA**: mesa de encantamientos, yunque, piedra de afilar, aldeanos bibliotecarios, botín de
    cofres y pesca.
- **Ranuras de encantamiento** por grupo de objetos, ampliables.
- **Lore en los paquetes**: el jugador ve una lista con formato (ordenada por rareza, con
  descripciones) y el objeto real queda limpio. El modo `ITEM` escribe el lore en el objeto, para los
  plugins que lo necesiten.
- **Menús** (`menus/`): listas de encantamientos por rareza (con un botón para filtrarlas por objeto),
  información de cada uno y una **tienda** de libros aleatorios por rareza, con dinero (Vault) o experiencia.
  Sin plugin de menús; PlaceholderAPI funciona si está instalada.
- **Editor en el juego** (`/ce editor`): crear y editar encantamientos, sus efectos, rarezas, grupos de objetos y
  encantamientos vanilla con menús de cofre y los diálogos de Minecraft ([más](enchantments/creating.md#editor-en-el-juego)).
- **Listo para jugar**: trae 112 encantamientos, 7 rarezas y sus menús (se instalan en el primer arranque; ver
  [Instalación](getting-started.md#instalacion)).
- **Borrar un encantamiento nunca rompe objetos**: sigue registrado como "tombstone".
- **Sin dependencias obligatorias.** Vault (dinero en los menús) y PlaceholderAPI (marcadores en los menús, y
  nuestros propios placeholders) son opcionales.
- **Efectos**: 32 triggers, 51 condiciones y 55 efectos (combate, herramientas, pasivos, utilidad), todos
  recargables con `/ce reload`. Ver [Efectos](effects/index.md).
- Compatible con **Folia**.
- Todos los mensajes en **MiniMessage**, con inglés y español incluidos. `/ce help` lista los comandos que
  puede usar cada jugador.
- **Errores de configuración claros**: archivo, clave, qué se esperaba y qué se usó en su lugar. Un
  archivo roto nunca impide cargar los demás.
