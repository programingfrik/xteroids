# -*- coding: utf-8 -*-

# Este modulo contiene la clase ovni y los objetos que derivan del

# Estos son los imports necesarios
import pygame, math, random

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

    def estaentre(self, v, ri, rf):
        """Dice si v está entre ri y rf, ri debe ser menor que rf."""
        return (ri < rf) and (v >= ri) and (v <= rf)

    def sesolapadim(self, ai, af, bi, bf):
        """Dice si los rangos de ai a af y de bi a bf se tocan en una dimensión."""
        return (self.estaentre(ai, bi, bf)
            or self.estaentre(af, bi, bf)
            or ((ai <= bi) and (af >= bf)))

    def sesolapan(self, a, b):
        """Dice si los ovnis en sus cuadros básicos se solapan."""
        return (self.sesolapadim(a.mnX, a.mxX, b.mnX, b.mxX)
            and self.sesolapadim(a.mnY, a.mxY, b.mnY, b.mxY))

    def colisionares(self, lovni, ovni):
        """Verifica las colisiones de todos los ovnis y avisa a los ovnis
        involucrados en esas colisiones."""
        if type(ovni) not in [Bala, Nave, Meteoro]:
            return
        pos = lovni.index(ovni) + 1
        print(f"verificando a partir de la posición {pos}")
        for covni in lovni[pos:]:
            if ((covni is ovni)
                or (type(covni) not in [Bala, Nave, Meteoro])
                or (isinstance(covni, Bala)
                    and isinstance(ovni, Bala))
                or (not self.sesolapan(covni, ovni))):
                continue
            print(f"Colisión detectada!")
            ovni.colision(covni)
            covni.colision(ovni)

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
        print(f"Los ovnis que vamos a verificar {tlovnis}")
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
        self.rotar(0)
        # print("creando un ovni confirmacion loc:", loc, " self.loc:", self.loc)
        # De momento este ovni no es parte de ningún espacio
        self.miespacio = None

    def dibujar(self):
        """Dibuja el Ovni en el surface srfce usando los puntos self.dibpuntos."""
        # aqui se manda a dibujar usando los puntos del dibujo
        # print("dibujando: ", type(self))
        srfce = self.miespacio.pantalla

        if self.miespacio.depuracion:
            pygame.draw.line(
                srfce, self.colordep,
                (self.mnX, self.mnY), (self.mxX, self.mnY))
            pygame.draw.line(
                srfce, self.colordep,
                (self.mnX, self.mxY), (self.mxX, self.mxY))
            pygame.draw.line(
                srfce, self.colordep,
                (self.mnX, self.mnY), (self.mnX, self.mxY))
            pygame.draw.line(
                srfce, self.colordep,
                (self.mxX, self.mnY), (self.mxX, self.mxY))

        for linea in self.lineas:
            pygame.draw.line(srfce, self.color, self.dibpuntos[linea[0]], self.dibpuntos[linea[1]])

    def actArea(self, punto):
        """Evalua si el punto esta dentro del area de coliciones si no
        lo esta amplia el area de acuerdo."""

        if (punto[0] < self.mnX):
            self.mnX = punto[0]
        elif (punto[0] > self.mxX):
            self.mxX = punto[0]

        if (punto[1] < self.mnY):
            self.mnY = punto[1]
        elif (punto[1] > self.mxY):
            self.mxY = punto[1]

    def rotSCPunt(self, punto, sinAngul, cosAngul):
        """Rota un punto en el angulo cuyo seno y coseno se incluyen
        como parametros y retorna el punto resultante."""

        #print("seno %f y coseno %f y el punto (%i,%i)"%(sinAngul, cosAngul, punto[0], punto[1]))

        # como el seno y el coseno son el mismo para todos los puntos
        # porque se trata del mismo angulo este se saca fuera de esta
        # funcion que corre para todos los puntos.
        px = punto[0] * cosAngul
        px -= punto[1] * sinAngul
        px = int(px)
        py = punto[0] * sinAngul
        py += punto[1] * cosAngul
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
        # self.actArea(temp)
        return temp

    def rotPDib(self, punto):
        """Para rotar un punto en el angulo self.ang. Esta funcion no
        necesita y no modifica el self.sinAngul y self.cosAngul"""
        temp = self.rotPunt(punto, self.ang)
        return temp

    def trasPunt(self, punto, puntotras):
        """Para trasladar el \"punto\" sumandole \"puntotras\""""
        return punto[0] + puntotras[0], punto[1] + puntotras[1]

    def trasPDib(self, punto):
        """Para trasladar con respecto al punto de localizacion del
        objeto"""
        # TODO: creo que no es correcto hacer la división entre 100 de
        # este lado.
        px = self.loc[0] / 100 + punto[0]
        py = self.loc[1] / 100 + punto[1]
        self.actArea((px, py))
        return (px, py)

    def acelerar(self, acel):
        """Para cambiar la aceleracion del objeto, la cantidad de posiciones que avanza,
        en el angulo del ovni."""
        px = int(self.vectord[0] + (acel * (self.cosAngul)))
        py = int(self.vectord[1] + (acel * (self.sinAngul)))
        self.vectord = px, py

    def rotar(self, angulo):
        """Rota el objeto la cantidad de radianes indicada por
        angulo."""

        # los valores del area se inicializan
        self.mxX = self.loc[0] / 100
        self.mnX = self.loc[0] / 100
        self.mxY = self.loc[1] / 100
        self.mnY = self.loc[1] / 100

        # sumo el angulo
        self.ang += angulo

        # hay que mantener el angulo entre 0 y 628 radianes
        if (self.ang > 628): self.ang = self.ang - 628
        elif (self.ang < 0): self.ang = self.ang + 628

        # como todos los puntos se rotan en el mismo angulo no vale la
        # pena sacar el seno y el coseno cada vez que es una operacion
        # que toma tiempo precioso del CPU
        anguloFl = self.ang / 100.0
        self.sinAngul = math.sin(anguloFl)
        self.cosAngul = math.cos(anguloFl)

        # TODO: verificar si esto se puede hacer en una sola pasada

        # hay que rotar todos los puntos del dibujo
        self.dibpuntos = list(map(self.rotSCPDib, self.puntos))

        # hay que trasladar los puntos del dibujo hacia loc
        self.dibpuntos = list(map(self.trasPDib, self.dibpuntos))

    def golpe(self):
        """En cada golpe de reloj se llama esta función en caso de que el
        objeto en cuestión tenga alguna cosa que hacer puede sobrescribir esta
        función. Esta función podría avanzar un objeto o hacer alguna verificación."""

        limites = self.miespacio.tamano

        # los valores del area se inicializan
        self.mxX = self.loc[0] / 100
        self.mnX = self.loc[0] / 100
        self.mxY = self.loc[1] / 100
        self.mnY = self.loc[1] / 100

        # traslado el punto de la localizacion
        self.loc = self.trasPunt(self.loc, self.vectord)

        # si la localizacion esta fuera de los limites
        # hay que introducirla por el otro extremo
        if (self.loc[0] < 0): self.loc = (limites[0] * 100), self.loc[1]
        elif (self.loc[0] > (limites[0] * 100)): self.loc = 0, self.loc[1]

        if (self.loc[1] < 0): self.loc = self.loc[0], limites[1] * 100
        elif (self.loc[1] > (limites[1] * 100)): self.loc = self.loc[0], 0

        # como todos los puntos se rotan en el mismo angulo no vale la
        # pena sacar el seno y el coseno cada vez que es una operacion
        # que toma tiempo precioso del CPU
        anguloFl = self.ang / 100.0
        self.sinAngul = math.sin(anguloFl)
        self.cosAngul = math.cos(anguloFl)

        # TODO: verificar si esto se puede hacer en una sola pasada

        # se necesita rotar los puntos del dibujo
        self.dibpuntos = list(map(self.rotSCPDib, self.puntos))
        # se necesita trasladar los puntos del dibujo
        self.dibpuntos = list(map(self.trasPDib, self.dibpuntos))

        # Reafirmar el color de depuración
        self.colordep = (0, 0, 255)

    def colision(self, ovnicol):
        pass

    def explotar(self, bala, objetos):
        """Cuando el objeto con masa explota tiene que dividirse en diferentes
        partes con tamano mas pequeno"""
        # TODO: implementar
        pass

    def __repr__(self):
        """La representación de este ovni."""
        return f"<Ovni loc={self.loc} ang={self.ang}>"

