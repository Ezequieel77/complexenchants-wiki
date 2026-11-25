# Comandos y permisos

Comando principal `/complexenchants`, alias `/ce`. Cada jugador solo ve los subcomandos para los que
tiene permiso.

| Comando | Permiso | Por defecto |
|---|---|---|
| `/ce help` (o `/ce`): los comandos que **tú** puedes usar, con clic; también los comandos propios de los menús | `complexenchants.command.help` | todos |
| `/ce shop` | `complexenchants.shop` | todos |
| `/ce shop <jugador>` | `complexenchants.shop.others` | op |
| `/ce menu open <menú> [jugador] [argumento] [página]`, `/ce menu list` | `complexenchants.command.menu` | op |
| `/ce debug` (ver qué efectos tuyos se ejecutan, o por qué no) | `complexenchants.command.debug` | op |
| `/ce give skillbook <jugadores> [cantidad]` (el libro de habilidades activas) | `complexenchants.command.give` | op |
| `/ce list [página]` | `complexenchants.command.list` | op |
| `/ce info <encantamiento>` (también `minecraft:sharpness`) | `complexenchants.command.info` | op |
| `/ce reload` | `complexenchants.command.reload` | op |
| `/ce enchant <encantamiento> [nivel]` | `complexenchants.command.enchant` | op |
| `/ce unenchant <encantamiento>` | `complexenchants.command.enchant` | op |
| `/ce item` (ranuras y encantamientos del objeto en la mano) | `complexenchants.command.item` | op |
| `/ce give book <jugadores> <encantamiento> [nivel] [éxito]` | `complexenchants.command.give` | op |
| `/ce give random <jugadores> [rareza\|any]` (sin rareza: cualquier encantamiento, según su peso) | `complexenchants.command.give` | op |
| `/ce give extractor\|catalyst\|transmuter <jugadores> [cantidad] [rareza\|any] [valor]` | `complexenchants.command.give` | op |
| `/ce give slot-expander <jugadores> [cantidad]` | `complexenchants.command.give` | op |
| `/ce editor` (crear y editar encantamientos, rarezas, grupos de objetos y encantamientos vanilla en el juego) | `complexenchants.editor` | op |

`complexenchants.admin` da todos los permisos de la tabla. Los textos de `/ce help` están en los archivos de
idioma (`command.help`).
`/ce enchant` y `/ce unenchant` actúan sobre el objeto de la mano principal y siguen las mismas reglas
que todo lo demás (objetos aplicables, incompatibilidades, ranuras).
