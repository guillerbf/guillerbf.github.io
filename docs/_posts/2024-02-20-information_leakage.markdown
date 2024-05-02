---
layout: single
title:  "Information Leakage (caso real)"
date:   2024-02-20 00:00:00 +0100
categories: data_science
---
Caso real de cómo los algoritmos te traicionan al menor fallo.

Estoy supervisando el trabajo de un Junior. En el problema en cuestión, una de las variable se calcula como una media exponencial. 

Reviso el código y me doy cuenta de que está calculada desde `t` hacia atrás cuando debería ser desde `t-1` para no incluir la muestra que se está prediciendo.

El impacto de acabar en `t` o `t-1` es ínfimo, porque la media ponderada cambia muy poco. Pero bueno, lo correcto es `t-1`.

Al día siguiente me dice, "oye, hay algo raro porque cuando meto una de los dos cálculos, los resultados no cambian, pero he probado con los dos a la vez sin querer y el modelo ha mejorado una barbaridad".

**Inciso. Es genial que una persona Junior se de cuenta de que hay information leakage y "algo está mal". Mucha gente con experiencia no se daría cuenta. (No se donde habrá estudiado este chico... ^^)

Anyway, la media exponencial calculada hasta `t` o `t-1` apenas cambia, como decía. 

¿Cuál es el problema entonces?

Que los algoritmos son greedy y van a aprovechar la menor oportunidad para mejorar sus objetivos. El problema aquí es que esas dos medias son muy parecidas pero no iguales, y en lo que cambian es precisamente en lo que haya ocurrido en `t`, que es justo lo que que quieres predecir!!

El algoritmo está aprendiendo a intuir lo que ocurre en `t`, a partir de la pequeña diferencia entre ambas medias! 

Esto se llama "information leakage" porque la media que incluye `t` no la tendrás disponible en producción. Y si no te das cuenta, tendrás un modelo que creerás que es mucho mejor de lo que realmente es. 

Lo pondrás en producción y seguramente destruirás valor en el proceso. Si al menos tienes un buen sistema de monitorización te darás cuenta de que no está funcionando. En caso de que lo despliegues sin monitorizarlo... buena suerte!

Y esta es la diferencia entre Data Scientists que crean o destruyen valor! Algo "tan tonto" pero tan importante.