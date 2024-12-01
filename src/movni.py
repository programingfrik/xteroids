# -*- coding: utf-8 -*-

# Este modulo contiene la clase ovni y los objetos que derivan del

# Estos son los imports necesarios
import pygame, math, random

# Para que los fuentes sean más legibles aquí declaro algunas
# constantes para usarlas en todo el programa.
X = 0
Y = 1
MIN = 0
MAX = 1

class Espacio:
    """Esta clase representa el espacio, cada instancia de esta clase
    sostiene unos objetos y los actualiza o los mueve y hace que
    interactuen entre ellos"""

    def __init__(self, pantalla, tamano, fondo):
        """Inicializando un "Espacio" nuevo."""
        self.pantalla = pantalla
        self.tamano = tamano
        self.fondo = fondo
        # Lista de ovnis, todos los objetos que existen en este espacio.
        self.lovnis = []
        self.depuracion = False

    def agregar(self, ovni):
        """Pone un ovni en este espacio y se encarga de que no choque
        con ningun otro objeto en este espacio."""

        # TODO: el objeto choca con otro objeto?
        # si choca hay que moverlo a otra coordenada al azar

        ovni.miespacio = self
        self.lovnis.append(ovni)

        return (len(self.lovnis) - 1)

    def quitar(self, ovni):
        """Para quitar el ovni que se indique del espacio."""
        # se quita el objeto de la lista de objetos
        self.lovnis.remove(ovni)

    def estaentre(self, v, ra, rb):
        """Dice si v está entre el rango formado por ra y rb, no importa el orden."""
        return (((ra < rb) and (v >= ra) and (v <= rb))
                or ((rb < ra) and (v >= rb) and (v <= ra)))

    def puntoestaentre(self, ps, pi, pf):
        """Asumiendo que los tres puntos ps, pi y pf estan sobre la misma
        recta verifica si ps está entre pi y pf."""
        global X, Y
        return (self.estaentre(ps[X], pi[X], pf[X])
                and self.estaentre(ps[Y], pi[Y], pf[Y]))

    def sesolapadim(self, ai, af, bi, bf):
        """Dice si los rangos de ai a af y de bi a bf se tocan en una dimensión."""
        return (self.estaentre(ai, bi, bf)
            or self.estaentre(af, bi, bf)
            or ((ai <= bi) and (af >= bf)))

    def sesolapan(self, ovniA, ovniB):
        """Dice si los limites de los ovnis en cuestión se solapan."""
        global X, Y, MIN, MAX
        a = ovniA.lim
        b = ovniB.lim
        return (self.sesolapadim(a[MIN][X], a[MAX][X], b[MIN][X], b[MAX][X])
            and self.sesolapadim(a[MIN][Y], a[MAX][Y], b[MIN][Y], b[MAX][Y]))

    def pendiente(self, a, b):
        """Calcula la pendiente de la recta por la que pasan los puntos a y
        b."""
        global X, Y
        if (b[X] - a[X]) == 0:
            return None
        return (b[Y] - a[Y]) / (b[X] - a[X])

    def secruzan(self, a1, a2, b1, b2):
        """Verifica si la linea A compuesta por los puntos a1 y a2 se cruza
        con la linea B compuesta por los puntos b1 y b2. Si se cruzan
        aunque sea en un punto lejano retorna el punto de intersección
        sino retorna None, o sea que son paralelas."""
        global X, Y
        ma = self.pendiente(a1, a2)
        mb = self.pendiente(b1, b2)
        if (ma == mb):
            return None
        elif (not ma):
            crucex = a1[X]
            crucey = mb * (crucex - b1[X]) + b1[Y]
        elif (not mb):
            crucex = b1[X]
            crucey = ma * (crucex - a1[X]) + a1[Y]
        else:
            crucex = ((-mb * b1[X]) + b1[Y] - a1[Y] + (ma * a1[X])) / (ma - mb)
            crucey = ma * (crucex - a1[X]) + a1[Y]
        return (crucex, crucey)

    def distancia(self, a, b):
        """Calcula la distancia entre dos puntos a y b"""
        global X, Y
        return math.sqrt((b[X] - a[X]) ** 2 + (b[Y] - a[Y]) ** 2)

    def baleado(self, ovni, bala):
        """Verifica si bala toca realmente alguna linea de ovni."""
        puntob = bala.punta()
        for linea in ovni.lineas:
            p1 = ovni.dibpuntos[linea[0]]
            p2 = ovni.dibpuntos[linea[1]]
            cruce = self.secruzan(p1, p2, puntob, ovni.loc)
            if ((not cruce) or (not self.puntoestaentre(cruce, p1, p2))):
                continue
            if (self.distancia(cruce, ovni.loc)
                  > self.distancia(puntob, ovni.loc)):
                return cruce
        return None

    def colisionado(self, ovniA, ovniB):
        """Verifica si los ovnis realmente se tocan entre ellos."""
        if self.distancia(ovniA.loc, ovniB.loc) > (ovniA.radiomayor + ovniB.radiomayor):
            return None
        for punto in ovniA.dibpuntos:
            if (self.distancia(punto, ovniB.loc) < ovniB.radiomayor):
                choque = self.baleado(ovniB, punto)
                if choque:
                    return choque
        return None

    def colisionares(self, lovni, ovni):
        """Verifica las colisiones de todos los ovnis y avisa a los ovnis
        involucrados en esas colisiones."""

        # Si no es una bala, nave o meteoro no se necesita verificar
        # las colisiones
        if type(ovni) not in [Bala, Nave, Meteoro]:
            return

        # Las colisiones se verifican de 2 en 2, después de que un
        # ovni es verificado contra todos los elementos de la lista,
        # esos elementos de la lista no tienen que verificar contra el
        # primero. Por eso este bucle comienza en pos + 1, esto reduce
        # a la mitad las verificaciones.
        pos = lovni.index(ovni)
        for covni in lovni[pos + 1:]:
            if ((covni is ovni)
                or (type(covni) not in [Bala, Nave, Meteoro])
                or (isinstance(covni, Bala)
                    and isinstance(ovni, Bala))
                or (not self.sesolapan(covni, ovni))):
                continue

            # Está tocandose el cuadro límite, verifica si realmente
            # toca la figura
            if ((type(ovni) in [Nave, Meteoro])
                 and isinstance(covni, Bala)):
                puntochoque = self.baleado(ovni, covni)
            elif ((type(covni) in [Nave, Meteoro])
                  and isinstance(ovni, Bala)):
                puntochoque = self.baleado(covni, ovni)
            elif ((type(ovni) in [Nave, Meteoro])
                  and (type(covni) in [Nave, Meteoro])):
                puntochoque = self.colisionado(ovni, covni)

            if not puntochoque:
                continue

            # Si se tocan
            # print(f"Colisión detectada!")
            ovni.colision(covni, puntochoque)
            covni.colision(ovni, puntochoque)

    def golpe(self):
        """Esta función debe ejecutarse en cada golpe del reloj. Esta
        función es la que hace todo el trabajo, de enviar a que se le
        haga render a los objetos y de verificar las interacciones y
        los sonidos que producen los diferentes objetos."""

        # borrando la pantalla y poniendo el color de fondo
        self.pantalla.fill(self.fondo)

        # dibujando los objetos en la pantalla
        self.pantalla.lock()

        # para todos los objetos en la pantalla
        tlovnis = self.lovnis.copy()
        # print(f"Los ovnis que vamos a verificar {tlovnis}")
        for ovni in tlovnis:
            ovni.golpe()
            self.colisionares(tlovnis, ovni)
            ovni.dibujar()

        # aqui se acabaron las funciones de dibujo
        # que necesitan lock
        self.pantalla.unlock()

