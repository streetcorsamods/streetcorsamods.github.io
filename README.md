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
| Home page text and feature boxes | `content/_index.md` |
| News | `content/news/` (one file per post, `date` in the front matter) |
| Downloads | `data/downloads.yaml` |
| Tutorials | `content/tutorials/` |
| About, credits | `content/about/` |

## Synced pages

Some pages are copies, marked `source:` in their front matter. Edit the source, then run:

```
python tools/sync.py
```

- `tutorials/playing/*`: the game repo's `docs/player/`
- `tutorials/street-rod/*`: the Street Rod setting's player docs
- `assets/credits/*.csv`: the game's icon and sound credits

## A release

1. Tag the game's release; upload the MSI and the mod zips to it.
2. In `hugo.toml`, set `release` to its version and `released = true`.
3. Add a news post.
4. A download hosted elsewhere: give its item a `url` in `data/downloads.yaml`.
