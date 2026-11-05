---
title: Street Corsa
description: A car career on top of Assetto Corsa. Buy a tired car, build it in your garage, race it for cash and pink slips.
tagline: A car career on top of Assetto Corsa. Buy a tired car, build it part by part, race it for cash and pink slips.
features:
  - title: Your garage
    text: Strip a car down part by part. Pull the engine onto the stand, rebuild it, bolt on speed parts.
  - title: Race in Assetto Corsa
    text: Drag races, road races and time attacks run in AC, on your own cars, with your parts on them.
  - title: A town that lives
    text: Dealers open and close, rivals build their cars, the paper sells used cars and parts. The police come at night.
  - title: Make it yours
    text: Everything is a mod. Settings, engines, places, words and rules. Make your own and share it.
talk:
  title: People who talk back
  lead: >-
    Turn on your own AI and the people of the town talk to you. Type what you say, in your own words.
  points:
    - title: Haggle for real
      text: Go see the car in the paper and the seller comes out to talk. Talk the price down. Every seller has their own limit, some won't move at all, and a lowball offer gets you nowhere.
    - title: They remember you
      text: The rival you beat last week brings it up. The salesman you insulted is still sore. Sellers, buyers and racers remember what you said, bought and won.
    - title: Everyone has a voice
      text: Salesmen pitch their lot as you walk in, rivals size up your car part by part, and the clerk at the counter finds the parts that fit.
    - title: Runs on your PC
      text: Free and private with Ollama on your own graphics card. LM Studio, OpenRouter, OpenAI and Claude work too.
  note: Optional and off by default. The game decides every price and every fact; the AI only speaks. Without it the game plays the same, only nobody talks back.
about:
  title: What it is
  intro: |-
    Street Corsa is a free career game. You play it in its own window: buy cars, work on them, pick your races.
    The races themselves run in **Assetto Corsa**, on the cars you have installed.

    The career you play is a **setting**. **Street Rod** is 1970 Los Angeles, muscle cars and Main Street at night.
    **Touge Nights** is 2002 Gunma, mountain passes and drift battles.
  steps_title: One race, start to finish
  steps:
    - title: Your garage
      text: Every part you bolt on changes the car. Before a race, the game turns your parts into the car's own data in Assetto Corsa.
    - title: Into Assetto Corsa
      text: The game sets up the race and starts AC for you, with damage, tyre wear and fuel use on. Your dents and your half-empty tank come along.
    - title: On the track
      text: Our own race mode runs it. The drag tree, crashes and false starts, a blown tyre, an axle that snaps.
    - title: Back home
      text: The timeslip, the damage and the wear come back to your garage. The engine you raced is the engine you fix.
  promise: "**Your Assetto Corsa stays yours.** Every file the game changes is kept first and put back after the race. A normal session in AC or Content Manager never sees a thing."
  files:
    summary: "For the curious: what the game touches in Assetto Corsa"
    rows:
      - paths: ['content\cars\<car>\data']
        text: Your parts become the car's data for the race (engine, power curve, gearbox, suspension, tyres). A packed `data.acd` is unpacked. Kept first, put back after.
      - paths: ['content\cars\<car>__sr_opponent']
        text: When a rival races the same model as you, a marked copy of that car with its own data. Deleted after the race.
      - paths: ['Documents\Assetto Corsa\cfg\race.ini', 'Documents\Assetto Corsa\cfg\assists.ini']
        text: The race itself (track, cars, our race mode), and damage at 100% with tyre wear and fuel use on. Kept first, put back after.
      - paths: ['extension\lua\new-modes\sc_race']
        text: Our race mode for Custom Shaders Patch. It runs the race and puts your dents, rust, dirt, fuel, paint and bolt-on parts on the car. Only a Street Corsa race uses it.
      - paths: ['Documents\Assetto Corsa\out\sc_race']
        text: What the mode writes when the race ends. Who won, the timeslips, and what the race left of each car (engine life, gearbox, tyres, body, fuel, temperatures). The game reads it.
    note: "The originals wait in `%AppData%\\StreetCorsa\\AcRestore` until they are back. After a crash or a power cut, the next start puts them back. Models, textures and skins are never written."
---

## What you need

- Windows 10 or 11, 64-bit
- Assetto Corsa with some cars installed
- Custom Shaders Patch 0.2.11 or newer

[Install guide](/tutorials/playing/install/)
