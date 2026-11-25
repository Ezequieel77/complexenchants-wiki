# Cómo funcionan los efectos

## Cómo se calcula el daño

Todos los efectos de daño de **un golpe** (los del atacante y los de la víctima) solo anotan su parte, y
el daño se calcula **una vez**, siempre en este orden:

```
daño base
+ add_damage
× (1 + bonus)          suma de damage_bonus
× (1 − reducción)      suma de damage_reduction (con tope)
− negate_damage
nunca por debajo de 0
```

Después Minecraft aplica la armadura, Protección y Resistencia como siempre. El resultado nunca depende
del orden de los efectos. En `config.yml`:

```yaml
damage:
  bonus-stacking: ADD        # ADD: se suman (15 % × 4 = 60 %). MULTIPLY: como otros plugins.
  reduction-stacking: ADD
  max-bonus: ""              # vacío = sin tope
  max-reduction: 75%         # la reducción nunca pasa del 100 % (el daño nunca cura)
```

El daño que hacen los efectos (`damage`, `lightning`, `bleed`) es daño normal de Minecraft, así que las
protecciones y el PvP lo ven, pero **nunca dispara más efectos**: dos jugadores con "espinas" nunca se
rebotan el daño sin fin.

## Herramientas: área, veta y drops

- **Qué bloques rompe un área o una veta**: los que tu herramienta mina bien, nunca irrompibles (lecho de
  roca), y como mucho el doble de duros que el que picaste. Picando piedra salen también los minerales de
  alrededor, pero no la obsidiana.
- **Las protecciones deciden bloque a bloque**: cada bloque extra se rompe como si lo rompieras tú (pasa
  por las protecciones, gasta durabilidad y suelta sus drops). Si una protección cancela el bloque que
  picaste, no se rompe nada más.
- **Tope**: como mucho `tools.max-blocks` bloques por acción, contando el picado, los más cercanos primero
  (`config.yml`, 64 por defecto, límite absoluto 512). La consola avisa al cargar si un nivel puede pasarse.
- **Los drops se aplican siempre en este orden**: multiplicar → fundir → recoger (telekinesis), los
  escribas en el orden que sea.

## Efectos pasivos

Los efectos pasivos (`attribute`, `permanent_potion`) no llevan trigger: están activos mientras el objeto lo esté.

- Los cambios de atributos nunca se guardan en el jugador: un cierre inesperado no deja bonus "fantasma".
- Las pociones permanentes vuelven tras la leche, un tótem o `/effect clear`, y al reaparecer. Se quitan al
  salir y se limpian al entrar si un cierre inesperado dejó alguna. Una poción más fuerte de otra fuente
  (faro, poción) nunca se quita.
- Sus valores solo pueden depender de `level` (sin `random`): se calculan al equipar el objeto.

## Valores en la descripción

La descripción puede mostrar los valores de un efecto para el nivel del objeto, así nunca escribes los
números dos veces:

```yaml
description:
  - "<gray>+<value:1:percent>% de daño (<value:1:chance>% de probabilidad)"
```

`<value:N:argumento>`: N es el número del efecto en la lista (desde 1, como en `/ce debug`; dentro de un grupo,
`<value:1.2:duration>` es el segundo efecto del grupo); también valen `chance` y `cooldown`. Si el valor depende
del juego (`"damage * 0.1"`) se muestra la fórmula; si la etiqueta está mal escrita, `?`.

**Cálculos con esos valores**: dentro de `<calc:…>`, `value(N, argumento)` es ese mismo número, así que puedes hacer
cuentas con él:

```yaml
description:
  - "<gray>Hasta <white><calc:value(1, percent) * 5>%</white> con 5 cargas"
```

Si el valor depende del juego, todo el `<calc>` muestra `?`.

**Encantamientos incompatibles**: `<conflicts>` los lista, por su nombre y en su color (los de su `conflicts:` y
los que lo nombran a él). Una línea de la descripción con `<conflicts>` y nada que listar se quita.
