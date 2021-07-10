class Cuenta:
    numeroCuenta=""
    pin=""
    saldo=0.0

    def __init__(self,numeroCuenta,pin,saldo):
        try:
            self.numeroCuenta=numeroCuenta
            self.pin=pin
            self.saldo=float(saldo)
        except ValueError:
            pass

    def consultar(self):
        return self.saldo

    def retirar(self,monto):
        try:
            if float(monto)<=self.saldo:
                self.saldo=self.saldo - float(monto)
                return  self.saldo
            else:
                return False
        except ValueError:
            return False

    def cambiarPin(self,nuevoPin):
        self.pin=nuevoPin


