# Depuración y limitaciones

## Depurar: /ce debug

`/ce debug` (permiso `complexenchants.command.debug`, op) muestra en tu chat cada efecto **tuyo** que se
ejecuta, o por qué no: enfriamiento (segundos restantes), la condición que falló, la tirada de
probabilidad, sin target, u otro plugin que lo canceló. Repítelo para desactivarlo.

Para mostrar variables, marcas, enfriamientos o el combate en un scoreboard o en TAB, usa los placeholders de
PlaceholderAPI `%ce_var_<nombre>%`, `%ce_mark_<nombre>%`, `%ce_cooldown_<encantamiento>%`,
`%ce_skill_cooldown_<encantamiento>%` y `%ce_in_combat%` ([README](../placeholders.md)).

## Limitaciones

- **Solo jugadores**: los mobs con objetos encantados no ejecutan efectos (por ahora).
- **`interval` va de segundo en segundo** (`every` como mínimo 1; un decimal espera al siguiente segundo entero).
  Cambios como `forward_speed` o que la lanza "se canse" pueden tardar hasta un segundo en notarse.
- **Plugins que cambian el daño después de ComplexEnchants** (`HIGHEST`/`MONITOR`) cambian su resultado.
  ComplexEnchants aplica el daño en `HIGH` y nunca en `MONITOR`, a propósito.
- **Pociones permanentes**: se reconocen por su firma (infinita, ambiental, sin partículas). Si otro plugin
  da exactamente el mismo tipo de poción, quitarse el objeto podría quitarla también. Es poco probable;
  usa `attribute` cuando haya uno equivalente (velocidad, vida…).
- **Partículas con datos extra** (color, bloque): aún no se admiten.
- **Folia**: un efecto sobre una entidad o un lugar de otra región (un target `nearby` lejano) se aplica un
  tick después, en el hilo de esa región. Los bloques de un área o veta que caen en otra región se omiten.
