from Lista import *
from Cola import *

class Grafos:
    def existeVector(self):
        pass

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
            print(datoValidar,"=>",end="")
            ### 4 B. VISITAR EL VECTOR SALIENTE
            lista = self.existeVector(datoValidar)
            nodoGuia=lista.getNodoCabeza()
            if nodoGuia.getDato()==dato2:
                break
            while True: #5. METER EN LA COLA TODOS LOS VERTICES ADYACENTES
                banderaMarca=False
                for marcado in marcas:
                    if marcado==nodoGuia.getDato():
                        banderaMarca=True
                        break
                if banderaMarca==False:
                    cola.insertar(nodoGuia.getDato())
                    marcas.append(nodoGuia.getDato())
                if (nodoGuia.getRefDerecha() != None):
                    nodoGuia = nodoGuia.getRefDerecha()
                else:
                    break
