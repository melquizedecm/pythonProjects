from Figuras import *


while True:
    print("PROGRAMA PARA CALCULAR AREAS DE FIGURAS\n")
    print("MENU")
    print("1. CIRCULO")
    print("2. TRIANGULO")
    print("3. CUADRO")
    print("4. RECTANGULO")
    print("5. POLIGONO")
    print("6. SALIR")
    opcion=input("Selecciona una opcion:  ")
    if opcion=="1":
        print("Has seleccionado el área de un CIRCULO:")
        radio=input("Escribe el radio:")
        circulo1=Circulo(float(radio))
        circulo1.calcularArea()
        print (circulo1)
    elif opcion=="2":
        print("Has seleccionado el área de un TRIANGULO:")
        base=input("Escribe la base del Triangulo")
        altura = input("Escribe la altura del Triangulo")
        triangulo1=Triangulo(float(base), float(altura))
        triangulo1.calcularArea()
        print(triangulo1)


    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        print("Adiós, Gracias por Utilizar el programa")
        break

