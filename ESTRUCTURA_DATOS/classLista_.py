from ClassNodo_ import *

class Lista:
    nodoCabeza=None

    def __init__(self):
        self.nodoCabeza=Nodo(None)
        self.nodoActual=None

    def agregarNodoDerecho(self,dato):
        nuevoNodo=Nodo(dato)
        nodo=self.nodoCabeza
        while nodo.getEnlaceDerecho() != None:
            nodo=nodo.getEnlaceDerecho()
        nodo.setEnlaceDerecho(nuevoNodo)

    def eliminarNodo(self,dato):
        self.nodoActual = self.nodoCabeza
        while True:
            #if self.nodoActual.getDato() == None:
            #    return False
            if self.nodoActual.getDato() == dato:
                nodoAnterior.setEnlaceDerecho(self.nodoActual.getEnlaceDerecho())
                self.nodoActual.setEnlaceDerecho(None)
                del(self.nodoActual)
            elif self.nodoActual.getDato() != dato:
                nodoAnterior=self.nodoActual
                self.nodoActual = self.nodoActual.getEnlaceDerecho()

    def recorrerLista(self):
        nodo = self.nodoCabeza
        while (nodo.getEnlaceDerecho() != None):
            print(nodo.getDato())
            nodo = nodo.getEnlaceDerecho()
        print(nodo.getDato())

    def agregarNodoIzquierdo(self,dato):
        nuevoNodo=Nodo(dato)
        nodo=self.nodoCabeza
        while(nodo.getEnlaceIzquierdo()!=None):
            nodo=nodo.getEnlaceIzquierdo()
        nodo.setEnlaceIzquierdo(nuevoNodo)

    def buscarNodo(self,dato):
        self.nodoActual=self.nodoCabeza
        while True:
            if self.nodoActual.getDato() ==None:
                return False
            elif self.nodoActual.getDato()==dato:
                return True
            elif self.nodoActual.getDato()!=dato:
                self.nodoActual=self.nodoActual.getEnlaceDerecho()
















