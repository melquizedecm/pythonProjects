def busquedaBinaria(lista,elemento):
    pi= 0
    pf= len(lista)-1 #posicion final es igual a tamaño de la lista -1
    while (pi<pf): # posicion inicial es menor que posicion final
        pm=int((pi+pf)/2) #aqui realiza la division para dividir la lista a la mitad, para buscar la posicin media
        if (lista[pm])==elemento: #en el if valida si la posicion media del arreglo es el que se esta buscan
            return pm       #si es retorna a la posicion media
        elif (lista[pm]<elemento): #en este caso valida si es menor que posicion media
            pi = pm + 1         #se le agrega 1 para que este busque la siguiente posicion de la segunda mitad
        else:
            pf = pm -1            # en donde resta esta buscando la primera mitad de arreglo.
        return -1 #retorna -1 por que no lo encontro

def main():
    lista =[3,4,6,8,10,15,34,45,67,89,100,102,109] #valores de menor a mayor.
    elemento =-2 #buscamos un elemento por ejemplo en este cas estaremos buscando el 34
    pos = busquedaBinaria(lista,elemento) #llamamos a la funcion busquedabinaria en a cual se coloca la lista y el elemento que estamos buscando.
    if (pos>-1):  #si la posicion es mayor que -1
        print("el elemento se encuentra en la posicion: ", pos)
    else:
        print("el elemento no se encuentra en la lista")

main()