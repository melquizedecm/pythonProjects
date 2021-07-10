from Nodo import *

class Lista:
    NodoCabeza=None
    NodoCola=None

    def __init__(self,dato):
        self.NodoCabeza=Nodo(dato)
        self.NodoCabeza.setRefDerecha(self.NodoCabeza)

    def insertarNodo(self,dato):
        nuevoNodo=Nodo(dato)
        nuevoNodo.setRefDerecha(self.NodoCabeza)
        nodoFin= self.irAlFinal()
        nodoFin.setRefDerecha(nuevoNodo)

    def irAlFinal(self):
        nodoGuia=self.NodoCabeza
        while True:
            if nodoGuia.getRefDerecha()!=self.NodoCabeza:
                nodoGuia=nodoGuia.getRefDerecha()
            else:
                return nodoGuia

    def eliminarNodo(self,dato):
        if self.listaVacia():
            return False
        else:
            #1. Verificar que el Nodo Cabeza es el dato a Buscar
            if self.NodoCabeza.getDato()==dato:
                self.NodoCabeza=None
                return True
            else:
            #2. Buscar el Nodo a eliminar
                nodoAnterior=self.NodoCabeza
                nodoGuia=self.NodoCabeza.getRefDerecha()
                while True:
                    if nodoGuia.getDato()==dato:
                    #3. hacer el intercambio
                        nodoAnterior.setRefDerecha(nodoGuia.getRefDerecha())
                    #4. eliminar el nodo
                        del nodoGuia
                        return True
                    else:
                        if nodoGuia.getRefDerecha()==self.NodoCabeza:
                            return False
                        else:
                            nodoAnterior=nodoGuia
                            nodoGuia=nodoGuia.getRefDerecha()

    def buscarNodo(self,dato):
        nodoGuia=self.NodoCabeza
        while True:
            if nodoGuia.getRefDerecha()!=self.NodoCabeza:
                if nodoGuia.getDato()==dato:
                    return True
                else:
                    nodoGuia=nodoGuia.getRefDerecha()
            else:
                return False

    def recorrerLista(self):
        if self.listaVacia():
            return False
        else:
            nodoGuia = self.NodoCabeza
            while True:
                print(nodoGuia.getDato())
                if (nodoGuia.getRefDerecha() != self.NodoCabeza):
                    nodoGuia = nodoGuia.getRefDerecha()
                else:
                    break

    def listaVacia(self):
        if self.NodoCabeza==None:
            return True
        else:
            return False









