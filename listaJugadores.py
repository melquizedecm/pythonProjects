from Nodo import *

nodo1=Nodo("impostor")

nodo2=Nodo("rojo")
nodo1.siguiente=nodo2

nodo3=Nodo("morado")
nodo2.siguiente=nodo3


print(nodo1.dato)
nodoGuia=nodo1.getSiguiente()
while True:

    if nodoGuia.siguiente==None:
        print (nodoGuia.getDato())
        break
    else:
        print(nodoGuia.getDato())
        nodoGuia=nodoGuia.getSiguiente()
