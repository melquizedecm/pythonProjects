
class Nodo:
    def __init__(self, dato):
        self.refIzq = None
        self.refDer = None
        self.dato = dato

    def setDato(self, nuevoDato):
        self.dato = nuevoDato

    def getDato(self):
        return self.dato

    # Metodo para asignar la referencia al siguiente nodo
    def setRefDer(self, nodo):
        self.refDer = nodo

    def getRefDer(self):
        return self.refDer

    def setRefIzq(self, nodo):
        self.refIzq = nodo

    def getRefIzq(self):
        return self.refIzq

    def __str__(self):
        return str(self.dato)




