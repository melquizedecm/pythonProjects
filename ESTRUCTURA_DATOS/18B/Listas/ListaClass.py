########################### Lista_Class ######################
# Program Name: ListaClass.oy
# Autor: Alan de Jesús Lizama Molina
# Descripción: Clase que crea la Lista que contiene los nodos, permite crearlos, eliminarlos,eliminar toda la lista, comprobar si la lista tiene datos
# imprimir todos los datos, o buscar un dato específico
# Date: septiembre 28, 2018
from NodoClass import *

class Lista:
    nodoCabeza=None
    nodoCola=None

    def __init__(self):
        nuevoNodo=Nodo("")
        self.nodoCabeza=nuevoNodo
        self.nodoCola=nuevoNodo

    def crearNodoDerecho(self,dato):
        nuevoNodo = Nodo(dato)
        if self.nodoCabeza.getReferenciaDerecha()==None:
            self.nodoCabeza.setReferenciaDerecha(nuevoNodo)
        else:
            temp=self.nodoCabeza
            while (temp.getReferenciaDerecha()!=None):
                temp=temp.getReferenciaDerecha() ##Avanza al siguiente Nodo
            temp.setReferenciaDerecha(nuevoNodo)

    def recorrerLista(self):
        temp=self.nodoCabeza
        if temp.getReferenciaDerecha()==None: ##Detecta si hay un nodo conectado a la cabeza
            print("La lista está vacía")
        while(temp.getReferenciaDerecha()!=None): ####Ciclo para recorrer los nodos
            print(temp.getDato())
            temp=temp.getReferenciaDerecha() ###Avanza al siguiente Nodo
        print(temp.getDato())


    def elimninarListaEntera(self):
        if self.nodoCabeza.getReferenciaDerecha()!=None:
            self.nodoCabeza.setReferenciaDerecha(None)
            print("La lista ha sido eliminada")
        else:
            pass

    def listaVacia(self):
        if self.nodoCabeza.getReferenciaDerecha()== None:
            return True
        else:
            return False

    def elimninarNodo(self,dato):
        temp=self.nodoCabeza
        nodoPrevio=temp
        ###Avanzar en la lista###
        while temp.getReferenciaDerecha()!=None:
            temp=temp.getReferenciaDerecha()
            ### verifica si el dato aborrar es igual al dato en actual en lista
            if temp.getDato()==dato:
                nodoPrevio.setReferenciaDerecha(temp.getReferenciaDerecha())
                temp=None
                return True
            nodoPrevio=temp ###El nodo previo avanza si no se cumple la condición anterior
        return False

    def buscarNodo(self,dato): #######Rcorre la lista para combprobar si un nodo esta en la lista
        temp=self.nodoCabeza
        i=0
        while temp.getReferenciaDerecha()!=None:
            temp=temp.getReferenciaDerecha()
            i=i+1
            if temp.getDato()==dato:
                return i
        return False

    def agregarNodoCabeza(self,dato):  ####### Agregar un nodo al principio de la lista
        nuevoNodo=Nodo(dato)
        if(self.listaVacia()):
            self.nodoCabeza.setReferenciaDerecha(nuevoNodo)
        else:
            nuevoNodo.setReferenciaDerecha(self.nodoCabeza.getReferenciaDerecha())
            self.nodoCabeza.setReferenciaDerecha(nuevoNodo)

    def eliminarNodoCabeza(self):   #####  Eliminar un nodo al principio de la lista
        if(self.listaVacia()):
            return False
        else:
            nodoEliminar=self.nodoCabeza.getReferenciaDerecha()
            self.nodoCabeza.setReferenciaDerecha(nodoEliminar.getReferenciaDerecha())
            return nodoEliminar.getDato()

