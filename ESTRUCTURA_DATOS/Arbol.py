
#############################################################
#       INSTITUTO TECNOLOGICO SUPERIOR PROGRESO
#       PROGRAMM:  U1ADA04-  clase Datos
#       ING. ANIMACION DIGITAL Y EFECTOS VISUALES  3er.sem
#       POO.  Prof. Melquizedec Moo Medina
#       DATE:  08-SEP-2017
#       DESCRIPTION: recorrido de un arbol.
#
# 		###This code is contributed by Bhavya Jain####
#############################################################

from Nodo import *

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert(root,dato):
    nuevoNodo=Nodo(dato)
    if root is None:
        root =nuevoNodo
    else:
        if root.getDato() < dato:
            if root.getApuntadorDerecho() is None:
                root.setApuntadorDerecho(nuevoNodo)
            else:
                insert(root.getApuntadorDerecho(), dato)
        else:
            if root.getApuntadorIzquierdo() is None:
                root.setApuntadorDerecho(nuevoNodo)
            else:
                insert(root.getApuntadorIzquierdo(), dato)

    # A utility function to do inorder tree traversal
def inorder(root):
    # type: (object) -> object
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)



