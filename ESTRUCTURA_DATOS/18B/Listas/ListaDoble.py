
########################### Lista_Class ######################
# Program Name: ListaClass.oy
# Autor: Alan de Jesus Lizama Molina
# Descripcion: Clase que crea la Lista que contiene los nodos, permite crearlos, eliminarlos,eliminar toda la lista, comprobar si la lista tiene datos
# imprimir todos los datos, o buscar un dato especfico
# Date: septiembre 28, 2018
from NodoClass import *

class ListaDoble:
    nodoCabeza=None
    nodoCola=None

    def __init__(self):
        nuevoNodo=Nodo("")
        self.nodoCabeza=nuevoNodo
        self.nodoCola=nuevoNodo

    def crearNodo(self,dato,datoBuscar):
        nuevoNodo = Nodo(dato)
        if self.nodoCabeza.getReferenciaDerecha()==None:
            nuevoNodo.setReferenciaDerecha(self.nodoCabeza)
            nuevoNodo.setReferenciaIzquierda(self.nodoCabeza)
            self.nodoCabeza.setReferenciaDerecha(nuevoNodo)
            self.nodoCabeza.setReferenciaIzquierda(nuevoNodo)

        else:
            temp=self.nodoCabeza
            ####1. buscar el lugar donde se insertara
            while (temp.getReferenciaDerecha()!=self.nodoCabeza):
                if temp.getDato()==datoBuscar:
                    ##2. Enlazar la referencia derecha del nuevo(copiar R.D. del nodo encontrado)
                    nuevoNodo.setReferenciaDerecha(temp.getReferenciaDerecha())
                    ##3. Enlazar la referencia izquierda del nuevo(copiar R.I. del nodo siguiente)
                    nuevoNodo.setReferenciaIzquierda(temp)
                    ##4. Enlazar la referencia derecha del nodo encontrado al nodo Nuevo.
                    temp.setReferenciaDerecha(nuevoNodo)
                    ##5. Enlazar la referencia izquierda del nodo siguiente al nodo Nuevo.
                    nodoSiguiente=nuevoNodo.getReferenciaDerecha()
                    nodoSiguiente.setReferenciaIzquierda(nuevoNodo)
                    return True
                temp=temp.getReferenciaDerecha() ##Avanza al siguiente Nodo
            ## nodo final se enlaza con el nodo cabeza
            nuevoNodo.setReferenciaDerecha(self.nodoCabeza)
            self.nodoCabeza.setReferenciaIzquierda(nuevoNodo)
            ## si no hay dato a Buscar el valor se agregar al final
            temp.setReferenciaDerecha(nuevoNodo)



    def recorrerLista(self):
        temp=self.nodoCabeza
        if temp.getReferenciaDerecha()==None: ##Detecta si hay un nodo conectado a la cabeza
            print("La lista esta vacia")
        while(temp.getReferenciaDerecha()!=self.nodoCabeza): ####Ciclo para recorrer los nodos
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
            nodoPrevio=temp ###El nodo previo avanza si no se cumple la condicion anterior
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

