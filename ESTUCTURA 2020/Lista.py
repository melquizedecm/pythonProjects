from Nodo import *

class Lista:

    def __init__(self):
        self.primero=None
        self.ultimo=None


    def agregarNodo(self,dato):
        nodoNuevo= Nodo(dato)
        if self.hayNodos():
            nodoNuevo.setRefDer(self.primero)
            self.primero=nodoNuevo
        else:
            self.primero=nodoNuevo

    def hayNodos(self):
        if self.primero==None:
            return False
        else:
            return True

    def imprimirLista(self):
        if self.hayNodos():
            nodoAux=self.primero
            while(nodoAux.getDato()):  #nodo, tienes algun apuntador derecho?
                print(nodoAux.getDato())     #nodo, imprime tu valor
                if nodoAux.getRefDer()==None:
                    break
                else:
                    nodoAux=nodoAux.getRefDer()  #muevete al siguiente nodo

    def eliminarNodo(self, dato):
        if self.hayNodos():
            nodoAux=self.primero
            nodoAnterior=None
            if dato==nodoAux.getDato():
                ##el elemento a eliminar es el nodo cabeza
                if nodoAux.getRefDer()!=None:
                    self.primero=nodoAux.getRefDer()
                else:
                    self.primero=None
                    self.ultimo=None
            else:
                while (nodoAux.getRefDer()!=None):
                    nodoAnterior = nodoAux
                    nodoAux=nodoAux.getRefDer()
                    if (dato==nodoAux.getDato()):
                        nodoAnterior.setRefDer(nodoAux.getRefDer())
                        return True
                if self.ultimo.getDato()==dato:
                    nodoAux.setRefDer(None)

    def buscarNodo(self,dato):
        if self.hayNodos():
            nodoAux=self.primero
            while(nodoAux.getDato()):
                if nodoAux.getDato()==dato:
                    return True
                else:
                    if nodoAux.getRefDer()!=None:
                        nodoAux=nodoAux.getRefDer()
                    else:
                        break

    def irAlFinal(self):
        if self.hayNodos():
            nodoAux=self.primero
            while nodoAux.getRefDer()!=None:
                nodoAux= nodoAux.getRefDer()
            return nodoAux
        else:
            return False

    def agregarNodoFinal(self,dato):
        nuevoNodo=Nodo(dato)
        self.ultimo=self.irAlFinal()
        if self.ultimo:
            self.ultimo.setRefDer(nuevoNodo)
            self.ultimo=nuevoNodo
        else:
            self.primero=nuevoNodo

    def eliminarPrimero(self):
        if self.hayNodos():
            aux=self.primero
            self.primero=self.primero.getRefDer()
            return aux
        else:
            return False

    def recorrerDerecha(self,nodo):
        if nodo.getDato()!=None:
            print(nodo.getDato())
            self.recorrerDerecha(nodo.getRefDer())
        print(nodo.getDato())

    def imprimir(self):
        self.recorrerDerecha(self.primero)