Diseño
======

Este documento es una descripción de como se espera que funcione
xteroids. Este documento es un complemento a la documentación de los
fuentes. El objetivo de este documento es poner en palabras el como de
la implementación del proyecto de este juego xteroids.

Casos de uso
------------

### Asteroides clásico ###

 - Inicia la partida, los puntos están en 0, aparece la nave espacial
   en el centro de la pantalla, aparecen meteoros generados con
   números al azar, en una trayectoria al azar, rotando a una
   velocidad angular también aleatoria.
 - Inicialmente la nave del jugador comienza protegida por un escudo y
   tiene un escudo a su disposición listo para usarlo.
 - La nave del jugador puede rotar, si el usuario presiona las teclas
   cursoras izquierda y derecha y puede avanzar o retroceder en el
   ángulo en que se encuentre presionando arriba o abajo.
 - El jugador Hace el esfuerzo por destruir todos los asteroides que
   están en la pantalla disparándoles con su ametralladora laser que
   se activa con la bárra espaciadora.
 - Cada vez que el jugador alcanza con sus lasers a un meteoro este se
   fragmenta en pedazos más pequeños.
 - Cuando los fragmentos de los meteoros llegan a cierto tamaño se
   desvanecen.
 - Algunos pocos fragmentos cuando se desvanecen dejan en su lugar
   algún power up que pueden ser 1 escudo, 1 bomba o 1
   teletransportador.
 - Los power ups se recogen pasandoles por arriba con la nave.
 - Solo se puede poseer un power up a la vez. Y se usan 1 sola vez.
 - Los power ups o poderes se activan con la tecla tab.
 - El escudo sirve para proteger la nave de colisiones muy fuertes que
   podrían destruirla. Si se activa el escudo antes de el o los
   impactos de los meteoros o sus fragmentos la nave queda
   completamente ilesa. La protección del escudo solo dura 15 segundos.
 - La bomba es un misil espacial termonuclear que se lanza en linea
   recta y produce una explosión enorme que destruye a los meteoros
   cercanos y expulsa todos los fragmentos y los meteoros que se
   encuentran cerca en una trayectoria de expansión alejandoce del
   lugar de la explosión. Si la nave está dentro de cierto radio es
   destruida, sino de todas formas tiene que tener cuidado con los
   fragmentos que serán expulsados por la explosión.
 - El teletransportador sirve para tele transportar la nave a un lugar
   seguro. Este poder está para recordar al asteroides clásico. En
   caso de que la nave estuviera apunto de chocar con un meteoro
   gigante con forma de boyo o que ese meteoro fuera a chocar la nave,
   el usuario puede activar este poder y la nave se teletransporta a
   un lugar feliz en el que todos la quiere y nadie va a hacerle daño,
   por lo menos no inmediatamente. Al teletransportarse la nave
   conserva su orientación y su velocidad.
 - 


Ficheros
--------

### xteroids.py ###


### movni.py ###


### texto.py ###


Clases
------

### movni.Espacio ###

### movni.Ovni ###

### movni.Omasa(Ovni) ###

### movni.Bala(Omasa) ###

### movni.Nave(Omasa) ###

### movni.Meteoro(Omasa) ###

### texto.Caracteres(Ovni) ###

### texto.Texto(Ovni) ###

