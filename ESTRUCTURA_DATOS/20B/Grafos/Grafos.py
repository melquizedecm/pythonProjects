#############################################################
#       AUTHOR: MELQUIZEDEC MOO MEDINA                      #
#       PROGRAMA: Grafo.py                                  #
#       Description: PROGRAMA DE LA CLASE GRAFO, AQUÍ SE    #
#       ENCUENTRAN LOS MÉTODOS QUE CORRESPONDEN AL RECORRIDO#
#       DE UN GRAFO.                                        #
#       DATE:  12/SEP/2020                                  #
#############################################################


from Lista import *
from Cola import *
import pygame


class Grafos:
    arreglo=[]
    pygame.init()

    def agregarVector(self,dato):
        lista=Lista(dato)
        self.arreglo.append(lista)

    def mostrarVectores(self):
        for lista in self.arreglo:
            lista.recorrerLista()
            print("\n")

    def relacionar(self,vector1,vector2):
        for lista in self.arreglo:
            if lista.NodoCabeza.dato==vector1:
                lista.insertarNodo(vector2)

    def recorrer(self, vector1,pantalla):
        #1. marcar el vertice de partida
        visitado=[]
        visitado.append(vector1)
        print(str(vector1), end="")
        #2. Meter en la cola el vértice de partida v.
        cola=Cola(vector1)
        #3. Repetir los pasos 4 y 5 hasta que se cumpla la condicion cola vacia
        while cola.tamanio>0:
            #4.Quitar el nodo frente de la cola, w, devolver la lista de w.
            lista=None
            nodoVisitar=cola.quitar()
            for lista1 in self.arreglo:
                if lista1.NodoCabeza.dato==nodoVisitar:
                    lista=lista1

            #5. Meterenlacolatodoslosverticesadyacentes
            nodoGuia=lista.NodoCabeza
          #  if nodoGuia.dato==vector2:
          #      break
            while True:
                nodoMarcado=False
                for nodo in visitado:
                    if nodo==nodoGuia.dato:
                        nodoMarcado=True
                        break
                ##meter en la cola los vertices no marcados
                if nodoMarcado==False:
                    cola.insertar(nodoGuia.dato)
                    #marcamos el vertice
                    visitado.append(nodoGuia.dato)
                    print(str(nodoGuia.dato), end="")
                #todos los vertices
                if nodoGuia.getRefDerecha()!=None:
                    nodoGuia=nodoGuia.getRefDerecha()
                else:
                    break











grafo=Grafos()
grafo.agregarVector("MERIDA")
grafo.agregarVector("PROGRESO")
grafo.agregarVector("CHICXULUB")
grafo.agregarVector("CHELEM")
grafo.agregarVector("CHUBURNA")


grafo.relacionar("MERIDA","PROGRESO")
grafo.relacionar("MERIDA","CHICXULUB")
grafo.relacionar("PROGRESO","CHELEM")
grafo.relacionar("CHELEM", "CHUBURNA")




grafo.mostrarVectores()

grafo.recorrer("MERIDA", "CHELEM")


