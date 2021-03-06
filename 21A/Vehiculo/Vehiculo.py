import pygame
###################################################################
###################################################################
# Program Name: Vehiculo.py
# Authors: Melquizedec Moo Medina
# Description:  Clase me crea el molde para los objetos de un
# Vehiculo, permitiendo operaciones básicas.
#
# Methods:
#
# getAtributos()                                //devuelve el valor del Atributo que se llame.
# setAtributos()                                //asigna o modifica los datos de la clase
# asignarMarca(tiempo, velocidad)       //cambia la marca del Vehiculo
# encender()
# apagar()
###################################################################
###################################################################

class Vehiculo:

    def __init__(self, recibiMarca,modelo="CHEVY",color="AZUL", halogenos=True):
        self.__marca=recibiMarca
        self.__modelo=modelo
        self.color=color
        self.__kilometraje=0.0
        self.__halogenos=halogenos
        self.imagen=pygame.image.load("img/autoApagar.png")

    def getMarca(self):
        return self.__marca

    def setColor(self, nuevoColor):
        self.color= nuevoColor

    def getColor(self):
        return self.color

    def setMatricula(self,nuevaMatricula):
        self.__matricula=nuevaMatricula

    def getMatricula(self):
        return self.__matricula

    def setHalogenos(self, valor):
        self.__halogenos=True

    def encender(self):
        self.imagen=pygame.image.load("img/autoEncendido.png")

    def apagar(self):
        self.imagen=pygame.image.load("img/autoApagar.png")

    def avanzar(self):
        self.imagen=pygame.image.load("img/autoLuzEncender.png")
        self.__kilometraje=self.__kilometraje+5

    def detener(self):
        self.imagen=pygame.image.load("img/autoVentanaAbajoApagar.png")

    def __str__(self):
        return "Hola, soy el Vehiculo " + self.__marca + " - " + self.__modelo + "  - Color:  " + self.color

