#############################################################
#       AUTHOR: MELQUIZEDEC MOO MEDINA                      #
#       PROGRAMA: Cola.py                                   #
#       Description: PROGRAMA DE LA CLASE NODO              #
#       DATE:  12/SEP/2020                                  #
#############################################################
from Lista import *

class Cola(Lista):

    def __init__(self, dato):
        Lista.__init__(self,dato)
        self.tamanio=1

    def insertar(self,dato):
        respuesta=self.insertarNodo(dato)
        if respuesta!=False:
            self.tamanio = self.tamanio + 1
            return respuesta

    def quitar(self):
        dato=self.eliminarNodoCabeza()
        if dato:
            self.tamanio=self.tamanio-1
            return dato
        else:
            return  False

