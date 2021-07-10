########################### Nodo_Class ######################
# Program Name: NodoClass.py
# Autor: Alan de Jesus Lizama Molina
# Descripcion: Clase que define y retorna el dato del nodo y su referencia derecha
# Date: septiembre 28, 2018
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
        return self.referenciaDerecha

    def setReferenciaDerecha(self,nodo):
        self.referenciaDerecha=nodo

    def getReferenciaIzquierda(self):
        return self.referenciaIzquierda

    def setReferenciaIzquierda(self,nodo):
        self.referenciaIzquierda=nodo

    def agregarNodosCabeza(self,dato):
        pass
    #### pagina 284 - 9.4