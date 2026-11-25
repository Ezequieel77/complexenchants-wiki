"""Reparte README(.es).md y EFFECTS(.es).md en las páginas de la wiki (MkDocs Material + static-i18n).

Uso: py split_docs.py <carpeta ComplexEnchants> <carpeta docs de la wiki>
Las secciones "## " de cada idioma están en el mismo orden, así que se reparten por posición.
"""
import os
import re
import sys
from markdown.extensions.toc import slugify as mk_slugify

SRC, OUT = sys.argv[1], sys.argv[2]

# (archivo, sección) -> sección por posición, sin contar el índice ("Contents"/"Índice").
R, E = "README", "EFFECTS"

# página: (título en, título es, [(doc, índice de sección)], introducción del doc o None)
PAGES = {
    "index": ("ComplexEnchants", "ComplexEnchants", [(R, 0)], R),
    "getting-started": ("Getting started", "Primeros pasos", [(R, 1), (R, 2), (R, 5), (R, 6)], None),
    "enchantments/creating": (None, None, [(R, 4)], None),
    "enchantments/modes": ("Modes: BOOKS and VANILLA", "Modos: LIBROS y VANILLA", [(R, 3), (R, 7), (R, 8)], None),
    "enchantments/vanilla": (None, None, [(R, 9)], None),
    "enchantments/slots": (None, None, [(R, 10)], None),
    "enchantments/display": (None, None, [(R, 11)], None),
    "menus": (None, None, [(R, 12)], None),
    "effects/index": ("Effects", "Efectos", [(E, 0), (E, 1), (E, 4), (E, 5)], E),
    "effects/groups": (None, None, [(E, 2)], None),
    "effects/skills": (None, None, [(E, 3)], None),
    "effects/triggers": (None, None, [(E, 6)], None),
    "effects/targets": (None, None, [(E, 7)], None),
    "effects/conditions": (None, None, [(E, 8)], None),
    "effects/reference": (None, None, [(E, 9)], None),
    "effects/mechanics": ("How effects work", "Cómo funcionan los efectos", [(E, 10), (E, 11), (E, 12), (E, 13)], None),
    "effects/debugging": ("Debugging and limitations", "Depuración y limitaciones", [(E, 14), (E, 16)], None),
    "placeholders": (None, None, [(R, 13)], None),
    "commands": (None, None, [(R, 14)], None),
    "api": ("API for developers", "API para desarrolladores", [(R, 15), (E, 15)], None),
    "compatibility": ("Compatibility and performance", "Compatibilidad y rendimiento",
                      [(R, 16), (R, 17), (R, 18)], None),
    "faq": (None, None, [(R, 19)], None),
}

# En la página de la API, la sección de efectos repetiría el título "API for developers".
RENAME = {(E, 15): ("Effects API", "API de efectos"), (R, 15): ("Enchantments API", "API de encantamientos")}


def github_slug(text):
    text = text.strip().lower().replace("`", "")
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def parse(path):
    """-> (intro: list[str], sections: list[(heading, lines)]) sin el índice."""
    lines = open(path, encoding="utf-8").read().splitlines()
    intro, sections, current, fence = [], [], None, False
    for line in lines:
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and line.startswith("## "):
            current = [line[3:].strip(), []]
            sections.append(current)
            continue
        (current[1] if current else intro).append(line)
    sections = [s for s in sections if s[0] not in ("Contents", "Índice")]
    return intro, sections


def clean(lines):
    """Quita líneas en blanco y separadores (---) de los extremos."""
    while lines and lines[0].strip() in ("", "---"):
        lines = lines[1:]
    while lines and lines[-1].strip() in ("", "---"):
        lines = lines[:-1]
    return lines


