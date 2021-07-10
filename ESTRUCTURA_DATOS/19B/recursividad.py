def a(contador):
    if contador>0:
        contador=contador-1
        print("funcion A",contador)
        b(contador)
    else:
        return False

def b(contador):
    if contador > 0:
        contador = contador - 1
        print("funcion B", contador)
        a(contador)
    else:
        return False


a(10)