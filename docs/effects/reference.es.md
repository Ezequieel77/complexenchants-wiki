# Referencia de efectos

Los argumentos con un valor entre corchetes son opcionales; ese es su valor por defecto.

## Combate

| Efecto | Argumentos | Target | Notas |
|---|---|---|---|
| `damage_bonus` | `percent` | — | +% de daño. Triggers con daño. |
| `add_damage` | `amount` | — | + daño fijo. |
| `damage_reduction` | `percent` | — | −% del daño recibido. |
| `negate_damage` | `amount` | — | − daño fijo recibido. |
| `lifesteal` | `percent` | — | Cura ese % del daño **final** que haces. `melee_attack`, `projectile_attack`. |
| `heal` | `amount` | self | |
| `damage` | `amount`, [`bypass-armor`: false] | victim | Hace daño (se respetan protecciones y PvP). `bypass-armor: true` = daño de magia: la armadura no lo reduce ni se desgasta (los tótems sí salvan). |
| `potion` | `potion`, `duration` (s), [`amplifier`: 0], [`particles`: true] | self | Amplificador 0 = nivel I. |
| `remove_potion` | `potion` | self | Quita ese efecto de poción al target. |
| `ignite` | `duration` (s) | victim | |
| `lightning` | [`damage`: false] | victim | Solo visual; con `damage: true` hace 5 de daño solo al target (sin fuego ni a nadie más). |
| `knockback` | [`strength`: 1] | victim | Empuja alejándolo de ti; negativo, lo atrae. |
| `bleed` | `damage`, [`interval`: 1] (s), [`times`: 3] | victim | Se para si el target muere. |
| `set_damage` | `amount` | — | El daño base pasa a ser ese; el resto de efectos de daño se aplican después. |
| `freeze` | `duration` (s), [`lock`: true] | victim | Congelado como en la nieve en polvo: lento y, del todo congelado, daño. `lock: true` = al máximo durante `duration`; `lock: false` = se le ponen esos segundos de congelación y se descongela solo (como `SCREEN_FREEZE` de AE). |
| `explode` | [`power`: 2] (TNT = 4, máx. 8), [`fire`: false], [`break-blocks`: false] | victim | No te daña a ti; con `break-blocks`, las protecciones deciden. |
| `pumpkin_head` | `duration` (s) | victim | Solo jugadores. Su casco vuelve siempre (al acabar, al salir, al morir, tras una caída del servidor). |

