import pygame
import random

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


fondo=pygame.image.load("img/BG00.png")
fondo2=pygame.image.load("img/BG2.png")
fondo3=pygame.image.load("img/BG3.png")


fondo=pygame.transform.scale(fondo,(800,600))
letra=pygame.font.Font(None,40)

ventanaAbierta=True
controlNiveles=1
velocidadJuego=3
records = 0

pantallaInicio = True
pantallaNiveles=False
pantallaJuego = False
pantallaFinal = False

while ventanaAbierta:


    # mostrar Pantalla de Inicio
    while pantallaInicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type ==pygame.KEYDOWN:
                    if event.key ==pygame.K_SPACE:
                        pantallaInicio=False
                        pantallaNiveles=True

        # Codigo para poner un fondo de color.
        ventana.fill(verde)
        ventana.blit(fondo,(0,0))

        mensaje = letra.render("BIENVENIDOS ...", 1, negro)
        ventana.blit(mensaje, (150, 300))

        mensaje=letra.render("Presiona Espacio para continuar",1,negro)
        ventana.blit(mensaje,(100,400))

        # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        reloj.tick(30)

        # mostrar Pantalla de Inicio
    while pantallaNiveles:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pantallaNiveles = False
                        pantallaJuego = True

            # Codigo para poner un fondo de color.
            ventana.fill(verde)
            ventana.blit(fondo, (0, 0))

            mensaje = letra.render("NIVEL  " + str(controlNiveles), 1, negro)
            ventana.blit(mensaje, (150, 300))

            mensaje = letra.render("Presiona Espacio para continuar", 1, negro)
            ventana.blit(mensaje, (100, 400))

            # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
            pygame.display.update()
            reloj.tick(30)




    #######################################################
    ###### CONFIGURACION DE  VARIABLES DEL JUEGO ##########
    #######################################################
    # configurar los colores
    # rgb , (0,255) Red=rojo, Green=verde    blue=azul
    rojo = (240, 50, 50)
    verde = (50, 240, 50)
    celeste = (40, 200, 200)
    negro = (0, 0, 0)
    blanco = (255, 255, 255)
    ventanaAbierta = True

    ##configuracion de Naves
    naves = []
    naveEnemiga = pygame.image.load("img/nave2.png")
    nave = pygame.image.load("img/nave.png")
    fondo = pygame.image.load("img/fondoEspacio.jpg")
    xNave = 350
    yNave = 500
    xNave2 = []
    yNave2 = []
    velocidad = []
    velocidadY = []
    fuente = pygame.font.Font(None, 40)

    ####OBTENER EL RECORD MAS ALTO#######
    archivo = open("records.txt", "r")
    recordAnterior = int(archivo.readline())
    archivo.close()
    ####################################

    ######VARIABLES PARA CONTROL DEL DISPARO DE NOSOTROS######
    laser = pygame.image.load("img/laser.png")
    disparoActivo = False
    xDisparo = 0
    yDisparo = 0
    laserVelocidad = 30
    naveEliminada = None
    tiempoFuego = 0
    contadorEliminadas = 0
    ############################################
    ######VARIABLES PARA CONTROL DE LOS ENEMIGOS######
    ############################################
    velocidadJuego=velocidadJuego+5
    for i in range(0, 5):
        naves.append(naveEnemiga)
        xNave2.append(100 * i)
        velocidad.append(velocidadJuego)
        yNave2.append(i * 20)
        velocidadY.append(velocidadJuego)

    ###### PARA CARGAR AUDIO#####
    musicaFondo = pygame.mixer_music.load("Centroid.mp3")
    pygame.mixer_music.play(-1)  # PARA REPRODUCIR

    ############################################
    ######VARIABLES PARA DISPAROS DE LOS ENEMIGOS######
    ############################################
    xDisparoE=[]
    yDisparoE=[]
    balaActiva=[]
    velDisparoE=5+velocidadJuego
    for i in range(0, len(naves)):
        xDisparoE.append(xNave2[i])
        yDisparoE.append(yNave2[i])
        rand=random.randrange(0,30)
        if rand==1:
            balaActiva.append(True)
        else:
            balaActiva.append((False))

    #######################################################
    ############### PANTALLA DEL JUEGO ####################
    #######################################################
    while pantallaJuego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            ##eventos del teclado- presiona una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # si la tecla es izquierda.
                    xNave = xNave - 20
                if event.key == pygame.K_RIGHT:  # si la tela es Derecha
                    xNave = xNave + 20
                if event.key == pygame.K_SPACE:
                    ##aqui vamos a programar el disparo
                    if disparoActivo == False:
                        disparoActivo = True
                        efectoDisparo = pygame.mixer_music.load("disparo.mp3")
                        pygame.mixer_music.play()
                        xDisparo = xNave + 45  ##colocar el disparo al centro de la nave
                        yDisparo = yNave
                elif event.key==pygame.K_r:
                    pantallaJuego=False
                    pantallaFinal=True

        ############### DESPLEGAR EL CONTENIDO###############
        ##################################################

        # Codigo para poner un fondo de color.
        ventana.blit(fondo, (0, 0))
        ventana.blit(nave, (xNave, yNave))

        if naveEliminada != None:
            if tiempoFuego >= 10:
                naves.pop(naveEliminada)
                xNave2.pop(naveEliminada)
                yNave2.pop(naveEliminada)
                naveEliminada = None
                tiempoFuego = 0
                #########PARA TERMINAR EL JUEGO####
                if contadorEliminadas == 5:
                    pantallaJuego = False
                    pantallaNiveles=True
                    controlNiveles=controlNiveles+1
            else:
                tiempoFuego = tiempoFuego + 1

        # imprimir las naves enemigas
        for i in range(0, len(naves)):
            ventana.blit(naves[i], (xNave2[i], yNave2[i]))

        ###IMPRIMIR LOS RECORDS
        mensaje = fuente.render("Records: " + str(records) + " pts. ", 1, verde)
        ventana.blit(mensaje, (0, 0))

        mensaje = fuente.render("Records Anterior: " + str(recordAnterior) + " pts. ", 1, blanco)
        ventana.blit(mensaje, (450, 0))

        ####mostrar el disparo
        if disparoActivo == True:
            ventana.blit(laser, (xDisparo, yDisparo))
            yDisparo = yDisparo - laserVelocidad
            if yDisparo <= 0:
                disparoActivo = False

            ############COLISION CON OTRAS NAVES##########
            for i in range(0, len(naves)):
                if yDisparo <= yNave2[i] and yDisparo >= yNave2[i] - 100 and xDisparo >= xNave2[i] and xDisparo <= \
                        xNave2[i] + 100:
                    naveExplosion = pygame.image.load("img/nave2Fuego.png")
                    naveEliminada = i
                    naves[i] = naveExplosion
                    contadorEliminadas = contadorEliminadas + 1
                    disparoActivo = False
                    records = records + 10
        ###############################################################
        ############### DESPLEGAR EL DISPARO DEL ENEMIGO###############
        ###############################################################
        for i in range(0, len(naves)):
            rand=random.randrange(0,30)
            if balaActiva[i]:
                yDisparoE[i]=yDisparoE[i]+velDisparoE
                pygame.draw.circle(ventana,rojo,(xDisparoE[i],yDisparoE[i]),5)
                if yDisparoE[i]>=600:
                    balaActiva[i]=False
                if yDisparoE[i]>=yNave and yDisparoE[i]<yNave+80 and xDisparoE[i]>=xNave and xDisparoE[i]<=xNave+100:
                    pantallaJuego=False
                    pantallaFinal=True
            elif rand==1:
                yDisparoE[i]=yNave2[i]
                xDisparoE[i]=xNave2[i]
                balaActiva[i]=True

        #####CONTROL DE LAS POSICIONES Y VELOCIDADES######
        for i in range(0, len(naves)):
            xNave2[i] = xNave2[i] + velocidad[i]
            yNave2[i] = yNave2[i] + velocidadY[i]
            if xNave2[i] <= 0:
                velocidad[i] = velocidad[i] * -1
            if xNave2[i] >= 750:
                velocidad[i] = velocidad[i] * -1
            if yNave2[i] <= 0:
                velocidadY[i] = velocidadY[i] * -1
            if yNave2[i] >= 400:
                velocidadY[i] = velocidadY[i] * -1

        # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        reloj.tick(20)


    if pantallaFinal:
        if records > recordAnterior:
            # cambiar el Record
            archivo = open("records.txt", "w")
            archivo.write(str(records))
            archivo.close()

    # mostrar Pantalla de RECORDS
    while pantallaFinal:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type ==pygame.KEYDOWN:
                    if event.key ==pygame.K_SPACE:
                        pantallaFinal=False
                        pantallaInicio=True
                        velocidadJuego=5
                        records=0
                        controlNiveles=1
                        velDisparoE=3

        # Codigo para poner un fondo de color.
        ventana.fill(verde)
        ventana.blit(fondo3,(0,0))
        mensaje=letra.render("RECORDS",1,negro)
        ventana.blit(mensaje,(350,50))
        mensaje = letra.render("PUNTAJE MÁS ALTO: "+str(recordAnterior), 1, blanco)
        ventana.blit(mensaje, (100, 150))
        mensaje = letra.render("PUNTAJE OBTENIDO: "+ str(records), 1, verde)
        ventana.blit(mensaje, (100, 300))



        # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        reloj.tick(30)
