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
negro=(0,0,0)
ventanaAbierta=True

x=0
y=0
velocidadX=20
velocidadY=20

#mostrar Pantalla de Juego
while ventanaAbierta:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ventanaAbierta=False

   # rect1= pygame.Rect(100,500,200,100)
   # pygame.draw.rect(ventana,rojo,rect1,20)

    #pygame.draw.circle(ventana, rojo, (512, 390), 200,10)
    ventana.fill(negro)
    pygame.draw.circle(ventana, rojo, (x+100, y), 40)
    pygame.draw.circle(ventana, verde, (x, y-200), 40)
    pygame.draw.circle(ventana, rojo, (x-200, y), 40)
    pygame.draw.circle(ventana, verde, (x, y+100), 40)

    x=x+velocidadX
    y=y+velocidadY

    if y>600:
        #regrese
        velocidadY=velocidadY * -1
    if y<=0:
        velocidadY = velocidadY * -1

    if x>800:
        #regresar
        velocidadX = velocidadX * -1
    if x<=0:
        velocidadX= velocidadX * -1

    #pygame.draw.polygon(ventana, verde,[(412,290),(612,490),(712,320)])
    pygame.display.update()
    reloj.tick(30)

pygame.quit()