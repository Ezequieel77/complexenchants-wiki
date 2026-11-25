# Grupos de efectos

Cada efecto tira su propia probabilidad y tiene su propio enfriamiento. Para que varios efectos salgan
**juntos o ninguno** (un +50 % de daño **y** una lentitud con la misma tirada), o para hacer **secuencias con
esperas**, se agrupan:

```yaml
effects:
  - effect: group
    trigger: projectile_attack
    chance: "11 + level"       # UNA tirada para todo el grupo
    cooldown: "9 - level"      # UN enfriamiento para todo el grupo
    conditions:                # se comprueban una vez
      - victim_type: [player]
    effects:
      - effect: damage_bonus
        percent: "40 + 10 * level"
      - effect: potion
        target: victim
        potion: slowness
        amplifier: 4
        duration: "level"
      - effect: sound
        sound: entity.ghast.scream
        delay: 0.5             # espera 0,5 s antes de este efecto y de los siguientes
```

- El grupo lleva `trigger`, `chance`, `cooldown`, `cooldown-message`, `conditions` y `levels` (y `every` con
  `interval`). Sus efectos **no** llevan `trigger`, `chance`, `cooldown` ni `every` (es un error al cargar).
- Cada efecto del grupo puede tener su `target`, sus `conditions` (solo filtran ese efecto), sus `levels` y un
  `delay` en segundos. Las esperas se suman: como mucho 60 s en total.
- Lo que cambia el propio evento (`damage_bonus` y demás efectos de daño, `cancel_event`, drops, experiencia,
  minería) **no puede ir después de una espera**: el evento ya terminó (error al cargar).
- Tras una espera, si te desconectas o mueres, el resto no se ejecuta; si el target de un paso ya no existe (murió
  o desapareció), ese paso se salta. Un `/ce reload` cancela las esperas pendientes.
- Las fórmulas de los efectos usan los valores del momento del trigger (`damage`, `health`…), aunque se ejecuten
  después de una espera.
- Si un efecto del grupo tiene un error, se descarta el grupo entero. Un grupo no puede contener otro.
- En `/ce debug` y en `<value:…>`, el paso 3 del grupo 2 es el `2.3`.

## Grupos reutilizables: effect-groups.yml

Un grupo que usan varios encantamientos se escribe una vez en `effect-groups.yml` y se usa con `use:`:

```yaml
# effect-groups.yml
aturdir:
  - effect: potion
    target: victim
    potion: slowness
    amplifier: 3
    duration: "1 + level"
  - effect: sound
    sound: entity.iron_golem.hurt

# enchants/martillo.yml
effects:
  - effect: group
    trigger: melee_attack
    chance: "5 * level"
    use: aturdir
```

Cada encantamiento que lo usa lo compila con **su** trigger y **sus** niveles (`level` es el nivel de ese
encantamiento). Si un grupo no vale para el trigger de un encantamiento, el error dice cuál:
`effect-groups.yml (enchants/martillo.yml)`.
