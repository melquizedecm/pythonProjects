# coding=utf-8
#######################################################################################################
#######################################################################################################
# Program Name: BaseJuego.py
# Authors: Melquizedec Moo Medina
# Description:  Código Base para iniciar un juego o animacion en python
# Date: 25/oct/2020
#######################################################################################################
#######################################################################################################

import pygame
from Mascota import *

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

#####
mascota1= Mascota("beige","labrador")



juego = True
while juego:
    ##detectar que presionaste alguna tecla o boton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego = False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                mascota1.jugar()

            if event.key== pygame.K_2:
                mascota1.ladrar()

            if event.key==pygame.K_0:
                mascota1.aquietar()

    pantalla.fill(blanco)
    pantalla.blit(mascota1.imagen,(200,50))

    pygame.display.update()
    clock.tick()

pygame.quit()