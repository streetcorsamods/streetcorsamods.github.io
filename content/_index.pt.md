---
title: Street Corsa
description: Uma carreira automobilística sobre o Assetto Corsa. Compre um carro cansado, monte na sua garagem e corra com ele por dinheiro ou valendo o carro.
tagline: Uma carreira automobilística sobre o Assetto Corsa. Compre um carro cansado, monte peça por peça e corra com ele por dinheiro ou valendo o carro.
features:
  - title: Sua garagem
    text: Desmonte um carro peça por peça. Tire o motor para o cavalete, recondicione, coloque peças de preparação.
  - title: Corra no Assetto Corsa
    text: Arrancadas, corridas em circuito e time attacks rodam no AC, com os seus carros e as suas peças.
  - title: Uma cidade viva
    text: Revendas abrem e fecham, os rivais preparam os carros deles, o jornal vende carros e peças usados. À noite a polícia aparece.
  - title: Do seu jeito
    text: Tudo é mod. Cenários, motores, lugares, textos e regras. Faça os seus e compartilhe.
talk:
  title: Gente que responde
  lead: >-
    Ligue a sua própria IA e o pessoal da cidade conversa com você. Digite o que você diz, com as suas palavras.
  points:
    - title: Pechinche de verdade
      text: Vá ver o carro do jornal e o vendedor sai para conversar. Baixe o preço. Cada vendedor tem o seu limite, alguns não cedem nada, e uma oferta muito baixa não leva a lugar nenhum.
    - title: Eles lembram de você
      text: O rival que você venceu na semana passada toca no assunto. O vendedor que você ofendeu ainda está magoado. Vendedores, compradores e pilotos lembram do que você disse, comprou e ganhou.
    - title: Todo mundo tem voz
      text: Os vendedores apresentam o pátio quando você entra, os rivais avaliam o seu carro peça por peça e o balconista acha as peças que servem.
    - title: Roda no seu PC
      text: Grátis e privada com o Ollama na sua própria placa de vídeo. LM Studio, OpenRouter, OpenAI e Claude também funcionam.
  note: Opcional e desligada por padrão. O jogo decide cada preço e cada fato; a IA só fala. Sem ela o jogo é o mesmo, só que ninguém responde.
about:
  title: O que é
  intro: |-
    Street Corsa é um jogo de carreira gratuito. Você joga numa janela própria: compra carros, mexe neles, escolhe as suas corridas.
    As corridas em si rodam no **Assetto Corsa**, com os carros que você tem instalados.

    A carreira que você joga é um **cenário**. **Street Rod** é Los Angeles em 1970, muscle cars e a Main Street à noite.
    **Touge Nights** é Gunma em 2002, estradas de serra e batalhas de drift.

    O jogo está em inglês por enquanto: nestas páginas os botões aparecem com o nome em inglês, do jeito que você vê.
  steps_title: Uma corrida, do começo ao fim
  steps:
    - title: Sua garagem
      text: Cada peça que você coloca muda o carro. Antes de uma corrida, o jogo transforma as suas peças nos dados do próprio carro no Assetto Corsa.
    - title: Para o Assetto Corsa
      text: O jogo monta a corrida e abre o AC para você, com dano, desgaste de pneus e consumo de combustível ligados. Os seus amassados e o tanque pela metade vão junto.
    - title: Na pista
      text: Quem roda a corrida é o nosso próprio modo de corrida. A árvore da arrancada, batidas e largadas queimadas, um pneu que estoura, um eixo que quebra.
    - title: De volta à garagem
      text: A ficha de tempo, o dano e o desgaste voltam para a sua garagem. O motor com que você correu é o motor que você conserta.
  promise: "**O seu Assetto Corsa continua seu.** Cada arquivo que o jogo muda é guardado antes e devolvido depois da corrida. Uma sessão normal no AC ou no Content Manager não percebe nada."
  files:
    summary: "Para os curiosos: em que o jogo mexe no Assetto Corsa"
    rows:
      - paths: ['content\cars\<car>\data']
        text: As suas peças viram os dados do carro para a corrida (motor, curva de potência, câmbio, suspensão, pneus). Um `data.acd` empacotado é desempacotado. Guardado antes, devolvido depois.
      - paths: ['content\cars\<car>__sr_opponent']
        text: Quando um rival corre com o mesmo modelo que você, uma cópia marcada desse carro com os próprios dados. Apagada depois da corrida.
      - paths: ['Documents\Assetto Corsa\cfg\race.ini', 'Documents\Assetto Corsa\cfg\assists.ini']
        text: A corrida em si (pista, carros, o nosso modo de corrida), e dano em 100% com desgaste de pneus e consumo de combustível. Guardados antes, devolvidos depois.
      - paths: ['extension\lua\new-modes\sc_race']
        text: O nosso modo de corrida para o Custom Shaders Patch. Roda a corrida e coloca no carro os seus amassados, ferrugem, sujeira, combustível, pintura e peças. Só uma corrida do Street Corsa usa.
      - paths: ['Documents\Assetto Corsa\out\sc_race']
        text: O que o modo escreve quando a corrida acaba. Quem ganhou, os tempos e o que a corrida deixou de cada carro (vida do motor, câmbio, pneus, carroceria, combustível, temperaturas). O jogo lê.
    note: "Os originais esperam em `%AppData%\\StreetCorsa\\AcRestore` até voltarem. Depois de um travamento ou uma queda de luz, a próxima abertura devolve. Modelos, texturas e skins nunca são escritos."
---

## Do que você precisa

- Windows 10 ou 11, 64 bits
- Assetto Corsa com alguns carros instalados
- Custom Shaders Patch 0.2.11 ou mais novo

[Guia de instalação](/tutorials/playing/install/)
