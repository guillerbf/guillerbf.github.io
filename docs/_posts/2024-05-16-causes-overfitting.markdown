---
layout: single
title:  "¿Por qué nadie se pregunta qué causa el overfitting?"
date:   2024-05-16 00:00:00 +0100
categories: data_science
---
Todo el mundo habla de overfitting, pero casi nadie piensa en cuáles son sus causas.

Podemos definir overfitting como: “el rendimiento en el entrenamiento es mejor que en test porque el modelo no generaliza bien (y no debido al ruido estadístico)”

Bien, hasta aquí todo claro. Overfitting es que mi modelo funciona muy bien en train (error bajo) pero no tan bien en test (error más alto).

Pero, qué causa el overfitting?
1. Train y test no provienen de la misma distribución!
2. Train y test vienen de la misma distribución, pero el modelo está ajustando el “ruido” del entrenamiento y no generaliza bien.

![Overfitting Causes](/assets/images/overfitting_causes.jpeg) 

Cuando se habla de overfitting se habla prácticamente el 100% de las veces de (2). Y (2) es sencillo de solucionar con regularización.

Sin embargo, nadie habla de (1), pero (1) está presente en muchos problemas reales de forma natural. Dos ejemplos:
- Una startup que cambia su estrategia de marketing y empieza a adquirir una base de usuarios distinta.
- Cambio en el mercado que modifica los patrones de comportamiento de usuarios.

Hay que ser consciente de estas posibles divergencias en la distribución de train y test para intentar minimizarlas al máximo posible (ej. usar datos más cercanos en el tiempo). 

Una vez se identifica y se conoce, no es algo para volverse loco, ni quiere decir que ya no se pueda modelar. 

Que los datos cambien su distribución en el tiempo es normal en muchos casos y simplemente significa que habrá que gestionarlo de la mejor forma posible durante la fase de modelado del problema. 

Como con todo en Data Science, la clave es entender bien lo que se tiene entre manos para poder tomar decisiones de diseño en consecuencia.