# streetcorsamods.github.io

The Street Corsa website: https://streetcorsamods.github.io/

Built with [Hugo](https://gohugo.io/) (extended, 0.169+), published to GitHub Pages by `.github/workflows/pages.yml`
on every push to `main`. No theme: the layouts and `assets/css/site.css` are the site's own.

## Work on it

```
hugo server        # http://localhost:1313, reloads as you edit
hugo --minify      # build into public/
```

## Where things are

| What | Where |
|---|---|
| Menu, release version | `hugo.toml` (`params.release`, `params.released`) |
| Home page text, feature boxes, the AI talk section | `content/_index.md` (`talk`; a screenshot for it: `talk.image` with `src`, `alt`, `width`, `height`, else an example talk is drawn) |
| News | `content/news/` (one file per post, `date` in the front matter) |
| Downloads | `data/downloads.yaml` |
| A mod's page | `content/mods/<page>.md` (text, `mod` id, `shots`), pictures in `static/images/mods/<page>/` |
| Tutorials | `content/tutorials/` |
| About, credits | `content/about/` |

## Synced pages

Some pages are copies, marked `source:` in their front matter. Edit the source, then run:

```
python tools/sync.py
```

- `tutorials/playing/*`: the game repo's `docs/player/` (`CORE_DOCS` in sync.py)
- `tutorials/street-rod/*`: the Street Rod setting's player docs
- `assets/credits/*.csv`: the game's icon and sound credits
- `data/mods/<id>.json`: a released mod's name, version, builds and credits, from its `mod.json` (`MODS` in sync.py)

## A release

1. Tag the game's release; upload the MSI and the mod zips to it.
2. In `hugo.toml`, set `release` to its version and `released = true`.
3. Add a news post.
4. A download hosted elsewhere: give its item a `url` in `data/downloads.yaml`.

## A mod's page

1. Give its item in `data/downloads.yaml` the mod's `id`, and add the id to `MODS` in `tools/sync.py`; run the sync.
2. Pictures: `tools/standshot` draws every build on the garage's engine stand with the game's own renderer. Build the
   game in Release, then:

   ```
   dotnet build tools/standshot -c Release
   # once, the game's Content beside the tool: see mklink.txt in tools/standshot
   tools/standshot/bin/Release/net10.0-windows/StandShot.exe <out> <mod id> [build id part ...]
   ```

   Four views a build (front, side, rear, top), 1600x900 PNG. `SHOT_ONLY=<mod id>` loads that mod alone with the core
   and the setting (what is published, not whatever else is installed); `SHOT_SETTING=<id>` another setting's garage;
   the mod id `radio` draws the garage's radio instead. `publish.py` (its `PICKS`) turns the chosen ones into
   the site's JPGs and prints the page's `shots`.
3. Write `content/mods/<page>.md`: title, `mod`, `group` (its downloads group: settings, engines, addons), `weight`,
   `description`, `shots` (a name in its pictures folder, or a site path such as a tutorial's screenshot), a paragraph.
   Optional: `shots_note`, `licence`, `credits` (over the synced ones), `models_note: true` (the word on the models
   drawn for the game, `layouts/partials/models-note.html`). The download card links to it from then on.
