import time
def ordenar(lista):
    signo=1
    while signo:
        for i in range(len(lista)-1):
            signo=0
            if lista[i]>lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                signo=1

    print (lista)


lista=[4,2,7,9,6,8,5]

tiempo=time.time()
ordenar(lista)
tiempo_final=time.time()
print (tiempo_final-tiempo)