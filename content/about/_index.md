---
title: About
description: Who makes Street Corsa, and the licences.
---

Street Corsa is a free, open source car career game on top of Assetto Corsa. It started as a love letter to
**Street Rod**, the 1989 DOS game: buy a junker, build it in your garage, race it on the strip for cash and pink slips.

It is made by **[Pablo Camardelli](https://github.com/pecamardelli)**, with help from people who share their models, sounds and icons.

## Open source

- **Code:** MIT. On [GitHub](https://github.com/streetcorsamods/street-corsa).
- **Content** (models, pictures, sounds, words, part data made for the game): CC BY 4.0. Use it, change it, name Street Corsa.
- Some content is other people's work, under its own licence: see [Credits](/about/credits/).
- The main theme is Lame Genie VGM's, used with their permission. It is not under an open licence.

## Privacy

The game sends nothing over the network unless you ask it to: no telemetry, no update check, no account.

This site loads nothing from other sites, with one exception: the trailer on the home page plays from YouTube
(youtube-nocookie.com), and only once you press play. From then on, YouTube's privacy policy applies.

The one exception is the optional **AI writer** (Settings, off by default). Once you turn it on, the game sends the
provider you pick what it needs to write the newspaper's and the people's lines: what you type to the people you talk
to, your offers when you haggle, and the parts of your career the talk is about (cars, racers, places, money, parts,
prices, earlier talks). Settings' talk detail sends less.

That provider is Ollama or ComfyUI on your own computer or network, or a cloud service you sign up to yourself, under
that service's own privacy policy and with your own key. With a cloud one, what you type leaves your computer.
The installer shows this note too.

## Code signing policy

The releases are unsigned for now, so Windows may warn about the installer. Street Corsa will apply again for free
code signing by [SignPath.io](https://about.signpath.io/), certificate by [SignPath Foundation](https://signpath.org/),
under this policy:

- **Committers and reviewers:** [streetcorsamods](https://github.com/streetcorsamods) (Pablo Camardelli)
- **Approvers:** [streetcorsamods](https://github.com/streetcorsamods) (Pablo Camardelli)

Every signed release is built by GitHub Actions from the [source](https://github.com/streetcorsamods/street-corsa),
and each signing is approved by hand. Only Street Corsa's own files are signed: `Street Corsa.exe`,
`Street Corsa.dll` and the installer. Libraries made by others keep their makers' signatures, or none.

## The name

**Street Corsa** and its logo belong to [Pablo Camardelli](https://github.com/pecamardelli). Fork the game, change it, ship it, but give your version a
name of its own. Mods can say they are for Street Corsa.

Street Corsa is an independent project, not made, endorsed or sponsored by Kunos Simulazioni or the makers of
Assetto Corsa. Nothing of Kunos' ships with it.

{{< donate >}}
