# coding=utf-8
#######################################################################################################
#######################################################################################################
# Program Name: BaseJuego.py
# Authors: Melquizedec Moo Medina
# Description:  Código Base para iniciar un juego o animacion en python
# Date: 25/oct/2019
#######################################################################################################
#######################################################################################################

import pygame

#iniciamos la libreria pygame
pygame.init()

#configuramos pantalla
screen=pygame.display.set_mode((800,600))

#configuramos el reloj
clock=pygame.time.Clock()

####### CONFIGURACION DE COLORES####ss
rojo=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
amarillo=(255,255,0)
blanco=(255,255,255)
negro=(0,0,0)

x=400
y=300
velocidadx=10
velocidady=3

####control del rectangulo1###
rectX=0
rectY=300

rectX2=780
rectY2=300


fondo=pygame.image.load("fondo.jpg")
pygame.mixer_music.load("sonido_golpe.mp3")



juego=True
while juego:
    ##detectar que presionaste alguna tecla o boton
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            juego=False
        ##control del rectangulo1
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                rectY=rectY-40
            elif event.key==pygame.K_s:
                rectY=rectY+40
        ##control del rectangulo2
            elif event.key==pygame.K_DOWN: #flecha abajo
                rectY2=rectY2+40
            elif event.key==pygame.K_UP: #flecha arriba
                rectY2=rectY2-40


    #Borrar pantalla
    screen.blit(fondo,(0,0))

    #####CIRCULO AZUL#####
    pygame.draw.circle(screen,azul,(x,y),40)
    x=x+velocidadx
    y=y+velocidady



    #rebotar pantalla
    #if x>=760:
    #    velocidadx=velocidadx*-1
    if y>=560 or y<=40:
        velocidady=velocidady*-1
    ####### FIN CIRCULO AZUL#####


    #######BARRITAS DE COLISION########

    #### barra lateral izquierda #####
    rectangulo1=pygame.Rect(rectX,rectY,20,70)
    pygame.draw.rect(screen,verde,rectangulo1)

    #### barra lateral derecha ######
    rectangulo2=pygame.Rect(rectX2,rectY2,20,70)
    pygame.draw.rect(screen,rojo,rectangulo2)

    ####COLISION CUADRO IZQUIERDO#####
    if x-40>=rectX and x-40<=rectX+20 and y>=rectY and y<=rectY+70:
        velocidadx=velocidadx*-1
        pygame.mixer_music.play(1)
    if x-40<=0:
        juego=False

    #####COLISION CUADRO DERECHO
    if x+40 >= rectX2 and y >=rectY2 and y<=rectY2+70:
        velocidadx=velocidadx*-1
        pygame.mixer_music.play(1)
    if x+40>=800:
        juego=False



    pygame.display.update()
    clock.tick(30)
pygame.quit()