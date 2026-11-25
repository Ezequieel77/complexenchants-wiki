# FAQ

**I added an enchantment and it doesn't exist.** New enchantments need a server restart. `/ce list`
shows "pending restart".

**I changed `max-level` and nothing happened.** Registry changes need a restart. `/ce reload` lists what
is still waiting.

**Can I delete an enchantment?** Prefer `enabled: false`. If you delete the file, it stays registered
as a tombstone so items keep working, and its lore shows it as removed.

**The console says `known-enchants.yml` was damaged.** ComplexEnchants recovered every id it could find
in it and kept a copy named `known-enchants.yml.damaged-<time>`. Check that no enchantment is missing.

**Players see the vanilla enchantment line too.** Set `display.hide-vanilla-enchant-lines: true`.

**Menu items that cost MONEY can't be paid.** Install Vault and an economy plugin, then restart.

**The console says a file is not saved as UTF-8.** It was edited with a program that saved it in another
encoding (old Windows Notepad does, as "ANSI"). It is still read, but accents may look wrong: open it and save
it as UTF-8. Until then, new options are not added to it.
