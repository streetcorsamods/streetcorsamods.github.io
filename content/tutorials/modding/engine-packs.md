---
title: Improve the engine packs
description: The engine packs' files are open. Ask to join and make them better.
weight: 3
---

The engine packs are open to modders. Better models, a missing intake, a gearbox that's wrong for its year: if you can
make a pack better, you can work on it and it ships in the pack's next release, with your name in its credits.

The packs' files are on SourceForge, in the [Street Corsa Mods](https://sourceforge.net/p/streetcorsa-mods/) project:
one Subversion (SVN) repository per pack, with the modding wiki and a tracker for tickets.

| Pack | Repository |
|---|---|
| [Buick V8](/mods/buick-v8/) | [buick-v8](https://sourceforge.net/p/streetcorsa-mods/buick-v8/) |
| [Cadillac V8](/mods/cadillac-v8/) | [cadillac-v8](https://sourceforge.net/p/streetcorsa-mods/cadillac-v8/) |
| [Chevrolet big block](/mods/chevrolet-big-block/) | [chevrolet-big-block-v8](https://sourceforge.net/p/streetcorsa-mods/chevrolet-big-block-v8/) |
| [Chevrolet W](/mods/chevrolet-w/) | [chevrolet-w-v8](https://sourceforge.net/p/streetcorsa-mods/chevrolet-w-v8/) |
| [Ford 385](/mods/ford-385/) | [ford-385-v8](https://sourceforge.net/p/streetcorsa-mods/ford-385-v8/) |
| [Ford Cleveland](/mods/ford-cleveland/) | [ford-cleveland-v8](https://sourceforge.net/p/streetcorsa-mods/ford-cleveland-v8/) |
| [Ford Falcon six](/mods/ford-falcon-six/) | [ford-inline-six](https://sourceforge.net/p/streetcorsa-mods/ford-inline-six/) |
| [Ford FE](/mods/ford-fe/) | [ford-fe-v8](https://sourceforge.net/p/streetcorsa-mods/ford-fe-v8/) |
| [Ford Y-block](/mods/ford-y-block/) | [ford-y-block-v8](https://sourceforge.net/p/streetcorsa-mods/ford-y-block-v8/) |
| [Lincoln-Mercury V8](/mods/lincoln-mercury-v8/) | [lincoln-v8](https://sourceforge.net/p/streetcorsa-mods/lincoln-v8/) |
| [Oldsmobile V8](/mods/oldsmobile-v8/) | [olds-v8](https://sourceforge.net/p/streetcorsa-mods/olds-v8/) |
| [Pontiac V8](/mods/pontiac-v8/) | [pontiac-v8](https://sourceforge.net/p/streetcorsa-mods/pontiac-v8/) |

The other packs follow once their credits are sorted out.

## How it works

1. **Look around.** Anyone can download a pack's files and open them, no account needed. What's there is the pack as
   the game loads it: its `mod.json`, the parts' JSON, the models (KN5) and the engine sounds.
2. **Ask to join.** Make a SourceForge account and open a
   [ticket](https://sourceforge.net/p/streetcorsa-mods/tickets/) of the kind *access-request*: your username, the pack,
   and what you'd like to do with it.
3. **Work on a branch.** Once you're in, you can commit to that pack. Your work goes on a branch of your own, so
   nothing reaches players until it's ready.
4. **Ask for a merge.** Try it in the game, then open a ticket of the kind *merge-request*. It's checked, merged and
   released in the pack's next version.

The [modding wiki](https://sourceforge.net/p/streetcorsa-mods/modding-guidelines/) has the details: the tools
(TortoiseSVN), getting a pack, trying it in the game, branches and commits.

## The rules, in short

- Your changes are released under the pack's licence: CC BY 4.0 for these.
- Only content you're allowed to share: your own work, or models, textures and sounds whose licence allows it, with
  their credit. Nothing ripped from other games, nothing from Assetto Corsa's own content.
- Try it in the game before you ask for a merge.

What the files mean, part by part, is in [the full guide](/tutorials/modding/guide/).
