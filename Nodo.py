class Nodo:

    dato=""
    siguiente=""

    def __init__(self, valor, nodoSiguiente=None):

        self.dato=valor
        self.siguiente=nodoSiguiente

    def getSiguiente(self):
        return self.siguiente

    def getDato(self):
        return self.dato




