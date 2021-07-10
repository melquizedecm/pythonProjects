from Arbol import *

existenDatos = False

if __name__ == "__main__":
    arbol = Arbol()
    while(True):
        print("--------------------------")
        print("---MENU---\n"+
              "1. AGREGAR DATO\n"+
              "2. RECORRER EL ARBOL\n" +
              "3. BUSCAR UN DATO\n" +
              "4. ELIMINAR UN DATO\n"
              "5. SALIR\n")

        print("--------------------------")
        opcion = input("Ingrese una opción:")
        if opcion == "1":
            print("---------------------------")
            nodo =input("Ingrese el nodo:")
            print("----------------------------")
            arbol.insertarNodo(nodo)
            print("Nodo agregado")
            print("---------------------------")
            existenDatos = True

        elif opcion == "2":
            if existenDatos:
                print("---Recorrer el arbol:---\n" +
                      "1. Pre-orden\n" +
                      "2. In-orden\n" +
                      "3. Post-orden\n")
                print("----------------------------")
                num = input("Ingrese una opcion:")
                print("----------------------------")
                if num == "1":
                    print("Imprimiendo por Pre-orden:")
                    arbol.preorden(arbol.raiz)
                elif num == "2":
                    print("Imprimiendo por In-orden:")
                    arbol.inorden(arbol.raiz)
                elif num == "3":
                    print("Imprimiendo por Post-orden:")
                    arbol.postorden(arbol.raiz)
                else:
                    print("-----------------------------")
                    print("**Escoga una opcion valida**")
            else:
                print("-------------------------------")
                print("**Deben existir datos primero**")

        elif opcion == "3":
            print("---------------------------")
            nodoB = input("Ingrese el nodo a buscar:")
            print("----------------------------")
            dato = arbol.encontrar(nodoB)
            if dato == True:
                print("Dato encontrado :D")
            else:
                print("Dato no encontrado :C")

        elif opcion == "4":
            print("---------------------------")
            nodoE = input("Ingrese el nodo a eliminar:")
            print("----------------------------")
            #arbol.eliminar(arbol.raiz, nodoE, None)
            arbol.eliminarNodo(nodoE)

        elif opcion == "5":
            break

        else:
            print("-----------------------------")
            print("**Escoga una opcion valida**")






#"---Menu---\n"+
              #"1. Agregar\n"+
              #"2. Preorder\n"+
              #"3. Postorder\n"+
              #"4. Inorder\n"