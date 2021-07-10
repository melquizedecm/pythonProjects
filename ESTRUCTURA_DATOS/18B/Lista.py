from Nodo import *

class Lista:
    nodoCabeza=None
    nodoCola=None

    def __init__(self):
        self.nodoCabeza=None

    def crearNodo(self,dato):
        if self.nodoCabeza.referenciaDerecha==None:
            nuevoNodo=Nodo(dato)
            self.nodoCabeza.referenciaDerecha(nuevoNodo)


