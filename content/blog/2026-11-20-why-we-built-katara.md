+++
title = "Por qué creamos Katara: qué queda del encargo después de la reunión"
description = "El traspaso de un proyecto ilustra por qué las personas y los agentes de IA necesitan las mismas decisiones, fuentes y reglas de acceso."
date = 2026-11-20
slug = "por-que-creamos-katara"

[extra]
cover = "images/blog/katara.svg"
category = "Ingeniería de memoria para IA"
+++

Imagina que el lunes te toca retomar el rediseño del proceso de compra de una tienda. El ticket dice «quitar la compra como invitado». El encargo aprobado dice que hay que mantenerla. Ambos documentos vienen del cliente. ¿A cuál haces caso?

<!-- more -->

La responsable de la cuenta conoce la respuesta: el viernes el cliente acordó quitar la compra sin registro solo en la tienda mayorista. En la minorista se mantiene. Ese matiz se perdió al redactar el ticket. Si se lo das a un agente de programación, puede hacer un cambio impecable en la tienda equivocada.

Victor Castell y Matthew Rossi crearon [Katara](https://katara.ai/) para esa parte del trabajo que viene antes de escribir código: conocer el proyecto lo suficiente como para hacer el cambio correcto. La llamamos una capa de contexto para personas e IA. Quien retoma un ticket y el agente que le ayuda deberían poder consultar la misma decisión y comprobar de dónde viene.

## ¿Qué se guarda en un Brain?

En Katara llamamos *Brains* a los espacios de conocimiento compartido. Para el ejemplo de las tiendas, empezaríamos con el encargo aprobado, la nota de la llamada del viernes y una decisión breve que haya revisado la responsable de la cuenta: «Mantenemos la compra como invitado en la tienda minorista. La quitamos en la mayorista». La nota importa: por sí sola, la frase no explica por qué cambió el alcance.

Cuando alguien pregunta por el proceso de compra, Katara puede recuperar la documentación pertinente sin que nadie tenga que volver a pegar todo el historial en otro chat. Aquí entran en juego los permisos. Una agencia puede gestionar dos tiendas de clientes distintos en la misma plataforma. Por muy útil que parezca un documento de la otra cuenta, no corresponde mostrarlo. Katara tiene en cuenta los permisos al recuperar la información.

Que dos fuentes discrepen también es información útil. Si nadie anotó la decisión del viernes, preferimos que alguien detecte la contradicción y pregunte a la responsable de la cuenta antes de que un agente elija una versión sin avisar. Ningún sistema de memoria puede recuperar un acuerdo que no salió de la sala de reuniones.

## Dónde encaja Hermes

En nuestro propio proyecto trabajamos con Hermes Agent. En una agencia, el reparto podría ser así: Katara aporta el contexto del proyecto y Hermes lo utiliza para preparar la siguiente tarea. En el ejemplo, podría redactar un ticket que especifique el cambio en la tienda mayorista y deje intacta la minorista. Antes de tocar ninguna tienda, quien vaya a hacer el cambio puede contrastarlo con la decisión original.

Si quieres probarlo con tu equipo, elige una pregunta que siempre acaba en la mesa de la misma persona. Dale a un compañero la documentación a la que tiene permiso para acceder y pídele que la responda. Después, hazle la misma pregunta a un agente. ¿Saben decirte los dos qué se decidió y señalar el documento que lo aclara? Para una primera prueba, eso dice más que el número de archivos que hayas subido.

[Descubre Katara](https://katara.ai/) o lee nuestro artículo sobre [qué hace útil la memoria de una IA](@/blog/2026-08-21-memory-is-a-product-surface.md).
