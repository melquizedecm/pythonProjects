class Nodo:
    dato=None
    refDer=None
    refIzq=None

    def __init__(self, dato):
        self.dato=dato

    def setDato(self, nuevoDato):
        self.dato=nuevoDato

    def getDato(self):
        return self.dato

    def setRefDer(self,nodo):
        self.refDer=nodo

    def getRefDer(self):
        return self.refDer

    def getRefIzq(self):
        return self.refIzq

    def setRefIzq(self, nodo):
        self.refIzq=nodo
