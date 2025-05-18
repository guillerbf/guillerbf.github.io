---
title: "Las dos decisiones más importantes en Data Science"
date: 2025-02-17 12:56:16 +0000
layout: single
categories: data_science
---

Las dos decisiones más importantes a la hora de resolver un problema con aprendizaje automático son: cómo dividir los datos y qué métrica utilizar.

No qué algoritmo super-turbo-fancy usar. No qué técnica súper avanzada de imputación de missing values aplicar. Cómo dividir los datos y la métrica.

Sé que la mayoría de cursos/másteres de Machine Learning/AI/Data Science ponen casi todo el énfasis en los modelos, y por eso no me canso de decirlo en [Zrive](https://programs.zriveapp.com/data-science): cómo dividir los datos y la métrica, y luego todo lo demás.

Cómo dividir los datos no es trivial en muchos casos, pero es fundamental, ya que necesitamos poder hacer el mejor uso de los datos existentes para entrenar nuestros modelos de ML. Además, necesitamos tener conjuntos de validación que nos permitan generar una estimación no sesgada de la capacidad predictiva de nuestro modelo. Derivas temporales, falta de representatividad e information leakage son nuestros enemigos aquí.

Las métricas, por su lado, son el timón de todo lo que hagamos. Queremos utilizar métricas que nos alineen al máximo posible con los objetivos de negocio. El alineamiento perfecto no es posible casi nunca y, si optimizamos la métrica errónea, podemos llegar a destruir valor en vez de crearlo (enter clickbait, por ejemplo).

Y una vez que tienes un buen pipeline de entrenamiento, con el que divides tus datos de forma correcta y tienes una buena métrica con la que medir "lo bien que lo estás haciendo", ya puedes empezar a iterar con tus algoritmos super-turbo-mega-fancy a ver cuánto puedes exprimir tus datos. Que al final, también es lo que mola.
