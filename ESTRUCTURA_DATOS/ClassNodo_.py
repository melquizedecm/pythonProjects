#######################PROGRAM:  Clase de Algo#################
########Author: MELQUIZEDEC MOO MEDINA
########Date:   22/09/2017
########Description:    Clase que configura Nodos de una lista
########
######## Items:
########    constructor:  recibe un dato y crea el nodo, la referncia apunta a None
########    setDato(nuevoDato): modifica el dato del Nodo
########    getDato():     retorna el valor del dato
########    setApuntadorDerecho(dato):modifica el valor del apuntador derecho
########    getApuntadorDerecho():  retorna el apuntador Derecho
########
########
########################################
class Nodo:
    dato=None
    enlaceDerecho=None
    enlaceIzquierdo=None

    def __init__(self,dato):
        self.dato=dato
        enlaceDerecho=None
        enlaceIzquierdo=None

    def setDato(self,nuevoDato):
        self.dato=nuevoDato

    def getDato(self):
        return self.dato

    def setEnlaceDerecho(self,nuevoNodo):
        self.enlaceDerecho=nuevoNodo

    def getEnlaceDerecho(self):
        return self.enlaceDerecho







