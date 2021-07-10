from Lista import *
from Validacion import *


def busqueda_binaria(lista, x):
    """Busqueda binaria
    Precondicion: lista esta ordenada
    Devuelve -1 si x no esta en lista;
    Devuelve p tal que lista[p] == x, si x esta en lista
    """

    # Busca en toda la lista dividiendola en segmentos y considerando
    # a la lista completa como el segmento que empieza en 0 y termina
    # en len(lista) - 1.

    izq = 0  # izq guarda el indice inicio del segmento
    der = len(lista) - 1  # der guarda el indice fin del segmento

    # un segmento es vacio cuando izq > der:
    while izq <= der:
        # el punto medio del segmento
        medio = (izq + der) / 2

        print "DEBUG:", "izq:", izq, "der:", der, "medio:", medio

        # si el medio es igual al valor buscado, lo devuelve
        if lista[medio] == x:
            return medio

        # si el valor del punto medio es mayor que x, sigue buscando
        # en el segmento de la izquierda: [izq, medio-1], descartando la
        # derecha
        elif lista[medio] > x:
            der = medio - 1

        # sino, sigue buscando en el segmento de la derecha:
        # [medio+1, der], descartando la izquierda
        else:
            izq = medio + 1
            # si no salio del ciclo, vuelve a iterar con el nuevo segmento

    # salio del ciclo de manera no exitosa: el valor no fue encontrado
    return -1


# Codigo para probar la busqueda binaria
def main():
    validar=Validacion()
    CL = Lista
    lista = CL.Lista()
    lista.agregarNodo(20)
    lista.agregarNodo(30)
    lista.agregarNodo(50)
    lista.agregarNodo(70)
    lista.agregarNodo(90)
    x = validar(input("Valor buscado?: "))
    print lista.longitud()

    #lista = input("Dame una lista ordenada ([[]] para terminar): ")
    #while lista != [[]]:

      #  resultado = busqueda_binaria(lista, x)
      #  print "Resultado:", resultado
      #  lista = input("Dame una lista ordenada ([[]] para terminar): ")

main()
