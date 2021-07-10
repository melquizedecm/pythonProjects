import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self, posicion):
        #cargar imagen de sprite
        self.sheet=pygame.image.load("esquimal.png")
        ###cargar la imagen incial, (X,Y, ancho, alto)
        self.sheet.set_clip(pygame.Rect(0,120,80,120))
        self.image=self.sheet.subsurface(self.sheet.get_clip())
        self.rect=self.image.get_rect()
        self.rect.topleft=posicion
        self.frame=0
        self.nitro=False
        ##para brincar##
        self.status=0      ###caminando=0, brincar=1
        self.contadorbrinco = 0  #cuenta 6 tiempos para brincar
        self.posicionActual = 0  #controla si estas arriba o abajo
        ######
        self.activo=True
         #0=izquierda, 1=derecha, 2 =nitro
        self.right_states={0:(0,120,80,120),1:(95,120,80,120),2:(185,120,80,120),3:(280,120,80,120),4:(375,120,80,120),5:(465,120,80,120)}
        self.left_states = {0:(0,390,80,120),1:(93,390,80,120),2:(180,390,80,120),3:(275,390,80,120),4:(365,390,80,120),5:(455,390,80,120)}
        self.up_states = {0:(0,275,80,120),1:(90,265,80,120),2:(190,250,80,120),3:(285,250,80,120),4:(375,265,80,120),5:(480,280,80,120)}
        self.fast_states={0:(260,0,80,120),1:(360,0,80,120),2:(465,0,80,120)}

    def getFrame(self,estados):
        self.frame= self.frame +1
        if self.frame>(len(estados)-1):
            self.frame=0
        return estados[self.frame]

    def clip(self, estados):
        if type(estados) is dict:
            self.sheet.set_clip(pygame.Rect(self.getFrame(estados)))
        else:
            self.sheet.set_clip(pygame.Rect(estados))
        return estados

    def update(self,direccion):
        if direccion=='derecha':
            self.clip(self.right_states)
            self.rect.x=self.rect.x+5
        if direccion=='izquierda':
            self.clip(self.left_states)
            self.rect.x=self.rect.x-5
        if direccion=="nitrogeno":
            self.clip(self.fast_states)
            self.rect.x = self.rect.x +10
            self.nitro=True
        if direccion=="arriba":
            self.clip(self.up_states)

        if direccion=="detenerDerecha":
            self.clip(self.right_states[0])
        if direccion=="detenerIzquierda":
            self.clip((self.left_states[5]))
        if direccion=="sinNitro":
            self.clip(self.right_states[0])
            self.nitro=False
        if direccion=="detenerArriba":
            self.clip(self.right_states[0])

        self.image=self.sheet.subsurface(self.sheet.get_clip())


    def brincar(self):
        if self.status==1  and self.contadorbrinco<3:
            if self.posicionActual == 1:
                self.rect.x-=10
            elif self.posicionActual==0:
                self.rect.x+=10
            self.rect.y-=60
        elif self.status==1 and self.contadorbrinco<6:
            if self.posicionActual == 1:
                self.rect.x-=10
            elif self.posicionActual==0:
                self.rect.x+=10
            self.rect.y+=60
        else:
            #self.rect.y=self.posicionActual
            self.detenerBrinco()
            return True
        self.contadorbrinco += 1
        self.update("arriba")

    def detenerBrinco(self):
        self.contadorbrinco=0
        self.status=0
        self.update("detenerArriba")

    def controles(self,event):
        if self.status==1:
            self.brincar()
        else:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    self.update("derecha")
                    self.posicionActual=0
                if event.key==pygame.K_LEFT:
                    self.update("izquierda")
                    self.posicionActual=1
                if event.key==pygame.K_DOWN:
                    self.update("nitrogeno")
                    self.posicionActual=2
                if event.key==pygame.K_UP:
                    if self.status==0:
                        self.status=1
                        self.brincar()

                    #self.update("arriba")

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.update('detenerDerecha')
                if event.key==pygame.K_LEFT:
                    self.update('detenerIzquierda')
                if event.key==pygame.K_DOWN:
                    self.update("sinNitro")
                if event.key == pygame.K_UP:
                    pass# self.update('detenerArriba')

