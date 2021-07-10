from Pila import *
####### programa principal ####

##### METER DATOS A LA PILA ####
dato="Jose"
pila=Pila(dato)
pila.push("Ricardo")
pila.push("Ana")
pila.push("Karla")
pila.push("Gerardo")

##### MOSTRAR PILA #####
pila.mostrarPila()


print("\n\n pop")
print(pila.pop())
print(pila.pop())
print(pila.pop())

print("\n\nDespues de eliminar")

pila.mostrarPila()
