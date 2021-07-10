#############################################################
#       AUTHOR: MELQUIZEDEC MOO MEDINA                      #
#       PROGRAMA: Pila.py                                   #
#       Description: PROGRAMA DE LA CLASE PILA              #
#       DATE:  20/NOV/2020                                  #
#############################################################
from Lista import *

class Pila(Lista):
    cima=None
    base=None

    def __init__(self,dato):
        Lista.__init__(self,dato)
        self.cima=1
        self.base=0

    def push(self,dato):
        self.insertarNodoCabeza(dato)
        self.cima=self.cima+1

    def pop(self):
        if self.listaVacia():
            return False
        else:
            datoEliminado=self.eliminarNodoCabeza()
            self.cima=self.cima-1
            return datoEliminado

    def mostrarPila(self):
        self.recorrerLista()

    def pilaVacia(self):
        if self.cima==0:
            return True
        else:
            return False



