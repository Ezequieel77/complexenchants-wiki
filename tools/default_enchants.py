"""Página "Encantamientos predeterminados" de la wiki, a partir de los archivos de fábrica del plugin.

Uso: py tools/default_enchants.py <defaults del plugin (inglés)> <carpeta en español> <carpeta docs de la wiki>
  p. ej. py tools/default_enchants.py ../ComplexEnchants/core/src/main/resources/defaults ../default/ComplexEnchants docs

Escribe docs/enchantments/defaults.md (inglés) y defaults.es.md (español): una tabla por rareza con nombre,
descripción (con los valores calculados para cada nivel), nivel máximo e incompatibilidades.
"""
import math
import os
import re
import sys

import yaml

EN, ES, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
# Ids que cambiaron al traducir: inglés -> español.
RENAMED = {'arachnophobia': 'aracnofobia', 'decapitation': 'decapitar', 'equity': 'equidad', 'atlantean': 'atlante'}


def load(folder):
    enchants = {}
    path = os.path.join(folder, 'enchants')
    for f in sorted(os.listdir(path)):
        if f.endswith('.yml') and not f.startswith('_'):
            enchants[f[:-4]] = yaml.safe_load(open(os.path.join(path, f), encoding='utf-8'))
    rarities = yaml.safe_load(open(os.path.join(folder, 'rarities.yml'), encoding='utf-8'))
    return enchants, rarities


def plain(text):
    return re.sub(r'<[^>]*>', '', str(text)).strip()


def effects_index(effects, prefix=''):
    out = {}
    for i, e in enumerate(effects or [], 1):
        key = f'{prefix}{i}'
        out[key] = e
        if isinstance(e, dict) and e.get('effects'):
            out.update(effects_index(e['effects'], key + '.'))
    return out


FUNCS = {'min': min, 'max': max, 'floor': math.floor, 'ceil': math.ceil, 'round': round, 'abs': abs,
         'sqrt': math.sqrt, 'clamp': lambda v, a, b: max(a, min(b, v))}


def evaluate(expr, level, value):
    if isinstance(expr, bool):
        return None
    if isinstance(expr, (int, float)):
        return expr
    s = str(expr).replace('^', '**').replace('&&', ' and ').replace('||', ' or ')
    s = re.sub(r'!(?!=)', ' not ', s)
    try:
        return eval(s, {'__builtins__': {}}, dict(FUNCS, level=level, value=value))
    except Exception:
        return None


def arg_at(effect, arg, level):
    if not isinstance(effect, dict):
        return None
    levels = effect.get('levels') or {}
    for key in (level, str(level)):
        if isinstance(levels.get(key), dict) and arg in levels[key]:
            return levels[key][arg]
    return effect.get(arg)


def number(v, decimal):
    if v is None:
        return '?'
    if isinstance(v, bool):
        v = int(v)
    v = round(float(v), 2)
    text = str(int(v)) if v == int(v) else f'{v:g}'
    return text.replace('.', decimal)


def per_level(values, decimal):
    texts = [number(v, decimal) for v in values]
    if len(set(texts)) == 1:
        return texts[0]
    if len(texts) <= 5:
        return '/'.join(texts)
    return f'{texts[0]}–{texts[-1]}'


def describe(enchant, decimal):
    index = effects_index(enchant.get('effects'))
    max_level = int(enchant.get('max-level', 1))

    def value_fn(level):
        def value(n, arg):
            key = str(n)
            key = key[:-2] if key.endswith('.0') else key
            raw = arg_at(index.get(key), arg, level)
            return evaluate(raw, level, value)
        return value

    def render(level):
        lines = []
        for line in enchant.get('description') or []:
            text = str(line)
            text = re.sub(r'<value:([\d.]+):([a-z_-]+)>',
                          lambda m: '\0' + str(evaluate(arg_at(index.get(m.group(1)), m.group(2), level), level,
                                                        value_fn(level))) + '\0', text)
            text = re.sub(r'<calc:([^>]*)>',
                          lambda m: '\0' + str(evaluate(m.group(1).replace("value(", "value(").strip(), level,
                                                        value_fn(level))) + '\0', text)
            text = text.replace('<level>', '\0' + str(level) + '\0')
            lines.append(plain(text))
        return ' '.join(lines)

    # Cada nivel por separado; luego se juntan los números que cambian ("10/20/30").
    renders = [render(level) for level in range(1, max_level + 1)]
    parts = [r.split('\0') for r in renders]
    result = []
    for i, piece in enumerate(parts[0]):
        if i % 2 == 0:
            result.append(piece)
        else:
            values = []
            for p in parts:
                try:
                    values.append(float(p[i]))
                except (ValueError, IndexError):
                    values.append(None)
            result.append(per_level(values, decimal))
    return re.sub(r'\s+', ' ', ''.join(result)).strip()


