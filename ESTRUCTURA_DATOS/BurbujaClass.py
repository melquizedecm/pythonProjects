from time import time

cMemoria=0

def ordenamientoBurbuja(lista,tam):
    contadorCiclos=0
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(lista[j] > lista[j+1]):
                contadorCiclos+=1
                temp = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = temp
    print("El numero de comparaciones  fue: ", contadorCiclos)

def imprimeLista(lista,tam):
    for i in range(0,tam):
        print (lista[i])

def leeLista():
    lista=[]
    cn=int(input("Cantidad de numeros a ingresar: "))

    for i in range(0,cn):
        lista.append(int(input("Ingrese numero %d : " % i)))
    return lista

tiempoinicial=time()
A=leeLista()
ordenamientoBurbuja(A,len(A))
imprimeLista(A,len(A))
tiempofinal=time()
tiempoTotal=tiempofinal-tiempoinicial
print ("El tiempo de inicio del programa fue: ",tiempoinicial, " y termino en : ", tiempofinal)
print ("Tiempo total = ", tiempoTotal)
