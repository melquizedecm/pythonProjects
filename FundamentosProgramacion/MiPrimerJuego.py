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
fondo1=pygame.image.load("BG.png")
fondo2=pygame.image.load("BG2.png")
fondo3=pygame.image.load("BG3.png")
fondo3=pygame.transform.scale(fondo3,(800,600))
fuente= pygame.font.Font(None ,40)


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

    pantallaJuego=True
    tierra= pygame.image.load("11.png")
    # mostrar Pantalla de Juego
    while pantallaJuego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pantallaJuego=False

        # Codigo para poner un fondo de color.
        ventana.fill(celeste)
        ventana.blit(fondo2, (0, 0))
        ventana.blit(tierra, (0, 500))
        ventana.blit(tierra, (100, 500))
        ventana.blit(tierra, (200, 500))
        ventana.blit(tierra, (300, 500))
        mensaje = fuente.render("AQUI VA EL JUEGO", 1, rojo)
        ventana.blit(mensaje, (200, 300))

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



