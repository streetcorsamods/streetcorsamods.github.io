---
title: Street Corsa
description: Un juego de modo carrera de autos sobre Assetto Corsa. Compra un auto cansado, ármalo en tu taller y córrelo por dinero o apostando el auto.
tagline: Un juego de modo carrera de autos sobre Assetto Corsa. Compra un auto cansado, ármalo pieza por pieza y córrelo por dinero o apostando el auto.
features:
  - title: Tu taller
    text: Desarma un auto pieza por pieza. Pasa el motor al soporte, reconstrúyelo, ponle piezas de preparación.
  - title: Corre en Assetto Corsa
    text: Carreras de drag, en circuito y contrarreloj, en AC, con tus propios autos y tus piezas puestas.
  - title: Una ciudad que vive
    text: Las concesionarias abren y cierran, los rivales preparan sus autos, el diario vende autos y piezas usados. De noche aparece la policía.
  - title: Hazlo tuyo
    text: Todo es un mod. Ambientaciones, motores, lugares, textos y reglas. Haz los tuyos y compártelos.
talk:
  title: Gente que te contesta
  lead: >-
    Activa tu propia IA y la gente de la ciudad te habla. Escribe lo que dices, con tus palabras.
  points:
    - title: Regatea de verdad
      text: Ve a ver el auto del diario y el vendedor sale a hablar. Baja el precio. Cada vendedor tiene su límite, algunos no se mueven nada, y una oferta ridícula no te lleva a ningún lado.
    - title: Se acuerdan de ti
      text: El rival al que le ganaste la semana pasada te lo echa en cara. El vendedor que insultaste sigue dolido. Vendedores, compradores y corredores recuerdan lo que dijiste, compraste y ganaste.
    - title: Todos tienen voz
      text: Los vendedores te ofrecen su lote apenas entras, los rivales te miran el auto pieza por pieza y el empleado del mostrador encuentra las piezas que le sirven a tu auto.
    - title: Funciona en tu PC
      text: Gratis y privada con Ollama en tu propia tarjeta gráfica. También funcionan LM Studio, OpenRouter, OpenAI y Claude.
  note: Opcional y desactivada por defecto. El juego decide cada precio y cada dato; la IA solo habla. Sin ella el juego es igual, solo que nadie te contesta.
about:
  title: Qué es
  intro: |-
    Street Corsa es un juego gratis de modo carrera. Se juega en su propia ventana: compras autos, trabajas en ellos, eliges tus carreras.
    Las carreras en sí se corren en **Assetto Corsa**, con los autos que tienes instalados.

    La carrera que juegas es una **ambientación**. **Street Rod** es Los Ángeles en 1970, muscle cars y Main Street de noche.
    **Touge Nights** es Gunma en 2002, pasos de montaña y batallas de drift.

    El juego está en inglés por ahora: en estas páginas los botones van con su nombre en inglés, tal como los ves.
  steps_title: Una carrera, de principio a fin
  steps:
    - title: Tu taller
      text: Cada pieza que pones cambia el auto. Antes de una carrera, el juego convierte tus piezas en los datos del propio auto en Assetto Corsa.
    - title: A Assetto Corsa
      text: El juego arma la carrera y abre AC por ti, con daños, desgaste de neumáticos y consumo de combustible activados. Tus abolladuras y tu tanque a medias vienen contigo.
    - title: En la pista
      text: La corre nuestro propio modo de carrera. El árbol de drag, choques y largadas en falso, un neumático que revienta, un eje que se parte.
    - title: De vuelta al taller
      text: La planilla de tiempos, los daños y el desgaste vuelven a tu taller. El motor con el que corriste es el motor que arreglas.
  promise: "**Tu Assetto Corsa sigue siendo tuyo.** Cada archivo que el juego cambia se guarda primero y se devuelve después de la carrera. Una sesión normal en AC o Content Manager no nota nada."
  files:
    summary: "Para los curiosos: qué toca el juego en Assetto Corsa"
    rows:
      - paths: ['content\cars\<car>\data']
        text: Tus piezas se vuelven los datos del auto para la carrera (motor, curva de potencia, caja, suspensión, neumáticos). Un `data.acd` empaquetado se desempaqueta. Se guarda primero y se devuelve después.
      - paths: ['content\cars\<car>__sr_opponent']
        text: Cuando un rival corre con tu mismo modelo, una copia marcada de ese auto con sus propios datos. Se borra después de la carrera.
      - paths: ['Documents\Assetto Corsa\cfg\race.ini', 'Documents\Assetto Corsa\cfg\assists.ini']
        text: La carrera en sí (pista, autos, nuestro modo de carrera), y daños al 100% con desgaste de neumáticos y consumo de combustible. Se guardan primero y se devuelven después.
      - paths: ['extension\lua\new-modes\sc_race']
        text: Nuestro modo de carrera para Custom Shaders Patch. Corre la carrera y le pone al auto tus abolladuras, óxido, mugre, combustible, pintura y piezas. Solo lo usa una carrera de Street Corsa.
      - paths: ['Documents\Assetto Corsa\out\sc_race']
        text: Lo que el modo escribe al terminar la carrera. Quién ganó, las planillas de tiempos y lo que la carrera le dejó a cada auto (vida del motor, caja, neumáticos, carrocería, combustible, temperaturas). El juego lo lee.
    note: "Los originales esperan en `%AppData%\\StreetCorsa\\AcRestore` hasta que vuelven. Después de un cuelgue o un corte de luz, el próximo inicio los devuelve. Modelos, texturas y skins nunca se escriben."
---

## Qué necesitas

- Windows 10 u 11, 64 bits
- Assetto Corsa con algunos autos instalados
- Custom Shaders Patch 0.2.11 o más nuevo

[Guía de instalación](/tutorials/playing/install/)
