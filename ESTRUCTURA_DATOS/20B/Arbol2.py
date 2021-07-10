from Nodo import *


class Arbol:

    def __init__(self):
        self.raiz = None

    def insertarNodo(self, dato):
        if self.raiz == None:
            self.raiz = Nodo(dato)
        else:
            self.insertar(self.raiz, dato)

    def insertar(self, raiz, dato):
        nuevoNodo = Nodo(dato)
        if dato >= raiz.getDato():
            if raiz.getRefDer() is not None:
                self.insertar(raiz.getRefDer(), dato)
            else:
                raiz.setRefDer(nuevoNodo)
                return True
        else:
            if raiz.getRefIzq() != None:
                self.insertar(raiz.getRefIzq(), dato)
            else:
                raiz.setRefIzq(nuevoNodo)
                return True

    def preorden(self, raiz):  # RAIZ, IZQUIERDA, DERECHA
        print(raiz)
        if raiz != None:
            if raiz.getRefIzq != None:
                self.preorden(raiz.getRefIzq())
            if raiz.getRefDer != None:
                self.preorden(raiz.getRefDer())
        else:
            print("*No hay elementos*")

    def inorden(self, raiz):  # IZQUIERDA, RAIZ, DERECHA
        if raiz != None:
            if raiz.getRefIzq() != None:
                self.inorden(raiz.getRefIzq())
            print(raiz.getDato())
            if raiz.getRefDer() != None:
                self.inorden(raiz.getRefDer())
        else:
            print("*No hay elementos*")

    def postorden(self, raiz):
        if raiz != None:
            if raiz.getRefIzq() != None:
                self.postorden(raiz.getRefIzq())
            if raiz.getRefDer() != None:
                self.postorden(raiz.getRefDer())
            print(raiz)
        else:
            print("*No hay elementos*")

    def agregar(self, raiz, padre):
        if padre.getRefIzq() != None:
            self.agregar(raiz, padre.getRefIzq)
        else:
            padre.setRefIzq(raiz.getRefIzq)

    def eliminarNodo(self, dato):
        nodo,padre,ubicacion=self.buscar(self.raiz,dato)
        if nodo:
            ##OPCION 1: NODO A ELIMINAR NO TIENE HIJOS
            if nodo.getRefDer()==None and nodo.getRefIzq()==None:
                if ubicacion=="i":
                    padre.setRefIzq(None)
                elif ubicacion=="d":
                    padre.setRefDer(None)
                return False
            ##OPCION 2: NODO A ELIMINAR TIENE UN HIJO
            if nodo.getRefDer()!=None and nodo.getRefIzq()==None:
                if ubicacion=="i":
                    padre.setRefIzq(nodo.getRefDer())
                elif ubicacion=="d":
                    padre.setRefDer(nodo.getRefDer())
            if nodo.getRefIzq()!=None and nodo.getRefDer()==None:
                if ubicacion=="i":
                    padre.setRefIzq(nodo.getRefIzq())
                elif ubicacion=="d":
                    padre.setRefDer(nodo.getRefIzq())

            #OPCION 3: NODO A ELIMINAR CUANDO TIENE DOS HIJOS
            #1. tenemos que tomar el hijo derecho del Nodo que queremos eliminar y recorrer hasta el hijo más a la izquierda
            nodoIzq=self.irIzquierda(nodo.getRefDer())
            #2. eemplazamos el valor del nodo que queremos eliminar por el nodo que encontramos
            aux=nodoIzq.getDato()
            #3. eliminar este nodo de las formas que conocemos
            self.eliminarNodo(nodoIzq.getDato())
            nodo.setDato(aux)
            return True

    def irIzquierda(self,raiz):
        if raiz.getRefIzq()!=None:
            return self.irIzquierda(raiz.getRefIzq())
        else:
            return raiz

    def encontrar(self, dato):
        return self.buscar(self.raiz, dato)

    def buscar(self, raiz, dato, ubicacion=None, padre=None):
        dato=str(dato)
        if raiz == None:
            return False
        elif raiz.getDato() == dato:
            return raiz,padre,ubicacion
        elif dato < raiz.getDato():
            return self.buscar(raiz.getRefIzq(), dato, "i", raiz)
        else:
            return self.buscar(raiz.getRefDer(), dato, "d", raiz)

