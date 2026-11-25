# Enchantment slots

Each item has a maximum number of custom enchantments:

```yaml
slots:
  default: 5
  count-vanilla: false     # do vanilla enchantments use slots too?
  per-group:
    armor: 4               # first matching group wins
  max-extra: 5             # max extra slots from slot expanders
```

Slots apply in both modes (books, table, anvil, commands and the API).
