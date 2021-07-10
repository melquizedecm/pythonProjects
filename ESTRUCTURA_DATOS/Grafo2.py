class Grafo:
    grafo={}
    def agregarNodo(self,nodo):
        self.grafo[nodo]=""

    def configurar(self,arreglo,nodo):
        self.grafo[nodo]=set(arreglo)

    def __str__(self):
        return str(self.grafo)



grafo=Grafo()
while True:


    grafo.agregarNodo("Progreso")
    grafo.agregarNodo("Merida")
    grafo.agregarNodo("Chicxulub")
    print (grafo)

    array=[]
    array.append("Merida")
    array.append("Chicxulub")
    grafo.configurar(array,"Progreso")


    array=[]
    array.append("Progreso")
    grafo.configurar(array,"Merida")
    grafo.configurar(array,"Chicxulub")

    print(grafo)

    grafo.agregarNodo("Valladolid")
    array=[]
    nodo="Progreso"
    while True:
        nodo=input("ingresa el nodo relacionado")
        array.append(nodo)
        opcion=input("Desea agregar nodo: s/n")
        if opcion=="n":
            break
    grafo.configurar(array,nodo)
    print (grafo)
