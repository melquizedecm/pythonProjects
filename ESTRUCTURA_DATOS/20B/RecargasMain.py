from RecargasClass import *
from test_validar import *

sistemaRecargas=[]
while True:
    print("##############################")
    print("\n\nMENU DE RECARGAS\n")
    print("1. REALIZAR UNA RECARGA\n")
    print("2. VER LISTA DE RECARAS\n")
    print("3. \n")
    print("4. REALIZAR UNA RECARGA\n")
    print("5. REALIZAR UNA RECARGA\n")
    opcion=input("ELIGE UNA OPCIÓN:")
    print (opcion)
    if opcion=="1":
         numero=""
         while True:
            numero=input("Dame el numero telefónico")
            if (esTelefono(numero)):
                break
            else:
                print("El numero es equivocado")


         recarga= Recargas("9982324","telcel",100)
         sistemaRecargas.append(recarga)
         print(sistemaRecargas)
         print(sistemaRecargas[0].numero)
    elif opcion=="2":
        for registro in sistemaRecargas:
            print(registro.numero)
            print(registro.compania)
            print(registro.monto)
            print(registro.hora)
        a=input("Presiona una tecla para continuar")
    elif opcion=="3":
        total=0
        for registro in sistemaRecargas:
            total=total+float(registro.monto)
        print(total)
        a = input("Presiona una tecla para continuar")
    elif opcion=="4":
        pass
    elif opcion =="5":
        break

