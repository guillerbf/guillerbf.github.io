---
layout: single
title:  "EconGOAT - RAG"
date:   2023-12-01 00:00:00 +0100
categories: data_science
---

El gran Tyler Cowen ha desarrollado con su equipo un bot de AI basado en chatGPT para explorar de forma interactiva su libro: GOAT: Who is the Greatest Economist of all Time and Why Does it Matter?

La idea es sencilla. Utilizan Retrieval Augmented Generation (RAG) para dotar a chatGPT de contexto particular sobre el libro en cuestión. A parte de eso, le dan unas instrucciones claras a chatGPT mediante el prompt de sistema para que responda con un tono e intención concreta, haciendo uso del libro siempre que se pueda pero complementando el libro con conocimiento externo.

![RAG](/assets/images/rag.jpeg) 

Veamos como funcionan estas soluciones a muy de alto nivel. Primero, necesitamos definir algunos conceptos:

Embeddings: Un array de números que representa un objeto (ej. un texto o imagen). Una forma de conceptualizarlos es pensar que estamos comprimiendo ese objeto (ej. texto/imagen) en una lista de números que lo representan. Debido al proceso de “compresión”, objetos similares (ej. textos relacionados) tendrán representaciones numéricas parecidas.

Vector database: La idea aquí es coger información relevante para el problema, cortarla en trozos y “comprimir” cada trozo en un embedding que guardamos en la base de datos. En el caso de econGOAT cortan el libro en trozos y crean un embedding para cada uno.

System prompt: El texto que nosotros introducimos en chatGPT en realidad se concatena a unas instrucciones de “sistema” que están preestablecidas por el equipo que ha diseñado la herramienta. Esas instrucciones de “sistema” son las que le dicen a chatGPT que sea amable, no insulte ni haga comentarios hirientes, etc. A parte de esas instrucciones se puede añadir otras para modular el comportamiento: “se breve y conciso”, “utiliza el contexto del libro siempre que puedas”, etc.

Con estos conceptos claros, ya podemos ver cómo funciona el sistema completo:

1. El usuario introduce un prompt.
2. Ese prompt se “comprime” en un embedding.
3. Se busca en la base de datos los N embeddings “más cercanos” al prompt del usuario (pensadlo como trozos del libro relevantes para la pregunta del usuario).
4. Se manda a chatGPT tanto el prompt del usuario como los trozos del libro más relevantes.
5. Se concatena la info de (4) junto al system prompt para que chatGPT genere la respuesta.
6. Se manda la respuesta de vuelta al usuario.

La mayor parte de soluciones que se están construyendo sobre chatGPT son o simplemente una página web que llama a openai directamente o estas soluciones que usan RAG para dotar a la solución de información contextual más específica. Cabe decir que los nuevos GPTs que ha anunciado Openai en su DevDay permiten construir estas soluciones (más la posibilidad de conectarse a sistemas externos) de forma sencilla y gestionada directamente por Openai.