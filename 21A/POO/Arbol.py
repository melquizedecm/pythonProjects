from Nodo import *

class Arbol:
    raiz=None

    def __init__(self,raiz):
        self.raiz=Nodo(raiz)
        self.tamanio=0

    def insertarDato(self,dato):
        self.tamanio += 1
        self.insertar(self.raiz,dato)


    def buscarDato(self,datoBuscar):
        if self.tamanio==0:
            print("NO TIENE NINGÚN DATO AÑADIDO")
            return False
        else:
            apuntador = self.raiz
            anterior=None
            lado=0
            try:
                while apuntador.getDato()!=datoBuscar:
                    if datoBuscar>apuntador.getDato():
                        anterior=apuntador
                        lado="Der"
                        apuntador=apuntador.getRefDer()
                    else:
                        lado="Izq"
                        anterior=apuntador
                        apuntador=apuntador.getRefIzq()
                print("EL DATO", datoBuscar, "FUE ENCONTRADO")
                return apuntador,anterior,lado

            except AttributeError:
                print("EL DATO",datoBuscar,"NO FUE ENCONTRADO EL EL ÁRBOL")
                return False

    def buscarMayor(self):
        if self.tamanio==0:
            print("No hay datos")
        else:
            apuntador=self.raiz


    def eliminarDato(self,datoEliminar):
        if self.tamanio==0:
            print("NO TIENE NINGÚN DATO AÑADIDO")
            return False
        else:
            apuntador=self.raiz
            if datoEliminar==apuntador.getDato():
                self.raiz=apuntador.getRefDer()
            else:
                datoBuscado= self.buscarDato(datoEliminar)
                print("EL DATO",datoBuscado,"FUE ELIMINADO")
                if datoEliminar==datoBuscado:
                    datoBuscado=datoBuscado.getRefDer()
                    return datoBuscado
                else:
                    if datoBuscado==apuntador.getRefIzq():
                        datoBuscado=apuntador.getRefIzq()
                        return datoBuscado


    def insertar(self,raiz,dato):
        if dato>=raiz.getDato():
            if raiz.getRefDer()!=None:
                self.insertar(raiz.getRefDer(),dato)
            else:
                newNodo=Nodo(dato)
                raiz.setRefDer(newNodo)
                return True
        else:
            if raiz.getRefIzq()!=None:
                self.insertar(raiz.getRefIzq(),dato)
            else:
                newNodo=Nodo(dato)
                raiz.setRefIzq(newNodo)
                return True

    def inorden(self,raiz):
        if raiz.getRefIzq() != None:
            self.inorden(raiz.getRefIzq())
        print(raiz.getDato())
        if raiz.getRefDer()!=None:
            self.inorden(raiz.getRefDer())

    def postorden(self,raiz):
        if raiz.getRefIzq()!=None:
            self.postorden(raiz.getRefIzq())
        if raiz.getRefDer()!=None:
            self.postorden(raiz.getRefDer())
        print(raiz.getDato())

    def preorden(self,raiz):
        print(raiz.getDato())
        if raiz.getRefIzq()!=None:
            self.preorden(raiz.getRefIzq())
        if raiz.getRefDer()!=None:
            self.preorden(raiz.getRefDer())

    def eliminar(self,dato):
        nodo, anterior, lado= self.buscarDato(dato)
        if nodo:
            ####1a opcion:  NO TIENE HIJOS ###
            hijos,siguiente=self.cuantosHijos(nodo)
            if hijos==0:
                if lado=="Der":
                    anterior.setRefDer(None)
                if lado=="Izq":
                    anterior.setRefIzq(None)

            ####2a opcion: TIENE UN HIJO ###
            if hijos==1:
                if lado=="Der":
                    anterior.setRefDer(siguiente)
                elif lado=="Izq":
                    anterior.setRefIzq(siguiente)

            if hijos==2:
                pass


    def cuantosHijos(self,nodo):
        if nodo.getRefIzq() == None and nodo.getRefDer() == None:
            return 0, None
        if nodo.getRefIzq()!=None:
            if nodo.getRefDer()!=None:
                return 2, None
            else:
                return 1,nodo.getRefIzq()
        elif nodo.getRefDer()!=None:
            return 1,nodo.getRefDer()





arbol=Arbol(18)
arbol.insertarDato(9)
arbol.insertarDato(7)
arbol.insertarDato(12)
arbol.insertarDato(2)
arbol.insertarDato(8)
arbol.insertarDato(11)
arbol.insertarDato(25)
arbol.insertarDato(23)
arbol.insertarDato(29)
arbol.insertarDato(21)
arbol.insertarDato(24)
arbol.insertarDato(31)



arbol.eliminar(12)
#arbol.inorden(arbol.raiz)

arbol.inorden(arbol.raiz)
#arbol.buscarDato(12)
#arbol.eliminarDato(10)

#arbol.inorden(arbol.raiz)

