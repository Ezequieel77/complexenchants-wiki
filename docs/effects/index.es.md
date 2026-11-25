# Efectos

Lo que **hacen** los encantamientos: bonus de daño, pociones, minería en área, autofundir, velocidad
permanente… Los efectos van en el archivo de cada encantamiento y se aplican con `/ce reload` (sin reiniciar).

## Ejemplo rápido

```yaml
# enchants/rayo_vital.yml (las opciones de la base: ver Crear un encantamiento)
name: "Rayo vital"
rarity: epic
max-level: 5
applicable: [swords]
description:
  - "<gray>+<value:1:percent>% de daño contra jugadores débiles"

effects:
  # +10 % de daño por nivel contra jugadores por debajo de la mitad de vida, el 15-25 % de las veces.
  - effect: damage_bonus
    trigger: melee_attack
    percent: "10 * level"
    chance: "15 + 2 * level"
    cooldown: 2
    conditions:
      - victim_type: [player]
      - victim_health_below: 50%

  # Ralentiza a la víctima.
  - effect: potion
    trigger: melee_attack
    target: victim
    potion: slowness
    duration: "1 + 0.5 * level"

  # Mientras la empuñas: +5 % de velocidad por nivel.
  - effect: attribute
    attribute: movement_speed
    operation: multiply
    amount: "0.05 * level"
```

## Partes de un efecto

| Clave | Significado |
|---|---|
| `effect` | Qué efecto es ([referencia](reference.md)). Obligatoria. |
| `trigger` | Cuándo se ejecuta ([triggers](triggers.md)). Obligatoria, salvo en los [efectos pasivos](mechanics.md#efectos-pasivos), que no llevan. |
| `target` | A quién se aplica ([targets](targets.md)), en los efectos que lo usan. |
| `chance` | Probabilidad en % (fórmula). Por defecto, 100. |
| `cooldown` | Segundos antes de poder volver a ejecutarse, por jugador y por efecto. Solo puede depender de `level`. |
| `cooldown-message` | `true` = muestra el tiempo restante en la barra de acción mientras está en enfriamiento. |
| `conditions` | Todas deben cumplirse ([condiciones](conditions.md)). |
| `levels` | Valores concretos para niveles sueltos: `levels: { 5: { chance: 100 } }`. Vale para cualquier argumento, `chance` o `cooldown`. |
| `every` | Solo con el trigger `interval`: cada cuántos segundos (mínimo 1). |
| *otras claves* | Los argumentos propios del efecto (`percent`, `potion`…). |

**Un error nunca deja un efecto a medias.** Si un efecto tiene un error (efecto desconocido, un trigger
que no puede usar, una fórmula mal escrita, una condición rota…), se descarta ese efecto entero y la
consola dice exactamente dónde y por qué; el resto sigue funcionando. Las claves desconocidas y los
valores fuera de rango solo son avisos.

Cuando ocurre un trigger, el orden de comprobación es: enfriamiento → condiciones → probabilidad →
targets → efecto. Si un efecto no se ejecuta, no gasta su enfriamiento.

## Dónde está activo un encantamiento

Los efectos solo funcionan mientras el objeto está **puesto o en la mano correcta**. Una espada en un
cofre o en la mochila no hace nada, y los libros encantados tampoco. Se indica con `active-in` en el
archivo del encantamiento:

| `active-in` | Activo cuando el objeto está en… |
|---|---|
| `MAINHAND` | la mano principal |
| `OFFHAND` | la mano secundaria |
| `HANDS` | cualquiera de las dos manos |
| `ARMOR` | su casilla de armadura |
| `ANY` | una mano o una casilla de armadura |

Si no lo pones, se deduce de `applicable`: armadura → `ARMOR`, escudos → `HANDS`, el resto → `MAINHAND`.
**Cada pieza cuenta por separado**: el mismo encantamiento en 4 piezas de armadura se ejecuta 4 veces
(así, "15 % de reducción" en cada pieza = 60 %).

## Fórmulas y niveles

Cualquier número puede ser una fórmula: `"10 + 5 * level"`, `"min(level, 3)"`,
`"victim_health / victim_max_health < 0.3"`.

- **Operadores**: `+ - * / % ^`, paréntesis, comparaciones `< <= > >= == !=`, y `&& || !` (verdadero = 1, falso = 0).
- **Funciones**: `min`, `max`, `floor`, `ceil`, `round`, `abs`, `sqrt`, `clamp(valor, mín, máx)`, `random(a, b)`,
  `nearby_players(radio)` (jugadores cerca, sin ti), `nearby_entities(radio)` (entidades vivas cerca, sin ti) y
  `nearby_enemies(radio)` (jugadores cerca a los que podrías golpear ahora: se pregunta a las protecciones, zonas
  sin PvP, facciones y equipos, como un golpe real, sin golpear a nadie); radio máximo 32; `var("nombre")` (variable del jugador como número), `mark_time("nombre")` (segundos que le quedan a
  una marca tuya) y `cooldown("encantamiento")` (segundos de enfriamiento que te quedan en ese encantamiento). Las de
  azar, entidades cercanas, variables, marcas y enfriamientos no se pueden usar en los efectos pasivos.
- **Variables**:

| Variable | Disponible |
|---|---|
| `level` | siempre |
| `health`, `max_health`, `food`, `player_level`, `y` | en todos los triggers (son del jugador) |
| `damage` | triggers con daño |
| `victim_health`, `victim_max_health` | triggers con víctima |
| `attacker_health`, `attacker_max_health` | triggers con atacante |
| `distance` | triggers con víctima o atacante |
| `speed` | siempre: tu velocidad real en bloques/s (andando ~4,3, corriendo ~5,6, a caballo, cayendo…), medida con tus posiciones del último cuarto de segundo; quieto = 0 |
| `fall_distance` | siempre: bloques que llevas cayendo (el golpe especial del mazo pide más de 1,5) |
| `forward_speed`, `side_speed` | siempre: tu velocidad real en horizontal (como `speed`) hacia donde miras (negativa = hacia atrás) y de lado (positiva = a tu derecha), en bloques/s |
| `victim_armor_pieces` | triggers con víctima: piezas de armadura que lleva (0–4; unas elytras o una calabaza no cuentan) |
| `potion_amplifier`, `potion_duration` | `potion_gain`: amplificador (0 = nivel I) y duración en segundos (infinita: -1) del efecto que llega |

Usar una variable que el trigger no tiene es un error al cargar, y el mensaje lista las que sí existen
ahí. Un resultado que no es un número (división por cero…) vale 0. Las fórmulas que solo usan `level` se
calculan una vez al cargar, así que en juego cuestan lo mismo que un número fijo.
