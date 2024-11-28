Historia
--------

Esta es la bitacora del proyecto a continuacion se muestran unas
cuantas entradas para llevar versiones y fechas:

- Version 0.0 (15/01/2009)

  Este es el dia que escribi la primera idea de esta cuestion. Estoy
  pensando que para tener un buen sistema de deteccion de coliciones
  hay que mejorar la idea que yo tenia antes de las coordenadas. No se
  deben probar todas las cuestiones juntas si no solo las coordenadas
  x si hay colicion en x pruebo y etc . De forma que se eviten
  comprobaciones innecesarias. Otra parte importante es la deteccion
  de colisiones a altas velocidades, para esto estoy pensando en tomar
  en cuenta la posicion anterior. Necesito saber como encotrar de
  forma rapida la  distancia entre una linea definida por dos puntos y
  un tercer punto.

- 03/02/2010

  Al dia hoy hay una buena parte del juego hecha, pero faltan algunas
  partecillas, hasta ahora tengo la nave espacial hecha, hay un objeto
  generico que se llama ovni que puede representar cualquier objeto del
  juego y tengo los meteoros. Antes pensaba que hiba a poder hacer
  todo en un solo archivo pero el archivo se ha vuelto muy grande y lo
  he tenido que separar.

  Aqui hay una lista de las cosas que faltan:

   - Texto
   - Menu del juego
   - Configuraciones
   - Puntuacion
   - Salon de la fama
   - Creditos
   - Deteccion de coliciones
   - Power Ups
   - Nave enemiga
   - Choques elasticos
   - Espacio infinito
   - Separacion de meteoros
   - Sonidos disparos, explosiones, motor
   - Musica estilo Metroid infinita

  En cuanto al sistema de coliciones, acabo de ver que en pygame hay
  una rutinas para detectar coliciones que me imagino que seran mas
  rapidas que cualquier rutina que pueda yo inventar, solo que
  detectan coliciones para areas rectangulares de la pantalla, pero
  tengo una idea de commo hacer detecciones mas precisas usando las
  detecciones de areas rectangulares.
