"""Copy the player docs and the credits from the game into the site, so the site never drifts from them.

    python tools/sync.py [--game <game repo>] [--setting-docs <folder>]

The copied pages say where they come from (front matter `source`): edit the source, then sync again.
Links between the docs (`install.md`) are rewritten to site paths; render-link.html turns them into page links.
"""
import argparse
import pathlib
import re
import shutil
import sys

SITE = pathlib.Path(__file__).resolve().parent.parent

# file name -> where it goes on the site (content/<dir>/<file>)
CORE_DOCS = {"install.md": "tutorials/playing", "help.md": "tutorials/playing"}
STREET_ROD_DOCS = {
    "first-steps.md": "tutorials/street-rod",
    "around-town.md": "tutorials/street-rod",
    "garage.md": "tutorials/street-rod",
    "racing.md": "tutorials/street-rod",
}
CREDITS = {
    "icons.csv": "Street Corsa/Assets/Images/Icons/credits.csv",
    "sfx.csv": "Street Corsa/Content/streetcorsa/sfx/credits.csv",
}
WHERE = {**CORE_DOCS, **STREET_ROD_DOCS}


def page(src: pathlib.Path, dest_dir: str, source_label: str) -> None:
    text = src.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit(f"{src}: no front matter")
    front, body = m.group(1), text[m.end():]
    # The page's title comes from the front matter; drop the doc's own first heading.
    body = re.sub(r"\A\s*# [^\n]*\n+", "", body)

    def link(mm: re.Match) -> str:
        name, frag = mm.group(2), mm.group(3) or ""
        if name not in WHERE:
            print(f"  warning: {src.name} links to {name}, which the site doesn't have")
            return mm.group(0)
        return f"]({'/' + WHERE[name] + '/' + name}{frag})"

    body = re.sub(r"\]\((\./)?([\w.-]+\.md)(#[\w-]+)?\)", link, body)
    out = SITE / "content" / dest_dir / src.name
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"---\n{front}\nsource: {source_label}\n---\n\n{body.lstrip()}", encoding="utf-8", newline="\n")
    print(f"  {source_label} -> content/{dest_dir}/{src.name}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", default=str(SITE.parent / "Street Corsa"))
    ap.add_argument("--setting-docs", default=r"D:\JUEGOS\STREET CORSA\docs\player")
    a = ap.parse_args()
    game, setting_docs = pathlib.Path(a.game), pathlib.Path(a.setting_docs)

    for name, dest in CORE_DOCS.items():
        page(game / "docs" / "player" / name, dest, f"street-corsa docs/player/{name}")
    if setting_docs.is_dir():
        for name, dest in STREET_ROD_DOCS.items():
            page(setting_docs / name, dest, f"streetrod docs/player/{name}")
    else:
        print(f"  {setting_docs} not found: Street Rod pages left as they are")
    for name, rel in CREDITS.items():
        out = SITE / "assets" / "credits" / name
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(game / rel, out)
        print(f"  {rel} -> assets/credits/{name}")


if __name__ == "__main__":
    main()
