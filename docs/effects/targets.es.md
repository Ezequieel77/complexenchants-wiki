# Targets

| `target` | Quién |
|---|---|
| `self` | tú (por defecto en la mayoría de efectos) |
| `victim` | la entidad que golpeaste o mataste |
| `attacker` | quien te golpeó o te mató |
| `nearby` | entidades a tu alrededor (sin ti), las más cercanas primero |
| `block` | el bloque del trigger (sonidos, partículas, rayos) |

`nearby` admite opciones:

```yaml
target:
  type: nearby
  radius: 6          # bloques, 0,5–32 (por defecto 5)
  max: 5             # entidades, 1–64 (por defecto 10)
  entities: [monster]   # filtro opcional (ver victim_type abajo)
```

Si el target no existe en ese evento (una muerte sin atacante), el efecto no se ejecuta.
