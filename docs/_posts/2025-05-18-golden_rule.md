---
title: "La regla de oro de Machine Learning"
date: 2025-05-17 13:00:50 +0000
layout: single
categories: data_science
---
Hay una regla de oro en Machine Learning que les repito por activa y por pasiva a mis alumnos: "Lo más importante es cómo divides tus datos, la métrica que eliges y el baseline que defines".

Y esto es así porque, una vez hecho eso de forma correcta, tienes un pipeline de entrenamiento sobre el que puedes iterar y mejorar de manera progresiva.

Caso real de qué pasa cuando no se hace bien:

Asesorando una empresa que tiene un problema de predicción de series temporales me enseñan el trabajo de un contractor previo. El chico ha hecho un montón de trabajo. El código tiene muy buena pinta. El proyecto está bien estructurado. El feature engineering, notable.

Y, sin embargo, me dicen que han apagado su modelo y han vuelto a usar una media móvil. ¿Qué ha pasado aquí?

Su modelo apenas mejora la media móvil y, por tanto, no justifica su uso. Ha cometido dos errores: uno de modelado y otro más fundamental.

El error de modelado es utilizar un modelo global para predecir series temporales de naturaleza notablemente distinta, por lo que el modelo no era capaz de capturar correctamente las dinámicas particulares de las distintas series.

Esto puede pasar, pero el error fundamental es no haber tenido una buena serie de baselines que le permitiesen ver que su modelo no era mejor que la media móvil. De haberlas tenido, probablemente habría cambiado su estrategia de modelado.

Un trabajo con una buena ejecución técnica, pero que ha destruido valor por un error fundamental. Ha destruido valor tanto por el coste del contractor (muchos miles de euros) como por el coste de oportunidad de no tener una mejor solución en producción durante todo este tiempo.

Así que sí, "lo más importante es cómo divides tus datos, la métrica que eliges y el baseline que defines".
