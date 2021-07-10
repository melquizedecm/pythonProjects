### RECUPERACION DE DATOS EN UNA LISTA ORDENADA ###

 ### IMPORTAMOS LA LIBRERIA MATH PARA UTILIZAR EL TRUNC ###
from math import trunc
 ### FUNCION INICIAR LA LISTA ###
def inicioquicksort(lista):
 ### LONGITUD DE LA LISTA ###
    lista=quicksort(lista,0,len(lista)-1)
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
def quicksort(lista,primero, ultimo):
 ### BUSCAMOS EL NUMERO CENTRAL ###
    central=trunc((primero+ultimo)/2)
 ### DECLARAMOS LAS VARIABLES ###
    pivote=lista[central]
    i=primero
    j=ultimo

 ### UTILIZAMOS LA RECURSIVIDAD ###
    while True:
 ### COMPARA EL DATO DE LA POSICION INICIAL CON EL PIVOTE ###
        while lista[i]<pivote:
 ### LA POSICION INICIAL RECORRE A LA DERECHA ###
            i=i+1
 ### SI NO, COMPARA EL DATO DE LA POSICION FINAL CON EL PIVOTE ###
        while lista[j]>pivote:
 ### LA POSICION FINAL RECORRE A LA IZQUIERDA ###
            j=j-1
 ### COMPARA LAS POSICIONES ###
        if i<=j:
 ### REALIZA LA FUNCION  INTERCAMBIO ###
            lista=intercambiar(lista,i,j)
 ### LOS DOS POSICIONES RECORREN ###
            i=i+1
            j=j-1
        else:
            break
 ## DIVISION DE LA LISTA ###
    if primero<j:
        quicksort(lista,primero,j)
    if i<ultimo:
        quicksort(lista,i, ultimo)
    return lista

 ### FUNCION INTERCAMBIAR ###
def intercambiar(lista,i,j):
 ### ALMACENA EL ELEMENTO ANTES DE INTERCAMBIAR ###
    aux = lista[i]
 ### HACE EL INTERCAMBIO ###
    lista[i] = lista[j]
    lista[j] = aux
    return lista
 ### IMPRIME LA LISTA ###
print("Lista: ", inicioquicksort(lista))

##############################
###                        ###
###  SEPARADOR DE CODIGOS  ###
###                        ###
##############################

### INICIAMOS LA LISTA PAPELERA ###
papelera = []
bandera = 1

### ELIMINA LOS DATOS DE LA LISTA Y LOS AGREGA A LA PAPELERA ###
while (bandera==1):
    var = int(input("¿Qué numero deseas eliminar?:  ")) ### PREGUNTA QUE DATO SE ELIMINARA ###
    if var in lista:                                    ### ASEGURARNOS QUE EL DATO A "ELIMINAR" ESTE EN LA LISTA ###
        papelera.append(var)                            ### AGREGAR DATO A LA PAPELERA ###
        lista.remove(var)                               ### ELIMINAR DATO DE LA LISTA ###
    else:
        print("Favor de ingresar un numero de la lista") ### EN CASO DE PONER UN DATO FUERA DE LA LISTA PREGUNTAR SI QUIEREN ELIMINAR OTRO NUMERO ###
    print("Lista: ", (lista))
    print("Papelera: ", (papelera))
    bandera = int(input("Desea eliminar otro numero?('1' para continuar):")) ### VERIFICAR SI QUIEREN CONTINUAR ###



### PREGUNTAR SI SE QUIEREN REGRESAR DATOS DE LA PAPELERA A LA LISTA ORIGINAL ###
bandera = int(input("Desea recuperar algun numero?('1' para continuar): "))
while (bandera==1):
    var = int(input("Numero a recuperar: "))            ### INGRESA DATO POR RECUPERAR ###
    if var in papelera:                                 ### VER SI EL DATO POR RECUPERAR ESTA EN LA LISTA ###
        lista.append(var)                               ### AGREGAR EL DATO A LA LISTA ###
        papelera.remove(var)                            ### ELIMINAR EL DATO DE LA PAPELERA ###
    else:
        print("Favor de ingresar un numero de la papelera") ### PREGUNTAR SI QUIEREN INTENTAR CON OTRO DATO A RECUPERAR ###
    ### ACOMODAR LISTA EN ORDEN DE MENOR A MAYOR ###
    print("Lista: ", inicioquicksort(lista))
    ### IMPRIMIR PAPELERA ###
    print("Papelera: ", (papelera))
    bandera = int(input("Desea recuperar otro numero?('1' para continuar): ")) ### VERIFICAR SI QUIEREN CONTINUAR ###




