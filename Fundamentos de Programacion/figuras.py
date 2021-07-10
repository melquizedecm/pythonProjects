import pygame

##iniciamos la libreria
pygame.init()
##tamanio de la pantalla
size=(800,600)
##configuramos el tamaño de la pantalla
screen=pygame.display.set_mode((800,600))
##configuramos el reloj
clock= pygame.time.Clock()

####### CONFIGURACION DE COLORES####
rojo=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
amarillo=(255,255,0)
blanco=(255,255,255)
negro=(0,0,0)


estadoJuego=True

##aqui se configura todo lo que se dibujara
while estadoJuego:
    #capturar los eventos
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            estadoJuego=False

    screen.fill(verde)  ##color de fondo

    rectangulo=pygame.Rect(100,100,100,100)
    pygame.draw.rect(screen,azul,rectangulo)

    rectangulo = pygame.Rect(250, 100, 50, 100)
    pygame.draw.rect(screen, amarillo, rectangulo)

    pygame.draw.circle(screen,negro,(400,300),60)
    pygame.draw.polygon(screen,negro,((100,100),(200,100),(300,300)),1)

    pygame.display.update()
    clock.tick(20)      ##reloj
pygame.quit()
