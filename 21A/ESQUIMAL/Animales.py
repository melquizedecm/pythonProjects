import pygame
class Pinguino(pygame.sprite.Sprite):
    def __init__(self, posicion):
        self.sheet=pygame.image.load("img/animales.png")
        self.sheet.set_clip((pygame.Rect(65,190,45,85)))
        self.image=self.sheet.subsurface((self.sheet.get_clip()))
        self.rect=self.image.get_rect()
        self.rect.topleft=posicion
        self.frame=0
        self.pasos=0
        self.activo=True
        self.accion="caminar"
        self.caminar={0:(65,195,45,85),1:(150,195,45,85),2:(235,195,45,85),3:(325,195,45,85),4:(405,195,45,85),5:(495,195,45,85)}
        self.deslizar={0:(80,295,60,85),1:(165,295,70,85),2:(274,295,95,80),3:(395,295,95,80)}

    def getFrame(self,estados):
        self.frame += 1
        if self.accion=="deslizar":
            if self.frame>(len(estados)-1):
                self.frame=2
        else:
            if self.frame>(len(estados)-1):
                self.frame=0
        return estados[self.frame]

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
            self.clip((self.deslizar))
            self.rect.x-=15

        self.image=self.sheet.subsurface((self.sheet.get_clip()))
        self.pasos+=1
        if self.pasos>=30:
            self.accion="deslizar"

class Ave(pygame.sprite.Sprite):
    pass

class Foca(pygame.sprite.Sprite):
    pass