---
title: Instalar
description: Qué necesitas y cómo instalar Street Corsa.
weight: 1
translated_from: 451dd83710d2
---

## Necesitas

- Windows 10 u 11, 64 bits
- **Assetto Corsa**, con algunos autos instalados (el juego usa tus autos; no trae ninguno)
- **Custom Shaders Patch 0.2.11 o más nuevo** para las carreras ([consíguelo aquí](https://acstuff.club/patch/), o desde Content Manager)
- Para el taller en 3D: [Visual C++ runtime (x64)](https://aka.ms/vs/17/release/vc_redist.x64.exe) y
  [DirectX runtime](https://www.microsoft.com/download/details.aspx?id=8109)

El instalador te dice cuáles de estos encontró.

## Instalación

1. Ejecuta `StreetCorsa-<versión>.msi`. No necesita permisos de administrador.
2. Indícale tu carpeta de Assetto Corsa (la que tiene `AssettoCorsa.exe`).
3. Listo. Abre el juego desde el escritorio o el menú Inicio.

Puede que Windows avise que el instalador es desconocido. Haz clic en **Más información → Ejecutar de todas formas**.

![La pantalla principal](/images/tutorials/main-menu.jpg "La pantalla principal")

## Una ambientación

![El Mod Manager](/images/tutorials/mod-manager.jpg "El Mod Manager: instalar, desactivar y borrar mods")

El instalador es la base. La carrera que juegas es una ambientación, una descarga aparte:

1. Descarga el zip de una ambientación (`StreetCorsa-<ambientación>-<versión>.zip`).
2. En la pantalla principal, abre **Mod Manager → Install mods** y elige el zip. También puedes elegir varios a la vez.
3. **New Game** la muestra.

Los packs de motores y los complementos se instalan igual. Un zip más nuevo de un mod instalado lo reemplaza (el juego pregunta antes).
El Mod Manager también activa y desactiva mods, y los borra.

A mano: **New Game → Open the Content folder** y descomprímelo ahí.

## Opcional

- **Gente que te contesta.** Instala [Ollama](https://ollama.com), ejecuta `ollama pull llama3.1:8b`, y en el juego, en
  **Settings → AI**, elige Ollama y presiona **Make the game's model**. Funciona mejor con una tarjeta gráfica de 12 GB.
- **Policía.** La policía solo aparece si hay un auto de policía instalado en Assetto Corsa: la ambientación dice cuál.
- **Mods.** Pon la carpeta de un mod en la carpeta `Content` de la carpeta de instalación del juego
  (`%LocalAppData%\Programs\Street Corsa\Content`). Las ambientaciones (la carrera que juegas) y los packs de motores vienen como mods.

## Desinstalar

Quítalo desde la lista de **Aplicaciones** de Windows. El desinstalador pregunta por tus partidas, tu configuración y tus mods:

- **Keep my saves, settings and mods** marcado: se quedan para la próxima vez que instales el juego.
- Desmarcado: se van con el juego.

Una desinstalación sin el asistente (una herramienta como winget, o `msiexec /x` a mano) siempre los conserva.