Los cinco primeros pasan por el [cálculo de daño](mechanics.md#como-se-calcula-el-dano).

## Herramientas

| Efecto | Argumentos | Triggers | Notas |
|---|---|---|---|
| `area_mining` | [`radius`: 1], [`depth`: 0], [`blocks`: cualquiera] | `mine_block` | Una pared de (2r+1)² delante de ti; mirando arriba/abajo, un suelo. `depth` añade capas. `blocks` limita qué bloques rompe (por ejemplo, solo cultivos). |
| `plant_seeds` | [`radius`: 1] (máx. 5), [`seeds`: cualquiera] | triggers con bloque | Siembra en la tierra arada (y la verruga en arena de almas) libre alrededor del bloque, con las semillas de tu inventario. Las protecciones deciden cada siembra. |
| `vein_mining` | [`max`: 16], [`blocks`: cualquiera] | `mine_block` | Bloques conectados del mismo tipo, también en diagonal. `blocks` limita qué vetas (bloques o etiquetas). |
| `autosmelt` | — | `block_drops`, `kill` | Usa las recetas de horno del servidor (incluidas las de datapacks). |
| `telekinesis` | — | `block_drops`, `kill` | Los drops a tu inventario (con `kill`, también la experiencia). Lo que no cabe se queda en el suelo. |
| `multiply_drops` | [`multiplier`: 2], [`blocks`: cualquiera] | `block_drops`, `kill` | Los decimales son una probabilidad: ×1,5 sobre 3 objetos da 4 o 5. |
| `xp_multiplier` | `multiplier` | `mine_block`, `kill`, `fish` | |

## Pasivos (sin trigger)

| Efecto | Argumentos | Notas |
|---|---|---|
| `attribute` | `attribute`, `amount`, [`operation`: add] | `add`, `multiply_base` o `multiply`. Velocidad, vida máxima, armadura, daño, alcance… |
| `permanent_potion` | `potion`, [`amplifier`: 0] | Infinita, sin partículas. |

## Utilidad

| Efecto | Argumentos | Target |
|---|---|---|
| `message` | `text` | self |
| `actionbar` | `text` | self |
| `title` | `title`, [`subtitle`: ""], [`fade-in`: 0.5], [`stay`: 2], [`fade-out`: 0.5] (s) | self |
| `sound` | `sound`, [`volume`: 1], [`pitch`: 1] | self |
| `particle` | `particle`, [`count`: 10], [`spread`: 0.5] | self |
| `command` | `command`, [`as`: console] (`console` o `player`) | self (una vez por target) |
| `cancel_event` | — (triggers cancelables) | — |
| `repair` | `amount` | — (el objeto encantado) |
| `damage_item` | `amount` | — (el objeto encantado) |
| `give_xp` | `amount` | self |
| `mark` | `name`, `duration` (s) | self |
| `remove_mark` | `name` | self |
| `set_var` | `name`, `value` (fórmula) **o** `text` (texto), [`persistent`: true] | — |
| `add_var` | `name`, `amount`, [`persistent`: true] | — |
| `reset_cooldown` | [`enchant`: este] | — |
| `temp_attribute` | `attribute`, `amount`, `duration` (s), [`operation`: add] | self | Se acumulan; nunca se guardan en el jugador. |
| `drop_item` | `item`, [`amount`: 1] | self (o `block`, `victim`…) | Lo suelta en el sitio del target. |
| `repair_armor`, `damage_armor` | [`amount`: 0], [`percent`: 0], [`slot`: all] (`all`, `head`, `chest`, `legs`, `feet`) | self | La armadura del target (toda o una pieza). `percent`: % de la durabilidad que le queda (desgastar) o le falta (reparar) a cada pieza, redondeado hacia abajo: el % solo nunca rompe una pieza. |
| `cancel_armor_damage` | — | — | Tu armadura no se desgasta por este golpe. |
| `remove_enchant` | [`enchant`: este] | — | Lo quita del objeto que lo lleva (un Fénix que se gasta). |
| `velocity` | [`strength`: 1], [`direction`: look] (`look`, `up`, `forward`), [`add`: true], [`no-fall`: false] | self | Impulso hacia donde miras, hacia arriba o hacia delante. `add: false` fija la velocidad en vez de sumarla; `no-fall` perdona la siguiente caída (como `BOOST` de AE: `BOOST:10` = `strength: 1`). |
| `temp_block` | `block`, [`radius`: 0] (máx. 5), `duration` (s) | self | Un cuadrado de (2r+1)² a los pies del target. Solo en aire; no se puede romper, mover ni volar; siempre vuelve a ser aire (también tras una caída del servidor). |
| `jail` | `block`, [`shape`: cuboid] (`cuboid`, `sphere`), [`radius`: 3], [`height`: 3], [`roof`: true], `duration` (s) | victim | Jaula alrededor del target, con las mismas reglas que `temp_block`. |
| `zone` | `name`, [`shape`: circle] (`circle`, `square`), `radius`, `duration` (s), [`particle`] | self | Zona temporal para la condición `in_zone`; la partícula dibuja el borde. |
| `launch_projectile` | [`entity`: arrow], [`speed`: 3], [`fuse`: 4], [`break-blocks`: false] | — | Lanza un proyectil desde tus ojos (flecha, tridente, TNT, bola de fuego, perla…). No se puede recoger. |
| `replace_projectile` | [`entity`: arrow], [`fuse`: 4], [`break-blocks`: false] | — | Solo `projectile_launch`: cambia el proyectil por otro (TNT en vez de flecha; un tridente "fantasma" que no sale de tu mano). |
| `bossbar` | `id`, `text`, [`color`: white], [`style`: solid], [`progress`: 1], [`duration`: 0] | self | Crea o actualiza la barra con ese id. Pídela cada segundo con `duration: 2` para verla mientras llevas el objeto. `duration: 0` = hasta `bossbar_remove`. |
| `bossbar_remove` | `id` | self | |

- **Texto** (`message`, `actionbar`, `title`): MiniMessage con `<player>`, `<target>`, `<victim>`,
  `<attacker>`, `<level>` y `<var:nombre>` (valor de una variable tuya).
- **`command`**: los mismos marcadores, en texto plano. En los mobs, `<victim>`, `<attacker>` y `<target>`
  son su UUID, nunca su nombre: un nombre personalizado no puede colar argumentos en un comando de consola.
- **`particle`**: solo acepta partículas sin datos extra (por ahora, nada de `dust` ni `block`).
- **Tipo Irrompibilidad**: `cancel_event` con el trigger `item_damage` y una `chance`. Solo protege el
  objeto que lleva el encantamiento.
