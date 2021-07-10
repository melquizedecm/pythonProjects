from Lista import *

lista=None

while(True):
    print("\n\nMENU:\n")
    print("1. INICIALIZAR LISTA. ")
    print("2. AGREGAR UN NODO")
    print("3. ELIMINAR UN NODO")
    print("4. BUSCAR UN NODO")
    print("5. IMPRIMIR LISTA")
    print("6. LISTA ESTA VACIA?")
    print("7. SALIR\n")

    opcion=input("ESCOGE UNA OPCION:")
    if opcion=="1":
        lista=Lista()
    elif opcion=="2":
        dato=input("Dame el valor del Nodo")
        lista.agregarNodo(dato)
    elif opcion=="3":
        dato=input("Dame el dato a eliminar")
        lista.eliminarNodo(dato)
    elif opcion=="4":
        dato=input("Dame el valor a buscar")
        if lista.buscarNodo(dato):
            print(dato, "encontrado")
        else:
            print(dato, "No existe en la lista")
    elif opcion=="5":
        lista.imprimir()
    elif opcion=="6":
        if lista.hayNodos():
            print("La lista contien datos")
        else:
            print("La lista esta vacia")
    elif opcion=="7":
        break
    else:
        print("Elige una opcion valida")