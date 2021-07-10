import pygame
class Mascota:
    nombre=""
    raza=""
    color=""
    imagen=pygame.image.load("img/pie.jpg")

    def __init__(self, color, raza):
        self.color=color
        self.raza=raza

    def getColor(self):
        return self.color

    def setNombre(self,nuevoNombre):
        self.nombre=nuevoNombre

    def getNombre(self):
        return self.nombre

    def ladrar(self):
        self.imagen=pygame.image.load("img/ladrando.jpg")

    def jugar(self):
        self.imagen=pygame.image.load("img/jugando.jpg")

    def aquietar(self):
        self.imagen=pygame.image.load("img/pie.jpg")

    def __str__(self):
        return "Hola, soy " + self.nombre + "  y soy de raza " + self.raza + " de color de pelaje: " + self.color