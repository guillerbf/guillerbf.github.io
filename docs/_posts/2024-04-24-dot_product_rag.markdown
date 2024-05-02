---
layout: single
title:  "La clave de los sistemas RAG es... el producto escalar"
date:   2024-04-24 00:00:00 +0100
categories: data_science
---
Quizás te sorprenda saber que los sistemas de AI basados en RAG... se basan en algo tan sencillo como un producto escalar!! 

Wait but... What?! 

![RAG diagram](/assets/images/rag.png) 

Una limitación que se identificó rápido con los sistemas de AI es que (1) son muy caros de entrenar y (2) no tienen (deberían tener ^^) acceso a datos privados. 

Por tanto, para construir sistemas de AI que hiciesen uso de esos datos se desarrolló la arquitectura RAG (Retrieval Augmented Generation). 

El concepto es sencillo. Los documentos privados se cortan en cachos (chunking), se codifican en un vector numérico que los representa (embeddings) y se guardan en una base de datos.

Así, cuando un usuario hace una pregunta al sistema:
(1) Se codifica la pregunta (embedding)
(2) Se busca en la base de datos los K vectores más cercanos (similarity score)
(3) Se pasa al modelo de AI tanto la pregunta como los chunks que tuviesen vectores más cercanos.

La idea aquí es que los chunks con vectores más cercanos a la pregunta serán los más relevantes para responderla. Como esos chunks son información privada, estamos permitiendo a la AI responder a la pregunta utilizando esa información exclusiva que no había visto durante su entrenamiento.

Y aquí llega el producto escalar. Para encontrar los chunks más relevantes, tenemos que comparar el vector de la pregunta con los vectores de los chunks para ver cuales son más "similares". 

El "similarity score" se suele calcular como "cosine similarity" que básicamente es el ángulo que forman los vectores. Cuánto menor es el ángulo, más cerca están, y más parecidos son. 

Bien, volviendo a Algebra Lineal (I): el producto escalar de dos vectores es igual al coseno del ángulo que forman (escalado por sus magnitudes). 

Por eso, muy hábilmente se calculan los embeddings normalizados a magnitud 1, para poder calcular el "cosine similarity" de forma eficiente como un simple producto escalar. 

Así que ya sabes, que no te digan que el algebra no sirve. Aquí tienes el producto escalar en el corazón de los sistemas de AI más avanzados!!