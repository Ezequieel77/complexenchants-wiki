# Compatibility and performance

## Compatibility

- **Protection and claim plugins**: respected through cancelled events and the API events above.
- **Plugins that read item lore** (some shops and auction houses) see items without the enchantment
  lines in `PACKETS` mode. That's expected; use `ITEM` mode if you need them.
- **Bedrock players (Geyser)**: enchantments work, since they are real enchantments. The formatted lore
  is sent in packets like any other lore and usually shows, but Geyser translates items in its own way,
  so how it looks on Bedrock is not guaranteed. ComplexEnchants does not depend on Geyser or Floodgate.
- **Archaeology** (suspicious sand and gravel) is not filtered: if an enchantment is allowed in loot or
  fishing, it may appear there. Its tag is shared with loot and Minecraft gives no event to separate it.

## Performance and profiling

ComplexEnchants is event-driven: it runs **no repeating tasks**, except the `interval` trigger and `bleed`,
and only for players who have them. Effects are compiled when loading, so nothing is parsed in game, and a
player without effects is skipped in the first check of every event. The only work that happens all the
time is adding the lore to inventory packets, which runs on the network threads (not the main thread):

- Before copying an item, a quick check skips everything without custom enchantments, including items
  with only vanilla enchantments (unless you gave them a name, rarity or visible description in
  `vanilla-enchants.yml`) or lore from other plugins.
- Formatted lore is cached per set of enchantments and cleared on `/ce reload`. A cache hit costs well
  under a microsecond; building a new entry takes about a quarter of a millisecond, once per combination.
- PlaceholderAPI placeholders are cheap enough for TAB or a scoreboard refreshing every few ticks: a few
  microseconds each. Values that don't depend on the player (`enchant_…`, `count`, `rarity_…`) and the
  lookup of enchantments by name are computed once per configuration.

### Measuring it on your server with spark

[spark](https://spark.lucko.me/) is the standard profiler for Paper.

1. Install spark (or use the built-in `/spark` on recent Paper builds).
2. At a busy time, start a profile that includes the network threads, where the lore is rendered:
   ```
   /spark profiler start --thread * --timeout 600
   ```
3. Let players play normally for 10 minutes. The profile stops on its own and spark posts a link.
4. Open the link and search for `complexenchants`:
   - **Server thread**: listeners (clicks, anvil, table, loot) and effects: `TriggerListener` and
     `Dispatcher` (triggered effects), `PassiveManager` (passives, only when equipment changes) and
     `ToolBreak` (area and vein mining). This should be a tiny fraction of a millisecond per tick. If
     `ToolBreak` stands out, lower `tools.max-blocks` or the radius of your area effects; if `Dispatcher`
     does, look for effects with `target: nearby` and a large radius on frequent triggers.
   - **Netty threads**: `DisplayHandler` and `ItemDisplay` (lore). This does not affect TPS, but it
     should stay a small share of those threads.
   - **Placeholders**: `PapiExpansion` and `Placeholders` appear under whichever thread asks for them
     (the server thread, or TAB's and scoreboard plugins' own threads). Each call should take a few
     microseconds.
   - **Menus**: `MenuService` and `MenuRenderer`, only when a menu is opened or clicked.
5. To compare, run the same profile once with `display.mode: ITEM` (no packet work at all).

If ComplexEnchants shows up high, please share the spark link in your report.

## Building from source

Requires JDK 25 (Gradle downloads it automatically if missing). The `.jar` runs on Java 21.

```
./gradlew build                 # jar in plugin/build/libs/, runs every test
./gradlew :plugin:runServer     # test server, Paper 1.21.11
./gradlew :plugin:runServer26   # test server, Paper 26.3
```

Modules: `api` (public API), `core` (all logic, Paper API only), `effects` (the effects module,
[Effects](effects/index.md)), `nms/v1_21` and `nms/v26_3` (packet
display per Minecraft version) and `plugin` (packaging). Tests use JUnit and MockBukkit; a skipped
test fails the build, so a green build means every test really ran.
