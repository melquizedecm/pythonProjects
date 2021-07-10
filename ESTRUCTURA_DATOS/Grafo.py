####################################################################
#       AUTHOR: MELQUIZEDEC MOO MEDINA                             #
#       PROGRAMA: Grafo.py                                         #
#       Description: Programa donde se describe el Grafo Completo  #
#       DATE:  10/SEP/2020                                         #
####################################################################

class Grafo:
    recorrido=[]
    camino=[]

    def __init__(self):
        self.grafo=[]

    def ingresarNodo(self,vector):
        if (self.existeVector(vector)):
            return False
        else:
            fila=[]
            fila.append(vector)
            self.grafo.append(fila)
            return True

    def relacionar(self,vector1, vector2):
        if self.existeVector(vector1) and self.existeVector(vector2):
            for fila in self.grafo:
                if vector1==fila[0]:
                    fila.append(vector2)
                if vector2==fila[0]:
                    fila.append(vector1)
            return True
        else:
            return False

    def recorrerCamino1(self, vector1, vector2):
        self.camino=self.grafo
        self.recorrrerCamino(vector1,vector2,self.camino)

    def recorrrerCamino(self, vector1,vector2,array):
        for fila in array:
            if vector1==fila[0]:
                self.recorrido.append(fila[0])
                print (fila[0])
                array.remove(fila)
                self.recorrer2(vector2,fila, array)

    def recorrer2(self,vector2,recorrido, array):
        for vectores in recorrido:
            for fila in array:
                if vectores==fila[0]:
                    for vector in range(1,len(fila)):
                        if vector2==vector:
                            print (" --> "+vector2 +  ": fin de destino")
                            return True
                        else:
                            self.recorrido.append(fila[0])
                            print ("--->" + fila[0])
                            try:
                                array.remove(fila)
                            except:
                                print ("Sin elementos")
                                return False
                            self.recorrer2(vector2,fila,array)




    def camino(self,vector1,vector2):
        caminos=[]
        visitados=[]
        c=1
        if self.existeVector(vector1) and self.existeVector(vector2):
            for fila in self.grafo:
                if fila[0]==vector1:
                    visitados.append(fila[0])
                    for vector in fila:
                        filas = []
                        filas.append(vector)
                        caminos.append(filas)
            for fila in range(1,len(caminos)):
                for caminosGrafo in range(1):
                    pass
            print(str(caminos))

        else:
            return False

    def existeVector(self,vector):
        for fila in self.grafo:
            if vector==fila[0]:
                return True
        return False

    def __str__(self):
        string=""
        for fila in self.grafo:
            string= string + str(fila)
        return string

'''
        if self.existeVector(vector1) and self.existeVector(vector2):
            rutas=[[]]
            caminos=[[]]
            visitados=[[]]
            imprimir=[[]]
            if vector1==vector2:
                print ("caminos: "+str(caminos))
                print ("")
                return True
            else:
                caminos.append(vector1)
                recorridos=[]
                for fila in grafo:
                    if fila[0]==vector1:
                        for i in range(1,len(fila)):
                            recorridos.append(fila[i])
                for nodoRecorrido in recorridos:
                    for fila in self.grafo:
                        for i in range(1,len(fila)):
                            if nodoRecorrido==len
                            
                            
                            
                            
                            
                            ####grafos####
class Grafos: listaGrafos=[]
    ori=0 #valor ingresado para origen
    des=0 #valor ingresado para destino
    recorrido=[] #recorrido guardado
    o=-1 #posicion del arreglo de origen
    d=-1 #posicion del arreglo de destino
    visitados=[] #arreglos visitados
    
    def crearGrafo(self): graf=[]
        band=0
        while band==0:
        print ("1.AGREGAR NODO") 
        print ("2.SALIR")
        opcion=str(input("ELIGE UNA OPCION : "))
        if opcion=="1": band2=0
            while band2==0: 
                try:
                    dato=int(input("Dame dato:"))
                    band2=1
                except ValueError:
                    print ("Debe colocar un numero")
                    graf.append(dato)
        elif opcion=="2": 
            band=1
            self.listaGrafos.append(graf)
        else:
            print ("Debe poner opcion correcta...")
    
    def verRecorrido(self): 
        band=0
        validar=0
        del self.recorrido[:] 
        v=0
        while band==0: 
            try:
                self.ori=int(input("Dame origen:"))
                self.des=int(input("Dame destino:"))
                band=1
            except ValueError:
                print ("Debe colocar un numero")
    #verifica si los datos obtenidos se encuentran como arreglos
        for i in range(len(self.listaGrafos)):
            lista=[]
            lista=self.listaGrafos[i]
            valor=lista[0]
            if self.ori==valor:
                self.o=i    #guarda la posicion origen  
                validar=validar+1 if self.des==valor:
                validar=validar+1
                self.d=i    #guarda la posicion destino
    #Valida si se encontro el destino y el origen
                if validar==2: 
                    self.recorrido.append(self.des) 
                    grafo.obtenerRecorrido(self.d)
    #Imprime el recorrido
                    for j in range (len(self.recorrido)-1):
                        print(str(self.recorrido[j])+"")
                        print (str(self.ori)) 
                else:
                    print ("Uno de los datos no se encuentra.")
    
    def obtenerRecorrido(self, pos):
    band=0 #Indica que no se encontro el final en el arreglo visitado=0
            #verifica si se ha visitado
    for i in range (len(self.visitados)): if self.visitados[i]==pos:
                    visitado=1
    #Si no lo ha visitado entra
    if visitado!=1: self.visitados.append(pos) lista=self.listaGrafos[pos] for j in range (len(lista)):
                    valor=lista[j]
                     #si encontro el final lo agrega
    if valor==self.ori: self.recorrido.append(valor) band=1
            #Si no encontro el final utiliza la recursividad
    if band==0:
    for k in range (1,len(lista)):
    valor=lista[k]
    for l in range(len(self.listaGrafos)):
    lista2=[] lista2=self.listaGrafos[l] if lista2[0]==valor:
                                self.recorrido.append(valor)
                                grafo.obtenerRecorrido(l)

'''
