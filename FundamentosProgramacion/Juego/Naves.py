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

##configuracion de Naves
naves=[]
naveEnemiga=pygame.image.load("img/nave2.png")
nave=pygame.image.load("img/nave.png")
fondo=pygame.image.load("img/fondoEspacio.jpg")
xNave=350
yNave=500
xNave2=[]
yNave2=[]
velocidad=[]
velocidadY=[]
fuente= pygame.font.Font(None,40)

####OBTENER EL RECORD MAS ALTO#######
archivo=open("records.txt","r")
recordAnterior=int(archivo.readline())
archivo.close()
####################################




######VARIABLES PARA CONTROL DEL DISPARO DE NOSOTROS######
laser=pygame.image.load("img/laser.png")
disparoActivo=False
xDisparo=0
yDisparo=0
laserVelocidad=20
naveEliminada=None
tiempoFuego=0
contadorEliminadas=0
records=0
############################################
######VARIABLES PARA CONTROL DEL DISPARO DE LOS ENEMIGOS######



############################################

for i in range(0,5):
    naves.append(naveEnemiga)
    xNave2.append(100*i)
    velocidad.append(5)
    yNave2.append(i*20)
    velocidadY.append(15)

###### PARA CARGAR AUDIO#####
musicaFondo=pygame.mixer_music.load("Centroid.mp3")
pygame.mixer_music.play(-1)   #PARA REPRODUCIR

# mostrar Pantalla de Juego
while ventanaAbierta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventanaAbierta = False

    ##eventos del teclado- presiona una tecla
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT: #si la tecla es izquierda.
                xNave=xNave-20
            if event.key==pygame.K_RIGHT: #si la tela es Derecha
                xNave=xNave+20
            if event.key==pygame.K_SPACE:
                ##aqui vamos a programar el disparo
                if disparoActivo==False:
                    disparoActivo=True
                    efectoDisparo = pygame.mixer_music.load("disparo.mp3")
                    pygame.mixer_music.play()
                    xDisparo = xNave + 45  ##colocar el disparo al centro de la nave
                    yDisparo = yNave

    ############### DESPLEGAR EL CONTENIDO###############
    ##################################################

    # Codigo para poner un fondo de color.
    ventana.blit(fondo,(0,0))
    ventana.blit(nave,(xNave,yNave))

    if naveEliminada!=None:
        if tiempoFuego>=10:
            naves.pop(naveEliminada)
            xNave2.pop(naveEliminada)
            yNave2.pop(naveEliminada)
            naveEliminada=None
            tiempoFuego=0
            #########PARA TERMINAR EL JUEGO####
            if contadorEliminadas==5:
                if records>recordAnterior:
                    #cambiar el Record
                    archivo=open("records.txt","w")
                    archivo.write(str(records))
                    archivo.close()
                ventanaAbierta=False
        else:
            tiempoFuego=tiempoFuego+1



    #imprimir las naves enemigas
    for i in range(0,len(naves)):
        ventana.blit(naves[i],(xNave2[i],yNave2[i]))


    ###IMPRIMIR LOS RECORDS
    mensaje=fuente.render("Records: "+ str(records)+ " pts. ",1,verde)
    ventana.blit(mensaje,(0,0))

    mensaje = fuente.render("Records Anterior: " + str(recordAnterior) + " pts. ", 1,blanco)
    ventana.blit(mensaje, (450, 0))

    ####mostrar el disparo
    if disparoActivo == True:
        ventana.blit(laser, (xDisparo, yDisparo))
        yDisparo = yDisparo - laserVelocidad
        if yDisparo <= 0:
            disparoActivo = False


        ############COLISION CON OTRAS NAVES##########
        for i in range(0,len(naves)):
            if yDisparo<=yNave2[i] and yDisparo >=yNave2[i]-100 and xDisparo>=xNave2[i] and xDisparo<=xNave2[i]+100 :
                naveExplosion=pygame.image.load("img/nave2Fuego.png")
                naveEliminada=i
                naves[i]=naveExplosion
                contadorEliminadas=contadorEliminadas+1
                disparoActivo=False
                records=records+10



    #####CONTROL DE LAS POSICIONES Y VELOCIDADES######
    for i in range(0,len(naves)):
        xNave2[i]=xNave2[i] + velocidad[i]
        yNave2[i]=yNave2[i] + velocidadY[i]
        if xNave2[i]==0:
            velocidad[i]=velocidad[i]*-1
        if xNave2[i]==750:
            velocidad[i]=velocidad[i]*-1
        if yNave2[i]<=0:
            velocidadY[i]=velocidadY[i]*-1
        if yNave2[i] >= 400:
            velocidadY[i] = velocidadY[i] * -1

    # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
    pygame.display.update()
    reloj.tick(30)

pygame.quit()