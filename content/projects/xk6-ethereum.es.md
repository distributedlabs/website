+++
title = "xk6 Ethereum"
description = "Una extensión de k6 para probar el rendimiento de cadenas de bloques compatibles con la EVM y de contratos inteligentes."
weight = 2

[extra]
thumbnail = "images/projects/xk6-ethereum.svg"
year = "2022"
services = ["Blockchain", "Ingeniería de rendimiento", "Código abierto"]
project_url = "https://github.com/distributedlabs/xk6-ethereum"
+++

## El encargo

Las herramientas convencionales de pruebas de carga trabajan con peticiones HTTP, pero el rendimiento de una cadena de bloques depende de aspectos propios del protocolo: el precio del gas, los *nonces*, el envío y minado de transacciones, los recibos, las llamadas a contratos y los cambios de estado de la cadena. Para probar una red compatible con la máquina virtual de Ethereum (EVM), la carga de prueba debe incorporar esos elementos de forma nativa.

## El enfoque

xk6 Ethereum amplía k6 con una API de JavaScript basada en un cliente de Ethereum en Go. Los escenarios de prueba permiten consultar saldos y bloques, estimar el gas necesario, enviar transacciones, esperar a que lleguen los recibos, desplegar contratos y llamar a contratos existentes sin tener que reconstruir esa capa del protocolo para cada prueba de rendimiento.

Además de la salida habitual de k6, la extensión ofrece métricas propias de la cadena: duración de las peticiones, transacciones minadas por segundo, avance de la cadena y tiempo de minado. La configuración de Grafana e InfluxDB que incluye permite supervisar las pruebas locales desde la primera ejecución.

## El resultado

Un conjunto de herramientas con licencia MIT para definir en JavaScript escenarios de carga reproducibles en Ethereum, sin renunciar al modelo de ejecución de k6 ni a sus herramientas de generación de informes. Los equipos pueden probar nodos y contratos compatibles con la EVM con cargas que reproducen la actividad real de la cadena en lugar de limitarse a generar tráfico de red genérico.

[Ver el código en GitHub](https://github.com/distributedlabs/xk6-ethereum)
