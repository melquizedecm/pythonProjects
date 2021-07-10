import Nodo

CNodo= Nodo

class Lista:
    def __init__(self):
        self.cabeza = None
        self.cola= None

    def agregarNodo(self,dato):
        if self.cabeza==None:
            self.cabeza=CNodo.Nodo(dato)
            self.cola=CNodo.Nodo(dato)
            #self.cola.setApuntador(None)
        else:
            self.temp=CNodo.Nodo(dato)
            self.temp.setApuntadorIzquierdo(self.cabeza)
            self.cabeza=self.temp

    def getNextNodo(self,nodo):
        return nodo.getApuntador()

    def imprimirLista(self):
        if self.cabeza==None:
            print ("No hay nodos en la lista")
        else:
            temp=self.cabeza
            print(self.temp.getDato())
            while(self.temp.getApuntadorIzquierdo()!=None):
                self.temp=self.temp.getApuntadorIzquierdo()
                print(self.temp.getDato())


    def buscarNodo(self,dato):
        if self.cabeza==None:
            print ("lista vacia")
        else:
            if (self.cabeza.getDato()==dato):
                print("El dato esta en la cabeza")
            elif(self.cola.getDato()==dato):
                print("esta en la cola")
            else:
                temp = self.cabeza.getApuntadorIzquierdo()
                c=0
                while( self.temp.getDato()!=dato):
                    self.temp = self.temp.getApuntadorIzquierdo()
                    c=c+1
            print("el Nodo se encuentra en "+ c+ " : ")
            print(self.temp.getDato())


    def estaVacia(self):
        if self.cabeza==None:
            print ("Lista vacia")
            return True
        else:
            return False

    def eliminarElemento(self):
        if self.cabeza==None:
            print ("lista vacia")
        elif self.cabeza.getApuntadorIzquierdo()==None:
            self.cabeza=None
        else:
            self.temp=self.cabeza.getApuntadorIzquierdo()
            self.cabeza=self.temp

    def longitud(self):
        if self.cabeza == None:
            return 0
        else:
            temp = self.cabeza.getApuntadorIzquierdo()
            c = 0
            while (self.temp.getDato()):
                self.temp = self.temp.getApuntadorIzquierdo()
                c = c + 1
            return  c

    def eliminacionLogica(self, dato):
        if self.cabeza == None:
            return False
        else:
            if (self.cabeza.getDato()==dato):
                print("El dato esta en la cabeza")
            elif(self.cola.getDato()==dato):
                print("esta en la cola")
            else:
                temp = self.cabeza.getApuntadorIzquierdo()
                c=0
                while( self.temp.getDato()!=dato):
                    self.temp = self.temp.getApuntadorIzquierdo()
                    c=c+1
            print("el Nodo se encuentra en "+ c+ " : ")
            print(self.temp.getDato())









