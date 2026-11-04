---
title: Ayuda
description: Problemas comunes y cómo resolverlos.
weight: 6
translated_from: b64be855e494
---

| Problema | Solución |
|---|---|
| El juego pide la **carpeta de Assetto Corsa** | Elige la carpeta donde está `AssettoCorsa.exe`. Para cambiarla después: **Settings → Assetto Corsa folder**. |
| **"Runtimes Missing"** o no hay 3D | Instala los runtimes de [Visual C++](https://aka.ms/vs/17/release/vc_redist.x64.exe) y [DirectX](https://www.microsoft.com/download/details.aspx?id=8109), reinicia. |
| La carrera no arranca: **Custom Shaders Patch is not installed** | Instala [CSP](https://acstuff.club/patch/). |
| **"Race Never Started"** | El modo de carrera no cargó en AC. No se perdió nada. Actualiza CSP; `Documents\Assetto Corsa\logs\custom_shaders_patch.log` dice por qué. |
| Señal de advertencia en la pantalla principal | Haz clic en ella: falta Custom Shaders Patch o es muy viejo. Actualízalo en Content Manager. |
| La carrera no arranca: **races need 0.2.11 or newer** | Actualiza CSP en Content Manager (Settings → Custom Shaders Patch). |
| **"Assetto Corsa is already running"** | Cierra Assetto Corsa (y el juego de Content Manager) y vuelve a intentar. |
| **"Mod Problems"** | Un mod está roto o es muy viejo. El resto del juego funciona; actualiza o quita ese mod. |
| El auto no puede correr | Abre **Repairs**: dice por qué (sin combustible, motor roto, falta una rueda...). |
| Nunca aparece la policía | Instala un auto de policía en Assetto Corsa. |

## Dónde está cada cosa

- Partidas, configuración, registro: `%AppData%\StreetCorsa`
- Mods: la carpeta `Content` en la carpeta de instalación del juego
- Música de la radio: `Documents\Street Corsa\Radio` (mp3, ogg, flac). Presiona **F2** para la radio.

¿Sigues trabado? Manda el registro (`%AppData%\StreetCorsa\Logs`) con tu reporte.
