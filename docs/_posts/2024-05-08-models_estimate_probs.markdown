---
layout: single
title:  "Los modelos de ML no toman decisiones, estiman probabilidades(*)"
date:   2024-05-08 00:00:00 +0100
categories: data_science
excerpt: "Los modelos de ML no generan decisiones, estiman probabilidades (*). Y entender esto es fundamental. Si hay un solo concepto que debería estar claro, es este."
---
Los modelos de ML no generan decisiones, estiman probabilidades (*).

Y entender esto es fundamental. Si hay un solo concepto que debería estar claro, es este.

Como los modelos de ML estiman probabilidades, es necesario tener un proceso que asigne acciones a ciertas probabilidades para poder automatizar decisiones a partir de ellas.

Esto se hace, normalmente con un umbral: si p > umbral, entonces X. Y a partir de esas decisiones basadas en el umbral, se pueden calcular todas las métricas que miden el comportamiento de un sistema.

Esta dicotomía entre probabilidad y decisión no es algo único de ML, por eso me gusta ejemplificarlo con los tests de COVID.

El test de COVID detecta ciertas reacciones químicas que indican la presencia del virus. Esto es equivalente a cómo un modelo de ML estima la probabilidad de un evento. Dada la magnitud de esas reacciones tendremos que decidir a partir de qué umbral daremos un resultado como positivo.

Si el umbral es muy bajo, diremos que el test es muy sensible, y tenderá a dar muchos positivos. El riesgo aquí es que muchos de ellos sean Falsos Positivos y pidamos a la gente quedarse en casa aunque en realidad no tenga el virus.

Si el umbral es muy alto, el test solo dará positivos en aquellos casos muy claros. El riesgo aquí es que muchos casos positivos, especialmente los menos claros, no serán detectados y podrían continuar propagando la enfermedad.

Y cuál es el umbral correcto? Pues no lo se, dependerá de cada problema. Lo que es seguro es que casi nunca será el 0.5 por defecto de sklearn.

Ya veis, un concepto super básico y evidente una vez que lo entiendes, pero realmente importante. Si aspiráis a pasar una entrevista o hacer cualquier proyecto de Data Science que tenga impacto, esto es de lo primero que debería estar claro.


(*) Hablamos de clasificación. Además, los modelos en realidad estiman un score (entre 0 y 1) que no tiene que estar necesariamente calibrado como una probabilidad.