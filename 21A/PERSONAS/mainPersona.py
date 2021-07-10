from Persona import *

print("BIENVENIDOS AL BANCO DE MEXICO")
nombre=input("Escribe el nombre del cuentahabiente:")
monto=input("indica el monto inicial a Depositar")
edad=input("indica la edad:")
monto= float(monto)

cuenta1= Cuentahabiente("01927",nombre,monto)
cuenta1.setEdad(edad)

print(cuenta1.retirar(600))

print(cuenta1)