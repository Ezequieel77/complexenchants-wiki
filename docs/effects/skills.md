# Active skills

An enchantment with effects using `trigger: active_skill` is a **skill**: it doesn't fire by itself, the
player activates it.

```yaml
# enchants/domain.yml
active-skill:
  cooldown: "65 - 5 * level"         # seconds (can only depend on level)
  requirements:                      # optional; checked in order
    - condition: { health_above: 50% }
      message: "<red>You need more than half your health."
effects:
  - effect: zone
    trigger: active_skill
    name: domain
    radius: 16
    duration: 8
```

- **How to activate them**:
  - with the **skill book** (`/ce give skillbook <players> [amount]`):
    right-click and a menu opens with your skills, their level and cooldown;
  - with the **key** in `skills.keybind` (`config.yml`): `sneak_swap` (sneak + swap hands key, F), `swap`
    (just F) or `none`. With one skill available it is activated; with several, the menu opens.
    `skills.keybind-requires-book` can make the key need the book too: `false` (it always works), `hotbar` (the book
    in the hotbar or the other hand: the same slot it costs Bedrock players, who can't use the keys) or `inventory`
    (anywhere in the inventory). Without the book, the key does what it normally does. The plugin's default
    configuration uses `hotbar`.
- **Which skills you have**: those of the items in your hands, armour and **hotbar** (with the book in your
  hand, the sword still counts). Outside their slot, effects that touch "the enchanted item" (`repair`,
  `damage_item`, `remove_enchant`) act on what you hold.
- **Before activating**, in this order: silence, the skill's cooldown and requirements. If something fails,
  the player gets the message and nothing else happens (no cooldown is spent).
- **Silence**: anyone with the `skills.silence-mark` mark (`silenced` by default, set with a `mark` effect)
  can't use skills.
- A skill's effects can also have their own conditions, chance and cooldown, like any other effect.

```yaml
# config.yml
skills:
  keybind: sneak_swap
  keybind-requires-book: hotbar   # false | hotbar | inventory
  silence-mark: silenced
  book:
    material: book
    name: "<gold><bold>Skill Book"
    lore: ["<gray>Right-click to see your skills."]
  menu-title: "<dark_gray>⚔ Active Skills"
```
