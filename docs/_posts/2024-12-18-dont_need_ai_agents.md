---
title: "No, lo más seguro es que no necesites un agente AI"
date: 2024-12-17 12:58:34 +0000
layout: single
categories: data_science
---
La mayoría de las aplicaciones que pueden beneficiarse del uso de modelos de lenguaje natural (LLMs) no necesitan, ni les conviene, utilizar agentes.

Quizás algún tipo de soporte al cliente avanzado sea la excepción.

En general, con la inteligencia artificial generativa, como con cualquier otra solución basada en datos (y en la vida en general), es recomendable comenzar con la solución más sencilla y solo aumentar la complejidad si realmente vale la pena.

Para la mayoría de las aplicaciones, optimizar simples llamadas a un LLM utilizando un buen prompt con algunos ejemplos bien seleccionados suele ser suficiente. 

Si se requiere más complejidad, la primera opción debería ser crear un "workflow", secuencia predefinida de llamadas al LLM, de modo que se pueda dividir el problema complejo en partes más manejables.

Construir un agente añade mucha incertidumbre, latencia y complejidad al sistema, por lo que esta estrategia debería reservarse únicamente para aquellos casos en los que todas estas desventajas se vean claramente compensadas por una mejor solución.
