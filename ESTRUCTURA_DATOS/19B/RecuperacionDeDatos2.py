### PROGRAMA PARA LA RECUPERACION DE DATOS DE UNA LISTA ###

 ### CREAMOS las listas ###
lista = []
papelera = []
posicion = []

 ### PREGUNTAMOS CUANTOS NUMEROS INGRESARA ###
cantidad = int(input("¿cuantos numeros deseas ingresar?:  "))

 ### INGRESA LOS NUMEROS ###
i = 1
while(cantidad  > 0 ):
    numero = int(input("numero #" + str(i) + ":  "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1

print("Lista: ", (lista))

listaref = []
listaref.extend(lista)

bandera = 1
### ELIMINA LOS DATOS DE LA LISTA Y LOS AGREGA A LA PAPELERA ###
while (bandera==1):
    var = int(input("¿Qué numero deseas eliminar?:  ")) ### PREGUNTA QUE DATO SE ELIMINARA ###
    if var in lista:                         ### ASEGURARNOS QUE EL DATO A "ELIMINAR" ESTE EN LA LISTA ###

        papelera.remove(var)


    else:
        print("Favor de ingresar un numero de la lista") ### EN CASO DE PONER UN DATO FUERA DE LA LISTA PREGUNTAR SI QUIEREN ELIMINAR OTRO NUMERO ###
    ### IMPRIMIR LISTA Y PAPELERA ###
    print("Lista: ", (lista))
    print("Papelera: ", (papelera))
    print("Posicion: ", (posicion))
    bandera = int(input("Desea eliminar otro numero?('1' para continuar):")) ### VERIFICAR SI QUIEREN CONTINUAR ###

### PREGUNTAR SI SE QUIEREN REGRESAR DATOS DE LA PAPELERA A LA LISTA ORIGINAL ###
bandera = int(input("Desea recuperar algun numero?('1' para continuar): "))
while (bandera==1):
    var = int(input("Numero a recuperar: ")) ### INGRESA DATO POR RECUPERAR ###
    if var in papelera:                      ### VER SI EL DATO POR RECUPERAR ESTA EN LA LISTA ###

        pos=papelera.index(var)              ### ASIGNA A POS EL INDICE DE POSICION DE NUESTRO NUMERO EN LA LISTA PAPELERA ###
        posaux=posicion[pos]                 ### EVALUAMOS A POS EN LA LISTA DE POSICION Y LO GUARDAMOS COMO POSAUX ###
        contador=0                           ### CREAMOS UN CONTADOR ###
        posaux2=posaux                       ### CREAMOS LA VARIABLE AUXILIAR DE POSAUX: POSAUX2
        while contador<len(posicion):        ### CORRE EL CODIGO MIENTRAS EL CONTADOR SEA MENOR AL NUMERO DE DATOS EN LA LISTA POSICION ###
            if posaux>posicion[contador]:    ### COMPARA EL INDICE DE NUESTRO NUMERO PARA VER SI HAY ALGUN OTRO INDICE MENOR ###
                posaux2=posaux2-1            ### EN CASO DE HABER UN INDICE MENOR LE RESTAMOS A POSAUX 1 PARA QUE AL MOMENTO DE TRAERLO A LA LISTA LO TOME EN CUENTA EL NUMERO DE LA PAPELERA ###
            contador=contador+1
        lista.insert(posaux2,var)            ### INSERTAMOS A LA LISTA NUESTRO NUMERO EN LA POSICION POSAUX ###
        papelera.remove(var)                 ### BORRAMOS NUESTRO NUMERO DE LISTA DE PAPELERA ###
        posicion.remove(posaux)              ### BORRAMOS EL INDICE DE NUESTRO NUMERO DE LA PAPELERA EN LA LISTA DE POSICIONES ###
    else:
        print("Favor de ingresar un numero de la papelera") ### PREGUNTAR SI QUIEREN INTENTAR CON OTRO DATO A RECUPERAR ###
    ### IMPRIMIMOS LAS LISTAS ###
    print("Lista: ", (lista))
    print("Papelera: ", (papelera))
    print("Posicion: ", (posicion))
    bandera = int(input("Desea recuperar otro numero?('1' para continuar): ")) ### VERIFICAR SI QUIEREN CONTINUAR ###
