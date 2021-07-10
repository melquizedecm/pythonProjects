#############################################################
#       AUTHOR: MELQUIZEDEC MOO MEDINA                      #
#       PROGRAMA: grafoMenu.py                              #
#       Description: PROGRAMA PRINCIPAL PARA USAR EL GRAFO  #
#       DATE:  12/SEP/2020                                  #
#############################################################
from Grafo import *

grafo=Grafo()
while True:
    print("\n\n MENU \n")
    print("1. AGREGAR VECTOR")
    print("2. VINCULAR VECTORES")
    print("3. RECORRER CAMINOS")
    print("4. VER GRAFO")
    print("5. SALIR")
    opcion=input("Selecciona una opcion: ")
    if(opcion=="1"):
        vector=input("Indica el vector a agregar")
        if grafo.ingresarNodo(vector):
            print("Vector agregado")
        else:
            print("No se pudo agregar:  Vector ya existe")
    elif (opcion=="2"):
        vector1=input("Escribe el primer vector a  vincular: ")
        vector2=input("Escribe el segundo vector a  vincular: ")
        if grafo.relacionar(vector1,vector2):
            print ("Vectores Relacionados exitosamente")
        else:
            print ("Hubo un error en los vectores, verifique su informacion")
    elif (opcion=="3"):
        vector1 = input("Escribe el primer vector de inicio: ")
        vector2 = input("Escribe el segundo vector final: ")
        grafo.recorrerCamino1(vector1,vector2)
        print(grafo.camino)

    elif (opcion=="4"):
        print(grafo)
    elif(opcion=="5"):
        print("Adios")
        break
    else:
        print("Opcion no valida")


'''
#Creador: Eduardo Javier Maldonado Acevedo
#Carrera: Ingenieria en informatica
import os

class Grafos:
    def __init__(self):
        self.grafo = {}

    def menu(self):
        print """>=================== Grafo =================<
[1] Agregar dato
[2] Mostrar grafo
[3] Recorrido en profundidad
[4] Recorrido en anchura
[0] Salir
>===========================================<"""

    def seleccion(self):
        while True:
                os.system("cls")
                g.menu()
                opcion = raw_input(">=> Ingresa tu opcion: ")
                if opcion=="1":
                 g.agregar()
                elif opcion=="2":
                 print "Los destinos agregados son: "
                 g.mostrar()
                 os.system("pause")
                elif opcion=="3":
                 print "Recorrido en Profundidad"
                 eleccion = raw_input("Ingresa el nodo de inicio: ")
                 g.profundidad(eleccion)
                elif opcion=="4":
                 print "Recorrido en Anchura"
                 eleccion = raw_input("Ingresa el nodo de inicio: ")
                 g.anchura(eleccion)
                elif opcion=="0":
                    break
                else:
                 print "No has ingresado una opcion correcta"
                 os.system("pause")

    def profundidad(self,eleccion):
        visitados=[]
        pila=[]
        imprimir=[]
        pila.append(eleccion)
        visitados.append(eleccion)
        if eleccion in self.grafo:
            while pila:
                x = pila[-1]
                print "Pila:",pila
                imprimir.append(x)
                pila.remove(pila[-1])
                for key,nada in self.grafo[x]:
                    if key not in visitados:
                        visitados.append(key)
                        pila.append(key)
            print "=========Resultados========="
            print "Visitados:",visitados
            print "Imprimir:",imprimir
            print "Pila:",pila
            os.system("pause")
        else:
            print "No existe"
            os.system("pause")

    def anchura(self,eleccion):
       visitados=[]
       cola=[]
       imprimir=[]
       cola.append(eleccion)
       visitados.append(eleccion)
       if eleccion in self.grafo:
           while cola:
               x = cola[0]
               print "Cola:",cola
               imprimir.append(x)
               cola.pop(0)
               for key,nada in self.grafo[x]:
                   if key not in visitados:
                       visitados.append(key)
                       cola.append(key)
           print "=========Resultados========="
           print "Visitados:",visitados
           print "Imprimir:",imprimir
           print "Cola:",cola
           os.system("pause")
       else:
           print "No existe"
           os.system("pause")

    def agregar(self):
        origen = raw_input("Ingresa tu Origen: ")
        destino = raw_input("Ingresa tu Destino: ")
        peso = raw_input("Ingresa el peso: ")
        if origen in self.grafo:
            if destino in self.grafo:
                lista = self.grafo[origen]
                self.grafo[origen] = lista+[(destino,peso)]
                lista = self.grafo[destino]
                lista.append((origen,peso))
                self.grafo[destino] = lista
                print("Datos agregados de forma correcta")
                os.system("pause")
            else:
                self.grafo[destino] = [(origen,peso)]
                lista = self.grafo[origen]
                lista.append((destino,peso))
                self.grafo[origen] = lista
                print("Datos agregados de forma correcta")
                os.system("pause")
        elif destino in self.grafo:
            self.grafo[origen] = [(destino,peso)]
            lista = self.grafo[destino]
            lista.append((origen,peso))
            self.grafo[destino] = lista
            print("Datos agregados de forma correcta")
            os.system("pause")
        else:
            self.grafo[destino] = [(origen,peso)]
            self.grafo[origen] = [(destino,peso)]
            print "Datos agregados de forma correcta"
            os.system("pause")

    def mostrar(self):
        for key, lista in self.grafo.items():
            print key
            print lista

g = Grafos()
g.seleccion()
'''