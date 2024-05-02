---
layout: single
title:  "Cómo un A/B test nos salvó de perder millones"
date:   2024-03-11 00:00:00 +0100
categories: data_science
---
Los A/B tests son clave. Siempre suelo contar cuando trabajé en un proyecto en el que personalizamos un motor de búsqueda y salió sorprendentemente mal.
Los resultados eran espectaculares. Todos los que lo habíamos probado veíamos que funcionaba muy bien. Las evaluaciones offline salían genial. 

Así, planteamos un A/B test, más pensando en poder reportar un buen uplift que en otra cosa. 

NADIE pensaba que saldría mal.

Primeros resultados. Las métricas de búsqueda mejoraban muchísimo, pero el AOV (average order value) era menor para el grupo que veía la personalización. 

🔴 Estábamos haciendo perder dinero a la empresa!! (y gracias al A/B test nos dábamos cuenta)

Tuvimos que apagar el sistema inmediatamente y empezar a investigar que había ocurrido. Nos dimos cuenta de que el sistema era tan bueno y personalizado, que los usuarios hacían click-click-click-click-checkout. 

Todo muy fluido, pero habían olvidado la mitad de la compra!

Tuvimos que ajustar el sistema para corregir esto y, una vez corregido, el motor de búsqueda personalizado se ha convertido en un elemento generador de valor indispensable.

Just ayer, acaba [Sergio Rozada](https://www.linkedin.com/in/sergio-rozada-doval/) su módulo de "Systems Design" del programa Zrive Applied Data Science, hablando de la importancia de los A/B test. 

Y es curioso, porque a pesar de que ningún módulo lo trata de forma específica (creemos que es algo que se puede estudiar en casa), quizás sea de los conceptos que más se repite a lo largo del programa. Es un concepto tan importante una vez trabajas en un entorno productivo complejos que todos los profesores y mentores lo acaban mencionando aquí y allá. 

Así de importante es!