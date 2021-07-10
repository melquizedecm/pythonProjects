class Nodo:
    dato=None
    apuntadorDerecho=None
    apuntadorIzquierdo=None

    def __init__(self,dato):
        self.dato=dato
        self.apuntadorDerecho=None

    def getDato(self):
        return self.dato

    def setDato(self,nuevoDato):
        self.dato=nuevoDato

    def getApuntadorDerecho(self):
        return self.apuntadorDerecho

    def setApuntadorDerecho(self, nodo):
        self.apuntadorDerecho=nodo

    def getApuntadorIzquierdo(self):
        return self.apuntadorIzquierdo

    def setApuntadorIzquierdo(self,nodo):
        self.apuntadorIzquierdo=nodo

