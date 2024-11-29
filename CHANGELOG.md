Historia (CHANGELOG.md)
=======================

Esta es la bitácora del proyecto a continuación se muestran unas
cuantas entradas para llevar versiones y fechas. Este documento toma
en cuenta las recomendaciones de https://keepachangelog.com/en/1.0.0/
pero este proyecto no usa Semantic Versioning. En lugar de eso solo
tenemos una versión mayor y una versión menor.

Versión 0.3 - 2024-11-28
------------------------

Esta nueva versión contiene una etapa inicial de la detección de
colisiones. Ahora xteroids, cuando está en modo de depuración, puede
mostrar el rectángulo con los límites de cada ovni, estos son los
límites que se usan para la detección de colisiones. Hice algunas
mejoras en la forma de hacer algunas cosas, más arreglo de estética
del código que cambios reales.


Versión 0.2 - 2024-11-24
------------------------

Retomando este proyecto que estaba durmiendo un sueño profundo ahí en
el disco duro de mi PC desktop. Encontré varias cosas hechas más que
las que dice en la última entrada de historial, Había texto, había un
menú de juego y hay un menú de configuraciones. Estas funcionalidades
son parciales.


Versión 0.1 - 2010-02-03
------------------------

Al día hoy hay una buena parte del juego hecha, pero faltan algunas
partecillas, hasta ahora tengo la nave espacial hecha, hay un objeto
genérico que se llama ovni que puede representar cualquier objeto del
juego y tengo los meteoros. Antes pensaba que iba a poder hacer
todo en un solo archivo pero el archivo se ha vuelto muy grande y lo
he tenido que separar.

Aquí hay una lista de las cosas que faltan:

 - Texto
 - Menú del juego
 - Configuraciones
 - Puntuación
 - Salón de la fama
 - Créditos
 - Detección de colisiones
 - Power Ups
 - Nave enemiga
 - Choques elásticos
 - Espacio infinito
 - Separación de meteoros
 - Sonidos disparos, explosiones, motor
 - Musica estilo Metroid infinita

En cuanto al sistema de colisiones, acabo de ver que en pygame hay
una rutinas para detectar colisiones que me imagino que serán mas
rápidas que cualquier rutina que pueda yo inventar, solo que
detectan colisiones para áreas rectangulares de la pantalla, pero
tengo una idea de como hacer detecciones mas precisas usando las
detecciones de áreas rectangulares.


Versión 0.0 - 2009-01-15
------------------------

Este es el día que escribí la primera idea de esta cuestión. Estoy
pensando que para tener un buen sistema de detección de colisiones hay
que mejorar la idea que yo tenia antes de las coordenadas. No se deben
probar todas las cuestiones juntas si no solo las coordenadas x si hay
colisión en X pruebo Y etc. De forma que se eviten comprobaciones
innecesarias. Otra parte importante es la detección de colisiones a
altas velocidades, para esto estoy pensando en tomar en cuenta la
posición anterior. Necesito saber como encontrar de forma rápida la
distancia entre una linea definida por dos puntos y un tercer punto.
