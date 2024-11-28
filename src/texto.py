# -*- coding: utf-8 -*-

# Este modulo es para manejar el texto del jueguillo y algunas otras
# partes relacionadas con el texto, el menu, los caracteres, etc...

import pygame
import sys

from movni import *

# Este es el cuadro dentro del que se definen los caracteres.

#  -2    0   +2
#   +--------+ -4
#   |        |
#   |________|_-2
#   |        |
#   |________|_ 0
#   |        |
#   |________|_+2
#   |        |
#   |        |
#   +--------+ +4

caracteres = {
    " ":([],[]),
    "?":([(-2,-3),(0,-4),(2,-3),(0,-1),(0,0),(0,1),(0,2)],[(0,1),(1,2),(2,3),(3,4),(5,6)]),
    "!":([(0,-4),(0,0),(0,1),(0,2)],[(0,1),(2,3)]),
    "*":([(0,-2),(0,2),(-2,-1),(2,1),(2,-1),(-2,1)],[(0,1),(2,3),(4,5)]),
    "<":([(2,-2),(-2,0),(2,2)],[(0,1),(1,2)]),
    ">":([(-2,-2),(2,0),(-2,2)],[(0,1),(1,2)]),
    "+":([(0,-2),(0,2),(-2,0),(2,0)],[(0,1),(2,3)]),
    "-":([(-2,0),(2,0)],[(0,1)]),
    "=":([(-2,-1),(2,-1),(-2,1),(2,1)],[(0,1),(2,3)]),
    ".":([(0,1),(0,2)],[(0,1)]),
    ",":([(0,1),(-1,2)],[(0,1)]),
    ":":([(0,-2),(0,-1),(0,1),(0,2)],[(0,1),(2,3)]),
    ";":([(0,-2),(0,-1),(0,1),(-1,2)],[(0,1),(2,3)]),
    "|":([(0,-3),(0,3)],[(0,1)]),
    "0":([(2,-4),(-2,-4),(-2,2),(2,2)],[(0,1),(1,2),(2,3),(3,0),(0,2)]),
    "1":([(0,-4),(0,2),(-2,-3)],[(0,1),(0,2)]),
    "2":([(-2,-4),(2,-4),(2,-2),(-2,2),(2,2)],[(0,1),(1,2),(2,3),(3,4)]),
    "3":([(-2,-4),(2,-4),(2,2),(-2,2),(-1,-1),(2,-1)],[(0,1),(1,2),(2,3),(4,5)]),
    "4":([(2,2),(2,-4),(-2,-1),(2,-1)],[(0,1),(1,2),(2,3)]),
    "5":([(2,-4),(-2,-4),(-2,-1),(2,-1),(2,1),(-2,2)],[(0,1),(1,2),(2,3),(3,4),(4,5)]),
    "6":([(2,-4),(-2,-4),(-2,2),(2,2),(2,-1),(-2,-1)],[(0,1),(1,2),(2,3),(3,4),(4,5)]),
    "7":([(-2,-4),(2,-4),(0,2)],[(0,1),(1,2)]),
    "8":([(2,-4),(-2,-4),(-2,2),(2,2),(2,-1),(-2,-1)],[(0,1),(1,2),(2,3),(3,4),(4,5),(4,0)]),
    "9":([(2,-4),(-2,-4),(-2,2),(2,2),(2,-1),(-2,-1)],[(2,3),(3,0),(0,1),(1,5),(5,4)]),
    "a":([(-2,-2),(2,-2),(2,2),(-2,2),(-2,0),(2,0)],[(0,1),(1,2),(2,3),(3,4),(4,5)]),
    "b":([(-2,-4),(-2,2),(2,2),(2,-2),(-2,-2)],[(0,1),(1,2),(2,3),(3,4)]),
    "c":([(2,-2),(-2,-2),(-2,2),(2,2)],[(0,1),(1,2),(2,3)]),
    "d":([(2,-2),(-2,-2),(-2,2),(2,2),(2,-4)],[(0,1),(1,2),(2,3),(3,4)]),
    "e":([(-2,0),(2,0),(2,-2),(-2,-2),(-2,2),(2,2)],[(0,1),(1,2),(2,3),(3,4),(4,5)]),
    "f":([(2,-4),(0,-4),(0,2),(2,-2),(-2,-2)],[(0,1),(1,2),(3,4)]),
    "g":([(-2,4),(2,4),(2,-2),(-2,-2),(-2,2),(2,2)],[(0,1),(1,2),(2,3),(3,4),(4,5)]),
    "h":([(-2,-4),(-2,2),(-2,-2),(2,-2),(2,2)],[(0,1),(2,3),(3,4)]),
    "i":([(0,-2),(0,2),(0,-4),(0,-3)],[(0,1),(2,3)]),
    "j":([(0,-2),(0,4),(-2,4),(0,-4),(0,-3)],[(0,1),(1,2),(3,4)]),
    "k":([(-2,-4),(-2,2),(2,-2),(-2,0),(2,2)],[(0,1),(2,3),(4,3)]),
    "l":([(0,-4),(0,2),(2,2)],[(0,1),(1,2)]),
    "m":([(-2,2),(-2,-2),(2,-2),(2,2),(0,-2),(0,2)],[(0,1),(1,2),(2,3),(4,5)]),
    "n":([(-2,2),(-2,-2),(2,-2),(2,2)],[(0,1),(1,2),(2,3)]),
    "o":([(2,-2),(-2,-2),(-2,2),(2,2)],[(0,1),(1,2),(2,3),(3,0)]),
    "p":([(-2,4),(-2,-2),(2,-2),(2,2),(-2,2)],[(0,1),(1,2),(2,3),(3,4)]),
    "q":([(2,2),(-2,2),(-2,-2),(2,-2),(2,4)],[(0,1),(1,2),(2,3),(3,4)]),
    "r":([(0,-2),(0,2),(2,-2),(0,-1)],[(0,1),(2,3)]),
    "s":([(-2,-2),(2,-2),(-2,0),(2,0),(-2,2),(2,2)],[(1,0),(0,2),(2,3),(3,5),(5,4)]),
    "t":([(0,-4),(0,2),(2,2),(-2,-2),(2,-2)],[(0,1),(1,2),(3,4)]),
    "u":([(-2,-2),(-2,2),(2,2),(2,-2)],[(0,1),(1,2),(2,3)]),
    "v":([(-2,-2),(0,2),(2,-2)],[(0,1),(1,2)]),
    "x":([(-2,-2),(2,2),(2,-2),(-2,2)],[(0,1),(2,3)]),
    "y":([(-2,-2),(0,2),(2,-2),(-2,4)],[(0,1),(2,3)]),
    "z":([(-2,-2),(2,-2),(-2,2),(2,2)],[(0,1),(1,2),(2,3)]),
    "A":([(-2,2),(0,-4),(2,2),(-1,-1),(1,-1)],[(0,1),(1,2),(3,4)]),
    "B":([(-2,-4),(2,-3),(1,-1),(-2,-1),(2,1),(-2,2)],[(0,1),(1,2),(2,3),(2,4),(4,5),(5,0)]),
    "C":([(2,-4),(-2,-4),(-2,2),(2,2)],[(0,1),(1,2),(2,3)]),
    "D":([(-2,-4),(0,-4),(2,-1),(0,2),(-2,2)],[(0,1),(1,2),(2,3),(3,4),(4,0)]),
    "E":([(2,-4),(-2,-4),(-2,2),(2,2),(2,-1),(-2,-1)],[(0,1),(1,2),(2,3),(4,5)]),
    "F":([(2,-4),(-2,-4),(-2,2),(2,-1),(-2,-1)],[(0,1),(1,2),(3,4)]),
    "G":([(2,-4),(-2,-4),(-2,2),(2,2),(2,-1),(0,-1)],[(0,1),(1,2),(2,3),(3,4),(4,5)]),
    "H":([(-2,-4),(-2,2),(2,-4),(2,2),(2,-1),(-2,-1)],[(0,1),(2,3),(4,5)]),
    "I":([(0,-4),(0,2),(1,-4),(-1,-4),(1,2),(-1,2)],[(0,1),(2,3),(4,5)]),
    "J":([(2,-4),(2,2),(-2,2),(-2,1)],[(0,1),(1,2),(2,3)]),
    "K":([(-2,-4),(-2,2),(2,-4),(-2,-1),(2,2)],[(0,1),(2,3),(4,3)]),
    "L":([(-2,-4),(-2,2),(2,2)],[(0,1),(1,2)]),
    "M":([(2,2),(2,-4),(0,-1),(-2,-4),(-2,2)],[(0,1),(1,2),(2,3),(3,4)]),
    "N":([(-2,2),(-2,-4),(2,2),(2,-4)],[(0,1),(1,2),(2,3)]),
    "O":([(2,-4),(-2,-4),(-2,2),(2,2)],[(0,1),(1,2),(2,3),(3,0)]),
    "P":([(-2,2),(-2,-4),(2,-4),(2,-1),(-2,-1)],[(0,1),(1,2),(2,3),(3,4)]),
    "Q":([(2,-4),(-2,-4),(-2,2),(2,2),(0,1),(2,3)],[(0,1),(1,2),(2,3),(3,0),(4,5)]),
    "R":([(-2,2),(-2,-4),(2,-4),(2,-1),(-2,-1),(1,-1),(2,2)],[(0,1),(1,2),(2,3),(3,4),(5,6)]),
    "S":([(2,-4),(-2,-4),(-2,-1),(2,-1),(2,2),(-2,2)],[(0,1),(1,2),(2,3),(3,4),(4,5)]),
    "T":([(2,-4),(-2,-4),(0,-4),(0,2)],[(0,1),(2,3)]),
    "U":([(2,-4),(-2,-4),(-2,2),(2,2)],[(1,2),(2,3),(3,0)]),
    "V":([(-2,-4),(0,2),(2,-4)],[(0,1),(1,2)]),
    "X":[[(-2,-4),(2,2),(2,-4),(-2,2)],[(0,1),(2,3)]],
    "Y":([(-2,-4),(0,-1),(2,-4),(0,2)],[(0,1),(1,2),(1,3)]),
    "Z":([(-2,-4),(2,-4),(-2,2),(2,2)],[(0,1),(1,2),(2,3)]),
    }

