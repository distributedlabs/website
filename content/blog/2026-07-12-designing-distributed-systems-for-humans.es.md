+++
title = "Cómo diseñar sistemas distribuidos que se entiendan"
description = "Los sistemas más robustos permiten entender qué ha fallado, tanto a quienes los usan como a quienes los mantienen."
date = 2026-07-12

[extra]
cover = "images/blog/systems.svg"
category = "Sistemas distribuidos"
+++

Solemos describir los sistemas distribuidos hablando de máquinas: nodos, mensajes, relojes, particiones de red y consenso. Pero, a la hora de la verdad, quien juzga la calidad de un sistema es la persona que intenta entender qué ha pasado y qué hacer a continuación.

<!-- more -->

Un protocolo correcto puede dar lugar a un producto difícil de usar. Un servicio fiable puede ser imposible de administrar. Que se entienda cómo funciona el sistema es una cuestión de arquitectura; no basta con documentarlo después.

## Dar nombre a los estados

En cualquier sistema asíncrono hay momentos en los que solo se sabe parte de lo que ocurre. Se ha aceptado una solicitud, pero el cambio aún no se ha aplicado. Una réplica está disponible, pero va con retraso. Un paso del proceso ha terminado en un servicio y sigue pendiente en otro.

Si la interfaz se limita a mostrar una rueda que gira, oculta información que necesitan tanto los usuarios como el equipo de operaciones. Dar nombre a esos estados permite que todos hablen el mismo idioma:

- solicitud recibida;
- pendiente;
- confirmada;
- servicio degradado;
- reintento en curso;
- fallo con una vía de recuperación segura.

Son estados del producto y también del sistema que lo sostiene. Diseñarlos a la vez evita que la interfaz prometa una certeza que el servidor no puede garantizar.

## Poner límites a la incertidumbre

No hay un modelo de consistencia que sirva para todo. La elección depende de qué errores pueda tolerar el producto.

Un contador en una red social puede admitir un desfase temporal. Una transferencia de saldo, no. Un editor colaborativo puede mostrar cambios locales sin confirmar, siempre que, en caso de conflicto, las copias converjan de forma predecible. Conviene decidir qué garantías se necesitan al diseñar la arquitectura, en lugar de dejar que las determine por accidente la configuración por defecto de la base de datos.

Es más fácil trabajar con una incertidumbre acotada que con la promesa de que todo acabará cuadrando en algún momento. Hay que especificar qué datos pueden quedar desactualizados, cuánto pueden desviarse, durante cuánto tiempo y qué hay que hacer para volver a fiarse de ellos.

## Contar con la recuperación desde el principio

Un corte de red puede dejar nodos incomunicados, los procesos se reinician y los servicios de los que dependemos a veces tardan en responder. Todo esto forma parte del funcionamiento normal. Un buen diseño prevé cómo repetir una operación sin riesgo, cómo reconocer que un trabajo ya se ha hecho y cómo conciliar los resultados cuando solo se ha completado una parte.

El producto debe seguir el mismo criterio. Si se puede volver a intentar una operación, la interfaz debe indicarlo. Si aún no se conoce el resultado, no debe darla por fallida. Y si hace falta que intervenga alguien, el sistema debe conservar información suficiente para que esa persona pueda resolver el problema.

## Acercar las capas del sistema

En los mejores productos distribuidos, los términos que ve el usuario reflejan lo que el sistema puede garantizar. Así, los equipos de ingeniería, diseño y operaciones pueden hablar de los mismos cambios de estado sin tener que traducir entre modelos incompatibles.

También en eso consiste la sencillez. No se trata de quitar componentes a toda costa, sino de evitar que un mismo estado signifique cosas distintas en capas distintas. El resultado es un producto que se comporta de forma coherente cuando todo va bien y que se sigue entendiendo cuando algo falla.
