# coding=utf-8
#######################################################################################################
#######################################################################################################
# Program Name: BaseJuego.py
# Authors: Melquizedec Moo Medina
# Description:  Código Base para iniciar un juego o animacion en python
# Date: 25/oct/2020
#######################################################################################################
#######################################################################################################
from Jugador import *
import pygame

# iniciamos la libreria pygame
pygame.init()

# configuramos pantalla
pantalla=pygame.display.set_mode((800, 600))

# configuramos el reloj
clock = pygame.time.Clock()

####### CONFIGURACION DE COLORES####
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)
blanco = (255, 255, 255)
negro = (0, 0, 0)

########CONFIGURAR FUENTES#######
fuente = pygame.font.Font(None, 60)

#####CREAMOS EL OBJETO DEL PERSONAJE######
posicion=(50,450)
lizi=Jugador(posicion)
fondoInicio=pygame.image.load("img/Inicio.jpg")
fondoJuego=pygame.image.load("assets/png/BG/BG.png")
fondoJuegoRect=pygame.Rect(600,0,200,600)
fondoPosicionX=0
fondoFinal=pygame.image.load("img/Final.jpg")

##declaración de objetos##
nieve=pygame.image.load("assets/png/Object/SnowMan.png")
nieveX,nieveY=300,400
nieveRect=pygame.Rect(355,400,100,200)
colision=0

ventanaJuego=True
pantallaInicio=True
while ventanaJuego:

    while pantallaInicio:
        ##detectar que presionaste alguna tecla o boton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    pantallaInicio=False
                    pantallaJuego=True


        lizi.controles(event)
        pantalla.fill(rojo)
        pantalla.blit(fondoInicio, (0,0))

        pygame.display.update()
        clock.tick(10)

    while pantallaJuego:
        ##detectar que presionaste alguna tecla o boton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pantallaJuego = False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_0:
                    pantallaJuego=False
                    pantallaFinal=True

        lizi.controles(event)
        pantalla.fill(blanco)
        pantalla.blit(fondoJuego, (fondoPosicionX,-200) )

        ####mover el fondo de la pantalla
        if fondoJuegoRect.colliderect(lizi):
            fondoPosicionX-=5
            lizi.rect.x-=5

        ###colocar Objetos sobre la plataforma
        pantalla.blit(nieve,(nieveX,nieveY))



        ##colision sobre objetos
        if nieveRect.colliderect(lizi):
            lizi.rect.x-=5
            colision=1
        else:
            colision=0

        if colision==0:
            lizi.rect.y=450






        pantalla.blit(lizi.image, lizi.rect)
        texto= fuente.render(str(lizi.recorrido),1,azul)
        pantalla.blit(texto,(700,20))

        pygame.display.update()
        clock.tick(10)

    while pantallaFinal:##detectar que presionaste alguna tecla o boton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pantallaFinal = False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pantallaFinal=False
                    pantallaInicio=True


        lizi.controles(event)
        pantalla.fill(verde)
        pantalla.blit(fondoFinal, (0,0))
        pygame.display.update()
        clock.tick(10)


pygame.quit()