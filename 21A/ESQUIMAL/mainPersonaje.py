from Personaje import *
from Animales import *
from records import *
import random
import pygame

pygame.init()
# configuracion de pantalla
size = (800, 600)  #
ventana = pygame.display.set_mode(size)
reloj = pygame.time.Clock()

# configurar los colores
# rgb , (0,255) Red=rojo, Green=verde    blue=azul
rojo = (240, 50, 50)
verde = (50, 240, 50)
celeste = (40, 200, 200)
negro = (0, 0, 0)
blanco=(255,255,255)

ventanaAbierta = True

####configurar la nieve#####
nieveX=[]
nieveY=[]
for i in range(0,200):
    nieveX.append(random.randrange(0,800))
    nieveY.append(random.randrange(0,600))

####configurar de la fuente (letra)######
fuente=pygame.font.Font("LETRA.TTF", 30)
fuenteTitulo=pygame.font.Font("LETRA.TTF", 60)

pantallaInicio=True
ventanaJuego=True
while ventanaJuego:

    fondoFinal = pygame.image.load("assets/png/BG/final.jpg")
    gameover = False
    ganador = False

    #####configuración de Personaje####
    posicion = (0, 400)
    nazareth = Personaje(posicion)
    fondo = pygame.image.load("fondo.jpg")
    fondoInicio = pygame.image.load("assets/png/BG/fondo01.jpg")

    #####configuracion del fondo de Juego
    fondoJuego = pygame.image.load("assets/png/BG/BG.png")
    fondoX, fondoY = 0, -200
    fondoRect = pygame.Rect(600, 0, 200, 600)

    ####CONFIGURACIÓN DE OBJETOS####
    hielo = pygame.image.load("assets/png/Object/IceBox.png")
    hieloX, hieloY = 600, 400
    hieloRect = pygame.Rect(620, 400, 100, 100)

    #######CONFIGURACION PESCADO####
    pescado = pygame.image.load("img/pescado.png")
    peces = []
    pezActivo = []
    pezRect = []
    X = []
    Y = []
    for i in range(0, 5):
        X.append(random.randrange(200, 1500))
        Y.append(470)
        pezRect.append((X[i] + 10, Y[i], 30, 50))
        pezActivo.append(True)

    ######configuracion del Pinguino
    posicionP = (600, 430)
    keykito = Pinguino(posicionP)


    #####configuración del igloo####
    posiglooX = 1300
    igloo = pygame.image.load("assets/png/Object/igloo.png")
    igloorect = (posiglooX + 150, 300, 200, 200)


    ####control de Records####
    record = 0
    contador=0
    activarMensaje=True
    while pantallaInicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pantallaInicio=False
                    pantallaJuego=True


        # Codigo para poner un fondo de color.

        ventana.fill(blanco)
        nazareth.controles(event)
        ventana.blit(fondoInicio,(0,0))
        mensaje=fuenteTitulo.render("Winterstorm",1,blanco)
        mensaje2=fuente.render("Presiona Espacio para Continuar",1,verde)
        ventana.blit(mensaje, (150,300))
        if activarMensaje:
            ventana.blit(mensaje2,(20,450))

        if contador>10:
            if activarMensaje:
                activarMensaje=False
            else:
                activarMensaje=True
            contador=0
        contador+=1

        # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        reloj.tick(10)

    comerSonido=pygame.mixer.Sound("comer_pescado.mp3")
    musica=pygame.mixer.music.load("musicaFondo1.mp3")
    pygame.mixer.music.play(-1)
    # mostrar Pantalla de Juego
    while pantallaJuego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pantallaJuego=False
                pantallaFinal=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_0:
                    pantallaJuego=False
                    pantallaFinal=True
                    nazareth=Personaje(posicion)

        # Codigo para colocar el fondo.
        ventana.fill(blanco)
        ventana.blit(fondoJuego, (fondoX, fondoY))
        mensajeRecord=fuente.render("Record: "+str(record),1,blanco)
        ventana.blit(mensajeRecord,(550,50))
        nazareth.controles(event)


        ####colision con el fondo
        if fondoRect.colliderect(nazareth):
            nazareth.rect.x -=5
            fondoX-=5
            hieloX-=5
            posiglooX-=5
            for i in range(0,5):
                X[i]-=5

        if keykito.rect.colliderect(nazareth.rect):
            if nazareth.nitro:
                keykito.activo=False
                record+=300
            else:
                nazareth.activo=False
                gameover=True

        #####colision con igloo  META###
        if nazareth.rect.colliderect(igloorect):
            record+=500
            ganador=True
            nazareth.activo=False
        if ganador:
            mensajeGanar = fuenteTitulo.render("Winner", 1, blanco)
            ventana.blit(mensajeGanar,(300,300))

        #######COLOCAR OBJETOS########
        ventana.blit(igloo, (posiglooX, 300))
        igloorect = (posiglooX + 150, 300, 200, 200)
        ventana.blit(hielo,(hieloX,hieloY))
        hieloRect = pygame.Rect(hieloX+10, hieloY, 100, 100)
        if nazareth.activo:
            ventana.blit(nazareth.image, nazareth.rect)
        if keykito.activo:
            ventana.blit(keykito.image, keykito.rect)
            keykito.update()


        #####desplegar varios pescados###
        for i in range(0,5):
            if pezActivo[i]:
                ventana.blit(pescado,(X[i],Y[i]))
                pezRect[i]=pygame.Rect(X[i]+20,Y[i],25,50)
            if pezRect[i].colliderect(nazareth):
                record+=100
                pygame.mixer.Sound.play(comerSonido)
                pezActivo[i]=False


        ###COLISIONES CON OBJETOS#####
        if hieloX > nazareth.rect.x > hieloX + 100:
            nazareth.rect.y = 400
        if hieloRect.colliderect(nazareth):
            if nazareth.status==1:
                nazareth.rect.y = 300
                nazareth.detenerBrinco()
            if nazareth.status==0 and nazareth.rect.y==400:
                nazareth.rect.x -=5
            if nazareth.status==0 and nazareth.posicionActual==1 and nazareth.rect.y==400:
                nazareth.rect.x +=5
            if nazareth.posicionActual==2 and nazareth.status==0:
                nazareth.rect.x -=10

        if nazareth.rect.x>=hieloX+100 and nazareth.status==0:
            nazareth.rect.y=400

        if gameover==True:
            pantallaJuego=False
            pantallaFinal=True

        ######EFECTO DE NIEVE#####
        for i in range(0, 200):
            ancho = random.randrange(1, 4)
            pygame.draw.circle(ventana, blanco, (nieveX[i], nieveY[i]), ancho)
            nieveY[i] += 2
            nieveX[i] -= 8
            if nieveY[i] > 605:
                nieveY[i] = -5
            if nieveX[i] < 0:
                nieveX[i] = 800


        # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        reloj.tick(10)

    ###aqui va la muscica de perdedores###

    while pantallaFinal:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                pantallaFinal=False
                pantallaInicio=True

        # Codigo para poner un fondo de color.

        ventana.fill(blanco)
        nazareth.controles(event)
        ventana.blit(fondoFinal, (0, 0))


        ####imprimir records#####
        posicion=1
        records=getRecords()
        for elemento in records:
            mensaje1=fuente.render(str(elemento[0])+ " *****",1,rojo)
            mensaje2=fuente.render(str(elemento[1]), 1,rojo)
            ventana.blit(mensaje1,(100,100*posicion))
            ventana.blit(mensaje2, (500, 100 * posicion))
            posicion+=1

        # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        reloj.tick(10)

pygame.quit()