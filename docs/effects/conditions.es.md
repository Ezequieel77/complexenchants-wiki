# Condiciones

Cada condición es una línea `nombre: valor`. Todas deben cumplirse; usa `any:` (basta una) y `not:` para
otra lógica:

```yaml
conditions:
  - health_below: 30%
  - any:
      - in_water: true
      - y_between: "-64-40"
  - not:
      sneaking: true
```

| Condición | Valor | Necesita |
|---|---|---|
| `health_below`, `health_above` | cantidad (`6`) o % de la vida máxima (`50%`) | — |
| `victim_health_below`, `victim_health_above` | igual | víctima |
| `attacker_health_below`, `attacker_health_above` | igual | atacante |
| `victim_type`, `attacker_type` | lista de tipos de entidad, etiquetas (`"#minecraft:undead"`) o `mob`, `monster`, `animal` | víctima / atacante |
| `victim_is_boss` | `true` / `false` (Wither, Dragón del End) | víctima |
| `attacker_holding`, `victim_holding` | lista de objetos o etiquetas en la mano principal del atacante / la víctima | atacante / víctima |
| `has_potion`, `victim_has_potion`, `attacker_has_potion` | lista de pociones activas (basta una) | — / víctima / atacante |
| `potion_type` | lista de pociones: la que llega es una de ellas | trigger `potion_gain` |
| `damage_cause` | lista de causas de daño (`fall`, `lava`, `fly_into_wall`, `projectile`…) o grupos: `fire` (fuego, lava, suelo de magma, fogata), `explosion` | daño |
| `is_projectile`, `critical`, `headshot` | `true` / `false`: el daño es de un proyectil, es un golpe crítico, el proyectil dio en la cabeza | daño |
| `sneaking`, `sprinting`, `on_ground`, `in_water`, `underwater`, `on_fire`, `blocking`, `gliding`, `using_item`, `charging` | `true` / `false` (`underwater` = con la cabeza bajo el agua; `using_item` = manteniendo el uso de un objeto: cargando la lanza, tensando el arco, comiendo, escudo arriba…; `charging` = cargando la lanza y la carga sigue activa: cuando la lanza "se cansa", deja de contar aunque sigas apretando) | — |
| `in_world` | lista de nombres de mundo; `*` es cualquier texto (`"dungeon_*"`) | — |
| `in_biome` | lista de biomas | — |
| `time` | `day` / `night` | — |
| `weather` | `clear` / `rain` / `thunder` | — |
| `y_between` | rango: `"0-64"` o `[0, 64]` | — |
| `light_below`, `light_above` | número 0–15 | — |
| `block_type` | lista de bloques o etiquetas (`"#minecraft:logs"`) | bloque |
| `block_natural` | `true` / `false`: el bloque no lo puso un jugador (lo que ya estaba puesto antes de esta versión cuenta como natural; los pistones y la arena/grava que cae conservan la marca) | bloque |
| `crop_grown` | `true` / `false`: el bloque es un cultivo maduro (trigo, zanahoria, patata, remolacha, verruga del Nether, cacao, bayas dulces) | bloque |
| `holding` | lista de grupos de objetos (de item-groups.yml) en la mano principal | — |
| `consumed_item` | lista de objetos o etiquetas (`golden_apple`, `"#minecraft:..."`) | trigger `consume` |
| `has_permission` | lista de permisos (hacen falta todos) | — |
| `level_above`, `food_above` | número | — |
| `in_combat` | `true` / `false` | — |
| `in_zone` | lista de zonas (de `zone`; basta una) | — |
| `has_mark`, `victim_has_mark`, `attacker_has_mark` | lista de marcas (basta una) | — / víctima / atacante |
| `var_is` | variables y su valor: `{ modo: tank, cargas: 3 }` (todas deben coincidir; sin valor = 0) | — |
| `expression` | fórmula; se cumple si no vale 0 | — |
