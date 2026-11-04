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
| News | `content/news/` (one file per post, `date` in the front matter; `image`: the card thumbnail, a 640x360 `-sm` picture, else `og.jpg`) |
| Downloads | `data/downloads.yaml` |
| A mod's page | `content/mods/<page>.md` (text, `mod` id, `shots`), pictures in `static/images/mods/<page>/` |
| Tutorials | `content/tutorials/` |
| About, credits | `content/about/` |
| Contact page, footer icons (Discord, YouTube, itch.io, email...) | `hugo.toml` (`params.social`; empty `url` hides one), icons in `layouts/partials/icon.html` |

## Languages

English at `/`, Spanish at `/es/`, Portuguese (Brazil) at `/pt/` (`[languages]` in `hugo.toml`).

| What | Where |
|---|---|
| A page's translation | a file beside it, named for the language: `install.md` → `install.es.md`, `install.pt.md` |
| The templates' words (buttons, footer, menu, Contact cards) | `i18n/en.toml`, `es.toml`, `pt.toml`, same keys |
| Downloads text | `data/downloads.yaml`: a group's or item's `es:` / `pt:` |

A page with no translation has none in that language: the menu, the footer and links in the text go to the English
page instead (`layouts/partials/page.html`, `link.html`). In a translation, link to site pages as the English does
(`/downloads/`, `install.md`): they go to the page in the same language. In-game names (**Mod Manager**, **Go race!**)
stay in English, as the game shows them.

Translated so far: home, Downloads, Contact, and the Getting started and Street Rod tutorials (but not the AI guide).
News, About, the mods' pages and the modding guide are English only.

The synced tutorials' translations are the site's own. Each says which English it was made from (front matter
`translated_from`, a hash of the English page). Every sync, and `python tools/sync.py --check` on its own, lists the
translations whose English has changed since, with the new hash to set once the translation is up to date.

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
