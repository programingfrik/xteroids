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

# Categorias de Meteoros
#          vectord    color          masa      vel vrot
catmet = [[(-40, 40), (255, 54, 59), (20, 40), 40, (-5, 5)],   # 0 los chiquitos
          [(-30, 30), (255, 82, 53), (40, 60), 30, (-10, 10)], # 1 los medianos
          [(-20, 20), (255, 161, 74), (60, 80), 20, (-8, 8)]]  # 2 los grandesitos

def estaentre(v, ra, rb):
    """Dice si v está entre el rango formado por ra y rb, no importa el orden."""
    return (((ra < rb) and (v >= ra) and (v <= rb))
            or ((rb < ra) and (v >= rb) and (v <= ra)))

def puntoestaentre(ps, pi, pf):
    """Asumiendo que los tres puntos ps, pi y pf estan sobre la misma
    recta verifica si ps está entre pi y pf."""
    global X, Y
    return (estaentre(ps[X], pi[X], pf[X])
            and estaentre(ps[Y], pi[Y], pf[Y]))

def sesolapadim(ai, af, bi, bf):
    """Dice si los rangos de ai a af y de bi a bf se tocan en una dimensión."""
    return (estaentre(ai, bi, bf)
        or estaentre(af, bi, bf)
        or ((ai <= bi) and (af >= bf)))

def sesolapan(ovniA, ovniB):
    """Dice si los limites de los ovnis en cuestión se solapan."""
    global X, Y, MIN, MAX
    a = ovniA.lim
    b = ovniB.lim
    return (sesolapadim(a[MIN][X], a[MAX][X], b[MIN][X], b[MAX][X])
        and sesolapadim(a[MIN][Y], a[MAX][Y], b[MIN][Y], b[MAX][Y]))

def pendiente(a, b):
    """Calcula la pendiente de la recta por la que pasan los puntos a y
    b."""
    global X, Y
    if (b[X] - a[X]) == 0:
        return None
    return (b[Y] - a[Y]) / (b[X] - a[X])

def secruzan(a1, a2, b1, b2):
    """Verifica si la linea A compuesta por los puntos a1 y a2 se cruza
    con la linea B compuesta por los puntos b1 y b2. Si se cruzan
    aunque sea en un punto lejano retorna el punto de intersección
    sino retorna None, o sea que son paralelas."""
    global X, Y
    ma = pendiente(a1, a2)
    mb = pendiente(b1, b2)
    if (ma == mb):
        return None
    elif (ma == None):
        crucex = a1[X]
        crucey = mb * (crucex - b1[X]) + b1[Y]
    elif (mb == None):
        crucex = b1[X]
        crucey = ma * (crucex - a1[X]) + a1[Y]
    else:
        crucex = ((-mb * b1[X]) + b1[Y] - a1[Y] + (ma * a1[X])) / (ma - mb)
        crucey = ma * (crucex - a1[X]) + a1[Y]
    return (crucex, crucey)

def distancia(a, b):
    """Calcula la distancia entre dos puntos a y b"""
    global X, Y
    return math.sqrt((b[X] - a[X]) ** 2 + (b[Y] - a[Y]) ** 2)

def baleado(ovni, puntob):
    """Verifica si bala toca realmente alguna linea de ovni."""
    for linea in ovni.lineas:
        p1 = ovni.dibpuntos[linea[0]]
        p2 = ovni.dibpuntos[linea[1]]
        cruce = secruzan(p1, p2, puntob, ovni.loc)
        if ((not cruce) or (not puntoestaentre(cruce, p1, p2))):
            continue
        if (distancia(cruce, ovni.loc)
            > distancia(puntob, ovni.loc)):
            return cruce
    return None

def colisionado(ovniA, ovniB):
    """Verifica si los ovnis realmente se tocan entre ellos."""
    valor = distancia(ovniA.loc, ovniB.loc)
    if valor > (ovniA.radiomayor + ovniB.radiomayor):
        return None
    for punto in ovniA.dibpuntos:
        if (distancia(punto, ovniB.loc) < ovniB.radiomayor):
            choque = baleado(ovniB, punto)
            if choque:
                return choque
    return None

def rotSCPunt(punto, sinAngul, cosAngul):
    """Rota un punto en el angulo cuyo seno y coseno se incluyen
    como parametros y retorna el punto resultante."""
    global X, Y

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

def rotPunt(punto, angulo):
    """Rota un punto cualquiera con respecto al origen, el angulo
    indicado, en radianes. Esta funcion no necesita y no modifica
    el sinAngul y cosAngul"""
    return rotSCPunt(punto, math.sin(angulo / 100.0),
                     math.cos(angulo / 100.0))

def trasPunt(punto, puntotras):
    """Para trasladar el \"punto\" sumandole \"puntotras\""""
    global X, Y
    return punto[X] + puntotras[X], punto[Y] + puntotras[Y]

def rotTrasSCPDib(punto, puntotras, sinAngul, cosAngul):
    """Rota y traslada un punto dada la traslacion que se le quiere dar,
    el seno y el coseno del ángulo enque se quiere rotar."""
    return trasPunt(rotSCPunt(punto, sinAngul, cosAngul), puntotras)


