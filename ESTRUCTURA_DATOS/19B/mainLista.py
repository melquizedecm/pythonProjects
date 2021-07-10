########## PROGRAMA PRINCIPAL########
from ListaCircular import *

while True:
    print("PROGRAMA PARA CONTROL DE LISTAS ENLAZADAS\n\n")
    print("MENU")
    print("1. INICIALIZAR LISTA")
    print("2. INGRESE NODOS A LA LISTA")
    print("3. ELIMINE NODOS DE LA LISTA")
    print("4. BUSCAR UN NODO")
    print("5. IMPRIMIR LISTA")
    print("6. COMPROBAR SI LISTA ESTA VACIA")
    print("7. SALIR\n")

    opcion = input ("SELECCIONA UNA OPCION : _")

    if opcion=="1":
        dato= input("\nPara inicializar un dato, Escribe el primer Elemento de la lista:")
        lista = ListaCircular(dato)

    elif opcion=="2":
        dato = input("\nEscribe el elemento a Insertar a la lista: _")
        lista.insertarNodo(dato)

    elif opcion=="3":
        dato = input("\nEscribe el elemento a Eliminar de la lista: _")
        lista.eliminarNodo(dato)

    elif opcion=="4":
        pass

    elif opcion=="5":
        print("\n\n ** IMPRESION DE LISTA ** \n ")
        lista.recorrerLista()
        print("\n ** FIN DE LISTA ** \n")

    elif opcion=="6":
        pass

    elif opcion=="7":
        break

    else:
        print("\n\n OPCION INVALIDA\n\n")

