# Triggers

| Trigger | Cuándo | Ofrece |
|---|---|---|
| `melee_attack` | golpeas algo cuerpo a cuerpo | daño, víctima, cancelable |
| `projectile_attack` | tu flecha/tridente impacta en algo. Cuentan los encantamientos del **arma que lo lanzó** (aunque ya no esté en tu mano, como un tridente lanzado) y los de tu armadura | daño, víctima, cancelable |
| `take_damage` | recibes cualquier daño | daño, cancelable |
| `take_entity_damage` | un mob o un jugador te daña | daño, atacante, cancelable |
| `fall_damage` | recibes daño de caída | daño, cancelable |
| `kill` | matas algo | víctima, drops, experiencia |
| `death` | mueres | atacante (si lo hay) |
| `mine_block` | rompes un bloque | bloque, experiencia, cancelable |
| `block_drops` | un bloque que rompiste suelta sus objetos | bloque, drops |
| `shoot` | disparas un arco o ballesta | cancelable |
| `shield_block` | bloqueas con escudo | daño (solo leerlo: el golpe antes del escudo), atacante, cancelable |
| `item_damage` | el **objeto encantado** pierde durabilidad | cancelable |
| `fish` | pescas algo | experiencia, cancelable |
| `consume` | comes o bebes | cancelable |
| `sneak` | empiezas a agacharte | — |
| `jump` | saltas | cancelable |
| `right_click` | haces clic derecho con la mano principal | bloque pulsado (si lo hay), cancelable |
| `interval` | cada `every` segundos mientras el objeto está activo | — |
| `fatal_damage` | un golpe te va a matar (ya calculado del todo); cancelarlo te salva (y el tótem no se gasta) | daño (solo leerlo), atacante si lo hay, cancelable |
| `totem_use` | se usa un tótem (cancelarlo = no te salva) | cancelable |
| `hunger_loss`, `hunger_gain` | baja / sube tu hambre | cancelable |
| `projectile_launch` | lanzas cualquier proyectil (flecha, tridente, perla, bola de nieve…) | cancelable |
| `combat_enter`, `combat_leave` | entras / sales de combate (ver `combat:` en config.yml) | — |
| `world_change` | cambias de mundo | — |
| `block_place` | colocas un bloque | bloque, cancelable |
| `projectile_hit_block` | tu proyectil choca con un bloque (cuenta el arma que lo lanzó) | bloque |
| `shield_disable` | te desactivan el escudo (un hacha, por ejemplo) | atacante, cancelable |
| `item_break` | el **objeto encantado** se va a romper con este desgaste; cancelarlo lo salva | cancelable |
| `active_skill` | el jugador activa la habilidad ([habilidades activas](skills.md)) | — |
| `potion_gain` | te van a poner un efecto de poción (nuevo, renovado o más fuerte), venga de donde venga; quitarlo o que se acabe no cuenta. Con `cancel_event` no se pone | poción, cancelable |

Los efectos y las condiciones que necesitan algo que el trigger no ofrece se rechazan al cargar, con la
lista de triggers que sí servirían. Los triggers solo reaccionan si otro plugin (protecciones,
parcelas…) no canceló el evento.
