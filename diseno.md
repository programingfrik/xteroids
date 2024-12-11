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
   ángulo en que se encuentre presionando arriba o abajo en las teclas
   cursoras.
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
 - Los power ups se recogen pasándoles por arriba con la nave.
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
 - La partida transcurre entre disparos, destrucciones de meteoros y
   poderes.
 - El jugador inicialmente tiene 3 vidas. Si la nave es destruida más
   de 3 veces, termina la partida en game over.
 - Si el jugador logra destruir todos los meteoros y subframentos pasa
   al siguiente nivel.
 - Mientras mayor sea el nivel más dificil es el juego, hay más
   meteoros, van más rápidos, hay menos ayuda de parte de los poderes,
   etc.
 - Los niveles son infinitos. Dependiendo de la habilidad del jugador
   va a poder llegar más lejos.
 - Cuando el usuario eventualmente termina en game over, si el puntaje
   fue mayor que alguno de los que está en la lista de puntajes altos
   entonces el nombre del jugador se inserta en el lugar del puntaje
   que superó.


Ficheros
--------

Esta sección detalla que se encuentra en cada uno de los ficheros que
componen este jueguillo.


### xteroids.py ###

El fichero principal que llama a todos los otros componentes. Este
fichero se encarga de poner los valores iniciales de las partidas,
manejar los menus y llevar el bucle principal del juego. Este es el
fichero que hay que llamar para iniciar el juego.


### movni.py ###

Tiene dentro casi todos los objetos que interactuan en el juego. Tiene
una jerarquía de clases que se presta para hacer funcionar este
juego. El objeto principal es un ovni, o sea un objeto volador no
identificado, un objeto que aparece en el juego, que hay que dibujar
en la pantalla, quizás tiene algún proceso que hacer en cada cuadro de
animación o golpe de reloj y quizás reaccióna a colisiones. La razón
por la que este modulo es movni, como módulo ovni es por este
objeto. También este fichero contiene unas cuantas funciones usadas
para hacer operaciones con los vectores, rotar puntos, detectar
colisiones y todas las cosas que hagan falta.


### texto.py ###

Este fichero contiene algunos objetos extras para dibujar texto en
forma de vectores que es de la manera en la que se muestra el texto en
la interface del juego.


Clases
------

Esta seccción habla un poco a nivel general de cada una de las clases
que componen el jueguillo.

### movni.Espacio ###

Esta clase representa el espacio en el que se desenvuelven los otros
objetos del juego. Por cada partida que se presente hay una instancia
de este objeto. Cada espacio tiene una lista de ovnis que existen
dentro de el y que hay que dibujar y que interactuan entre ellos en
cada golpe de reloj.


### movni.Ovni ###

Esta es la clase principal del juego. Todos los objetos del juego que
se dibujan y tienen alguna reacción a los eventos que ocurren son
herederos de esta clase. Se aprovecha esta clase para definir las
acciones que todos los demás objetos derivados comparten entre ellos,
la función de rotar, la función de dibujar, la función que dice lo que
el objeto tiene que hacer en caso de una colisión, etc.


### movni.Omasa(Ovni) ###

Esta subclase de ovni, un ovni con masa, existe para diferenciar los
objetos que solo son dibujos de los que tienen presencia real y chocan
con los otros objetos que tienen masa.


### movni.Bala(Omasa) ###

Cada bala que dispara el jugador que sale desde su nave es
representada como una instancia de esta clase. Cada bala pasa a ser
parte de la lista de ovnis del espacio.


### movni.Nave(Omasa) ###

Representa una nave en el espacio. Inicialmente la nave del jugador
pero también las naves que aparecen casualmente en el espacio.


### movni.Meteoro(Omasa) ###

Cada asteroide que aparece en el espacio ... es en realidad una
instancia de la clase Meteoro (:-P). Ya estoy enterado que asteroide y
meteoro no son sinónimos y que son cosas muy diferentes de hecho, pero
como este es mi juego y yo nombro las cosas como me da la gana esta es
la clase meteoro, gracias por participar. Esta clase genera meteoros
al azar a partir de algunos parámetros y los coloca en un sitio
azaroso del espacio.


### texto.Caracteres(Ovni) ###

Una clase para cuando hay que dibujar una letra en el espacio.


### texto.Texto(Ovni) ###

Otra clase de texto, esta para una frase o conjunto de caracteres.
