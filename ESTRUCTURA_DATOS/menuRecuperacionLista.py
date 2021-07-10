from Lista1 import *

lista=Lista()
papelera=Lista()


lista.agregarNodoDerecho("BERE")
lista.agregarNodoDerecho("RODRI")
lista.agregarNodoDerecho("JOSE")
lista.agregarNodoDerecho("ALDAIR")

lista.recorrerLista()

datoEliminar=raw_input("QUE DATO DESEAS ELIMINAR:")

if lista.eliminarNodo(datoEliminar):
    papelera.agregarNodoDerecho(datoEliminar)
    print("DatoEliminado: ", datoEliminar)


datoEliminar=raw_input("QUE DATO DESEAS ELIMINAR:")

if lista.eliminarNodo(datoEliminar):
    papelera.agregarNodoDerecho(datoEliminar)
    print("DatoEliminado: ", datoEliminar)




lista.recorrerLista()

print("\n\nPAPELERA DE RECICLAJE")
papelera.recorrerLista()

print ("\n\n\nRECUPERACION DE DATOS")
datoRecuperar=raw_input("Que dato deseas recuperar:")
if papelera.eliminarNodo(datoRecuperar):
    lista.agregarNodoDerecho(datoRecuperar)
    print("dato recuperado")

print("\n\nLISTA :  ")
lista.recorrerLista()

print("\n\nPAPELERA DE RECICLAJE")
papelera.recorrerLista()





