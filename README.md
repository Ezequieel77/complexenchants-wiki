# Wiki de ComplexEnchants

Hecha con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) y
[mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n). Cada página está en dos archivos:
`pagina.md` (inglés) y `pagina.es.md` (español).

| Para | Comando |
|---|---|
| Instalar lo necesario | `py -m pip install -r requirements.txt` |
| Verla en local mientras se edita | `py -m mkdocs serve` → http://127.0.0.1:8000 |
| Comprobar que no hay enlaces rotos | `py -m mkdocs build --strict` |
| Publicarla a mano en GitHub Pages | `py -m mkdocs gh-deploy` |

Con el repositorio en GitHub, `.github/workflows/deploy.yml` la publica sola en cada push a `main`.

## De dónde salen las páginas

`docs/` se generó a partir de `README(.es).md` y `EFFECTS(.es).md` del plugin con `tools/split_docs.py`, que
reparte cada sección en su página y corrige los enlaces:

    py tools/split_docs.py ../ComplexEnchants docs

**Ojo:** volver a ejecutarlo sobrescribe `docs/`. Mientras la documentación se mantenga en los README del
plugin, edita allí y regenera. Si pasas a editar la wiki directamente, deja de usar el script.

## Encantamientos predeterminados

`docs/enchantments/defaults(.es).md` no sale del README: lo genera `tools/default_enchants.py` a partir de los
archivos de fábrica del plugin (inglés) y de la carpeta en español:

```
py tools/default_enchants.py ../ComplexEnchants/core/src/main/resources/defaults ../default/ComplexEnchants docs
```
