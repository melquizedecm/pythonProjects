 ### PROGRAMA ORDENACION DE DATOS, METODO ORDENACION RAPIDA (QUICKSORT)

 ### IMPORTAMOS LA LIBRERIA MATH PARA UTILIZAR EL TRUNC ###
from math import trunc
 ### FUNCION INICIAR LA LISTA ###
def inicioquicksort(lista):
 ### LONGITUD DE LA LISTA ###
    espacio=0
    lista=quicksort(lista,0,len(lista)-1,espacio)
    return lista

 ### CREAMOS UNA LISTA ###
lista = []
 ### PREGUNTAMOS CUANTOS NUMEROS INGRESARA ###
cantidad = int(input("¿cuantos numeros deseas ingresar?:  "))
i = 1

 ### INGRESA LOS NUMEROS ###
while(cantidad  > 0 ):
    numero = int(input("numero #" + str(i) + ":  "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1



 ### ORDENACION DE LA LISTA ###
 ### FUNCION QUICSORT ###
def quicksort(lista,primero, ultimo,espacio):
 ### BUSCAMOS EL NUMERO CENTRAL ###
    central=trunc((primero+ultimo)/2)
 ### DECLARAMOS LAS VARIABLES ###
    pivote=lista[central]
    i=primero
    j=ultimo
    espacio+=4

 ### UTILIZAMOS LA RECURSIVIDAD ###
    while True:
 ### COMPARA EL DATO DE LA POSICION INICIAL CON EL PIVOTE ###
        while lista[i]<pivote:
 ### LA POSICION INICIAL RECORRE A LA DERECHA ###
            i=i+1
            espacio+=1
 ### SI NO, COMPARA EL DATO DE LA POSICION FINAL CON EL PIVOTE ###
        while lista[j]>pivote:
 ### LA POSICION FINAL RECORRE A LA IZQUIERDA ###
            j=j-1
            espacio+=1
 ### COMPARA LAS POSICIONES ###
        if i<=j:
 ### REALIZA LA FUNCION  INTERCAMBIO ###
            lista=intercambiar(lista,i,j)
 ### LOS DOS POSICIONES RECORREN ###
            i=i+1
            j=j-1
            espacio+=6
        else:
            break
 ## DIVISION DE LA LISTA ###
    if primero<j:
        quicksort(lista,primero,j,espacio)
    if i<ultimo:
        quicksort(lista,i, ultimo,espacio)
    return lista,espacio

 ### FUNCION INTERCAMBIAR ###
def intercambiar(lista,i,j):
 ### ALMACENA EL ELEMENTO ANTES DE INTERCAMBIAR ###
    aux = lista[i]
 ### HACE EL INTERCAMBIO ###
    lista[i] = lista[j]
    lista[j] = aux
    return lista



 ### IMPRIME LA LISTA ###
lista, espacio =inicioquicksort(lista)

espacio=int(espacio*4)
print (str(espacio*8) + "bits de memoria\n" + str(espacio) + "bytes de memoria RAM")



