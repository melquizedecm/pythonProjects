# coding=utf-8
#######################################################################################################
#######################################################################################################
# Program Name: mainGelatina.py
# Authors: Melquizedec Moo Medina
# Description:  Código Base para presentar el objeto Gelatina
# Date: 30/oct/2021
#######################################################################################################
#######################################################################################################

import pygame
from Gelatina import *

# iniciamos la libreria pygame
pygame.init()

# configuramos pantalla
pantalla = pygame.display.set_mode((800, 600))

# configuramos el reloj
clock = pygame.time.Clock()

####### CONFIGURACION DE COLORES####
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)
blanco = (255, 255, 255)
negro = (0, 0, 0)

gelatina1=Gelatina("diet","blanco")

juego = True
while juego:
    ##detectar que presionaste alguna tecla o boton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                gelatina1.setColor("naranja")
            if event.key==pygame.K_0:
                gelatina1.derretir()

    pantalla.fill(blanco)
    pantalla.blit(gelatina1.imagen,(200,0))

    pygame.display.update()
    clock.tick()

pygame.quit()