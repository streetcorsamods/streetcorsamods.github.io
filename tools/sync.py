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

# Screenshots the site adds to the synced pages (static/images/tutorials). Each goes right under a heading
# ("" = the top of the page), or just before one with "before:". The docs themselves stay text only.
SHOTS = {
    "install.md": [
        ("before:## A setting", "main-menu", "The main screen"),
        ("## A setting", "mod-manager", "The Mod Manager: install, switch off and delete mods"),
    ],
    "first-steps.md": [
        ("## New game", "new-game", "New Game: your name, then a setting"),
        ("## Your first day", "garage", "The garage: every place is a button round your car"),
        ("## Winning", "career", "Career: pick a victory path"),
    ],
    "around-town.md": [
        ("", "car-dealers", "Car dealers: pick a lot and drive out"),
        ("before:## Selling a car", "newspaper", "The Newspaper: private sellers, rivals, parts"),
        ("before:## Selling a car", "parts-shop", "A parts shop: what's on the shelves, the clerk at the counter"),
    ],
    "garage.md": [
        ("## Moving around", "garage", "Your car in the garage"),
        ("## Working on parts", "parts-view", "Parts view: the car turns see-through, the shelf on the left, the engine on the right"),
    ],
    "racing.md": [
        ("", "go-race", "Go race: invitations, Free Run, Test & Tune and the streets"),
        ("## Where", "diners", "The diners: each has its regulars and a horsepower class"),
    ],
}


def add_shots(name: str, body: str) -> str:
    for anchor, image, caption in SHOTS.get(name, []):
        alt = caption.split(":")[0]
        figure = f'![{alt}](/images/tutorials/{image}.jpg "{caption}")'
        if not (SITE / "static" / "images" / "tutorials" / f"{image}.jpg").is_file():
            sys.exit(f"{name}: screenshot {image}.jpg is missing")
        if anchor == "":
            body = f"{figure}\n\n{body.lstrip()}"
            continue
        before = anchor.startswith("before:")
        heading = anchor.removeprefix("before:")
        m = re.search(rf"^{re.escape(heading)}[ \t]*$", body, re.M)
        if not m:
            sys.exit(f"{name}: no heading {heading!r} for the screenshot {image}")
        if before:
            body = f"{body[:m.start()]}{figure}\n\n{body[m.start():]}"
        else:
            body = f"{body[:m.end()]}\n\n{figure}{body[m.end():]}"
    return body


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
    body = add_shots(src.name, body)
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
