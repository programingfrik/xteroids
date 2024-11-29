LÉEME (README)
==============

Esto es un proyecto para crear un clon del antiguo Asteroids. El
objetivo de este proyecto es crear un juego usable en la mayor parte
de las computadoras que se parezca mucho en la forma de jugar y en
sentimiento al antiguo asteroids. Bueno, realmente modernizado,
agregándole algunas funcionalidades y cosas que no tenía el juego
antiguo.

El Asteroids era un juego recreativo que consistía en una pequeña nave
espacial que destruía asteroides, de ahí su nombre. El objetivo del
juego es destruir la mayor cantidad de asteroides posibles sin chocar
con los mismo, obteniendo así la mayor puntuación. Según se iban
pasando los niveles el juego iba creciendo en dificultad, según
aparecían más asteroides y era más difícil de evitar chocar con los
asteroides. También en algunos momentos aparecían naves enemigas que
también disparaban a los asteroides. Hasta este punto el clon se va a
mantener igual, pero quiero que el juego que resulte de este proyecto
tenga un par de cosas diferentes al juego original de asteroids que
son las siguientes:

1 - En el juego original de asteroides los asteroides podían solaparse
quiero que en esta versión eso no ocurra, que los asteroides choquen y
reboten entre ellos, incluso que se destruyan si chocan a una
velocidad muy alta.

2 - Efecto de fricción y rotación, si dos asteroides chocan o rozan la
rotación cambia como reacción al choque.

3 - La nave no siempre se destruye ante una colisión, para que la nave
se destruya tiene que ocurrir una colisión con cierta fuerza. Un toque
leve deja a la nave intacta.

4 - Las naves enemigas también pueden ser destruidas por los
asteroides.

5 - Existen 3 powerups que podrían aparecer flotando en el espacio
escudos, bombas y teleportadores. Solo se puede tener un power up a la
vez y solo una vez.

6 - Existen algunos efectos visuales especiales. Cuando se encienden
las turbinas de la nave hay efecto de partículas. Cuando rozan dos
objetos se desprenden partículas y pequeñas lineas. Cuando la nave
choca o se destruye las lineas (pedazos de la nave) siguen un vector
parecido al que que hubiera tenido la nave resultado de la colisión
pero sin penetrar en los asteroides que son considerados cuerpos
solidos. Cuando se destruye alguna cosa se ven pequeños círculos como
ondas expansivas que desaparecen de una vez. Las bombas dejan un
rastro de lineas cortas perpendiculares a la trayectoria de la bomba
que van desapareciendo. Las explosiones de las bombas arrojan algunas
balas en todas direcciones que desaparecen mas rápido que las balas de
la nave. Las balas de la nave se desaparecen después de cierto tiempo.

7 - Los asteroides son de diferentes tamaños (al azar) y mientras mas
grandes son mas se pueden subdividir. Los asteroides son polígonos
cerrados que se asemejan a círculos pero son irregulares. Los
asteroides tienen un vector inicial y una velocidad. Mientras vaya
aumentando la dificultad del juego aparecerán mayor cantidad de
asteroides y tendrán la posibilidad de moverse a mayores velocidades.

8 - Las balas no son lanzadas exactamente en la misma dirección en
que esta apuntando la nave, tienen cierto componente de azar, cuestión
que si se deja presionado el botón de fuego se ve algo como una
ametralladora en la que todas las balas tienen un vector parecido pero
no el mismo exactamente.

Como yo espero algún día poder llamarme un desarrollador de juegos
espero poder hacer algunas implementaciones diferentes, en python
primero, quizás luego en .NET, en C usando SDL (que por sus
prestaciones espero que sea la versión mas profesional y mas jugable),
y tal vez en java ?

Espero poder poner una sección de créditos donde se vean en una letra
con vectores mi nombre en todos los renglones y el nombre del juego.

Tal vez en alguna de las versiones podamos hacer una versión que se
pueda jugar de más de un jugador de forma cooperativa. ya sea en la
misma pc o a través de la red.

Otros ficheros con documentación
--------------------------------

Dentro de la carpeta hay otros ficheros con documentación que son los
siguientes:

- CHANGELOG.md : Este fichero contiene una colección de versiones y
  eventos notables de este proyecto, está hecho para ser leído por
  humanos, los cambios más técnicos se pueden tomar del control de
  versiones.

- diseno.md : Este otro es para llevar explicaciones generales
  del proyecto de como se unen las partes, de como funciona y de
  referencias a más documentación técnica.

- LICENSE: La licencia, GNU GPL Versión 3.

- README.md: El fichero que usted está leyendo ahora mismo que tiene
  una idea general del proyecto y referencias a otras partes del
  proyecto.
