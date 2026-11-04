---
title: Instalar
description: Do que você precisa e como instalar o Street Corsa.
weight: 1
---

## Você precisa

- Windows 10 ou 11, 64 bits
- **Assetto Corsa**, com alguns carros instalados (o jogo usa os seus carros; não vem nenhum)
- **Custom Shaders Patch 0.2.11 ou mais novo** para as corridas ([baixe aqui](https://acstuff.club/patch/), ou pelo Content Manager)
- Para a garagem em 3D: [Visual C++ runtime (x64)](https://aka.ms/vs/17/release/vc_redist.x64.exe) e
  [DirectX runtime](https://www.microsoft.com/download/details.aspx?id=8109)

O instalador diz quais desses ele encontrou.

## Instalação

1. Rode `StreetCorsa-<versão>.msi`. Não precisa de permissão de administrador.
2. Aponte para a sua pasta do Assetto Corsa (a que tem o `AssettoCorsa.exe`).
3. Pronto. Abra o jogo pela área de trabalho ou pelo menu Iniciar.

O Windows pode avisar que o instalador é desconhecido. Clique em **Mais informações → Executar assim mesmo**.

![A tela principal](/images/tutorials/main-menu.jpg "A tela principal")

## Um cenário

![O Mod Manager](/images/tutorials/mod-manager.jpg "O Mod Manager: instalar, desligar e apagar mods")

O instalador é a base. A carreira que você joga é um cenário, um download à parte:

1. Baixe o zip de um cenário (`StreetCorsa-<cenário>-<versão>.zip`).
2. Na tela principal, abra **Mod Manager → Install mods** e escolha o zip. Vários de uma vez também funciona.
3. O **New Game** mostra o cenário.

Pacotes de motores e complementos se instalam do mesmo jeito. Um zip mais novo de um mod instalado substitui o antigo (o jogo pergunta antes).
O Mod Manager também liga e desliga mods, e apaga mods.

Na mão: **New Game → Open the Content folder** e descompacte lá.

## Opcional

- **Gente que responde.** Instale o [Ollama](https://ollama.com), rode `ollama pull llama3.1:8b` e, no jogo, em
  **Settings → AI**, escolha Ollama e aperte **Make the game's model**. Funciona melhor com uma placa de vídeo de 12 GB.
  Mais em [People who talk back](/tutorials/playing/ai.md) (em inglês).
- **Polícia.** A polícia só aparece se houver um carro de polícia instalado no Assetto Corsa: o cenário diz qual.
- **Mods.** Coloque a pasta de um mod na pasta `Content` da pasta de instalação do jogo
  (`%LocalAppData%\Programs\Street Corsa\Content`). Cenários (a carreira que você joga) e pacotes de motores vêm como mods.

## Desinstalar

Remova pela lista de **Aplicativos** do Windows. O desinstalador pergunta sobre os seus saves, configurações e mods:

- **Keep my saves, settings and mods** marcado: eles ficam para a próxima vez que você instalar o jogo.
- Desmarcado: vão embora com o jogo.

Uma desinstalação sem o assistente (uma ferramenta como o winget, ou `msiexec /x` na mão) sempre mantém tudo.
