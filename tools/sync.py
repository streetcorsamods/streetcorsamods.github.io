"""Copy the player docs and the credits from the game into the site, so the site never drifts from them.

    python tools/sync.py [--game <game repo>] [--setting-docs <folder>] [--mods <folder>]
    python tools/sync.py --check     (only: which translations are behind their English)

The copied pages say where they come from (front matter `source`): edit the source, then sync again.
Links between the docs (`install.md`) are rewritten to site paths; render-link.html turns them into page links.
The released mods' manifests become data/mods/<id>.json (name, version, builds, credits) for their pages (content/mods).

The site's own translations of the synced pages (install.es.md) say which English they were made from: front matter
`translated_from`, the English page's hash. Every run lists the ones whose English has changed since, with the hash to
set once the translation is brought up to date.
"""
import argparse
import hashlib
import json
import pathlib
import re
import shutil
import sys

SITE = pathlib.Path(__file__).resolve().parent.parent

# file name -> where it goes on the site (content/<dir>/<file>)
CORE_DOCS = {"install.md": "tutorials/playing", "ai.md": "tutorials/playing", "help.md": "tutorials/playing", "changelog.md": "about"}
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

# The released mods with a page of their own: id -> its folder under the mods folder
MODS = {
    "buick_v8": "engines/buick_v8",
    "cadillac_v8": "engines/cadillac_v8",
    "chevy_small_block": "engines/chevy_small_block",
    "chevy_w_v8": "engines/chevy_w_v8",
    "ford_385": "engines/ford_385",
    "ford_cleveland": "engines/ford_cleveland",
    "ford_six": "engines/ford_six",
    "lincoln_v8": "engines/lincoln_v8",
    "olds_v8": "engines/olds_v8",
    "pontiac_v8": "engines/pontiac_v8",
    "streetrod": "settings/streetrod",
    "touge_nights": "settings/touge_nights",
    "bushradio": "addons/bushradio",
}

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


def english_hash(en: pathlib.Path) -> str:
    """What a translation of this English page records as `translated_from`"""
    return hashlib.sha256(en.read_text(encoding="utf-8").replace("\r\n", "\n").encode()).hexdigest()[:12]


def stale_translations() -> int:
    """Warn about each translation of a synced page made from an older English (or not saying which); how many"""
    n = 0
    for name, dest in WHERE.items():
        en = SITE / "content" / dest / name
        if not en.is_file():
            continue
        want = english_hash(en)
        for tr in sorted(en.parent.glob(f"{en.stem}.*.md")):
            m = re.search(r"^translated_from:[ \t]*(\S*)", tr.read_text(encoding="utf-8"), re.M)
            if not m or m.group(1) != want:
                n += 1
                print(f"  warning: content/{dest}/{tr.name} is behind content/{dest}/{name}: bring it up to date, "
                      f"then set its translated_from: {want}")
    return n


def read_jsonc(path: pathlib.Path) -> dict:
    """A mod's .json, which may have whole-line // comments"""
    text = path.read_text(encoding="utf-8-sig")
    return json.loads(re.sub(r"^\s*//.*$", "", text, flags=re.M))


def tidy(name: str) -> str:
    """A build name written all in capitals (an older pack's: "FORD 221 SP - 203 HP") as the others are written"""
    if name != name.upper():
        return name
    words = []
    for w in name.replace(" - ", ", ").split():
        bare = w.rstrip(",")
        if bare == "HP":
            w = w.replace("HP", "hp")
        elif bare.isalpha() and len(bare) > 2:
            w = w.capitalize()
        words.append(w)
    return " ".join(words)


def mod_data(folder: pathlib.Path) -> dict:
    """What a mod's page shows of its manifest: the builds (the rated ones when a mod has both kinds), the credits"""
    m = read_jsonc(folder / "mod.json")
    builds = m.get("builds", [])
    if any(b.get("origin") == "rated" for b in builds):
        builds = [b for b in builds if b.get("origin") == "rated"]
    rows = []
    for b in builds:
        engine, _, gearbox = tidy(b["name"]).partition(" + ")
        rows.append({"engine": engine, "gearbox": gearbox, "crate": b.get("origin") == "kit"})
    credits = set()
    # The parts' credits of an engine pack (a setting's are too many for its page: the game's Settings list them)
    for part in sorted((folder / "parts").rglob("*.json")) if folder.parent.name == "engines" and (folder / "parts").is_dir() else []:
        credit = read_jsonc(part).get("credit")
        if credit:
            credits.add(str(credit))
    return {
        "id": m["id"], "name": m["name"], "version": m.get("version", ""), "description": m.get("description", ""),
        "settings": m.get("settings", []), "builds": rows, "credits": sorted(credits),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", default=str(SITE.parent / "Street Corsa"))
    ap.add_argument("--setting-docs", default=r"D:\JUEGOS\STREET CORSA\docs\player")
    ap.add_argument("--mods", default=r"D:\JUEGOS\STREET CORSA\mods")
    ap.add_argument("--check", action="store_true", help="only list the translations behind their English; exit 1 if any")
    a = ap.parse_args()
    if a.check:
        sys.exit(1 if stale_translations() else 0)
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
    mods = pathlib.Path(a.mods)
    if mods.is_dir():
        out_dir = SITE / "data" / "mods"
        out_dir.mkdir(parents=True, exist_ok=True)
        for mod_id, rel in MODS.items():
            data = mod_data(mods / rel)
            (out_dir / f"{mod_id}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
            print(f"  mods/{rel}/mod.json -> data/mods/{mod_id}.json ({len(data['builds'])} builds)")
    else:
        print(f"  {mods} not found: mod data left as it is")
    stale_translations()


if __name__ == "__main__":
    main()
