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
from Vehiculo import *

# iniciamos la libreria pygame
pygame.init()

# configuramos pantalla
ventana=pygame.display.set_mode((1024, 780))

# configuramos el reloj
clock = pygame.time.Clock()

####### CONFIGURACION DE COLORES####
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)
blanco = (255, 255, 255)
negro = (0, 0, 0)
autoEvelyn=Vehiculo("CHEVROLET")


juego = True
while juego:
    ##detectar que presionaste alguna tecla o boton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                autoEvelyn.avanzar()


    ventana.blit(autoEvelyn.imagen,(0,0))

    pygame.display.update()
    clock.tick(30)

pygame.quit()