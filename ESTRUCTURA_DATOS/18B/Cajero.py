from CuentaClass import *

class Cajero:
    cuentas=[]

    def __init__(self):
        while True:
           numeroCuenta=raw_input("Dame el numero de cuenta (escribe False para salir.): ")
           if numeroCuenta=="False":
               break
           pin= input("Dame el pin a utilizar: ")
           try:
               saldo=float(raw_input("Escribe el saldo para iniciar la cuenta:"))
               cuenta=Cuenta(numeroCuenta,pin,saldo)
               self.cuentas.append(cuenta)
           except ValueError:
               print "Error en el saldo"

    def imprimirCuentas(self):

        for cuenta in self.cuentas:
            print(cuenta.numeroCuenta, cuenta.pin,str(cuenta.saldo))







