#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Este es el archivo principal de mi version del antiguo y poderoso Asteroids
# Espero que lo disfruten

# cargando los modulos necesarios
import sys, pygame, math, random
# estos son modulos propios
from movni import *
from texto import *

def partida(screen, tamano, fondo, mapa):
    """Controla las partidas, el programa entra en esta funcion cuando
    el usuario elige jugar una partida nueva, y no sale hasta que el
    usuario pierde todas las naves."""

    # inicializando el reloj
    reloj = pygame.time.Clock()

    espacio = Espacio(screen, tamano, fondo)
    espacio.depuracion = True
    vidas = 3
    poder = "Escudo"
    limitePoder = 30
    contPoder = 0
    meteoros = []
    navejug = None
    contNivel = 1
    estado = "nivel"
    limiteEstado = 20
    contEstado = 0

    intblqfg = 3 # cuando se dispara una rafaga de balas la cantidad de
                 # cuadros entre una bala y la otra

    fuegoblq = 0 # el contador de los cuadros para una rafaga de balas

    # la nave del jugador
    navejug = Nave(((tamano[0] / 2 * 100), (tamano[1] / 2 * 100)), 471, (0, 0), colorA)
    espacio.agregar(navejug)

    # armando los meteoros
    for cont in range(random.randrange(3, 5)):
        espacio.agregar(Meteoro(
            (random.randrange(tamano[0] * 100), random.randrange(tamano[1] * 100)),
            0,
            (random.randrange(-30, 30), random.randrange(-30, 30)),
            colorB,
            random.randrange(50, 120),
            random.randrange(30),
            random.randrange(-10, 10)))

    # este es el bucle principal del juego y va a correr mientras el
    # usuario no presione <ESC> para salir al menu principal
    while True:

        # manejando los estados del juego
        if estado == "juego":
            # que verifique los cambios de estados
            # print("jugando estado comun")
            estado = "juego"

            # si se acaban los meteoros hay que cambiar el nivel

            # si algo golpea la nave hay muerte

        elif estado == "inicio":
            print("inicio de vida o partida")

            estado = "juego"
        elif estado == "nivel":
            print("cambio de nivel")

            estado = "inicio"
        elif estado == "muerte":
            print("se destruyo una nave")

            # si le quedan vidas puede seguir jugando
            if vidas >= 0:
                estado = "inicio"
            else:
                estado = "gameover"
        elif estado == "gameover":
            print("se acabaron las vidas")

            # si el usuario tiene un record sobresaliente que le pregunte sus
            # iniciales para ponerlo en la lista de records.

            estado = "record"
        elif estado == "record":
            print("guardando un record")

        # revisando la cola de eventos
        for event in pygame.event.get():
            # si me piden que cierre, cierro
            if event.type == pygame.QUIT:
                sys.exit(0)

        # revisando las teclas, que haga lo que haya que hacer
        presionados = pygame.key.get_pressed()

        if presionados[mapa["arriba"]]:
            # print("arriba")
            navejug.acelerar(-30)

        if presionados[mapa["abajo"]]:
            # print("abajo")
            navejug.acelerar(30)

        if presionados[mapa["izquierda"]]:
            # print("izquierda")
            navejug.rotar(-20)

        if presionados[mapa["derecha"]]:
            # print("derecha")
            navejug.rotar(20)

        if (presionados[mapa["fuego"]] and (fuegoblq == 0)):
            # print("fuego")
            navejug.disparar()
            fuegoblq = intblqfg
        elif (fuegoblq > 0):
            fuegoblq -= 1

        if presionados[mapa["poder"]]:
            print("poder")
            # empieza el contador de poder
            # se usa el poder

        if presionados[mapa["salir"]]:
            break

        # el espacio que haga su parte
        espacio.golpe()

        # que actualice el texto de la pantalla

        # que espere un tiempito
        reloj.tick(30)

        # actualizando la pantalla
        pygame.display.flip()

