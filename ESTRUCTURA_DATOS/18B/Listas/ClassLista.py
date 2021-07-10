from ClassNodo import *

class Lista:
    cabeza=None
    cola=None

    def __init__(self):
        nuevoNodo=Nodo("")
        self.cabeza=nuevoNodo
        self.cola=nuevoNodo

    def agregarNodoDerecho(self,dato):
        nuevoNodo = Nodo(dato)
        if self.cabeza.getApuntadorDerecho()==None:
            self.cabeza.setApuntadorDerecho(nuevoNodo)
        else:
            temp=self.cabeza
            while(temp.getApuntadorDerecho()!=None):
                temp=temp.getApuntadorDerecho()
            temp.setApuntadorDerecho(nuevoNodo)

    def recorrerLista(self):
        print ("\n\n  LISTA \n")
        temp=self.cabeza.getApuntadorDerecho()
        while(temp.getApuntadorDerecho()):
            aux=temp.getDato()
            if aux[0]=="*":
                pass
            else:
                print(str(temp.getDato()) + " ==> ")
            temp=temp.getApuntadorDerecho()
        print(temp.getDato()+ "==>None")

    def recorrerListaEliminados(self):
        print ("\n\n  LISTA PAPELERA \n")
        temp=self.cabeza.getApuntadorDerecho()
        while(temp.getApuntadorDerecho()):
            aux=temp.getDato()
            if aux[0]=="*":
                print(str(temp.getDato()) + " ==> ")
            temp=temp.getApuntadorDerecho()


    def eliminacionLogica(self,dato):
        ##falta validar que exista nodo cabeza##
        temp = self.cabeza
        while (temp.getApuntadorDerecho() != None):
            if(temp.getDato()==dato):
                temp.setDato("*" + temp.getDato())
                return True
            temp = temp.getApuntadorDerecho()

    def recuperarDato(self,dato):
        temp = self.cabeza
        while (temp.getApuntadorDerecho()):
            if(temp.getDato()=="*"+dato):
                temp.setDato(dato)
                return True
            temp = temp.getApuntadorDerecho()

