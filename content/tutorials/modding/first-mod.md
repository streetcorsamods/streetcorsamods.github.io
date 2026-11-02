---
title: Your first mod
description: Copy the example mod and change it.
weight: 1
---

A mod is a folder with a `mod.json` and some JSON files. No coding.

## Try the example

1. Get the example mod: [`examples/mods/small_imports`](https://github.com/streetcorsamods/street-corsa/tree/main/examples/mods/small_imports) in the game's repository.
2. Copy the folder into the game's `Content` folder.
   On the main screen: **New Game → Open the Content folder**.
3. Start the game. It adds four small European cars, their engines and speed parts, a shop, a car lot, a rival and a race night.

## Make it yours

1. Copy `small_imports` and rename the folder.
2. In `mod.json`, change `id`, `name` and `author`. The `id` must be unique.
3. Change or delete the files you don't need.

```json
{
  "id": "mymod",
  "name": "My Mod",
  "version": "1.0",
  "author": "you",
  "type": "addon"
}
```

If the game can't read something, it tells you at start-up. The game's log lists every mod it loaded.

## What's in the example

| Folder | What |
|---|---|
| `cars` | Which AC cars, their price and factory engine |
| `parts` | Engines and speed parts, one file per part |
| `dealers` | A car lot |
| `partshops` | A parts shop |
| `racers` | A rival |
| `events`, `formats` | A race night and its race format |
| `text` | Words the game says |

## Share it

Zip the folder. Players install it with **Mod Manager → Install mods**.
