from Jugador import *
from Animales import *
from records import *
import random
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
ventanaAbierta=True

##nieve
nieveX=[]
nieveY=[]
for i in range(0,100):
    nieveX.append(random.randrange(0,800))
    nieveY.append(random.randrange(0,600))

#######FUENTES DE MENSAJES########
fuentes=pygame.font.Font("LETRA.TTF",30)
fuente60=pygame.font.Font("LETRA.TTF",70)

#######CONFIGURACION DE MUSICA######
sonido_comer=pygame.mixer.Sound("efecto_comer.mp3")

ventanaJuego=True
while ventanaJuego:
    #######CONFIGURACIÓN DE INICIO DEL JUEGOO#######
    estadoJuego = "Jugando"
    ganador = False
    gameOver = False
    pantallaInicio = True

    ###### CREAMOS EL OBJETO DEL PERSONAJE ######
    posicion = (0, 385)
    lizi = Jugador(posicion)
    posicionP = (710, 420)
    keykito = Pinguino(posicionP)

    ###CONFIGURACIÓN DE FONDOS######
    fondo = pygame.image.load("img/Inicio.jpg")
    fondoInicio = pygame.image.load("assets/png/BG/fondo01.jpg")
    fondoJuego = pygame.image.load("assets/png/BG/BG.png")
    fondoX, fondoY = 0, -200
    fondoRect = pygame.Rect(600, 0, 200, 600)
    fondoFinal = pygame.image.load("assets/png/BG/final.jpg")

    #######CONFIGURACIÓN DE OBJETOS###
    piedra = pygame.image.load("assets/png/Object/Stone.png")
    piedraX, piedraY = 300, 415
    piedraRect = pygame.Rect(piedraX + 30, piedraY, 180, 100)

    pescado = pygame.image.load("img/pescado.png")
    pescadoX, pescadoY = 200, 450
    pescadoRect = pygame.Rect(pescadoX, pescadoY, 50, 40)
    pescadoOn = True

    ##igloo
    posiglooX = 1300
    igloo = pygame.image.load("assets/png/Object/igloo.png")
    iglooRect = pygame.Rect(posiglooX + 120, 280, 300, 300)

    ####### FIN DE CONFIGURACION DEL INICIO DEL JUEGO#######
    #MOSTRAR PANTALLA DE INICIO
    while pantallaInicio:
        ##detectar que presionaste alguna tecla o boton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pantallaInicio=False
                    pantallaJuego=True

        pantalla.fill(blanco)
        lizi.controles(event)
        pantalla.blit(fondoInicio, (0, 0))
        titulo=fuente60.render("WINTERSTORM",1,blanco)
        pantalla.blit(titulo,(50,300))
        pygame.display.update()
        clock.tick(15)

    record=0
    musica_fondo = pygame.mixer.music.load("musicaFondo1.mp3")
    pygame.mixer.music.play()
    # mostrar Pantalla de Juego
    while pantallaJuego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_0:
                    pantallaJuego=False
                    pantallaFinal=True
                    lizi=Jugador(posicion)

        ####DESPLEGAR EL FONDO DEL JUEGO####
        pantalla.fill(blanco)
        lizi.controles(event)
        pantalla.blit(fondoJuego,(fondoX,fondoY))
        mensajeRecord=fuentes.render("Score: "+str(record),1,blanco)
        pantalla.blit(mensajeRecord,(550,50))

        #####efecto de nieve####
        for i in range(0,100):
            tamanioNieve=random.randrange(2,4)
            pygame.draw.circle(pantalla,blanco,(nieveX[i],nieveY[i]),tamanioNieve)
            nieveY[i]+=8
            nieveX[i]-=2
            if nieveY[i]>=600:
                nieveY[i]=-5
            if nieveX[i]<=0:
                nieveX[i]=800

        #####COLISION CON EL FONDO DEL JUEGO#####
        if fondoRect.colliderect(lizi):
            lizi.rect.x-=5
            fondoX-=5
            piedraX-=5
            posiglooX-=5

        ####DESPLEGAR LOS OBJETOS#######
        pantalla.blit(piedra,(piedraX,piedraY))
        piedraRect = pygame.Rect(piedraX + 30, piedraY, 100, 50)
        pantalla.blit(igloo,(posiglooX,280))
        iglooRect = pygame.Rect(posiglooX + 120, 280, 300, 300)

        if pescadoOn:
            pantalla.blit(pescado,(pescadoX,pescadoY))
            pescadoRect=pygame.Rect(pescadoX,pescadoY,50,40)
            if pescadoRect.colliderect(lizi):
                record+=100
                pygame.mixer.Sound.play(sonido_comer)
                pescadoOn=False

        #####COLISIÓN CON OBJETOS######
        if piedraRect.colliderect(lizi):
            lizi.rect.x-=5
        if keykito.rect.colliderect(lizi):
            if lizi.modo=="nitro":
                keykito.activo=False
            else:
                gameOver=True
        if iglooRect.colliderect(lizi):
            ganador=True

        if ganador:
            mensajeGanador = fuentes.render("..- WINNER -..", 1, blanco)
            pantalla.blit(mensajeGanador,(200,300))
            lizi.activo=False


        ######## MOSTRAR PERSONAJES SPRITE
        if lizi.activo:
            pantalla.blit(lizi.image,lizi.rect)
        if keykito.activo:
            pantalla.blit(keykito.image, keykito.rect)
            keykito.update()

        if gameOver:
            pantallaFinal=True
            pantallaJuego=False

        # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        clock.tick(15)

    #MOSTRAR PANTALLA FINAL
    while pantallaFinal:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                pantallaFinal=False
                pantallaInicio=True

        # Codigo para poner un fondo de color.

        pantalla.fill(blanco)
        lizi.controles(event)
        pantalla.blit(fondoFinal,(0,0))

        ##########llamar la lista de Records#######
        records=listarRecords()
        posiciones=1
        for elemento in records:
            mensaje=fuentes.render(str(records[posiciones-1][0])+ " .... ",1,rojo)
            mensaje2=fuentes.render(str(records[posiciones-1][1]),1,rojo)
            pantalla.blit(mensaje,(100,100*posiciones))
            pantalla.blit(mensaje2,(500,100*posiciones))
            posiciones+=1


        # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        clock.tick(15)

pygame.quit()