class Omasa(Ovni):
    """Representa los objetos con masa, que reaccionan a las balas."""
    def __init__(self, loc, ang, vectord, colorApl, masa):
        Ovni.__init__(self, loc, ang, vectord, colorApl)
        self.masa = masa

    def colision(self, ovnicol):
        """Cuando se produce una colisión el espacio llama esta función para
        que el ovni en cuestión tome la acción que corresponda. ovnicol es el
        objeto con el que se produjo la colisión."""
        # Si hubo una colisión cambiale el color de depuración.
        self.colordep = (0, 255, 0)

    def __repr__(self):
        """La representación de este ovni con masa."""
        return f"<Omasa loc={self.loc} ang={self.ang}>"

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
        return f"<Bala loc={self.loc} ang={self.ang}>"


class Nave(Omasa):
    """Cada instancia representa una nave"""
    def __init__(self, loc, ang, vectord, colorApl):
        Omasa.__init__(self, loc, ang, vectord, colorApl, 5)
        self.puntos = [(13, 0), (10, 0), (0, 0), (-3, -5), (-3, 5)]
        self.lineas = [(1, 3), (1, 4), (2, 3), (2, 4)]
        self.rotar(0)

    def disparar(self):
        """Hay que poner una bala nueva en la lista de balas"""
        angulo = self.ang + random.randrange(-10,10)
        self.miespacio.agregar(
            Bala((self.dibpuntos[0][0] * 100, self.dibpuntos[0][1] * 100)
                 , angulo, self.vectord, self.color, (0, 0 , 200), 50, 360))

    def __repr__(self):
        """La representación de esta Nave."""
        return f"<Nave loc={self.loc} ang={self.ang}>"


class Meteoro(Omasa):
    def __init__(self, loc, ang, vectord, colorApl, masa, vel, vrot):
        Omasa.__init__(self, loc, ang, vectord, colorApl, masa)
        self.vrot = vrot
        # los puntos del meteoro se generan al azar
        self.puntos = []
        cantp = random.randrange(10, 20)
        fact = 628.0 / cantp
        for cont in range(cantp):
            magnitudaz = self.masa + random.randrange(-10, 10)
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
        return f"<Meteoro loc={self.loc} ang={self.ang}>"
