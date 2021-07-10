import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self,posicion):
        #configurar el clip del sprite y lo cargo en image y
        #configuro el atributo rect
        self.sheet=pygame.image.load("esquimal.png")
        self.sheet.set_clip(pygame.Rect(0,120, 80,120))
        self.image= self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft=posicion
        self.frame=0
        self.right_states={0:(0,120,80,120),1:(95,120,80,120),2:(196,120,80,120),3:(280,120,80,120),4:(374,120,80,120),5:(470,120,80,120)}
        self.left_states={}
        self.up_states={0:(0,274,80,120),1:(95,255,80,120),2:(190,245,80,120),3:(290,246,80,120),4:(380,260,80,120),5:(475,280,80,120)}
        self.down_states={}
        self.space_states={0,1,2}
        self.recorrido=0

    ##pasar de marco en marco
    def get_frame(self,frame_set):
        self.frame=self.frame+1
        if self.frame>(len(frame_set)-1):
            self.frame=1
        return frame_set[self.frame]

    ##para obtener el clip
    def clip(self,rectangulo):
        if type(rectangulo) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(rectangulo)))
        else:
            self.sheet.set_clip(pygame.Rect(rectangulo))
        return rectangulo

    #actualizar la posicion del personaje
    def update(self, direccion):
        if direccion=='derecha':
            self.clip(self.right_states)
            self.rect.x=self.rect.x+5
            self.recorrido=self.recorrido+2
        if direccion=='izquierda':
            pass
        if direccion=='arriba':
            self.clip(self.up_states)
            self.rect.x+=5
            self.rect.y-=15
            self.recorrido+=2

        if direccion=='detenerDerecha':
            self.clip(self.right_states[0])

        ###mostrar la nueva imagen
        self.image=self.sheet.subsurface(self.sheet.get_clip())

    def controles(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                self.update('derecha')
            if event.key== pygame.K_LEFT:
                self.update('izquierda')
            if event.key== pygame.K_UP:
                self.update('arriba')

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                self.update('detenerDerecha')



