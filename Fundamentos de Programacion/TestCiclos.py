import random
import pygame

def imprimirMensaje(screen, mensaje,x,y):
    fuente = pygame.font.Font(None, 60)
    screen.blit(fuente.render(mensaje, 1, White), (x,y))



####### CONFIGURACION PARA VISUALIZAR EL JUEGO #####

pygame.init()
size = 800, 600
Block_1 = (238, 143, 33)
Block_2 = (215, 114, 22)
Line = (82, 71, 69)
Arc = (176, 79, 73)
White = (255, 255, 255)
Red = (255, 20, 20)
Black = (0, 0, 0)
Background = (235, 222, 240)
screen = pygame.display.set_mode(size)

###############FIN DE CONFIGURACION###########
##############################################

############### DEFINICION DE IMAGENES EN VARIABLES######
roca=pygame.image.load("roca.png")
balas= pygame.image.load("bala.png")
nave2Fuego=pygame.image.load("nave2_fuego.png")
sinNave=pygame.image.load("sin_nave.png")
pantallaInicio=pygame.image.load("Next_Level.jpg")

############ CONFIGURACION DE MENSAJES ############
fuente = pygame.font.Font(None, 60)
puntos=0
mensaje=fuente.render(str(puntos),1,White)

############ INICIALIZACION DE RELOJ (TEMPORIZADOR) ######
clock = pygame.time.Clock()

###########  INICIO DEL JUEGO ##############
#Estados:
# 1= Pantalla de Inicio
# 2= Juego
# 3= Records
# 4= Salir
Game = 1
contadorNiveles=0
velocidadJuego=20
estadoJuego=True
while Game!=4:
    Xnave, Ynave = 400, 500
    # Posicion
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    nave = pygame.image.load("nave.png")
    #### DISPAROS NAVE ENEMIGA############
    balasX = []
    balasY = []
    velocidadBalas = 20
    for i in range(0, 6):
        balasX.append(None)
        balasY.append(None)
    ########################################

    ####CONFIGURACION NAVE ENEMIGA######
    enemigoX = 100
    enemigoY = 50
    velocidad = 15
    naves = []
    for i in range(0, 6):
        naves.append(pygame.image.load("nave2.png"))
    balaActiva = False
    balaY = 0
    balaX = 0

    ####ANIMACION DEL FONDO####
    # arreglo de estrellas
    x = []
    y = []

    x1 = []
    y1 = []
    for i in range(0, 100):
        x.append(random.randrange(0, 800))
        y.append(random.randrange(0, 600))
        x1.append(random.randrange(0, 800))
        y1.append(random.randrange(0,600))


    #### CONSTRUCCIÓN DE LA NAVE
    naves = []
    for i in range(0, 6):
        naves.append(pygame.image.load("nave2.png"))

    while Game==1:
        screen.fill(Black)
    ####### CONTROLES PARA INICIAR O SALIR ########
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game=4
            #Movimiento de la nave
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game=2
                if event.key==pygame.K_ESCAPE:
                    Game=4
    ################ MENSAJES #######################
        screen.blit(pantallaInicio,(0,0))
        imprimirMensaje(screen,"PRESIONA SPACE PARA CONTINUAR",100,100)
        imprimirMensaje(screen,"NIVEL"+ str(contadorNiveles),250,200)

        pygame.display.update()
        clock.tick(25)
    contadorNavesDestruidas=0





    while Game==2:
        screen.fill(Black)
    ####### CONTROLES DE LA NAVE ########
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = 3
            #Movimiento de la nave
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Xnave = Xnave -20
                if event.key == pygame.K_RIGHT:
                    Xnave = Xnave +20
                if event.key == pygame.K_SPACE:
                    if balaActiva==False:
                        balaActiva=True
                        balaX=Xnave+30
                        balaY=Ynave-20
    #################################################

    ################ MENSAJES #######################
        screen.blit(fuente.render("NIVEL " + str(contadorNiveles),1,White),(100,0))
        screen.blit(fuente.render(str(puntos), 1, White), (600, 0))
    #################################################

    ###############BORAR NAVES#################
        for i in range(0,6):
            if naves[i]==nave2Fuego:
                naves[i]=sinNave
        disparo=random.randrange(0,5)
        xAux = enemigoX + i * 90
    ########### NAVES ENEMIGAS #####################
        for i in range(0,6):
            if i==disparo and balasY[i]==None and naves[i]!=sinNave:
                balasX[i]=xAux+velocidad
                balasY[i]=60
            if balasY[i]!=None:
                pygame.draw.circle(screen,Red,(balasX[i],balasY[i]),5)
                balasY[i]=balasY[i]+15
                if balasY[i]>=600:
                    balasY[i]=None
                elif balasY[i]>=Ynave and balasY[i]<=Ynave+100:
                    if balasX[i]>=Xnave and balasX[i]<=Xnave+90:
                        Game=3
                        estadoJuego=False

            #############  COLISIONES DISPARO ##########################
            xAux = enemigoX + i * 90
            if balaActiva and naves[i]!=sinNave :
                if balaX >= xAux and balaX <= xAux + 80:
                    if balaY >= enemigoY and balaY <= enemigoY + 60:
                        naves[i] = nave2Fuego
                        puntos=puntos+100
                        balaActiva=False
                        contadorNavesDestruidas += 1
            screen.blit(naves[i],(xAux,enemigoY))

        ####################################################
        enemigoX=enemigoX+velocidad
        if enemigoX<=-90 or enemigoX>=470:
                velocidad=velocidad *-1
    ###################################################
        if contadorNavesDestruidas >= 6:
            Game = 3
    ############### FONDO ANIMADO #####################
        for i in range(0,100):
            pygame.draw.circle(screen, White, [x[i], y[i]], 4)
            pygame.draw.circle(screen, White, [x1[i], y1[i]], 1)
            y[i] = y[i] + 10
            # reinicia el proceso
            if y[i] >= 600:
                y[i] = 5
                x[i]=random.randrange(0,800)

            y1[i] = y1[i] + 5
            # reinicia el proceso
            if y1[i] >= 600:
                y1[i] = 5
                x1[i]=random.randrange(0,800)
    ####################################################

    ############### NAVE PRINCIPAL ####################
        screen.blit(nave,(Xnave,Ynave))
        # Xnave y Ynave son las coordenadas de la nave
    ####################################################

    ########### CONTROL DE DISPAROS ####################
        if balaActiva:
            screen.blit(balas,(balaX,balaY))
            balaY=balaY-30
            if balaY<=-30:
                balaActiva=False
    ####################################################
        pygame.display.update()
        clock.tick(velocidadJuego)



    while Game==3:
        screen.fill(Black)
    ####### CONTROLES DE LA NAVE ########
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game=4
            #Movimiento de la nave
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game=1

    ################ MENSAJES #######################
        imprimirMensaje(screen,"RECORDS",300,100)
        imprimirMensaje(screen,"MMM      "+ str(puntos),300,150)

        pygame.display.update()
        clock.tick(25)

    ############ CONTADOR NIVELES ################
    if estadoJuego==False:
        puntos = 0
        velocidadJuego = 20
        estadoJuego=True
        contadorNiveles=0
    else:
        velocidadJuego +=3
        contadorNiveles += 1

pygame.quit()