from Vehiculo import *
import pygame

#1. iniciar la libreria
pygame.init()
#2. configurar Pantalla
size=(1024,780)
ventana=pygame.display.set_mode(size)

#3. Configurar el Reloj
reloj=pygame.time.Clock()

####configurar colores#####
#R (Red) G (Green) B (Blue)
# 0-255     0-255    0-255
negro=(0,0,0)
rojo=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
morado=(200,0,200)
blanco=(255,255,255)
#######################

##crear el Objeto de Vehiculo
autoClarissa=Vehiculo("CHEVROLET","AVEO","AZUL", True)

###AREA DE BOTONES
imgBoton2=pygame.image.load("img/boton2.png")
imgBoton3=pygame.image.load("img/boton3.png")


#4. INICIALIZO EL CICLO DEL JUEGO
juego=True
while juego:
    ##CAPTURA DE EVENTOS
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            juego=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                autoClarissa.avanzar()
            if event.key==pygame.K_LEFT:
                autoClarissa.detener()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if 100<=event.pos[0]<=250 and 100<=event.pos[1]<=150:
               autoClarissa.avanzar()

            if 300<=event.pos[0]<=450 and 100<=event.pos[1]<=150:
                autoClarissa.apagar()

        if event.type== pygame.JOYBUTTONDOWN:
            pass


    ventana.fill(verde)
    ventana.blit(autoClarissa.imagen,(50,300))

    ventana.blit(imgBoton2, (100,100) )
    ventana.blit(imgBoton3, (300,100))


    #5. actualiza ventana
    pygame.display.update()
    #6. asigna el tiempo al reloj
    reloj.tick(10)

#7. salir
pygame.quit()












