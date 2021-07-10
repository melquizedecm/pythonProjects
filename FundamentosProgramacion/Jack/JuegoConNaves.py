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
ventanaAbierta = True

##CONFIGURACION DE NAVES
naves=[]  ##ARREGLO DE NAVES
naveEnemiga=pygame.image.load("img/nave2.png")
for i in range(0, 4):  ##0, 1, 2 y 3
    naves.append(naveEnemiga)


nave=pygame.image.load("img/nave.png")
naveEnemiga=pygame.image.load("img/nave2.png")
xNave=350  ##posiciones iniciales
yNave=500

disparo=False

laser=pygame.image.load("img/laser.png")

xNave2=[]  ##RREGLO DE POSICIONES
velocidad=[]
for i in range(0, 4):
    xNave2.append(80*i)
    velocidad.append(4)

    yNave2=50
velocidad=2

###PARA CARGAR AUDIO###
musicaFondo=pygame.mixer_music.load("")
pygame.mixer_music.play()  ###PARA REPRODUCIR

# mostrar Pantalla de Juego
while ventanaAbierta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventanaAbierta = False

    ##Eventos del teclado- presiona una tecla
        if event.type == pygame.KEYDOWN:
            #si la tecla presionada es izquierda
            if event.key==pygame.K_LEFT:
                xNave = xNave-20
            if event.key == pygame.K_RIGHT:
                xNave = xNave+20
            if event.key==pygame.K_SPACE:
                efectoDisparo=pygame.mixer_music.load("disparo.mp3")
                pygame.mixer_music.play()

                disparo=True
                xDisparo=xNave
                yDisparo=yNave+20

    # Codigo para poner un fondo de color.
    ventana.fill(rojo)

    ventana.blit(nave,(xNave,yNave))

    #mostrar el disparo
    ventana.blit(laser,(xDisparo,yDisparo))
    xDisparo=xDisparo+velocidad[0]
    yDisparo=yDisparo+velocidad[0]
    #ventana.blit(naveEnemiga, (xNave2, yNave2))
    #imprimir las naves enemigas
    for i in range(0, 4):  ### i es un numero
        ventana.blit(naves[i], (xNave2[i], yNave2[i]))

    ####CONTROL NAVE ENEMIGA###
    for i in range(0, 4):
        xNave2[i]=xNave2[i] + velocidad

    if xNave2[i]==200:
        velocidad = velocidad * -1
    if xNave2[i]==740:
        velocidad = velocidad * -1
    # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
    pygame.display.update()
    reloj.tick()

pygame.quit()

###ARREGLO DE NAVES###
#naves=[]