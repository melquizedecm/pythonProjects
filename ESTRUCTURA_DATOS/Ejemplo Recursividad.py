def funcion2(n):
    if n==0:
        return 0

    print ("funcion2")
    funcion1(n-1)

def funcion1(n):
    if n==0:
        return 0
    print ("funcion1")
    funcion2(n-1)

def Hanoi(n,Fuente,Auxiliar,Destino, mov=0):
    if(n == 1):
        mov+=1
        print Fuente,"a",Destino," Movimiento: ",mov
    else:
        Hanoi(n-1,Fuente,Destino,Auxiliar,mov)
        mov+=1
        print Fuente,"a", Destino,"Movimiento: ",mov
        Hanoi(n-1,Auxiliar,Fuente,Destino,mov)

Hanoi(3,1,2,3)

#print (funcion2(20))