class Espacio:
    """Esta clase representa el espacio, cada instancia de esta clase
    sostiene unos objetos y los actualiza o los mueve y hace que
    interactuen entre ellos"""

    def __init__(self, pantalla, tamano, fondo, demo = False):
        """Inicializando un "Espacio" nuevo."""
        self.pantalla = pantalla
        self.tamano = tamano
        self.fondo = fondo
        # Lista de ovnis, todos los objetos que existen en este espacio.
        self.lovnis = []
        self.depuracion = False
        self.demo = demo
        self.navejug = None
        self.poblar()

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
        if ovni in self.lovnis:
            self.lovnis.remove(ovni)

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
                or (not sesolapan(covni, ovni))):
                continue

            # Está tocandose el cuadro límite, verifica si realmente
            # toca la figura
            if ((type(ovni) in [Nave, Meteoro])
                 and isinstance(covni, Bala)):
                puntochoque = baleado(ovni, covni.punta())
            elif ((type(covni) in [Nave, Meteoro])
                  and isinstance(ovni, Bala)):
                puntochoque = baleado(covni, ovni.punta())
            elif ((type(ovni) in [Nave, Meteoro])
                  and (type(covni) in [Nave, Meteoro])):
                puntochoque = colisionado(ovni, covni)

            if not puntochoque:
                continue

            # Si se tocan
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
        for ovni in tlovnis:
            ovni.golpe()
            self.colisionares(tlovnis, ovni)
            ovni.dibujar()

        # aqui se acabaron las funciones de dibujo
        # que necesitan lock
        self.pantalla.unlock()

    def poblar(self, nivel = 0):
        """Se encarga de poblar el espacio con una nave en el centro y varios meteoros."""
        global catmet, X, Y

        # Centro de la pantalla.
        centro = ((self.tamano[X] / 2 * 100), (self.tamano[Y] / 2 * 100))

        # Ponga la nave del jugador en el centro
        self.navejug = Nave(centro, 471, (0, 0), (0, 255, 0))
        self.agregar(self.navejug)

        # Arme un par de meteoros al azar en posiciones que no se solapen
        cantm = random.randrange(3, 5)
        fact = 628.0 / cantm
        distanciac = random.randrange(90, (self.tamano[Y] / 2) - 30) * 100
        for cont in range(cantm):
            anguloaz = (fact * cont) + random.randrange(-40, 40)
            # la categoria del meteoro en cuestión
            cat = random.randrange(0, 2)
            self.agregar(Meteoro(
                trasPunt(rotPunt((distanciac, 0), anguloaz), centro),
                0,
                (random.randrange(catmet[cat][0][MIN], catmet[cat][0][MAX]),
                 random.randrange(catmet[cat][0][MIN], catmet[cat][0][MAX])),
                catmet[cat][1],
                random.randrange(catmet[cat][2][MIN], catmet[cat][2][MAX]),
                random.randrange(catmet[cat][3]),
                random.randrange(catmet[cat][4][MIN], catmet[cat][4][MAX]),
                cat))

