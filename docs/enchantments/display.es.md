# Cómo se muestran los encantamientos

- **`display.mode: PACKETS`** (recomendado): la lista con formato solo se añade a lo que ve el
  jugador. Los objetos reales quedan limpios y no se guarda nada en ellos. El modo creativo está
  resuelto: el lore que devuelve el cliente se quita antes de guardarse.
- **`display.mode: ITEM`**: el lore se escribe en los objetos. Úsalo solo si otro plugin necesita leer
  el lore. También se usa automáticamente si esta versión de Minecraft no tiene soporte de paquetes.

Otras opciones: `sort-by` (`RARITY`, `NAME`, `LEVEL`), `descriptions` (`items` / `books`: mostrar la
descripción de cada encantamiento en los objetos encantados y en los libros; el antiguo
`show-descriptions` sigue funcionando para los dos; `vanilla`: también las descripciones de
`vanilla-enchants.yml`, apagado por defecto) y `hide-vanilla-enchant-lines`. El formato de cada
línea está en `lang/*.yml`, en `display`.

**Libros de encantamiento** (modo BOOKS): el nombre y el lore salen de `enchanted-book:` en `items.yml`,
con estos marcadores: `<name>`, `<level>` (del mismo color que el nombre; vacío en los encantamientos de un
solo nivel), `<max-level>`, `<rarity>`, `<applicable>`, `<conflicts>`, `<success>`, `<destroy>` y una línea que sea solo
`<description>`. `<applicable>` lista los grupos de objetos del encantamiento por su `name:` en
`item-groups.yml` (si no tiene, el id: `fishing_rods` → "Fishing Rods"), separados con
`applicable-separator`.

```yaml
enchanted-book:
  name: "<name> <level>"
  lore:
    - "<description>"
    - "<gray>Se aplica a: <white><applicable>"
    - "<gray>Incompatible con: <conflicts>"
    - ""
    - "<green>Éxito: <success>%"
    - "<red>Destrucción: <destroy>%"
  applicable-separator: ", "
```

**`<conflicts>`** lista los encantamientos incompatibles, por su nombre y en su color: los de su `conflicts:` y
los que lo nombran a él (los vanilla, como dice Minecraft, salvo que `vanilla-enchants.yml` los cambie); los
desactivados o que no existen no salen. Una línea con `<conflicts>` y nada que listar se quita. También funciona
en las descripciones, en los menús y en el texto `books.info`.