# las clases que se usaran en el jueguillo
class Ovni:
    """Objeto Volador No Identificado, un asteroide, una nave, etc.

    Esta es la clase base de la que van a derivar los elementos del
    juego que se mueven en la pantalla."""
    def __init__(self, loc, ang, vectord, colorApl):
        # inicializando variables
        self.loc = loc
        # print("creando un ovni nuevo loc:", loc, " self.loc:", self.loc)
        self.ang = ang
        self.vectord = vectord
        self.color = colorApl
        self.colordep = (0, 0, 255)
        # los puntos del dibujo del ovni
        self.puntos = [(10, 0),(-3, 0)]
        self.lineas = [(0, 1)]
        # hay que llamar a la función rotar para que
        # se inicialicen los puntos del dibujo
        self.lim = [(0, 0), (0, 0)]
        self.rotar(0)
        # print("creando un ovni confirmacion loc:", loc, " self.loc:", self.loc)
        # De momento este ovni no es parte de ningún espacio
        self.miespacio = None
        # El cuadrado de los límites de este Ovni expresado en dos
        # coordenadas un punto con los valores mínimos de coordenadas
        # X, Y y otro con los valores máximos X, Y.

    def dibujar(self):
        """Dibuja el Ovni en el surface srfce usando los puntos self.dibpuntos."""
        global X, Y, MIN, MAX

        # aqui se manda a dibujar usando los puntos del dibujo
        # print("dibujando: ", type(self))

        srfce = self.miespacio.pantalla

        if self.miespacio.depuracion:
            # Si estamos en modo depuración dibuja el rectángulo de los límites.
            temppuntos = [self.lim[MIN],
                          (self.lim[MIN][X], self.lim[MAX][Y]),
                          self.lim[MAX],
                          (self.lim[MAX][X], self.lim[MIN][Y])]
            templineas = [(0, 1), (1, 2), (2, 3), (3, 0)]
            for linea in templineas:
                pygame.draw.line(srfce, self.colordep, temppuntos[linea[0]], temppuntos[linea[1]])

        for linea in self.lineas:
            pygame.draw.line(srfce, self.color, self.dibpuntos[linea[0]], self.dibpuntos[linea[1]])

        # Vuelve a inicializar el color de depuración para la próxima vuelta.
        self.colordep = (0, 0, 255)


    def delimitar(self, punto):
        """Crea el rectangulo con los valores máximos y mínimos de X y Y para
        este Ovni."""
        global X, Y, MIN, MAX
        for D in [X, Y]:
            if punto[D] < self.lim[MIN][D]:
                llim = list(self.lim[MIN])
                llim[D] = punto[D]
                self.lim[MIN] = tuple(llim)
            elif punto[D] > self.lim[MAX][D]:
                llim = list(self.lim[MAX])
                llim[D] = punto[D]
                self.lim[MAX] = tuple(llim)

    def rotSCPunt(self, punto, sinAngul, cosAngul):
        """Rota un punto en el angulo cuyo seno y coseno se incluyen
        como parametros y retorna el punto resultante."""
        global X, Y

        # print("seno %f y coseno %f y el punto (%i,%i)"%(sinAngul, cosAngul, punto[X], punto[Y]))

        # como el seno y el coseno son el mismo para todos los puntos
        # porque se trata del mismo angulo este se saca fuera de esta
        # funcion que corre para todos los puntos.
        px = punto[X] * cosAngul
        px -= punto[Y] * sinAngul
        px = int(px)
        py = punto[X] * sinAngul
        py += punto[Y] * cosAngul
        py = int(py)
        return px, py

    def rotPunt(self, punto, angulo):
        """Rota un punto cualquiera con respecto al origen, el angulo
        indicado, en radianes. Esta funcion no necesita y no modifica
        el self.sinAngul y self.cosAngul"""
        return self.rotSCPunt(punto, math.sin(angulo / 100.0)
                         , math.cos(angulo / 100.0))

    def rotSCPDib(self, punto):
        """Rota un punto cualquiera el angulo indicado por el seno y
        el coseno del angulo en radianes que deben ponerse
        previamente en self.sinAngul y self.cosAngul"""
        temp = self.rotSCPunt(punto, self.sinAngul, self.cosAngul)
        return temp

    def rotPDib(self, punto):
        """Para rotar un punto en el angulo self.ang. Esta funcion no
        necesita y no modifica el self.sinAngul y self.cosAngul"""
        temp = self.rotPunt(punto, self.ang)
        return temp

    def trasPunt(self, punto, puntotras):
        """Para trasladar el \"punto\" sumandole \"puntotras\""""
        global X, Y
        return punto[X] + puntotras[X], punto[Y] + puntotras[Y]

    def trasPDib(self, punto):
        """Para trasladar con respecto al punto de localizacion del
        objeto"""
        # TODO: creo que no es correcto hacer la división entre 100 de
        # este lado.
        localpunto = tuple([self.loc[D] / 100 + punto[D] for D in [X, Y]])
        self.delimitar(localpunto)
        return localpunto

    def rotTrasSCPDib(self, punto):
        return self.trasPDib(self.rotSCPDib(punto))

    def acelerar(self, acel):
        """Para cambiar la aceleracion del objeto, la cantidad de posiciones que avanza,
        en el angulo del ovni."""
        global X, Y
        px = int(self.vectord[X] + (acel * (self.cosAngul)))
        py = int(self.vectord[Y] + (acel * (self.sinAngul)))
        self.vectord = px, py

    def calcularDibPuntos(self):
        # como todos los puntos se rotan en el mismo angulo no vale la
        # pena sacar el seno y el coseno cada vez que es una operacion
        # que toma tiempo precioso del CPU
        anguloFl = self.ang / 100.0
        self.sinAngul = math.sin(anguloFl)
        self.cosAngul = math.cos(anguloFl)

        # Inicializa los límites del Ovni
        for P in [MIN, MAX]:
            self.lim[P] = tuple([V / 100 for V in self.loc])

        # Rota y traslada los puntos para poder usarlos al momento de dibujar.
        self.dibpuntos = list(map(self.rotTrasSCPDib, self.puntos))

    def rotar(self, angulo):
        """Rota el objeto la cantidad de radianes indicada por
        angulo."""
        global X, Y, MIN, MAX

        # sumo el angulo
        self.ang += angulo

        # hay que mantener el angulo entre 0 y 628 radianes
        if (self.ang > 628): self.ang = self.ang - 628
        elif (self.ang < 0): self.ang = self.ang + 628

        self.calcularDibPuntos()

    def golpe(self):
        """En cada golpe de reloj se llama esta función en caso de que el
        objeto en cuestión tenga alguna cosa que hacer puede sobrescribir esta
        función. Esta función podría avanzar un objeto o hacer alguna verificación."""
        global X, Y, MIN, MAX

        limites = self.miespacio.tamano

        # traslado el punto de la localizacion
        self.loc = self.trasPunt(self.loc, self.vectord)

        # Si la localizacion esta fuera de los limites
        # introducelo por el otro extremo
        for D in [X, Y]:
            if self.loc[D] < 0:
                llim = list(self.loc)
                llim[D] = limites[D] * 100
                self.loc = tuple(llim)
            elif self.loc[D] > (limites[D] * 100):
                llim = list(self.loc)
                llim[D] = 0
                self.loc = tuple(llim)

        self.calcularDibPuntos()

    def colision(self, ovnicol, puntochoque):
        pass

    def explotar(self, bala, objetos):
        """Cuando el objeto con masa explota tiene que dividirse en diferentes
        partes con tamano mas pequeno"""
        # TODO: implementar
        pass

    def __repr__(self):
        """La representación de este ovni."""
        return f"<Ovni loc={self.loc} ang={self.ang} lim={self.lim}>"

