#################################################################
#       INSTITUTO TECNOLOGICO SUPERIOR PROGRESO                 #
#       TEACHER: MELQUIZEDEC MOO MEDINA                         #
#       STUDENT: RAFAEL CARBALLO , VASTI SUAREZ, ESTHER CADENA  #
#       PROGRAMA: Nodo.py                                       #
#       Description: PROGRAMA DE LA CLASE NODO                  #
#       DATE:  12/SEP/2019                                      #
#################################################################
class Nodo:
    dato=None
    refDerecha=None
    refIzquierda=None

    def __init__(self,nuevoDato):
        self.dato=nuevoDato

    def getDato(self):
        return self.dato

    def getRefDerecha(self):
        return self.refDerecha

    def setDato(self,nuevoDato):
        self.dato=nuevoDato

    def setRefDerecha(self,nuevaRef):
        self.refDerecha=nuevaRef

    def getRefIzquierda(self):
        return self.refIzquierda

    def setRefIzquierda(self,nuevaRef):
        self.refIzquierda=nuevaRef












