from Lista import *
from Cola import *

class Grafos:
    vectores=[]

    def __init__(self,dato):
        lista=Lista(dato)
        self.vectores.append(lista)

    def agregarVector(self,dato):
        lista=Lista(dato)
        self.vectores.append(lista)

    def mostrarVectores(self):
        for lista in self.vectores:
            lista.recorrerLista()
            print("")

    def vincular(self,dato1,dato2):
        ###validar que  el Nodo escrito exista
        lista=self.existeVector(dato1)
        lista.insertarNodo(dato2)

    def existeVector(self,dato):
        for lista in self.vectores:
            NodoCabeza=lista.getNodoCabeza()
            if NodoCabeza.getDato()==dato:
                return lista
        return False

    def recorrerGrafo(self,dato1,dato2):
        marcas=[]
    ###1. MARCAR EL VERTICE DE PARTIDA
        marcas.append(dato1)
    ###2. METER EN LA COLA, EL VERTICE DE PARTIDA
        cola=Cola(dato1)
    ###3. REPETIR LOS PASOS 4 Y 5
        while cola.tamanio>0:
            ##4. QUITAR EL NODO FRENTE DE LA COLA
            datoValidar=cola.quitar()
            ### 4 B. VISITAR EL VECTOR SALIENTE
            lista = self.existeVector(datoValidar)
            if lista:
                print(datoValidar, "=>", end="")
            ##5. METER EN LA COLA TODOS LOS VERTICES ADYACENTES
            #5b. obtengo el nodoGuia
            nodoGuia=lista.getNodoCabeza()
            if nodoGuia.getDato()==dato2:
                break
            while True: ##HACE EL RECORRIDO PARA METER LOS VERTICES A LA COLA
                #5c. meto en la cola los vertices adyacentes y los marco
                banderaMarca=False
                for marcado in marcas:
                    if marcado==nodoGuia.getDato():
                        banderaMarca=True
                        break
                if banderaMarca==False:
                    cola.insertar(nodoGuia.getDato())
                    marcas.append(nodoGuia.getDato())
                    #print(nodoGuia.getDato(),"=>")
                if (nodoGuia.getRefDerecha() != None):
                    nodoGuia = nodoGuia.getRefDerecha()
                else:
                   # print("")
                    break

    def camino(self,dato1,dato2):

        self.encontrarCamino(dato1,dato2)

    #def encontrarCamino(dato1,dato2):


grafo  = Grafos("MERIDA")
grafo.agregarVector("PROGRESO")
grafo.agregarVector("CHELEM")
grafo.agregarVector("CHUBURNA")
grafo.agregarVector("CHICXULUB")
grafo.agregarVector("TELCHAC")
grafo.agregarVector("MOTUL")

grafo.vincular("MERIDA","PROGRESO")
grafo.vincular("PROGRESO","CHELEM")
grafo.vincular("CHELEM","CHUBURNA")
grafo.vincular("PROGRESO","CHICXULUB")
grafo.vincular("CHICXULUB","TELCHAC")
grafo.vincular("MOTUL","TELCHAC")
grafo.vincular("MERIDA","MOTUL")


#grafo.mostrarVectores()
print ("########----- RECORRER GRAFO -----#######")
grafo.recorrerGrafo("MERIDA","CHELEM")

