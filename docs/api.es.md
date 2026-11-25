# API para desarrolladores

## API de encantamientos

El módulo `api` no depende del resto del plugin.

```java
ComplexEnchantsApi api = Bukkit.getServicesManager().load(ComplexEnchantsApi.class);

api.enchant("rayo_vital").ifPresent(enchant -> {
    ApplyResult result = api.apply(player, item, enchant.key(), 2, ApplyCause.API);
    if (!result.isSuccess()) {
        player.sendMessage("No se pudo aplicar: " + result.status());
    }
});
Map<CustomEnchant, Integer> enObjeto = api.enchantsOn(item);
api.openShop(player);
api.openMenu(player, "enchant_list", "epic");
```

Eventos cancelables, para que los plugins de protecciones, parcelas o clanes puedan intervenir:

| Evento | Cuándo |
|---|---|
| `EnchantApplyEvent` | Antes de aplicar cualquier encantamiento personalizado (libro, yunque, mesa, comando, API) |
| `EnchantRemoveEvent` | Antes de quitar uno (extractor, comando, API) |
| `BookPurchaseEvent` | Antes de cobrar una compra con `[buy]` (la tienda). Se puede cambiar el precio (descuentos) |
| `BookTransmuteEvent` | Antes de usar un transmutador sobre un libro. Se puede cambiar la probabilidad |
| `EnchantEffectEvent` | Antes de ejecutar un efecto (por ejemplo, para impedir efectos entre aliados de un clan) |
| `ComplexEnchantsReloadEvent` | Tras cada `/ce reload` correcto (no cancelable) |

Efectos, condiciones y triggers propios: ver la sección de API de [Efectos](#api-de-efectos).

Todos los listeners usan `ignoreCancelled = true`: si tu plugin cancela un clic o un evento,
ComplexEnchants no hace nada. Los métodos que modifican objetos deben llamarse desde el hilo dueño del
objeto (el principal en Paper; el de su región en Folia).

## API de efectos

```java
ComplexEnchantsEffects effects = Bukkit.getServicesManager().load(ComplexEnchantsEffects.class);

effects.registerEffect(new CustomEffect() {
    public String id() { return "miplugin:bola_fuego"; }
    public List<EffectArgument> arguments() { return List.of(EffectArgument.number("speed", 1.0)); }
    public void execute(EffectContext context) {
        context.player().launchProjectile(Fireball.class)
                .setVelocity(context.player().getLocation().getDirection().multiply(context.number("speed")));
    }
});
effects.registerCondition(miCondicion);                 // "miplugin:en_territorio_clan: true"
effects.registerTrigger("miplugin:impulso", true);       // y luego: effects.fireTrigger(player, "miplugin:impulso", event, target)
```

- Tus ids llevan espacio de nombres (`miplugin:…`), así nunca chocan con los del catálogo.
- Regístralos en `onEnable`. La primera carga de efectos espera al primer tick del servidor, cuando todos
  los plugins ya registraron lo suyo; si registras más tarde, los efectos se recargan solos.
- Tus efectos tienen la misma validación, `chance`, `cooldown`, `conditions` y `levels` que los del catálogo.
- **`EnchantEffectEvent`** (cancelable) se lanza justo antes de ejecutar cualquier efecto, con el jugador,
  el encantamiento, el efecto, el trigger, el nivel y los targets. Si lo cancelas (por ejemplo, entre
  aliados de un clan), el efecto no se ejecuta ni empieza su enfriamiento. Solo se crea si algún plugin lo escucha.
- **`ComplexEnchantsReloadEvent`** se lanza tras cada `/ce reload` correcto.
