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

# iniciamos la libreria pygame
pygame.init()

# configuramos pantalla
pygame.display.set_mode((800, 600))

# configuramos el reloj
clock = pygame.time.Clock()

####### CONFIGURACION DE COLORES####
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)
blanco = (255, 255, 255)
negro = (0, 0, 0)

juego = True
while juego:
    ##detectar que presionaste alguna tecla o boton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego = False

    pygame.display.update()
    clock.tick()

pygame.quit()