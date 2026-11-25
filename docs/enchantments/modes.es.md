# Modos: LIBROS y VANILLA

## Modos: LIBROS y VANILLA

El modo decide cómo se **obtienen y aplican** los encantamientos personalizados. Nunca cambia cómo se
**guardan**, así que se puede cambiar de modo en cualquier momento sin convertir objetos.

| | LIBROS (`BOOKS`) | VANILLA |
|---|---|---|
| Cómo se aplica | Arrastrando el libro sobre el objeto | Yunque (y mesa de encantamientos) |
| Probabilidad de éxito / destrucción | Sí, guardada en cada libro | No |
| Extractor, catalizador, transmutador | Sí | — |
| Combinar libros | Arrastrando un libro sobre otro igual | Yunque |
| Mesa, yunque, aldeanos, botín, pesca | Apagados por defecto | Encendidos por defecto |

El modo global va en `config.yml` (`mode: BOOKS` o `mode: VANILLA`). Una rareza puede cambiarlo con `mode:` en
`rarities.yml`, y un encantamiento con `mode: BOOKS | VANILLA | INHERIT` en su archivo. Gana el más concreto:
encantamiento → rareza → `config.yml` (`INHERIT` = el del siguiente). `/ce info <encantamiento>` dice de dónde
sale el modo. Los encantamientos vanilla siempre se comportan como en vanilla.

## Modo LIBROS

- **Libros**: libros encantados cuya probabilidad de éxito se sortea al crear el libro
  (con la del encantamiento o, si no tiene, la de su rareza). La de destrucción es siempre 100 − éxito
  (58 % de éxito = 42 % de destrucción). El jugador arrastra el libro sobre un
  objeto de su propio inventario. Una sola tirada:
  - **Éxito**: se aplica el encantamiento (o sube de nivel).
  - **Fallo**: se pierde el libro. Con `books.on-fail: BOOK` (por defecto) solo se pierde el libro; con
    `BOOK_AND_ITEM`, además se destruye el objeto.
- **Combinar**: arrastrar un libro sobre otro idéntico (mismo encantamiento y nivel) da uno de nivel
  superior, con la media del éxito de los dos.
- **Extractor**: arrastrado sobre un objeto, pasa un encantamiento personalizado al azar a un libro nuevo.
  Siempre funciona: la probabilidad que muestra es la de éxito que tendrá el libro.
- **Catalizador**: arrastrado sobre un libro, sube su probabilidad de éxito, hasta `max-success`.
- **Ampliador de ranuras**: arrastrado sobre un objeto, le añade ranuras, hasta `slots.max-extra`.
- **Transmutador**: arrastrado sobre un libro de ComplexEnchants, con su probabilidad (sale en su nombre) lo
  convierte en otro encantamiento **distinto** al azar de la **misma rareza**; si falla, se pierde el transmutador
  y, por defecto, también el libro (`destroy-book-on-fail`). Otros plugins pueden cancelarlo o cambiar la
  probabilidad con `BookTransmuteEvent`.

El extractor, el catalizador y el transmutador son **de una rareza** o **genéricos**:

| | De una rareza (p. ej. legendary) | Genérico |
|---|---|---|
| Extractor | solo saca del objeto encantamientos legendarios | cualquiera |
| Catalizador | solo sirve en libros legendarios | cualquier libro |
| Transmutador | solo acepta libros legendarios (y da otro legendario) | cualquier libro (da otro de su rareza) |

Usados sobre algo de otra rareza, avisan y no se gastan.
`/ce give extractor|catalyst|transmuter <jugadores> [cantidad] [rareza|any] [valor]`: sin rareza (o con `any`)
se da el genérico; sin valor, se sortea con `items.yml`. En `items.yml`, `<rarity>` es el nombre de la rareza,
`generic:` cambia solo lo que escribas para el aspecto del genérico (nombre, lore, material, modelo) y
`any-rarity` es lo que muestra `<rarity>` en el genérico. Objetos de antes de la 1.1.0: los extractores y
catalizadores pasan a ser genéricos (los extractores viejos ya no fallan: su probabilidad pasa al libro) y los
transmutadores conservan su rareza.

**Información del libro**: clic derecho con un libro encantado de ComplexEnchants en la mano muestra sus
encantamientos en el chat (descripción, aplicable en, nivel máximo y, en los libros del modo LIBROS, éxito y
destrucción). Se apaga o se deja solo con Shift con `books.right-click-info` / `right-click-info-sneak` en
`config.yml`; el texto es `books.info` del archivo de idioma. Al hacer clic derecho en un cofre, una puerta…
con el libro, solo se muestra si estás agachado.

Los libros del modo LIBROS nunca funcionan en el yunque (se saltarían sus probabilidades). Los montones
de objetos nunca se encantan, y en modo creativo actúa Minecraft.

Los libros y objetos auxiliares se dan con `/ce give` (ver [comandos](../commands.md)) o se venden
en la [tienda](../menus.md).

## Modo VANILLA

Los encantamientos personalizados se comportan como los vanilla. Cada fuente tiene un interruptor
global en `config.yml` (`vanilla-mechanics`) y otro por encantamiento (`sources:`); tienen que estar
encendidos los dos. Una rareza también puede llevar `sources:` (en `rarities.yml`): cada fuente que el
encantamiento no menciona se toma de su rareza, y si la rareza tampoco la menciona, está encendida.

- **Mesa de encantamientos**: respeta las ranuras. Si no queda nada que añadir, la mesa no cobra.
- **Yunque**: combina libros y objetos como en vanilla, respetando las ranuras. `anvil-max-cost` sube el
  límite de "¡Demasiado caro!" solo cuando hay encantamientos personalizados de por medio. Por encima de
  40, el cliente puede seguir mostrando "¡Demasiado caro!", pero el resultado se puede coger.
- **Piedra de afilar**: con `grindstone-removes: false`, los encantamientos personalizados se conservan
  (como las maldiciones). También se puede poner por rareza (`rarities.yml`) y por encantamiento (en su archivo);
  gana el más concreto: encantamiento → rareza → `config.yml`. Se aplica al reiniciar.
- **Aldeanos, botín de cofres y pesca**: Minecraft usa la misma etiqueta para el botín y la pesca;
  ComplexEnchants los separa en tiempo real. Los vaults de las cámaras de prueba cuentan como botín. Si
  un objeto se quedara sin encantamientos, recibe uno permitido al azar.
