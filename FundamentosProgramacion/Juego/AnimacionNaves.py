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

# mostrar Pantalla de Juego
while ventanaAbierta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventanaAbierta = False

    # Codigo para poner un fondo de color.
    ventana.fill(rojo)

    # pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
    pygame.display.update()
    reloj.tick(30)

pygame.quit()