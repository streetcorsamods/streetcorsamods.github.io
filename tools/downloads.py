"""How many times each download has been downloaded, counted where the files are hosted (no browser involved).

    python tools/downloads.py            (every mod, all its versions added up)
    python tools/downloads.py --files    (also each file: one line per version)

Street Corsa's files (data/downloads.yaml, file:) are assets of the game's GitHub releases: GitHub counts each
asset's downloads, every release, the old versions too, whether people came from the site or not.
The Assetto Corsa cars (data/ac.yaml, url:) are on SourceForge: its stats per folder, since the project was
registered (2026-11-04).

GitHub's API allows 60 calls an hour without a token. It uses $GITHUB_TOKEN, else `gh auth token`, when there is one.
"""
import argparse
import datetime
import json
import pathlib
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request

import yaml

SITE = pathlib.Path(__file__).resolve().parent.parent
REPO = "streetcorsamods/street-corsa"
SF_PROJECT = "streetcorsa-mods"
# A release asset: StreetCorsa-<version>.msi (the game) or StreetCorsa-<mod id>-<version>.zip
GAME_ASSET = re.compile(r"^StreetCorsa-(?P<ver>\d+(?:\.\d+)*)\.msi$")
MOD_ASSET = re.compile(r"^StreetCorsa-(?P<id>.+)-(?P<ver>\d+(?:\.\d+)*)\.zip$")
GAME_ID = "game"


def get_json(url, token=None):
    req = urllib.request.Request(url, headers={"User-Agent": "streetcorsa-downloads", "Accept": "application/json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def github_token():
    import os
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    if shutil.which("gh"):
        r = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    return None


def items(data_file):
    """(id, name, item) for each item with an id in a downloads data file."""
    data = yaml.safe_load((SITE / "data" / data_file).read_text(encoding="utf-8"))
    for group in data["groups"]:
        for item in group["items"]:
            if item.get("id"):
                yield item["id"], item["name"], item


def github_counts():
    """{mod id: [(release tag, file, downloads)]}, the game under GAME_ID; plus the files matching no pattern."""
    token = github_token()
    counts, other, page = {}, [], 1
    while True:
        releases = get_json(f"https://api.github.com/repos/{REPO}/releases?per_page=100&page={page}", token)
        if not releases:
            break
        for rel in releases:
            for asset in rel["assets"]:
                name, n = asset["name"], asset["download_count"]
                if m := GAME_ASSET.match(name):
                    counts.setdefault(GAME_ID, []).append((rel["tag_name"], name, n))
                elif m := MOD_ASSET.match(name):
                    counts.setdefault(m["id"], []).append((rel["tag_name"], name, n))
                else:
                    other.append((rel["tag_name"], name, n))
        page += 1
    return counts, other


def sourceforge_count(url):
    """(file, downloads) of a SourceForge download url (.../files/<folder>/<zip>/download): its folder's stats."""
    path = urllib.parse.urlparse(url).path.split("/")
    folder, zip_name = path[4], path[5]
    end = datetime.date.today().isoformat()
    stats = get_json(f"https://sourceforge.net/projects/{SF_PROJECT}/files/{folder}/stats/json"
                     f"?start_date=2000-01-01&end_date={end}")
    return zip_name, stats.get("total", 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--files", action="store_true", help="also list each file")
    args = ap.parse_args()

    rows = []  # (section, name, total, [(where, file, n)])
    gh, gh_other = github_counts()
    listed = {GAME_ID}
    rows.append(("Street Corsa", "Street Corsa (the game)", gh.get(GAME_ID, [])))
    for mod_id, name, _ in items("downloads.yaml"):
        listed.add(mod_id)
        rows.append(("Street Corsa", name, gh.get(mod_id, [])))
    for mod_id in sorted(set(gh) - listed):  # in old releases, no longer on the Downloads page
        rows.append(("Street Corsa", f"{mod_id} (not on the site now)", gh[mod_id]))
    for _, name, item in items("ac.yaml"):
        files = []
        if item.get("url"):
            zip_name, n = sourceforge_count(item["url"])
            files.append(("SourceForge", zip_name, n))
        rows.append(("Assetto Corsa", name, files))

    width = max(len(r[1]) for r in rows) + 2
    section = None
    grand = 0
    for sec, name, files in rows:
        if sec != section:
            section = sec
            where = "GitHub releases" if sec == "Street Corsa" else "SourceForge"
            print(f"\n{sec} ({where})")
        total = sum(f[2] for f in files)
        grand += total
        print(f"  {name:<{width}}{total:>6}")
        if args.files:
            for where, file, n in files:
                print(f"      {where:<12} {file:<{width}}{n:>6}")
    if args.files and gh_other:
        print("\nOther release files")
        for tag, file, n in gh_other:
            print(f"  {tag:<12} {file:<{width}}{n:>6}")
    print(f"\n  {'All downloads':<{width}}{grand:>6}")


if __name__ == "__main__":
    sys.exit(main())
