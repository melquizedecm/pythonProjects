import pygame

#####Inicializar pygame

pygame.init()

#muestra una ventana de 800 x 600

size =800,600
pantalla = pygame.display.set_mode(size)

#comenzamos el bucle del juego
reloj = pygame.time.Clock()
run=True
x=20
y=20

while run:
    #capturamos los eventos que se han producido
    for event in pygame.event.get():
        #Si el evento es Salir  de la ventana,, terminamos el juego
        if event.type == pygame.QUIT:
            run = False
    pantalla.fill([255, 255, 255])
    pygame.draw.circle(pantalla,[255,50,50],[100+x,100+y],50,0)
    pygame.draw.circle(pantalla, [0, 0, 250], [200, 100], 50, 0)
    pygame.display.update()
    reloj.tick(20)
#salgo de pygame
pygame.quit()