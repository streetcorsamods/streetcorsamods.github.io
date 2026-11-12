---
title: "Street Rod shops"
mod: streetrod_shops
group: addons
weight: 3
description: "Street Rod's rooms: the paint booth and its painter, the part shop, the machine shop, and the warehouse your cars are kept in."
source: street-rod-shops
shots_note: "In Street Rod, drawn by the game."
shots:
  - { img: paint-booth, caption: "The painter at work: a '63 Galaxie going Silver Frost" }
  - { img: paint-job, caption: "The paint job: the make's colours, or one of your own, seen on the car before he sprays it" }
  - { img: machine-shop, caption: "Gardena Machine & Engine: a block on the stand, the work on the counter" }
  - { img: warehouse, caption: "Your warehouse: a bay for each car, room for ten" }
  - { img: /images/tutorials/parts-shop.jpg, caption: "Inside a part shop: the shelves, the counter, the parts on show" }
---

The rooms Street Rod drives you into. The part shops' inside, with its shelves and counter, where every specialist and
speed shop in town shows its stock. The machine shop, where the blocks get bored and the heads milled. The paint booth,
with the painter going round your car with his gun. And the warehouse at the car lot, a car in each bay. Each comes
with its own air: the shop's hum, the machine shop's, the booth's fans and the gun, the warehouse's echo.

## With Street Rod

They're Street Rod's own rooms, and they play in Street Rod only. Up to Street Rod 0.1.1 they came inside the setting's
download; from Street Rod 0.4.0 on they're a mod of their own, and the setting needs it installed. The shops
themselves, who sells what and at what price, stay Street Rod's: this is the rooms they're drawn in.

## Your own rooms

A mod of your own that plays in Street Rod (`"settings": ["streetrod"]`) adds a room of its kind: a `booths/`,
`shopscenes/` or `warehouses/` folder of its own. To have yours in place of one of these, also take that one out:
`"removes": { "booths": ["booth"] }` (or `"shopscenes": ["shop"]`, `["machine_shop"]`, `"warehouses": ["warehouse"]`).
Their files are on [SourceForge](https://sourceforge.net/p/streetcorsa-mods/street-rod-shops/): start from them. New
to modding? The [modding guide](/tutorials/modding/guide/) starts at the beginning.

The rooms are our own, drawn by the game's scene tools, with surface textures from Poly Haven (CC0); the paint booth,
its painter and its sounds are all ours.
