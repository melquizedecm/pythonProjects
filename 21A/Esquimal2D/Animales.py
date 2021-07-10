import pygame

class Pinguino(pygame.sprite.Sprite):
    def __init__(self, posicion):
        self.sheet=pygame.image.load("img/animales.png")
        self.sheet.set_clip(pygame.Rect(70,195,45,80))
        self.image=self.sheet.subsurface(self.sheet.get_clip())
        self.rect=self.image.get_rect()
        self.rect.topleft=posicion
        self.accion="caminar"
        self.activo=True
        self.contador=0
        self.frame=0
        self.caminar={0:(70,195,45,80),1:(150,195,45,80),2:(235,195,45,80),3:(322,195,45,80),4:(410,195,45,80),5:(495,195,45,80)}
        self.deslizar={0:(80,300,55,85),1:(165,295,70,75),2:(270,295,95,70),3:(400,295,95,70)}

    ##moverte en los Frames###
    def getFrame(self,estados):
        self.frame = self.frame + 1
        if self.accion=="deslizar":
            if self.frame>(len(estados)-1):
                self.frame=0
        else:
            if self.frame>(len(estados)-1):
                self.frame=0
        return estados[self.frame]

    def frameDeslizar(self):
        pass

    def clip(self, estados):
        if type(estados) is dict:
            self.sheet.set_clip(pygame.Rect(self.getFrame(estados)))
        else:
            self.sheet.set_clip(pygame.Rect(estados))
        return estados

    def update(self):
        if self.accion=="caminar":
            self.clip(self.caminar)
            self.rect.x-=5
        if self.accion=="deslizar":
            self.clip(self.deslizar)
            self.rect.x-=15

        self.image=self.sheet.subsurface(self.sheet.get_clip())
        self.contador+=1
        if self.contador>=40:
            self.accion="deslizar"

class Ave(pygame.sprite.Sprite):
    pass

class Foca(pygame.sprite.Sprite):
    pass