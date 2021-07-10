import pygame

pygame.init()

#configuracion de pantalla
size=(800,600)
ventana=pygame.display.set_mode(size)
reloj=pygame.time.Clock()


#configurar los colores
#rgb , (0,255) Red=rojo, Green=verde    blue=azul
rojo=(240,50,50)
verde=(50,240,50)
celeste=(40,200,200)
negro=(0,0,0)
ventanaAbierta=True
fondo1=pygame.image.load("img/BG.png")
fondo2=pygame.image.load("img/BG2.png")
fondo3=pygame.image.load("img/BG3.png")
fondo3=pygame.transform.scale(fondo3,(800,600))
fuente= pygame.font.Font(None ,40)
records = 0
velocidadJuego=30

while ventanaAbierta:

    pantalla1=True
    #mostrar Pantalla de Inicio
    while pantalla1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pantalla1=False

        #Codigo para poner un fondo de color.
        ventana.fill(celeste)
        ventana.blit(fondo1,(0,0))
        mensaje=fuente.render("PRESIONA SPACE PARA INICIAR",1,rojo)
        ventana.blit(mensaje,(200,300))

        #pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        reloj.tick(30)



    #####PANTALLA DEL JUEGO


    # configuracion de Naves
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

    ######VARIABLES PARA CONTROL DEL DISPARO######
    laser = pygame.image.load("img/laser.png")
    disparoActivo = False
    xDisparo = 0
    yDisparo = 0
    laserVelocidad = 20
    naveEliminada = None
    tiempoFuego = 0
    contadorEliminadas = 0
    velocidadJuego=velocidadJuego+5

    ############################################

    for i in range(0, 5):
        naves.append(naveEnemiga)
        xNave2.append(100 * i)
        velocidad.append(5)
        yNave2.append(i * 20)
        velocidadY.append(15)

    ###### PARA CARGAR AUDIO#####
    musicaFondo = pygame.mixer_music.load("Centroid.mp3")
    pygame.mixer_music.play(-1)  # PARA REPRODUCIR
    pantallaJuego=True
    # mostrar Pantalla de Juego
    while pantallaJuego:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ventanaAbierta = False

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
                if contadorEliminadas == 5:
                    pantallaJuego = False
            else:
                tiempoFuego = tiempoFuego + 1

        # imprimir las naves enemigas
        for i in range(0, len(naves)):
            ventana.blit(naves[i], (xNave2[i], yNave2[i]))
        ###imprimir el record
        mensaje = fuente.render("Records: " + str(records) + " pts. ", 1, verde)
        ventana.blit(mensaje, (0, 0))

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

        #####CONTROL DE LAS POSICIONES Y VELOCIDADES######
        for i in range(0, len(naves)):
            xNave2[i] = xNave2[i] + velocidad[i]
            yNave2[i] = yNave2[i] + velocidadY[i]
            if xNave2[i] == 0:
                velocidad[i] = velocidad[i] * -1
            if xNave2[i] == 750:
                velocidad[i] = velocidad[i] * -1
            if yNave2[i] <= 0:
                velocidadY[i] = velocidadY[i] * -1
            if yNave2[i] >= 400:
                velocidadY[i] = velocidadY[i] * -1


        # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        reloj.tick(30)

    pantallaRecords=True


    # mostrar Pantalla de Final
    while pantallaRecords:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pantallaRecords = False

        # Codigo para poner un fondo de color.
        ventana.fill(celeste)
        ventana.blit(fondo3, (0, 0))

        mensaje = fuente.render("RECORDS", 1, rojo)
        ventana.blit(mensaje, (400, 50))

        # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
        pygame.display.update()
        reloj.tick(30)



