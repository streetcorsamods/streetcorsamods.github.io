---
title: "Auburn 851 Supercharged Speedster 1935"
mod: auburn_851_speedster_1935
weight: 15
description: "Gordon Buehrig's boattail speedster with the supercharged Lycoming straight-eight, 150 bhp, and the Columbia Dual-Ratio axle on a key. Fourteen skins in the 1935-36 Auburn colours."
version: "1.0"
folder: content/cars/auburn_851_speedster_1935
source: auburn-851-sc-speedster-boattail-1935
skins: 14
licence: "CC BY-NC-SA 4.0"
credits:
  - "3D model: \"1935 Auburn 851 SC Speedster\" by Kryox Shade, CC BY 4.0: https://sketchfab.com/3d-models/1935-auburn-851-sc-speedster-c8987d3ff4ba4aa4bc8d7cde74bb2ccd - reworked by Street Corsa Mods"
  - "Port, rework, physics, engine sound (engine-sim, Lycoming GH straight-eight), interior, gauges and skins: Street Corsa Mods"
  - "Horn: \"Old Car Ahooga Horn\" by craigsmith, Freesound 480002, CC0"
  - "Engine sound banks built on Kunos Simulazioni's Assetto Corsa audio SDK; driver pose, animations and collider box from Kunos Simulazioni's Alfa Romeo GTA"
shots:
  - { img: shot-plaza-cream, caption: "On the plaza" }
  - { img: shot-plaza-red, caption: "Vermilion on the plaza" }
  - { img: shot-rear-three-quarter, caption: "The boattail and its spear" }
  - { img: shot-side, caption: "From the side" }
  - { img: shot-front, caption: "The V grille and the dipped bumper" }
  - { img: shot-mascot, caption: "The Flying Goddess" }
  - { img: shot-night-lamps, caption: "Headlamps and spot lamps lit" }
shots_note: "In Assetto Corsa's showrooms. The pack has fourteen skins."
---

The 1935 Auburn 851 Supercharged Boattail Speedster, Gordon Buehrig's last Auburn. Lycoming GH straight-eight, 279.9 cu
in, with a Schwitzer-Cummins centrifugal supercharger: 150 bhp at 4000 rpm and 232 lb-ft at 2800. Three-speed gearbox
(2.86/1.68/1.00) and the Columbia Dual-Ratio axle (high 3.06, low 4.50), Lockheed hydraulic drums, beam axles on
semi-elliptic springs, 6.50-16 whitewalls on welded wire wheels, 3765 lb. Every car carried Ab Jenkins' dash plaque:
driven over 100 mph before shipment.

The base model, Kryox Shade's, was reworked part by part to photographs of surviving cars: the V grille with the 851
figures, the Flying Goddess mascot, the V windscreen with wipers that sweep, spot lamps and a working centre mirror,
the louvred hood with its four flex exhaust pipes, dipped bumpers, the boattail and its chrome spear, doors that open,
the pleated leather bench, the two-pod dash with working gauges, and a full underside. Own straight-eight engine sound
and ahooga horn. Fourteen skins: thirteen 1935-36 Auburn colours, each with a period leather, and the cream car with
black leather photographed at RM Sotheby's (851 SC 33151E).

**Custom Shaders Patch is required** for this one (the axle runs on CSP's extended physics); the Dual-Ratio shift needs
CSP 0.3.1 or newer.

## The Dual-Ratio axle

The real car had a two-speed rear axle: a chrome lever on the steering-wheel hub preselects LOW or HIGH, and a vacuum
unit shifts the axle the next time you press the clutch. Three gears times two axle ratios: six speeds.

- The car starts in **HIGH** (3.06). Drive it like any three-speed.
- Press **Extra A** once: **LOW** (4.50) is preselected. The lever on the hub swings over and a message confirms it.
- Press the clutch, or change gear, **below 40 mph**: the axle shifts and the revs jump about half again. Above 40 mph
  nothing happens; a message tells you to slow down first.
- Press Extra A again, then the clutch: back to HIGH. The gear display shows the range: 1L, 2L, 3L or 1H, 2H, 3H.
- Paddles, H-shifter and auto-shift work as on any car. AI drivers stay in high.

**Binding Extra A.** It's a Custom Shaders Patch key, not an Assetto Corsa one. The default is Alt+Numpad 7, so on a
laptop without a numpad you need another key: Content Manager → Settings → Assetto Corsa → Controls → Patch tab, group
"Car (extras)", **Extra A**. Click it, press the key or wheel button you want, and save the controls before you start.
It's a toggle, one press each way, not a hold. If it does nothing, the car simply stays in high and drives fine.
