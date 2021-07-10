def main():

    i = 0
    vec = [3,65,8,1,2,88,9,0,6,2] #arreglo
    encontro = False #se declara una variable para saber si se encontro o no

    numero =int(input("ingrese un numero: ")) #se ingresa un numero para pode ingresar

    while(not(encontro) and i < 10): #la variable de not(hace que se inviertan los valores)busca si la variable es menor a 10
        if(numero == vec[i]):  #si el numero es igual al arreglo de la posicion i
            encontro = True              #si es cierto lo encontro
            pos = i                      #la posicion es igual a i (se le asigna)

        i = i + 1        #a la i sele agrega 1

    if(encontro):
        print("El dato se encuentra y esta en la posicion: " + str(pos + 1))
#en caso de ser cierto y que haya encontrado dira en donde se encuentra la posicion.
    else:
        print("el elemento no se encuentra en la lista")
main()