class Caracter(Ovni):
    """Esta es una clase para representar un caracter

    Este objeto Caracter puede moverse en la pantalla igual que los
    demas objetos pero ademas tiene una particularidad que es que
    tiene una escala.
    """
    def __init__(self, car, escala, loc, ang, vectord, color):
        """El constructor de los caracteres"""

        # los caracteres son Ovnis
        Ovni.__init__(self, loc, ang, vectord, color)
        self.car = car
        self.escala = escala

class Texto(Ovni):
    """Esta es una clase que usa la clase letra para
    representar un conjunto de caracteres en los que los"""

    def __init__(self, texto, escala, loc, ang, vectord, color):
        """El constructor que inicializa el texto"""

        # el texto tambien es un Ovni
        Ovni.__init__(self, loc, ang, vectord, color)
        self.texto = texto
        self.escala = escala

        indp = 0
        contx = 0
        conty = 0
        self.puntos = []
        self.lineas = []
        # poniendo los puntos y las lineas de cada caracter
        for car in self.texto:
            if car == "\n":
                contx = 0
                conty += 6 * self.escala
                continue
            for punto in caracteres[car][0]:
                punto = (punto[X] * self.escala, punto[Y] * self.escala)
                self.puntos += [(punto[X] + contx, punto[Y] + conty)]
            for linea in caracteres[car][1]:
                self.lineas += [(linea[0] + indp, linea[1] + indp)]
            indp += len(caracteres[car][0])
            contx += 6 * self.escala

        #print("creando Texto, estos son los puntos", self.puntos)
        #print("creando Texto, estas son las lineas", self.lineas)

