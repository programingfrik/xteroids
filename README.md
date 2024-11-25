Leeme
-----

Este archivo es para hablar a nivel general del proyecto y talvez para iniciar
a los usuarios de la aplicacion.

que es ?

Esto es un proyecto para crear un clon del antiguo Asteroids. El
objetivo de este proyecto es crear un juego usable en la mayor parte
de las computadoras que se parezca mucho en la forma de jugar y en
sentimiento al antiguo asteroids.

El Asteroids era un juego recreativo que consistia en una pequena nave
espacial que destruia asteroides, de ahi su nombre. El objetivo del
juego es destruir la mayor cantidad de asteroides posibles sin chocar
con los mismo, obteniendo asi la mayor puntuacion. Segun se hiban
pasando los niveles el juego hiba creciendo en dificultad segun
aparecian mas asteroides y era mas dificil de evitar chocar con los
asteroides. Tambien en algunos momentos aparecian naves enemigas que
tambien disparaban a los asteroides. Hasta este punto el clon se va a
mantener igual pero quiero que el juego que resulte de este proyecto
tenga un par de cosas diferentes al juego original de asteroids que
son las siguientes:

1 - En el juego original de asteroides los asteroides podian solaparse
quiero que en esta version eso no ocurra, que los asteroides choquen y
reboten entre ellos

2 - Efecto de friccion y rotacion, si dos asteroides chocan o rozan la
rotacion cambia de acuerdo con esto.

3 - La nave no siempre se destruye ante una colicion, para que la nave
se destruya tiene que ocurrir una colicion con cierta fuerza.

4 - Las naves enemigas tambien pueden ser destruidas por los
asteroides

5 - La pantalla no esta fija trata siempre de poner la nave del
jugador en el centro y lo sigue por el espacio. El espacio esta
confinado a un cuadro (que podria variar de tamano ??) pero al usuario
le parecera infinito porque cada vez que algun objeto vaya a salir del
cuadro entra por el otro lado. Esto ocurre con todos los objetos menos
con los power-ups y las naves enemigas.

6 - Las coliciones son detectadas sin tomar en cuenta la
representacion de los objetos.

7 - Existen 3 power ups que podrian aparecer flotando en el espacio escudos,
bombas y teleportadores. Solo se puede tener un power up a la vez,
cuando se empieza a usar el power up este dura un tiempo y luego se
hagota, siempre es el mismo tiempo si importar el power up, si el
jugador tiene un escudo se va a cubrir durante el tiempo, si tiene una
bomba podra usar todas las bombas que puedan invocar sus dedos durante
el tiempo, si tiene la habilidad de la teletransportacion puede
teletransportarse de forma azarosa a algun lugar que no haya un
asteroide.

8 - Existen algunos efectos visuales especiales. Cuando se encienden
las turbinas de la nave hay efecto de particulas. Cuando rozan dos
obetos se desprenden particulas y pequenas lineas. Cuando la nave
choca o se destrulle las lineas (pedazos de la nave) siguen un vector
parecido al que que hubiera tenido la nave resultado de la colicion
pero sin penetrar en los asteroides que son considerados cuerpos
solidos. cuando se destrulle alguna cosa se ven pequenos circulos como
ondas expancivas que desaparecen de una vez. las bombas dejan un
rastro de lineas cortas perpenticulares a la trayectoria de la bomba
que van desapareciendo. Las explociones de las bombas arrojan algunas
balas en todas direcciones que desaparecen mas rapido que las balas de
la nave. Las balas de la nave se desaparecen despues de cierto tiempo.

9 - Los asteroides son de diferentes tamanos (al azar) y mientras mas
grandes son mas se pueden subdividir. Los asteroides son poligonos
cerrados que se asemejan a circulos pero son irregulares. Los
asteroides tienen un vector inicial y una velocidad. Mientras vaya
aumentando la dificultad del juego apareceran mayor cantidad de
asteroides y tendran la posibilidad de moverse a mayores velocidades.

10 - las balas no son lanzadas exactamente en la misma direccion en
que esta apuntando la nave, tienen cierto componente de azar, cuestion
que si se deja precionado el boton de fuego se ve algo como una
metralladora en la que todas las balas tienen un vector parecido pero
no el mismo exactamente.

Como yo espero algun dia poder llamarme un desarrollador de juegos
espero poder hacer algunas implementaciones diferentes, en python
primero,  en .NET, en c usando SDL (que por sus prestaciones espero
que sea la version mas profesional y mas jugable), y talvez en java ?

Espero poder poner una seccion de creditos donde se vean en una letra
con vectores mi nombre en todos los renglones y el nombre del juego.

Talvez en alguna de las versiones podamos hacer una version que se
pueda jugar de mas de un jugador de forma cooperativa. ya sea en la
misma pc o en a traves de la red.

para que se usa (que problema resuelve)?

El resultado de este proyecto es un juego sirve para jugar, entonces
el problema que resuelve es el problema de las personas que no tienen
que hacer con su tiempo (existen esas personas ? entretenimiento
... que concepto mas raro ese), en caso de que no existan es para mi
para.

como se usa ?

Debe ser algun tipo de ejecutable que se invoque de la forma mas
conveniente la forma de juego es igual la flecha para arriba o
parecido.

otros archivos con documentacion !!

Esta carpeta es una plantilla para todo los proyectos de aplicaciones
o librerias que me proponga hacer por mi cuenta.

Dentro de la carpeta hay tres archivos que son los siguientes:

- leeme.txt : con informacion del proyecto de que es para que sirve,
  mas bien del lado de como usarlo que de como funciona.

- historia.txt : este archivo es para llevar los cambios que han ido
  ocurriendo aunque no haya un sistema de versiones. Si es asi de todos
  modos se pueden comprimir las versiones viejas o usar diferencias de
  manera manual para poder mantener la historia, eso en cuanto al codigo
  fuente. Este archivo hace las veces de bitacora del proyecto.

- desarrollo.txt : Este archivo es para llevar explicaciones generales
  del proyecto de como se unen las partes, de como funciona y de
  referencias a mas documentacion tecnica.