class Omasa(Ovni):
    """Representa los objetos con masa, que reaccionan a las balas."""
    def __init__(self, loc, ang, vectord, colorApl, masa):
        Ovni.__init__(self, loc, ang, vectord, colorApl)
        self.masa = masa
        self.radiomayor = 2
        self.radiomenor = 1

    def colision(self, ovnicol, puntochoque):
        """Cuando se produce una colisión el espacio llama esta función para
        que el ovni en cuestión tome la acción que corresponda. ovnicol es el
        objeto con el que se produjo la colisión."""
        # Si hubo una colisión cambiale el color de depuración.
        # print(f"{self} procesando colision")
        self.colordep = (0, 255, 0)

    def __repr__(self):
        """La representación de este ovni con masa."""
        return f"<Omasa loc={self.loc} ang={self.ang} lim={self.lim}>"

class Bala(Omasa):
    """Para representar las balas que disparan las naves"""
    def __init__(self, loc, ang, vectord, colorApl, colorFin, vida, vel):
        Ovni.__init__(self, loc, ang, vectord, colorApl)
        self.colorf = colorFin
        self.vida = vida
        self.puntos = [(0, 0),(5, 0)]
        self.lineas = [(0,1)]
        self.rotar(0)
        self.acelerar(vel)

    def dibujar(self):
        srfce = self.miespacio.pantalla
        if (self.vida > 15):
            colorbala = self.color
        else:
            colorbala = self.colorf
        pygame.draw.line(srfce, colorbala, self.dibpuntos[0], self.dibpuntos[1])
        self.vida -= 1

    def golpe(self):
        Omasa.golpe(self)
        if (self.vida <= 0):
            self.miespacio.quitar(self)
        else:
            self.vida -= 1

    def __repr__(self):
        """La representación de esta Bala."""
        return f"<Bala loc={self.loc} ang={self.ang} lim={self.lim}>"

    def punta(self):
        """Retorna el punto que va a llegar primero a cualquier colision."""
        return self.dibpuntos[1]


