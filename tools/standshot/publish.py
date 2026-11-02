"""Picks the renders for each pack, writes them as web JPGs into the site (static/images/mods/<slug>/) and prints the
front matter `shots` for each page.  publish.py <out dir> <site dir> <mods dir>"""
import json
import pathlib
import re
import sys

from PIL import Image

out, site, mods = (pathlib.Path(a) for a in sys.argv[1:4])

# mod id -> (page slug, hero build, other builds)
PICKS = {
    "pontiac_v8": ("pontiac-v8", "389-gto-tri-power-360-m20", ["400-ram-air-iv-370-m21", "389-gto-335-m20", "400-w72-1977-th400"]),
    "buick_v8": ("buick-v8", "nailhead-425-super-wildcat-360-st400", ["455-gs-stage-1-360-m21", "nailhead-364-300-dynaflow", "455-stage-1-headers-crate"]),
    "cadillac_v8": ("cadillac-v8", "365-eldorado-335-hydra-matic", ["331-eldorado-270-hydra-matic", "500-eldorado-400-th400", "500-headers-crate"]),
    "chevy_w_v8": ("chevrolet-w", "409-dual-quad-409-t10", ["348-tri-power-335-t10", "427-z11-430-m20", "409-360-t10"]),
    "ford_385": ("ford-385", "boss-429-375-toploader-3-91", ["429-cobra-jet-370-c6-3-50", "460-365-c6-2-80", "429-super-cobra-jet-headers-crate"]),
    "ford_cleveland": ("ford-cleveland", "boss-351-330-toploader-close-3-91", ["351c-4v-300-toploader-close-3-25", "351c-2v-250-fmx-3-00", "boss-351-headers-crate"]),
    "ford_six": ("ford-falcon-six", "oreste-berta-racing-221", ["ford-221-sp-203-hp", "ford-188-116-hp"]),
    "lincoln_v8": ("lincoln-mercury-v8", "mercury-430-super-marauder-400-merc-o-matic", ["368-300-turbo-drive", "lincoln-462-340-c6", "edsel-410-345-merc-o-matic"]),
    "olds_v8": ("oldsmobile-v8", "455-w30-370-m21", ["400-l69-tri-carb-360-m21", "455-hurst-olds-380-th400", "455-headers-crate"]),
}
VIEWS = {"front": "", "side": "from the other side", "top": "from above", "rear": "from behind, with its gearbox"}


def names(mod_id: str) -> dict:
    text = (mods / "engines" / mod_id / "mod.json").read_text(encoding="utf-8-sig")
    m = json.loads(re.sub(r"^\s*//.*$", "", text, flags=re.M))
    return {b["id"].split("/")[-1]: b["name"] for b in m["builds"]}


def save(src: pathlib.Path, dest: pathlib.Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("RGB")
    im.resize((1600, 900), Image.LANCZOS).save(dest.with_suffix(".jpg"), quality=80, optimize=True, progressive=True)
    im.resize((640, 360), Image.LANCZOS).save(dest.with_name(dest.stem + "-sm.jpg"), quality=78, optimize=True, progressive=True)


for mod_id, (slug, hero, others) in PICKS.items():
    builds = names(mod_id)
    shots = []
    for view, words in VIEWS.items():
        name = f"{hero}-{view}" if view != "front" else hero
        save(out / mod_id / f"{hero}_{view}.png", site / "static" / "images" / "mods" / slug / name)
        caption = builds[hero].split(" + ")[0] if view == "front" else f"The same {words}"
        if view == "rear":
            caption = f"From behind, with its {builds[hero].split(' + ')[1]}" if " + " in builds[hero] else "From behind"
        shots.append((name, caption))
    for b in others:
        save(out / mod_id / f"{b}_front.png", site / "static" / "images" / "mods" / slug / b)
        shots.append((b, builds[b].split(" + ")[0]))
    print(f"## {slug}")
    print("shots:")
    for name, caption in shots:
        print(f'  - {{ img: {name}, caption: "{caption}" }}')