def configuracion(fnd):
    """Cuando el usuario necesita modificar las opciones"""

    opciones = ["arriba", "abajo", "izquierda", "derecha", "fuego",
                "poder", "salir", "vidas", "escudos", "nivel", "regresar"]
    menu = Menu((10000,10000),opciones, colorA, colorC, fnd)
    eleccion = menu.mostrar()

    pass

def fama(fnd):
    """Cuando el usuario quiere ver los records de los juegos
    anteriores"""
    pass

def creditos(fnd):
    """Muestra los creditos del jueguillo :P"""
    pass

# main - esto es el motor del jueguillo

# inicializaciones
pygame.init()

# se puede poner en pantalla completa??

# pygame.display.toggle_fullscreen()
# pygame.display.set_mode((640,480), pygame.FULLSCREEN | pygame.DOUBLEBUF, 24)

# pygame.font.init()

#variables a usar
size = 640, 480 # tamano de la pantalla
screen = pygame.display.set_mode(size)
pygame.display.set_caption("xteroids")
colorA = 0, 200, 0
colorB = 200, 0, 0
colorC = 0, 0 , 200
colfondo = 0,0,0
pta = 0, 0
ptb = 0, 0
poder = "Escudo"
objetos = [] # La lista con todos los objetos
             # que se encuentran en la pantalla actualmente
balas = [] # La lista de las balas
dispositivo = "teclado"
mapa = {"arriba": pygame.K_UP,
        "abajo": pygame.K_DOWN,      # las teclas a usar
        "izquierda": pygame.K_LEFT,  # para el juego
        "derecha": pygame.K_RIGHT,
        "fuego": pygame.K_SPACE,
        "poder": pygame.K_TAB,
        "salir": pygame.K_ESCAPE}
fontusada = pygame.font.SysFont("Comic_Sans_MS.ttf", 20)
pygame.key.set_repeat(250, 50)

# TODO: cargar la configuracion de los controles y los puntajes

# va a haber una configuracion por defecto y si no se pueden cargar
# las configuraciones se cargan los puntajes vacios y las
# configuraciones por defecto. Cuando se cambien las configuraciones o
# halla un nuevo puntaje se escribe el archivo de configuraciones y se
# sustituye el anterior con los nuevos valores.

# Fondo inicial
fondo = Espacio(screen, size, colfondo)
fondo.depuracion = True

# poniendo los objetos que van en el fondo.

# armando los meteoros
for cont in range(random.randrange(3, 5)):
    fondo.agregar(Meteoro(
        (random.randrange(size[0] * 100), random.randrange(size[1] * 100)),
        0,
        (random.randrange(-30, 30), random.randrange(-30,30)),
        colorB,
        random.randrange(50, 120),
        random.randrange(30),
        random.randrange(-10, 10)))

while True:
    # se muestra el titulo
    titulo = Texto("Xteroids", 5, (10000,5000),0,(0,0), colorA)
    fondo.agregar(titulo)
    credito = Texto("por Pablo Mercader Alcantara",2, (10000,46000),0,(0,0), colorA)
    fondo.agregar(credito)

    # Se muestra el menu principal donde hay cuatro opciones
    # jugar, controles, salon fama, creditos y salir.

    opciones = ["jugar", "configuracion", "fama", "creditos", "salir"]
    menu = Menu((10000,10000), opciones, colorA, colorC, fondo)
    eleccion = menu.mostrar()

    # si elige jugar una partida
    if (eleccion == 0):
        partida(screen, size, colfondo, mapa)

    # si elige modificar las opciones
    elif (eleccion == 1):
        configuracion(fondo)

    # si elige ver el salon de la fama
    elif (eleccion == 2):
        fama(fondo)

    # si se elige ver los creditos
    elif (eleccion == 3):
        creditos(fondo)

    # la quinta opcion es salir
    elif (eleccion == 4) or (eleccion == -1):
        # que lance un mensajito bonito y salga
        print("Gracias por jugar Xteroids!!")
        break

# fin

# soltando recursos
pygame.font.quit()