class Nave(Omasa):
    """Cada instancia representa una nave"""
    def __init__(self, loc, ang, vectord, colorApl):
        Omasa.__init__(self, loc, ang, vectord, colorApl, 5)
        self.puntos = [(13, 0), (10, 0), (0, 0), (-3, -5), (-3, 5)]
        self.lineas = [(1, 3), (1, 4), (2, 3), (2, 4)]
        self.radiomayor = 13
        self.radiomenor = 5
        self.rotar(0)

    def disparar(self):
        """Hay que poner una bala nueva en la lista de balas"""
        angulo = self.ang + random.randrange(-10,10)
        self.miespacio.agregar(
            Bala((self.dibpuntos[0][X] * 100, self.dibpuntos[0][Y] * 100)
                 , angulo, self.vectord, self.color, (0, 0 , 200), 50, 360))

    def __repr__(self):
        """La representación de esta Nave."""
        return f"<Nave loc={self.loc} ang={self.ang} lim={self.lim}>"


class Meteoro(Omasa):
    def __init__(self, loc, ang, vectord, colorApl, masa, vel, vrot):
        Omasa.__init__(self, loc, ang, vectord, colorApl, masa)
        self.vrot = vrot
        # los puntos del meteoro se generan al azar
        self.puntos = []
        cantp = random.randrange(10, 20)
        fact = 628.0 / cantp
        self.radiomenor = 10
        self.radiomayor = -10
        for cont in range(cantp):
            magnitudaz = self.masa + random.randrange(-10, 10)
            if (magnitudaz > self.radiomayor):
                self.radiomayor = magnitudaz
            elif (magnitudaz < self.radiomenor):
                self.radiomenor = magnitudaz
            anguloaz = (fact * cont)  + random.randrange(-10, 10)
            tsin = math.sin(anguloaz / 100)
            tcos = math.cos(anguloaz / 100)
            self.puntos.append(self.rotPunt((magnitudaz, 0), anguloaz))

        # las lineas de los meteoros se hacen usando los puntos
        self.lineas = []
        for cont in range((len(self.puntos) - 1), -1, -1):
            self.lineas.append((cont, cont - 1))

#        for c in range(len(self.puntos)):
#             print("self.puntos[%i] : %s " % (c, str(self.puntos[c])))
#         for c in range(len(self.lineas)):
#            print("self.lineas[%i] : %s " % (c, str(self.lineas[c])))

        self.rotar(0)
        self.acelerar(vel)

    def golpe(self):
        self.ang += self.vrot
        Omasa.golpe(self)

    def dividir(self):
        # TODO: implementar
        pass

    def __repr__(self):
        """La representación de este Meteoro."""
        return f"<Meteoro loc={self.loc} ang={self.ang} lim={self.lim}>"

    def dibujar(self):
        """Manda a dibujar las cosas específicas de un Meteoro."""
        Omasa.dibujar(self)
        srfce = self.miespacio.pantalla
        if self.miespacio.depuracion:
            pygame.draw.circle(srfce, self.colordep, self.loc, self.radiomenor)
            pygame.draw.circle(srfce, self.colordep, self.loc, self.radiomayor)
