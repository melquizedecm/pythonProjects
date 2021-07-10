#############################################################
#       INSTITUTO TECNOLOGICO SUPERIOR PROGRESO             #
#       AUTHOR: MELQUIZEDEC MOO MEDINA                     #
#       SOURCE: Arbol.py                                   #
#       DESCRIPTION: PROGRAMA DE LA CLASE NODO              #
#       DATE:  6/NOV/2019                                  #
#############################################################
from Nodo import *

class Arbol:
    raiz=None

    def __init__(self, dato):
        self.raiz=Nodo(dato)

    def insertarDato(self,dato):
        self.insertar(self.raiz,dato)

    def insertar(self,raiz,dato):
        if dato >= raiz.getDato():
            if raiz.getRefDerecha()!=None:
                self.insertar(raiz.getRefDerecha(),dato)
            else:
                nuevoNodo=Nodo(dato)
                raiz.setRefDerecha(nuevoNodo)
                return False
        else:
            if raiz.getRefIzquierda()!=None:
                self.insertar(raiz.getRefIzquierda(),dato)
            else:
                nuevoNodo=Nodo(dato)
                raiz.setRefIzquierda(nuevoNodo)
                return False

    def preorden(self,raiz): ##raiz, izquierda, derecha
        print(raiz.getDato())
        if raiz.getRefIzquierda()!=None:
            self.preorden(raiz.getRefIzquierda())
        if raiz.getRefDerecha()!=None:
            self.preorden(raiz.getRefDerecha())


    def inorden (self, raiz): #izquierda, raiz, derecha
        if raiz.getRefIzquierda()!= None:
            self.inorden(raiz.getRefIzquierda())
        print(raiz.getDato())
        if raiz.getRefDerecha()!=None:
            self.inorden(raiz.getRefDerecha())

    def postorden(self,raiz): ##izquierda, derecha, raiz
        if raiz.getRefIzquierda()!= None:
            self.postorden(raiz.getRefIzquierda())
        if raiz.getRefDerecha()!=None:
            self.postorden(raiz.getRefDerecha())
        print(raiz.getDato())





arbol=Arbol(10)   #__init__
arbol.insertarDato(8)
arbol.insertarDato(15)
arbol.insertarDato(20)
arbol.insertarDato(4)
arbol.insertarDato(7)
arbol.insertarDato(2)

arbol.postorden(arbol.raiz)