def conflicts_of(enchants):
    found = {id_: set() for id_ in enchants}
    for id_, e in enchants.items():
        for other in e.get('conflicts') or []:
            other = str(other)
            found[id_].add(other)
            if ':' not in other and other in found:
                found[other].add(id_)
    return found


def cell(text):
    return text.replace('|', '\\|')


T = {
    'en': {'title': 'Default enchantments', 'decimal': '.',
           'intro': ('These are the {n} enchantments that come with ComplexEnchants (they are installed on a new '
                     'server, in `plugins/ComplexEnchants/enchants/`, and you can change or delete any of them). '
                     'Values that change with the level are shown for every level ("10/20/30%") or from the first '
                     'to the last level ("1–5").'),
           'cols': ('Enchantment', 'Description', 'Max level', 'Incompatible with'), 'none': '—'},
    'es': {'title': 'Encantamientos predeterminados', 'decimal': ',',
           'intro': ('Estos son los {n} encantamientos que trae ComplexEnchants (se instalan en un servidor nuevo, en '
                     '`plugins/ComplexEnchants/enchants/`, y puedes cambiar o borrar cualquiera). Los valores que '
                     'cambian con el nivel se muestran para cada nivel ("10/20/30%") o del primero al último '
                     '("1–5").'),
           'cols': ('Encantamiento', 'Descripción', 'Nivel máximo', 'Incompatible con'), 'none': '—'},
}


def page(lang, enchants, rarities, names_for_conflicts):
    t = T[lang]
    conflicts = conflicts_of(enchants)
    by_rarity = {}
    for id_, e in enchants.items():
        if e.get('enabled', True) is False:
            continue
        by_rarity.setdefault(e.get('rarity'), []).append(id_)
    order = sorted(rarities, key=lambda r: rarities[r].get('order', 0))
    out = [f'# {t["title"]}', '', t['intro'].format(n=sum(len(v) for v in by_rarity.values())), '']
    for rarity in order:
        ids = sorted(by_rarity.get(rarity, []), key=lambda i: plain(enchants[i].get('name', i)).lower())
        if not ids:
            continue
        out += [f'## {plain(rarities[rarity].get("name", rarity))} ({len(ids)})', '',
                '| ' + ' | '.join(t['cols']) + ' |', '|---|---|---|---|']
        for id_ in ids:
            e = enchants[id_]
            others = sorted(names_for_conflicts(c) for c in conflicts[id_])
            out.append('| ' + ' | '.join(cell(x) for x in [
                f'**{plain(e.get("name", id_))}**<br>`{id_}`',
                describe(e, t['decimal']),
                str(e.get('max-level', 1)),
                ', '.join(others) if others else t['none']]) + ' |')
        out.append('')
    return '\n'.join(out)


def main():
    en, en_rar = load(EN)
    es_raw, es_rar = load(ES)
    # Las tablas en español tienen los mismos ids que el plugin (los de inglés).
    es = {}
    for id_ in en:
        es_id = RENAMED.get(id_, id_)
        if es_id not in es_raw:
            raise SystemExit(f'falta {es_id} en la carpeta en español')
        es[id_] = es_raw[es_id]
    # Las incompatibilidades de los archivos en español usan los ids en español.
    back = {v: k for k, v in RENAMED.items()}
    for e in es.values():
        if e.get('conflicts'):
            e['conflicts'] = [back.get(str(c), str(c)) for c in e['conflicts']]

    def namer(enchants):
        def name(key):
            if ':' in key:
                return key.split(':', 1)[1].replace('_', ' ').title()
            return plain(enchants[key].get('name', key)) if key in enchants else key
        return name

    os.makedirs(os.path.join(OUT, 'enchantments'), exist_ok=True)
    for lang, data, rar, suffix in (('en', en, en_rar, ''), ('es', es, es_rar, '.es')):
        text = page(lang, data, rar, namer(data))
        if '?' in re.sub(r'`[^`]*`', '', text).replace('¿', ''):
            for line in text.split('\n'):
                if '?' in line:
                    print('AVISO valor sin calcular:', line[:160])
        with open(os.path.join(OUT, 'enchantments', 'defaults' + suffix + '.md'), 'w', encoding='utf-8',
                  newline='\n') as f:
            f.write(text + '\n')
    print('ok:', len(en), 'encantamientos')


main()
