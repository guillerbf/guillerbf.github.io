---
layout: single
title:  "¿Quién es quién en Datos? De inteligencia artificial a Big Data."
date:   2024-05-13 00:00:00 +0100
categories: data_science
excerpt: "Pongamos algo de sentido al hype. Definamos qué significan realmente los conceptos más usados en el campo de los datos: inteligencia artificial, Big Data, aprendizaje automático y Data Science."
---
Inteligencia artificial, Big Data, aprendizaje automático y Data Science, son términos que suelen aparecer de la mano e incluso utilizarse indistintamente para hacer referencia, de forma algo confusa, a tecnologías que se relacionan con el uso de los datos y la automatización.

En Zrive hablamos con muchos universitarios y jóvenes profesionales que tienen gran interés por el campo de los datos. Ingenieros, matemáticos y físicos que ven este sector como una salida profesional muy atractiva (esto da para otro post ^^). Y sin embargo, a pesar de que son perfiles técnicos con un interés explícito en el sector, sigue habiendo mucha confusión con los términos y con qué es cada cosa.

Por eso quería escribir este post en el que veremos como estos términos hacen referencia en realidad a conceptos relativamente concretos a pesar de la confusión. 

Una confusión en cierta medida creada por el empeño de muchos por utilizarlos más con fines publicitarios que explicativos.

![AI meme](/assets/images/ai_meme.jpg) 

## Big Data

Comenzando por el más sencillo, Big Data se refiere a conjuntos de datos que no pueden ser gestionados por sistemas tradicionales debido a que son demasiado grandes, se generan demasiado rápido, y son demasiado complejos. Esto es lo que se conoce como las tres Vs del Big Data: volumen, velocidad y variedad.

Por eso, trabajar con Big Data requiere normalmente del uso de sistemas de computación distribuida que dividen y procesan los datos en múltiples servidores interconectados. Los datos se dividen en fragmentos que son distribuidos a través de una red de servidores. Una vez distribuidos, se utilizan paradigmas de computación que permiten que cada servidor procese su parte de los datos en paralelo a todos los demás servidores, pero de forma coordinada con ellos.

Por eso, este enfoque no solo facilita el almacenamiento de grandes volúmenes de información, sino que también permite un análisis eficiente gracias al procesamiento en paralelo.

A parte de la infraestructura, a medida que aumenta el volumen y la complejidad de los datos, la gobernanza se convierte en un problema en sí mismo. Tener un control razonable del lineage de los datos, así como unas garantías de fiabilidad y exactitud, se vuelve capital para poder explotarlos de forma efectiva.

## Data Science

La ciencia de datos o Data Science, es un campo interdisciplinar que se encuentra en la intersección entre la estadística, la programación y el negocio y cuyo objetivo es extraer valor de los datos.

Para hacerlo, los Data Scientist utilizan dos vías principales. La primera es extrayendo información valiosa (insights) de los datos mediante su procesamiento y visualización, y el testeo de hipótesis contrastables con los mismos. Estos análisis permiten sacar conclusiones o identificar oportunidades, proporcionando conocimiento que mejora la toma de decisiones en la empresa. Esta primera avenida de valor se asocia a veces al analista de datos, pero de cualquier forma, es parte del campo de Data Science.

La segunda vía es mediante el diseño e implementación de sistemas de aprendizaje automático que modelen datos históricos. Estos modelos, una vez entrenados, pueden utilizarse para generar predicciones que permitan la automatización de decisiones (ej. sistemas de recomendación) o pueden utilizarse para descubrir patrones en los datos que apoyen la toma de decisiones (ej. agrupación de usuarios similares).

En ambos casos, es crucial que el Data Scientist sea capaz de implementar estas soluciones en sistemas de software que se integren bien en la empresa, así como de comunicarse de forma efectiva con otros stakeholders del negocio.

## Aprendizaje automático

El aprendizaje automático se centra en crear sistemas que aprenden de los datos sin ser explícitamente programados para ello.

Esto puede sonar algo confuso, pero si se entiende el desarrollo software convencional como una herramienta genérica para automatizar procesos mediante la definición de unas reglas que regulen esa automatización, vemos que el aprendizaje automático es simplemente ir un paso más allá.

Si podemos definir una serie de reglas, podemos escribir una pieza de código que las ejecute automáticamente. Por eso, el aprendizaje automático surge como respuesta a la necesidad de automatizar procesos demasiado complejos para ser definidos mediante reglas fijas. En lugar de reglas, se estima estadísticamente una función a partir de datos históricos que mapee las entradas con las salidas, reemplazando así la necesidad de una serie de reglas explícitas.

Por eso, en mi opinión el nombre español de aprendizaje automático es mucho más descriptivo que el término ingles de machine learning: se aprende de forma automática una función matemática en base a los datos disponibles.

## Inteligencia artificial

Este es el concepto más difuso de los cuatro. En un sentido amplio, la inteligencia artificial (IA) es un campo cuyo objetivo es crear sistemas inteligentes, lo cual es ambiguo debido a la dificultad de definir qué es inteligencia y, por tanto, un sistema inteligente. Bajo esta definición amplia, el aprendizaje automático sería un subconjunto de la inteligencia artificial

Por otro lado, recientemente también ha comenzado a utilizarse IA para referirse a modelos avanzados de lenguaje natural (LLM) como chatGPT y de generación de imágenes como Midjourney. Estos modelos, que en realidad han sido entrenados utilizando aprendizaje automático no muy distinto a modelos previos, son promocionados como modelos de inteligencia artificial en vez de como modelos de aprendizaje automático.

Esta decisión se justifica, típicamente, alegando que estos modelos son capaces de realizar tareas que logran imitar la inteligencia humana, como generar texto. Lo cual es bastante arbitrario y parece responder más a fines publicitarios que a la existencia de una nueva categoría con características claramente diferenciadas.

De todas formas, esto no es algo nuevo, el ánimo de rebranding es algo muy propio del mercado anglosajón. En los últimos 15 años al aprendizaje automático se ha etiquetado como statistical learning c. 2012, machine learning c. 2017 y artificial intelligence c. 2022. E incluso este último término, que empezó haciendo referencia únicamente a los nuevos modelos generativos, ya ha empezado a extenderse al resto de modelos de aprendizaje automático a los que se les empieza a etiquetar como traditional AI.


Vemos que, aunque todos estos conceptos se suelan meter en un mismo saco, cada término tiene su propio significado más o menos claro y diferenciado. El Data Scientist, utiliza aprendizaje automático sobre Big Data para automatizar decisiones. El Big Data también permite a las empresas tener una visión muy granular de su negocio y hacer análisis detallados de cada parte. El aprendizaje automático se utiliza también por Data Scientists en entornos de “small data” para modelar datos de menor volumen pero con alto valor (ej. MedTech). Y la inteligencia artificial reemplaza el aprendizaje automático como etiqueta de branding a la vez que mantiene una puerta abierta a sistemas que puedan desarrollar otros tipos de inteligencia más compleja.