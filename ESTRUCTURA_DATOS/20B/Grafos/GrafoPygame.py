# coding=utf-8
#######################################################################################################
#######################################################################################################
# Program Name: GrafoPyGame.py
# Authors: Melquizedec Moo Medina
# Description:  Muestra los grafos en forma gráfica!
# Date: 25/oct/2020
#######################################################################################################
#######################################################################################################
from Grafos import *
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
fuente=pygame.font.Font(None,40)

grafos=Grafos()
vectores=[]
lugares=[]
for i in range(0,3):
    x = int(input("Escribe la posicion X del vector: "))
    y = int(input("Escribe la posicion Y  del vector:"))
    lugar=input("indica el lugar: ")
    lugares.append(lugar)
    vector=(x,y)
    vectores.append(vector)
    vector=(vector,lugar)
    grafos.agregarVector(vector)

for i in range(0,2):
    grafos.relacionar(vectores[i],vectores[i+1])

#grafos.recorrer(vectores[0],pantalla)


grafos.mostrarVectores()

juego = True
while juego:
    ##detectar que presionaste alguna tecla o boton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego = False
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                x = int(input("Escribe la posicion X del vector: "))
                y = int(input("Escribe la posicion Y  del vector:"))
                lugar = input("indica el lugar: ")
                lugares.append(lugar)
                vector = (x, y)
                vectores.append(vector)
                vector = (vector, lugar)
                grafos.agregarVector(vector)
            if event.key==pygame.K_0:
                grafos.recorrer(vectores[0], pantalla)

    pygame.draw.polygon(pantalla,verde,(vectores),10)
    for i in range(0, len(vectores)):
        pygame.draw.circle(pantalla,amarillo,(vectores[i]),20)
        pantalla.blit(fuente.render(lugares[i], 1, blanco), vectores[i])














    pygame.display.update()
    clock.tick(2)

pygame.quit()