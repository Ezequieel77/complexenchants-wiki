# Preguntas frecuentes

**Añadí un encantamiento y no existe.** Los encantamientos nuevos necesitan reiniciar el servidor.
`/ce list` lo muestra como "pendiente de reinicio".

**Cambié `max-level` y no pasó nada.** Los cambios de registro necesitan reiniciar. `/ce reload` lista
lo que queda pendiente.

**¿Puedo borrar un encantamiento?** Mejor `enabled: false`. Si borras el archivo, sigue registrado como
tombstone para que los objetos sigan funcionando, y su lore lo muestra como borrado.

**La consola dice que `known-enchants.yml` estaba dañado.** ComplexEnchants rescató todos los ids que
encontró en él y guardó una copia llamada `known-enchants.yml.damaged-<hora>`. Comprueba que no falte
ningún encantamiento.

**Los jugadores ven también la línea vanilla del encantamiento.** Pon `display.hide-vanilla-enchant-lines: true`.

**Los ítems de menú que cobran dinero no se pueden pagar.** Instala Vault y un plugin de economía, y reinicia.

**La consola dice que un archivo no está guardado en UTF-8.** Se editó con un programa que lo guardó en otra
codificación (el Bloc de notas antiguo de Windows lo hace, como "ANSI"). Se lee igual, pero las tildes pueden
verse mal: ábrelo y guárdalo en UTF-8. Mientras tanto, no se le añaden opciones nuevas.