class Menu:
    def __init__(self, loc, opciones, colorS, colorN, fondo):
        self.loc = loc
        self.opciones = opciones
        self.colorS = colorS
        self.colorN = colorN
        self.fondo = fondo
        # cantidad de cuadros que se va a esperar para leer el teclado
        self.cuadEspTec = 2

    def mostrar(self, opcion = 0):
        """Mueve el fondo, mientras maneja el menu. Cuando el usuario
        elige una opcion la funcion retorna con el indice de la
        opcion. Si el usuario presiona <ESC> retorna -1 indicando que
        no selecciono ninguna de las opciones. """

        # inicializando el reloj
        reloj = pygame.time.Clock()
        # inicializando el contador de opciones
        if (opcion >= len(self.opciones)) or (opcion < 0):
            opcion = 0
        # inicializando el contador de cuadros
        contCuadr = 0

        # la opcion que selecciono el usuario
        seleccion = -2

        # agregando las opciones
        tOpciones = []
        tpOpciones = []
        i = 0
        while i < len(self.opciones):
            temp = Texto(self.opciones[i], 3
                    , (self.loc[X], self.loc[Y] + (i * 3000))
                    , 0, (0,0), self.colorN)
            tpOpciones.append(self.fondo.agregar(temp))
            tOpciones.append(temp)
            i += 1

        tOpciones[opcion].color = self.colorS

        while seleccion == -2:
            # revisando la cola de eventos
            for event in pygame.event.get():
                # si me piden que cierre, cierro
                if event.type == pygame.QUIT:
                    seleccion = -1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # pongo la opcion actual en el color normal
                        tOpciones[opcion].color = self.colorN
                        # moviendo el menu teniendo en cuenta los limites
                        if opcion == 0:
                            opcion = len(self.opciones) - 1
                        else:
                            opcion -= 1
                        # poniendo el color seleccionado en la nueva opcion
                        tOpciones[opcion].color = self.colorS

                    elif event.key == pygame.K_DOWN:
                        # pongo la opcion actual en el color normal
                        tOpciones[opcion].color = self.colorN
                        # moviendo el menu teniendo en cuenta los limites
                        if opcion == (len(self.opciones) - 1):
                            opcion = 0
                        else:
                            opcion += 1
                        # poniendo el color seleccionado en la nueva opcion
                        tOpciones[opcion].color = self.colorS
                    elif event.key == pygame.K_RETURN:
                        seleccion = opcion
                    elif event.key == pygame.K_ESCAPE:
                        seleccion = -1

            # el fondo que haga su parte
            self.fondo.golpe()

            # que espere un tiempito
            reloj.tick(30)

            # actualizando la pantalla
            pygame.display.flip()

        # cuando se cierra el menu

        # hay que quitar las opciones del espacio
        for opt in range(len(tpOpciones) - 1,-1,-1):
            self.fondo.quitar(tOpciones[opt])

        # la opcion que estaba seleccionada es la que se eligio
        return seleccion


# class Cantidad:


# class Opcion:


# class Input:



