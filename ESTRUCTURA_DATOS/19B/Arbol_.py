#############################################################
#       INSTITUTO TECNOLOGICO SUPERIOR PROGRESO             #
#       TEACHER: MELQUIZEDEC MOO MEDINA                     #
#       STUDENT: RAFAEL CARBALLO , VASTI SUAREZ, ESTHER CADENA  #
#       PROGRAMA: Nodo.py                                   #
#       Description: PROGRAMA DE LA CLASE NODO              #
#       DATE:  12/SEP/2019                                  #
#############################################################

from Nodo import *

class Arbol:
    raiz=None


    def __init__(self, dato):       ###Inicializamos el objeto
        self.raiz=Nodo(dato)

    def insertarDato(self,dato):        ###nos sirve para añadir datos a la raiz y al dato
        self.insertar(self.raiz,dato)

    def insertar(self,raiz,dato):   ##agrega un nuevo
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

    def vacio(self):  # decide si el arbol etara vacio
        if self.raiz == None:
            return True
        else:
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

    def postorden(self,raiz):

        if raiz.getRefIzquierda()!= None:
            self.postorden(raiz.getRefIzquierda())

        if raiz.getRefDerecha()!=None:
            self.postorden(raiz.getRefDerecha())

        print(raiz.getDato())





  #  arbol=Arbol(55)   #__init__
  #  arbol.insertarDato(30)
   # arbol.insertarDato(75)
   # arbol.insertarDato(41)
  #  arbol.insertarDato(4)

  #  arbol.postorden(arbol.raiz)