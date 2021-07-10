from Nodos import *
####INICIO DE LA CLASE LISTA
class Lista:
##ATRIBUTOS
    siguiente=""
    dato=0
    tamanio=0
    ultimo=""
    siguientedato=""
##CONSTRUCTOR
    def __init__(self):
        self.primero=None
        self.tamanio=0
        self.dato=0
###MÉTODO STRING
    def __str__(self):##Para que le lea el dato ya que lo lee como cadena de texto
        return self.siguiente
###AGREGAR NODO, RECORDAR EN ESTE RECORRE EL DATO A POR LA DERECHA PARA ASI AGREGARSE
    def agregarNodo(self,dato):
        newNodo=Nodo(dato)
        if self.tamanio==0:
            self.primero=newNodo
        else:
            apuntador= self.primero
            while apuntador.refDer !=None:##CICLO PARA SI YA OCUPÓ UN ESPACIO EL DATO DARLE AL SIGUIENTE
                apuntador = apuntador.refDer
            apuntador.refDer = newNodo##AGREGA NODO
##AUMENTA TAMAÑO
        self.tamanio+=1
        print("Nodo agregado")
        return newNodo.dato##DEVUELVE EL VALOR DEL NODO

##MÉTODO PARA ELIMINAR CUALQUIER NODO
    def eliminarNodo(self, dato):
        if self.tamanio == 0:
            return False
        else:
            apuntador = self.primero
            if apuntador.dato!=dato:##CONDICION
                self.primero=apuntador.refDer#CAMBIA DE LUGAR PARA ESTABLECER EL DATO QUE SE ELIMINO SE DESCONECTE.
                self.tamanio -= 1

            try:
                while apuntador.refDer.dato != dato:###CONDICION PARA SI NO HAY EL DATO BUSCADO SEGUIR BUSCANDO
                    apuntador = apuntador.refDer
                dato_a_eliminar = apuntador.refDer
                apuntador.refDer = dato_a_eliminar.refDer

            except AttributeError:##PARA QUE NO SALGA ERROR EN PYTHON
                return False##REGRESA VALOR FALSO

        print("Nodo eliminado")
        return apuntador.dato #DEVUELVE VALOR PARA ELIMINAR
##MÉTODO PARA BUSCAR UN NODO(CUALQUIERA)
    def buscarNodo(self,dato):
        if self.tamanio==0:
            print("NO TIENE NINGÚN NODO AÑADIDO")
            return False
        else:
            apuntador = self.primero##EL APUNTADOR SIEMPRE PREMANECE DE PRIMERO PARA PODER RECORRER
            try:
                if apuntador.refDer.dato==dato:##PARA VALIDAR QUE EXISTE EL NODO
                    print("EL DATO", dato, "FUE ENCONTRADO")
                else:
                    print("DATO NO ENCONTRADO")

            except AttributeError:
                return False
##MÉTODO PARA IMPRIIR DATOS
    def imprimirLista(self):
        print("\n\n########  LISTA ########\n")
        if self.tamanio!=0:##TIENE QUE HABER NODOS PARA QUE SE EFECTUE
            datoSiguiente= self.primero
            print("Los nodos son:")
            while datoSiguiente.getDato()!=None:##OBTIENE EL DATO Y PARA DE UNO EN UNO
                print(datoSiguiente.getDato())##LOS IMPRIME
                if datoSiguiente.getRefDer()==None:
                    break #ROMPE CICLO
                else:
                    datoSiguiente = datoSiguiente.getRefDer() ##SI NO EL DATO QUE SIGUE SIGUE SU CAMINO
        else:
            print("No hay datos en la lista")
###MÉTODO PARA VALIDAR SI LA LISTA ESTA VACIA
    def listaVacia(self):
        if self.tamanio==0:
            print("NO HAY DATOS EN LA LISTA")
        else:
            print("SI HAY DATOS EN LA LISTA")

    def ordenarBurbuja(self):
        if self.tamanio==0:
            print("No hay ningun número añadido")
            return False
        else:
            puntero1 = self.primero
            puntero2 = self.primero.getRefDer()
            for numPasada in range(self.tamanio+2,0,-1):
                for i in range(numPasada):
                    if puntero1.getDato()>puntero2.getDato():
                        ##SE INTERCAMBIAN LOS VALORES
                        temp=puntero1.getDato()
                        puntero1.setDato(puntero2.getDato())
                        puntero2.setDato(temp)

                    ##NOS MOVEMOS HACIA LA DERECHA
                    if puntero2.getRefDer()== None:
                        puntero1 = self.primero
                        puntero2 = self.primero.getRefDer()
                    else:
                        puntero1 = puntero2
                        puntero2 = puntero2.getRefDer()
