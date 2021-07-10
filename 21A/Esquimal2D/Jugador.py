import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self,posicion):   ### METODO CONSTRUCTOR
        ### Configurar el clip del sprite, lo cargo en imagen y configuro el atributo rect
        self.sheet= pygame.image.load("esquimal.png")  ### Cargar la hoja
        self.sheet.set_clip(pygame.Rect(0,120, 80,120))
        self.image= self.sheet.subsurface(self.sheet.get_clip())
        self.rect= self.image.get_rect()
        self.rect.topleft=posicion
        self.frame=0
        self.activo=True
        self.modo="sinNitro"
        self.right_states= {0:(0,120, 80,120),1:(95,120, 80,120),2:(196,120, 80,120),3:(280,120, 80,120),4:(374,120, 80,120),5:(470,120, 80,120)}
        self.left_states= {0:(0,390,80,120),1:(93,390,80,120),2:(180,390,80,120),3:(275,390,80,120),4:(365,390,80,120),5:(455,390,80,120)}
        self.up_states= {0:(0,275,80,120),1:(95,260,80,120),2:(190,250,80,120),3:(285,250,80,120),4:(375,265,80,120),5:(475,280,80,120)}
        self.fast_states={0:(260,0,80,120),1:(360,0,80,120),2:(465,0,80,120)}
        self.down_states= {}
        self.space_state= {0,1,2}

    ### Obtener el marco del sprite / Pasar de marco en marco
    def get_frame(self,frame_set):
        self.frame=self.frame+1
        if self.frame>(len(frame_set)-1):
            self.frame=1
        return frame_set[self.frame]

    ### Para obtener el clip
    def clip(self, rectangulo):
        if type(rectangulo) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(rectangulo)))
        else:
            self.sheet.set_clip(pygame.Rect(rectangulo))
        return rectangulo

    ### Actualizar la posicion del personaje
    def update(self, direccion):
        if direccion=='derecha':
            self.clip(self.right_states)
            self.rect.x=self.rect.x+5
        if direccion=="izquierda":
            self.clip(self.left_states)
            self.rect.x=self.rect.x-5
        if direccion=="nitro":
            self.clip(self.fast_states)
            self.rect.x= self.rect.x+10
            self.modo="nitro"
        if direccion=='arriba':
            self.clip(self.up_states)
            self.rect.x+=10

        if direccion=='detenerDerecha':
            self.clip(self.right_states[0])
        if direccion== "detenerIzquierda":
            self.clip(self.left_states[5])
        if direccion=="sinNitro":
            self.clip(self.fast_states[0])
            self.modo="sinNitro"
        if direccion== "detenerArriba":
            self.clip(self.right_states[0])

        ### Mostrar la nueva imagen
        self.image=self.sheet.subsurface(self.sheet.get_clip())

    def controles(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                self.update('derecha')
            if event.key == pygame.K_LEFT:
                self.update('izquierda')
            if event.key==pygame.K_DOWN:
                self.update("nitro")
            if event.key==pygame.K_UP:
                self.update("arriba")

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                self.update('detenerDerecha')
            if event.key==pygame.K_LEFT:
                self.update("detenerIzquierda")
            if event.type==pygame.K_DOWN:
                self.update("sinNitro")
            if event.key==pygame.K_UP:
                self.update("detenerArriba")