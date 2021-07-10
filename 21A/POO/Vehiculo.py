class Vehiculo:
    __color=""
    __marca=""
    __matricula=""
    __kilometraje=0.0
    __modelo=""

    def __init__(self,marca,modelo,color):
        self.__marca=marca
        self.__modelo=modelo
        self.__kilometraje=0.0
        self.__color=color

    def setColor(self, nuevoColor):
        self.__color=nuevoColor

    def getColor(self):
        return self.__color

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getKilometraje(self):
        return self.__kilometraje

    def encender(self):
        return "Ya arranque"

    def apagar(self):
        return "Estoy apagado"

    def avanzar(self):
        return "Avanzando"

    def detener(self):
        return "Detenido"

class Tractor:
    pass

class Barco:
    pass


