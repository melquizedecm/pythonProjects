from Vehiculo import *
import pygame

#1. iniciar el pygame
pygame.init()

#2. configurar la pantalla
size=(1024,780)
ventana=pygame.display.set_mode(size)

#3. configurar el reloj
reloj=pygame.time.Clock()

#4. configurar colores
#  RED   GREEN    BLUE
rojo=(255,0,0)
azul=(0,0,255)
verde=(0,255,0)
morado=(128,0,128)

autoFrida=Vehiculo("FERRARI","GRAND","AZUL",True)

imgChofer=pygame.image.load("img/choferFuera.png")
#####BOTONES###
imgBoton2=pygame.image.load("img/boton2.png")
imgBoton3=pygame.image.load("img/boton3.png")


#####AREA DE DESPLIEGUE######
juego=True
while juego:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                autoFrida.avanzar()
            if event.key==pygame.K_LEFT:
                autoFrida.detener()
            if event.key==pygame.K_DOWN:
                autoFrida.apagar()
            if event.key==pygame.K_UP:
                autoFrida.encender()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if 100<=event.pos[0]<=250 and 500<=event.pos[1]<=550:
                autoFrida.avanzar()




    ventana.fill(morado)

    ventana.blit(autoFrida.imagen, (0,0))

    ###Despliegue Botones
    ventana.blit(imgBoton2,(100,500))


    # 5. mostrar la pantalla
    pygame.display.update()
    reloj.tick(20)


