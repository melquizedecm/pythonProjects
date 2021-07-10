import pygame

class Gelatina:
    sabor=""
    __color=""
    estado=""
    imagen=""

    def __init__(self,nuevoSabor,color):
        self.sabor=nuevoSabor
        self.__color=color
        self.estado="liquido"
        self.imagen=pygame.image.load("img/diet.png")


    def setEstado(self,nuevoEstado):
        self.estado=nuevoEstado

    def setColor(self,nuevoColor):
        self.__color=nuevoColor
        if self.__color=="naranja":
            self.imagen=pygame.image.load("img/naranja.png")

    def derretir(self):
        self.estado="derretido"
        if self.__color=="naranja":
            self.imagen=pygame.image.load("img/naranjaDerr.png")
        else:
            self.imagen=pygame.image.load("img/dietDerr.png")

    def enfriar(self):
        self.estado="gelificar"

    def __str__(self):
        return "Hola, soy la gelatina sabor: " + self.sabor + " y estoy en estado: " + self.estado