# Compatibilidad y rendimiento

## Compatibilidad

- **Plugins de protección y parcelas**: se respetan mediante los eventos cancelados y los eventos de la API.
- **Plugins que leen el lore** (algunas tiendas y casas de subastas): en modo `PACKETS` ven los objetos
  sin las líneas de encantamientos. Es lo esperado; usa el modo `ITEM` si las necesitas.
- **Jugadores de Bedrock (Geyser)**: los encantamientos funcionan, porque son encantamientos reales. El
  lore con formato se envía en los paquetes como cualquier otro lore y normalmente se ve, pero Geyser
  traduce los objetos a su manera, así que no se puede garantizar cómo se verá en Bedrock.
  ComplexEnchants no depende de Geyser ni de Floodgate.
- **Arqueología** (arena y grava sospechosas): no se filtra. Si un encantamiento se permite en el botín
  o en la pesca, puede salir ahí; comparte la etiqueta del botín y Minecraft no da un evento para separarla.

## Rendimiento y perfilado

ComplexEnchants funciona por eventos: **no tiene tareas repetitivas**, salvo el trigger `interval` y
`bleed`, y solo para los jugadores que los tienen. Los efectos se compilan al cargar, así que en juego no
se interpreta nada, y un jugador sin efectos sale en la primera comprobación de cada evento. Lo único que
ocurre todo el rato
es añadir el lore a los paquetes de inventario, y eso se hace en los hilos de red (no en el principal):

- Antes de copiar un objeto, un filtro rápido descarta todo lo que no tiene encantamientos
  personalizados, incluidos los objetos con solo encantamientos vanilla (salvo que les hayas dado nombre,
  rareza o descripción visible en `vanilla-enchants.yml`) o con lore de otros plugins.
- El lore con formato se guarda en caché por conjunto de encantamientos y se vacía con `/ce reload`.
  Una consulta a la caché cuesta bastante menos de un microsegundo; crear una entrada nueva, en torno a
  un cuarto de milisegundo, una sola vez por combinación.
- Los placeholders de PlaceholderAPI aguantan sin problema que TAB o un scoreboard los pidan cada pocos
  ticks: unos pocos microsegundos cada uno. Lo que no depende del jugador (`enchant_…`, `count`,
  `rarity_…`) y la búsqueda de encantamientos por nombre se calculan una vez por configuración.

### Medirlo en tu servidor con spark

[spark](https://spark.lucko.me/) es el perfilador estándar de Paper.

1. Instala spark (o usa el `/spark` que ya incluyen las versiones recientes de Paper).
2. En un momento con jugadores, empieza un perfil que incluya los hilos de red, donde se genera el lore:
   ```
   /spark profiler start --thread * --timeout 600
   ```
3. Deja que se juegue con normalidad 10 minutos. El perfil se detiene solo y spark publica un enlace.
4. Abre el enlace y busca `complexenchants`:
   - **Server thread** (hilo principal): listeners (clics, yunque, mesa, botín) y efectos:
     `TriggerListener` y `Dispatcher` (efectos con trigger), `PassiveManager` (pasivos, solo al cambiar
     de equipo) y `ToolBreak` (minería en área y en veta). Debería ser una fracción mínima de
     milisegundo por tick. Si destaca `ToolBreak`, baja `tools.max-blocks` o el radio de tus áreas; si
     destaca `Dispatcher`, busca efectos con `target: nearby` y mucho radio en triggers frecuentes.
   - **Hilos de Netty**: `DisplayHandler` e `ItemDisplay` (el lore). No afecta a los TPS, pero debería
     ser una parte pequeña de esos hilos.
   - **Placeholders**: `PapiExpansion` y `Placeholders` aparecen en el hilo que los pida (el principal, o
     los propios de TAB y de los plugins de scoreboard). Cada llamada debería tardar unos microsegundos.
   - **Menús**: `MenuService` y `MenuRenderer`, solo al abrir un menú o hacer clic.
5. Para comparar, repite el perfil con `display.mode: ITEM` (sin trabajo en los paquetes).

Si ComplexEnchants aparece alto, comparte el enlace de spark en tu reporte.

## Compilar desde el código

Hace falta el JDK 25 (Gradle lo descarga si no está). El `.jar` funciona con Java 21.

```
./gradlew build                 # .jar en plugin/build/libs/; ejecuta todos los tests
./gradlew :plugin:runServer     # servidor de pruebas, Paper 1.21.11
./gradlew :plugin:runServer26   # servidor de pruebas, Paper 26.3
```

Módulos: `api` (API pública), `core` (toda la lógica, solo API de Paper), `effects` (el módulo de
efectos, [Efectos](effects/index.md)), `nms/v1_21` y `nms/v26_3`
(visualización por paquetes de cada versión de Minecraft) y `plugin` (empaquetado). Los tests usan JUnit
y MockBukkit; un test saltado hace fallar el build, así que un build en verde significa que todos los
tests se ejecutaron de verdad.
