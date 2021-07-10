class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.apuntadorIzquierdo=None
        self.apuntadoDerecho=None

    def __str__(self):
        return str(self.dato)

    def getDato(self):
        return self.dato

    def setApuntadorIzquierdo(self,dato):
        self.apuntadorIzquierdo=dato

    def getApuntadorIzquierdo(self):
        return self.apuntadorIzquierdo

    def getApuntadorDerecho(self):
        return self.apuntadoDerecho

    def setApuntadorDerecho(self,dato):
        self.apuntadoDerecho=dato