def build(lang):
    suffix = "" if lang == "en" else ".es"
    docs = {doc: parse(os.path.join(SRC, f"{doc}{suffix}.md")) for doc in (R, E)}

    # Dónde acaba cada encabezado: (doc, slug de GitHub) -> (página, ancla de MkDocs o None si es el título)
    anchors = {}
    pages = {}
    for page, (title_en, title_es, parts, intro_doc) in PAGES.items():
        title = title_en if lang == "en" else title_es
        single = title is None
        body = []  # trozos (doc, líneas): los enlaces se resuelven con el documento de cada trozo
        if intro_doc:
            intro = docs[intro_doc][0]
            # Fuera el título original y las líneas "Leer en español" (MkDocs tiene selector de idioma).
            intro = [l for l in intro if not l.startswith("# ") and not (l.startswith("> *") and ".md)" in l)]
            body.append((intro_doc, clean(intro) + [""]))
        for doc, index in parts:
            heading, lines = docs[doc][1][index]
            if (doc, index) in RENAME:
                heading = RENAME[(doc, index)][0 if lang == "en" else 1]
            original = docs[doc][1][index][0]
            if single:
                title = heading
                anchors[(doc, github_slug(original))] = (page, None)
                # Los ### pasan a ## (la sección es la página entera).
                fence = False
                shifted = []
                for l in clean(lines):
                    if l.lstrip().startswith("```"):
                        fence = not fence
                    shifted.append(l[1:] if not fence and l.startswith("### ") else l)
                lines = shifted
            else:
                anchors[(doc, github_slug(original))] = (page, mk_slugify(heading, "-"))
                body.append((doc, [f"## {heading}", ""]))
            fence = False
            for l in lines:
                if l.lstrip().startswith("```"):
                    fence = not fence
                if not fence and re.match(r"#{2,3} ", l):
                    text = l.lstrip("#").strip()
                    anchors.setdefault((doc, github_slug(text)), (page, mk_slugify(text, "-")))
            body.append((doc, clean(lines) + [""]))
        pages[page] = [(parts[0][0], [f"# {title}", ""])] + body

    def fix_links(page, text, doc_of_page):
        def repl(match):
            label, target = match.group(1), match.group(2)
            if re.match(r"[a-z]+://", target) or target.startswith("mailto:"):
                return match.group(0)
            file, _, anchor = target.partition("#")
            if file:
                name = os.path.basename(file).replace(".es.md", ".md")
                doc = {"README.md": R, "EFFECTS.md": E}.get(name)
                if doc is None:
                    return match.group(0)  # enlace a otro archivo: se deja
            else:
                doc = doc_of_page
            if anchor:
                found = anchors.get((doc, anchor))
                if found is None:
                    print(f"[{lang}] {page}: ancla sin destino: {target}", file=sys.stderr)
                    return match.group(0)
                dest_page, dest_anchor = found
            else:
                dest_page, dest_anchor = ("index" if doc == R else "effects/index"), None
            rel = os.path.relpath(dest_page + ".md", os.path.dirname(page) or ".").replace("\\", "/")
            if dest_page == page and dest_anchor:
                return f"[{label}](#{dest_anchor})"
            return f"[{label}]({rel}{'#' + dest_anchor if dest_anchor else ''})"
        # En la wiki no hay archivos: los textos de enlace con nombre de archivo pasan a ser el de la página.
        names = {"EFFECTS.md": "Effects", "EFFECTS.es.md": "Efectos", "README.md": "Home", "README.es.md": "Inicio"}
        for name, page_name in names.items():
            text = text.replace(f"[{name}]", f"[{page_name}]")
        return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", repl, text)

    for page, chunks in pages.items():
        text = "\n".join(fix_links(page, "\n".join(lines), doc) for doc, lines in chunks).rstrip() + "\n"
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = text.replace("(the base options are explained in the README)",
                            "(the base options: see Creating an enchantment)")
        text = text.replace("(las opciones de la base se explican en el README)",
                            "(las opciones de la base: ver Crear un encantamiento)")
        path =os.path.join(OUT, page + suffix + ".md")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)


for language in ("en", "es"):
    build(language)
print("ok:", len(PAGES), "páginas por idioma")
