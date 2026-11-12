---
title: "Street Rod gas station"
mod: streetrod_gas_station
group: addons
weight: 2
description: "Crossroads Gas: the forecourt, the pumps under the canopy, the office by the road, and the attendant at the pump."
source: street-rod-gas-station
shots_note: "At Crossroads Gas, drawn by the game."
shots:
  - { img: /images/tutorials/gas-station.jpg, caption: "Pulling in at Crossroads Gas: the attendant waits at the pump" }
---

Street Rod's gas station: Crossroads Gas, out where the road leaves town. Four pumps under the canopy, the office with
its soda machine and chalkboard, a tow truck behind it and old cars parked round the lot. You drive in off the road and
stop at the island; the attendant fills the tank, checks the oil, washes the car, and sends the tow truck when your car
can't make it there on its own. The bell over the drive, the pump running and the air of the place come with it.

## With Street Rod

It's Street Rod's own station, and it plays in Street Rod only. Up to Street Rod 0.1.1 it came inside the setting's
download; from Street Rod's next version on it's a mod of its own, and the setting needs it installed. The attendant's
words stay Street Rod's, so another station still has him talking.

## Your own station

A mod of your own that plays in Street Rod (`"settings": ["streetrod"]`) and ships a `stations/<yours>/` adds a
station. The game drives to one of the stations at random, so to have yours in place of Crossroads, also take it out:
`"removes": { "stations": ["crossroads"] }`. Its files are on
[SourceForge](https://sourceforge.net/p/streetcorsa-mods/street-rod-gas-station/): start from them. New to modding?
The [modding guide](/tutorials/modding/guide/) starts at the beginning.

The station is made in part from free models on Sketchfab (CC BY 4.0): the office, the pumps, the sign, the cars and
trucks round it. The attendant is one too. Each one is named in the credits beside, with what was changed in
`CREDITS.txt` in the station's folder, and in the game's Settings. The rest is Poly Haven (CC0) and our own.
