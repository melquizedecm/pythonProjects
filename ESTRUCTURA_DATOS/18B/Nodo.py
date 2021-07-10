class Nodo:
    dato=None
    referenciaDerecha=None
    referenciaIzquierda=None

    def __init__(self,dato):
        self.dato=dato
        self.referenciaDerecha=None
        self.referenciaIzquierda=None

    def getDato(self):
        return self.dato

    def setDato(self,nuevoValor):
        self.dato=nuevoValor

    def getReferenciaDerecha(self):
        return  self.referenciaDerecha

    def setReferenciaDerecha(self,nuevaReferencia):
        self.referenciaDerecha=nuevaReferencia

    def getReferenciaIzquierda(self):
        return  self.referenciaIzquierda

    def setReferenciaIzquierda(self,nuevaReferencia):
        self.referenciaIzquierda=nuevaReferencia