# las clases que se usaran en el jueguillo
class Ovni:
    """Objeto Volador No Identificado, un asteroide, una nave, etc.

    Esta es la clase base de la que van a derivar los elementos del
    juego que se mueven en la pantalla."""
    def __init__(self, loc, ang, vectord, colorApl):
        # inicializando variables
        self.ponerloccien(loc)
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
        # De momento este ovni no es parte de ningún espacio
        self.miespacio = None
        # El cuadrado de los límites de este Ovni expresado en dos
        # coordenadas un punto con los valores mínimos de coordenadas
        # X, Y y otro con los valores máximos X, Y.

    def ponerloccien(self, loc):
        """Pone el valor de locreal y de loc. locreal trabaja con más
        precisión, loc se usa para dibujar y hacer colisiones, operaciones que
        necesita valores enteros de pixeles."""
        global X, Y
        self.locreal = loc
        self.loc = tuple([self.locreal[D] // 100 for D in [X, Y]])

    def dibujar(self):
        """Dibuja el Ovni en el surface srfce usando los puntos self.dibpuntos."""
        global X, Y, MIN, MAX

        # aqui se manda a dibujar usando los puntos del dibujo
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

    def acelerar(self, acel):
        """Para cambiar la aceleracion del objeto, la cantidad de posiciones que avanza,
        en el angulo del ovni."""
        global X, Y

        px = int(self.vectord[X] + (acel * self.cosAngul))
        py = int(self.vectord[Y] + (acel * self.sinAngul))
        self.vectord = px, py

    def calcularDibPuntos(self):
        """Calcula los puntos a dibujar realmente, rotandolos el angulo real y
        trasladandolos al punto donde se encuentra el ovni. Para ser
        más eficientes se calcula el seno y el coseno del ángulo que
        se va a rotar todo, 1 sola vez por la figura completa, que
        esta al mismo angulo y se calucula en el momento de rotar la
        figura."""

        # Inicializa los límites del Ovni
        for P in [MIN, MAX]:
            self.lim[P] = self.loc

        # Rota y traslada los puntos para poder usarlos al momento de dibujar.
        self.dibpuntos = []
        for punto in self.puntos:
            ptemp = rotTrasSCPDib(punto, self.loc, self.sinAngul, self.cosAngul)
            self.dibpuntos.append(ptemp)
            self.delimitar(ptemp)

    def rotar(self, angulo):
        """Rota el objeto la cantidad de radianes indicada por
        angulo."""
        global X, Y, MIN, MAX

        # sumo el angulo
        self.ang += angulo

        # hay que mantener el angulo entre 0 y 628 radianes
        if (self.ang > 628): self.ang = self.ang - 628
        elif (self.ang < 0): self.ang = self.ang + 628

        anguloFl = self.ang / 100.0
        self.sinAngul = math.sin(anguloFl)
        self.cosAngul = math.cos(anguloFl)

        self.calcularDibPuntos()

    def golpe(self):
        """En cada golpe de reloj se llama esta función en caso de que el
        objeto en cuestión tenga alguna cosa que hacer puede sobrescribir esta
        función. Esta función podría avanzar un objeto o hacer alguna verificación."""
        global X, Y, MIN, MAX

        limites = self.miespacio.tamano

        # traslado el punto de la localizacion
        self.ponerloccien(trasPunt(self.locreal, self.vectord))

        # Si la localizacion esta fuera de los limites
        # introducelo por el otro extremo
        for D in [X, Y]:
            if self.locreal[D] < 0:
                lloc = list(self.locreal)
                lloc[D] = limites[D] * 100
                self.ponerloccien(tuple(lloc))
            elif self.locreal[D] > limites[D] * 100:
                lloc = list(self.locreal)
                lloc[D] = 0
                self.ponerloccien(tuple(lloc))

        self.calcularDibPuntos()

    def colision(self, ovnicol, puntochoque):
        """Cuando se produce una colisión el espacio llama esta función para
        que el omasa en cuestión tome la acción que
        corresponda. ovnicol es el objeto con el que se produjo la
        colisión. Y puntochoque es el punto en el que se produjo el
        choque."""
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
        que el omasa en cuestión tome la acción que
        corresponda. ovnicol es el objeto con el que se produjo la
        colisión. Y puntochoque es el punto en el que se produjo el
        choque."""
        # Si hubo una colisión cambiale el color de depuración.
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

    def colision(self, ovnicol, puntochoque):
        """Esto es lo que debe hacer una bala ante un choque"""
        self.miespacio.quitar(self)


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
    def __init__(self, loc, ang, vectord, colorApl, masa, vel, vrot, cat):
        Omasa.__init__(self, loc, ang, vectord, colorApl, masa)
        self.vrot = vrot
        # los puntos del meteoro se generan al azar
        self.puntos = []
        cantp = random.randrange(10, 20)
        fact = 628.0 / cantp
        self.radiomenor = self.masa + 10
        self.radiomayor = -10
        self.cat = cat
        for cont in range(cantp):
            magnitudaz = self.masa + random.randrange(-10, 10)
            if (magnitudaz > self.radiomayor):
                self.radiomayor = magnitudaz
            elif (magnitudaz < self.radiomenor):
                self.radiomenor = magnitudaz
            anguloaz = (fact * cont)  + random.randrange(-10, 10)
            self.puntos.append(rotPunt((magnitudaz, 0), anguloaz))

        # las lineas de los meteoros se hacen usando los puntos
        self.lineas = []
        for cont in range((len(self.puntos) - 1), -1, -1):
            self.lineas.append((cont, cont - 1))

        self.rotar(0)
        self.acelerar(vel)

    def golpe(self):
        self.rotar(self.vrot)
        Omasa.golpe(self)

    def dividir(self):
        # TODO: implementar
        pass

    def __repr__(self):
        """La representación de este Meteoro."""
        return f"<Meteoro loc={self.loc} ang={self.ang} lim={self.lim}>"

    def dibujar(self):
        """Manda a dibujar las cosas específicas de un Meteoro."""
        global X, Y
        srfce = self.miespacio.pantalla
        if self.miespacio.depuracion:
            pygame.draw.circle(srfce, self.colordep, self.loc, self.radiomenor, width = 1)
            pygame.draw.circle(srfce, self.colordep, self.loc, self.radiomayor, width = 1)
        Omasa.dibujar(self)

    def colision(self, ovnicol, puntochoque):
        """La reacción de un meteoro cuando lo chocan."""
        Omasa.colision(self, ovnicol, puntochoque)

        # En que plano tangente a ambos ovnis se produjo el choque.

        # Cual es el ángulo de este ovni con respecto a ese plano.

        # Cual es el vector reflejo de ese ángulo.

        # Los choques no son elásticos completamente, una parte de la fuerza se absorve

        # El objeto con más masa recibe menos influencia del otro objeto.

        # El objeto con menos masa recibe máyor influencia del otro.




