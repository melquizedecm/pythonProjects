numeros=[]

numeros.append(1)  ##POSICION 0
numeros.append(2)  ##POSICION 1
numeros.append(4)  ##POSICION 2
numeros.append(5)  ##POSICIOP 3
numeros.append(6)  ##POSICION 4
numeros.append(2)  ##POSICION 5
numeros.append(3)  ##POSICION 6
numeros.append(4)  ##POSICION 7

##print(numeros)
##print(numeros[3])

###TRUCO 1.   COMO RECORRO UN ARREGLO
for num in numeros:  ##recorre todos lo numeros del arreglo y los agrega a la variable num
    print(num)

###TRUCO 2.   CARGAR VALORES EN MI ARREGLO
for i in range(0,10):
    numeros.append(i)