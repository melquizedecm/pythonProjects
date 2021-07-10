from Nodo import *

class Lista:
    NodoCabeza=None
    NodoCola=None

    def __init__(self,dato):
        self.NodoCabeza=Nodo(dato)

    def insertarNodo(self,dato):
        if self.listaVacia():
            self.NodoCabeza=Nodo(dato)
        else:
            nuevoNodo=Nodo(dato)
            nodoFin= self.irAlFinal()
            nodoFin.setRefDerecha(nuevoNodo)

    def insertarNodoCabeza(self,dato):
        nuevoNodo=Nodo(dato)
        if self.listaVacia():
            self.NodoCabeza=nuevoNodo
        else:
            nuevoNodo.setRefDerecha(self.NodoCabeza)
            self.NodoCabeza=nuevoNodo
            return True

    def eliminarNodoCabeza(self):
        if self.listaVacia():
            return False
        else:
            dato=self.NodoCabeza.getDato()
            self.NodoCabeza=self.NodoCabeza.getRefDerecha()
            return dato

    def irAlFinal(self):
        nodoGuia=self.NodoCabeza
        while True:
            if nodoGuia.getRefDerecha()!=None:
                nodoGuia=nodoGuia.getRefDerecha()
            else:
                return nodoGuia

    def eliminarNodo(self,dato):
        if self.listaVacia():
            return False
        else:
            #1. Verificar que el Nodo Cabeza es el dato a Buscar
            if self.NodoCabeza.getDato()==dato:
                self.NodoCabeza=self.NodoCabeza.getRefDerecha()
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
                        if nodoGuia.getRefDerecha()==None:
                            return False
                        else:
                            nodoAnterior=nodoGuia
                            nodoGuia=nodoGuia.getRefDerecha()

    def eliminarNodoFinal(self):
        if self.listaVacia():
            return False
        else:
            nodoFinal=self.irAlFinal()
            self.eliminarNodo(nodoFinal.getDato())
            return nodoFinal.getDato()

    def buscarNodo(self,dato):
        nodoGuia=self.NodoCabeza
        while True:
            if nodoGuia.getRefDerecha()!=None:
                if nodoGuia.getDato()==dato:
                    return nodoGuia
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
                print(nodoGuia.getDato()," => ",end="")
                if (nodoGuia.getRefDerecha() != None):
                    nodoGuia = nodoGuia.getRefDerecha()
                else:
                    break

    def listaVacia(self):
        if self.NodoCabeza==None:
            return True
        else:
            return False

    def getNodoCabeza(self):
        return self.NodoCabeza















