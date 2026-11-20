+++
title = "Dkron"
description = "Un sistema distribuido y tolerante a fallos para programar tareas en entornos nativos de la nube."
weight = 1

[extra]
thumbnail = "images/projects/dkron.svg"
year = "2015—actualidad"
services = ["Sistemas distribuidos", "Ingeniería de producto", "Código abierto"]
project_url = "https://dkron.io/"
+++

## El encargo

Las tareas programadas son una pieza crítica de la infraestructura, pero con el cron tradicional todo depende de una sola máquina. Dkron nació para automatizar tareas en entornos distribuidos sin renunciar a la sencillez de cron.

## El enfoque

Dkron coordina las tareas programadas entre los nodos de un clúster. Utiliza Raft para alcanzar el consenso y elegir un líder, y un protocolo ligero de tipo *gossip* para que los nodos se comuniquen y detecten fallos. Si el líder deja de estar disponible, otro nodo toma el relevo. Así, las tareas pueden seguir ejecutándose sin depender de un único punto de fallo.

Para gestionar las tareas, Dkron ofrece una interfaz web, una API JSON, un historial de ejecuciones y registros. También permite configurar reintentos, definir dependencias entre tareas, controlar la concurrencia y seleccionar nodos por etiquetas.

## El resultado

Un programador de tareas de código abierto escrito en Go, fácil de instalar y administrar tanto en un clúster pequeño como en uno de miles de nodos. Dkron está disponible para Linux, macOS y Windows, con ediciones gratuitas y comerciales para distintas necesidades operativas.

[Visitar dkron.io](https://dkron.io/) · [Ver el código en GitHub](https://github.com/dkron-io/dkron)
