# Crear un encantamiento

Copia `enchants/_example.yml` (los archivos que empiezan por `_` no se cargan) y cámbiale el nombre.
**El nombre del archivo es el id**: `rayo_vital.yml` pasa a ser `complexenchants:rayo_vital`. Usa solo
minúsculas, números y `_`.

```yaml
enabled: true
name: "Rayo vital"                # el color de la rareza se añade solo
description:
  - "<gray>Golpea con el poder de la vida."
rarity: epic                      # de rarities.yml
max-level: 3
applicable: [swords, axes]        # grupos de item-groups.yml
conflicts: [otro_encantamiento, minecraft:sharpness]
mode: INHERIT                     # BOOKS | VANILLA | INHERIT
anvil-cost: 4
sources:                          # fuentes VANILLA (cada una necesita también su interruptor en config.yml)
  enchanting-table: true
  villagers: true
  loot: true
  fishing: false
book-chances:                     # modo LIBROS: "50", "40-80" o "random" (destrucción = 100 − éxito)
  success: "40-80"
```

La plantilla explica todas las opciones.

> **Nunca borres un encantamiento que ya tengan los jugadores.** Usa `enabled: false`. Si borras el
> archivo, ComplexEnchants lo recuerda (`data/known-enchants.yml`) y lo sigue registrando, así que los
> objetos que lo tienen no se rompen; en su lore aparece como "borrado".

## Editor en el juego

`/ce editor` (permiso `complexenchants.editor`, op) edita los mismos archivos sin salir del juego: menús de cofre
para moverse y los formularios propios de Minecraft (diálogos, 1.21.6+) para editar. Su pantalla de inicio tiene
cuatro botones:

- **Encantamientos**: todos (los desactivados en gris, los que esperan un reinicio marcados), por rareza e id, con
  filtro por rareza, buscador (id o nombre) y, al final, los archivos que no cargaron (clic: sus problemas). Clic en
  uno para abrirlo:
  - **Propiedades**: nombre, descripción, rareza, nivel máximo, grupos aplicables, incompatibilidades, dónde está
    activo.
  - **Fuentes y libro**: modo, las cuatro fuentes, éxito del libro, peso, coste en el yunque, piedra de afilar.
  - **Efectos**: un ítem por efecto. Clic para editarlo, Shift + clic izquierdo/derecho para moverlo, clic derecho
    para quitarlo. "Añadir" pide el efecto, luego el trigger (solo los compatibles) y luego su formulario. Mover o
    quitar un efecto renumera las etiquetas `<value:N:…>` de la descripción.
  - Activar/desactivar, duplicar (pide el id nuevo) y sus avisos.
  - **Crear** (en la lista): id, nombre, descripción, rareza, nivel máximo y grupos. El archivo solo lleva eso; lo
    demás sale de su rareza.
- **Rarezas**, **Grupos de objetos** y **Encantamientos vanilla**: los mismos formularios para `rarities.yml`,
  `item-groups.yml` y `vanilla-enchants.yml`. Una rareza o un grupo en uso no se puede quitar (dice quién lo usa);
  "Restablecer" quita la sección de un encantamiento vanilla, que vuelve a ser como en Minecraft.

Cada cambio se comprueba con los cargadores reales antes de guardar: si hay errores, el formulario vuelve a
abrirse con ellos y con lo que escribiste. Guardar escribe el archivo (el anterior se copia en `backups/editor/`,
los últimos 10 de cada uno) y lo aplica como `/ce reload`; lo que necesita reinicio sale marcado con ⏻. Si alguien
cambió el archivo desde que lo abriste, no se sobrescribe nada y te avisa. Desde el editor no se borra nada: para
quitar un encantamiento, usa su archivo.

Lo avanzado se muestra de solo lectura y se conserva tal cual al guardar lo demás: grupos de efectos con pasos o
retardos, `levels:`, condiciones `any:`/`not:`, grupos con nombre (`use:`), `active-skill` y targets con opciones.
Un archivo guardado desde el editor conserva sus comentarios, pero puede cambiar de estilo (comillas, listas).

> **El editor equivale a la consola**: el efecto `command` ejecuta comandos de consola. Da
> `complexenchants.editor` solo a administradores de confianza. Los jugadores de Bedrock (Geyser) no ven bien los
> diálogos.
