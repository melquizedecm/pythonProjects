from Lista import *

class Cola(Lista):

    def __init__(self):
        Lista.__init__(self)
        self.limite=3

    def encolar(self,dato):
        if self.limite<=0:
            print("Cola llena")
        else:
            self.agregarNodoFinal(dato)
            self.limite =self.limite-1

    def desencolar(self):
        nodo=self.eliminarPrimero()
        if nodo:
            print ("Turno de: ", nodo.getDato())
            self.limite=self.limite+1
        else:
            print( "No hay nadie esperando..." )


colaBanco=Cola()

colaBanco.encolar("Arantxa")
colaBanco.encolar("Montserrat")
colaBanco.encolar("Fabian")

colaBanco.desencolar()

colaBanco.encolar("Jair")

colaBanco.imprimirLista()
