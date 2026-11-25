# API for developers

## Enchantments API

The `api` module has no dependency on the rest of the plugin.

```java
ComplexEnchantsApi api = Bukkit.getServicesManager().load(ComplexEnchantsApi.class);

api.enchant("life_bolt").ifPresent(enchant -> {
    ApplyResult result = api.apply(player, item, enchant.key(), 2, ApplyCause.API);
    if (!result.isSuccess()) {
        player.sendMessage("Could not apply: " + result.status());
    }
});
Map<CustomEnchant, Integer> onItem = api.enchantsOn(item);
api.openShop(player);
api.openMenu(player, "enchant_list", "epic");
```

Cancellable events, so protection, claim and clan plugins can intervene:

| Event | When |
|---|---|
| `EnchantApplyEvent` | Before any custom enchantment is applied (book, anvil, table, command, API) |
| `EnchantRemoveEvent` | Before one is removed (extractor, command, API) |
| `BookPurchaseEvent` | Before a `[buy]` purchase (the shop) is charged. The price can be changed (discounts) |
| `BookTransmuteEvent` | Before a transmuter is used on a book. The chance can be changed |
| `EnchantEffectEvent` | Before an effect runs (for example, to stop effects between clan allies) |
| `ComplexEnchantsReloadEvent` | After every successful `/ce reload` (not cancellable) |

Custom effects, conditions and triggers: see the API section of [Effects](#effects-api).

Every listener uses `ignoreCancelled = true`, so if your plugin cancels a click or event, ComplexEnchants
does nothing. Methods that change items must be called on the thread that owns them (the main thread on
Paper, the region thread on Folia).

## Effects API

```java
ComplexEnchantsEffects effects = Bukkit.getServicesManager().load(ComplexEnchantsEffects.class);

effects.registerEffect(new CustomEffect() {
    public String id() { return "myplugin:fireball"; }
    public List<EffectArgument> arguments() { return List.of(EffectArgument.number("speed", 1.0)); }
    public void execute(EffectContext context) {
        context.player().launchProjectile(Fireball.class)
                .setVelocity(context.player().getLocation().getDirection().multiply(context.number("speed")));
    }
});
effects.registerCondition(myCondition);                 // "myplugin:in_clan_territory: true"
effects.registerTrigger("myplugin:dash", true);         // then: effects.fireTrigger(player, "myplugin:dash", event, target)
```

- Your ids need a namespace (`myplugin:…`), so they never clash with the built-in ones.
- Register them in `onEnable`. The first effects load waits for the server's first tick, when every plugin
  has registered its own; registering later reloads the effects automatically.
- Your effects get the same validation, `chance`, `cooldown`, `conditions` and `levels` as built-in ones.
- **`EnchantEffectEvent`** (cancellable) is fired right before any effect runs, with the player, the
  enchantment, the effect, the trigger, the level and the targets. Cancel it (for example, between clan
  allies) and the effect doesn't run nor start its cooldown. It's only created if some plugin listens to it.
- **`ComplexEnchantsReloadEvent`** is fired after every successful `/ce reload`.
