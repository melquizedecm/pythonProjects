class Persona:
    nombre=""
    __edad=0
    __peso=0
    __altura=0

    def __init__(self,nombre):
        self.nombre=nombre

    def setEdad(self,edad):
        self.__edad=edad

    def setPeso(self,peso):
        self.__peso=peso

    def setAltura(self,altura):
        self.__altura=altura

    def getEdad(self):
        return self.__edad

    def getPeso(self):
        return self.__peso

    def getAltura(self):
        return self.__altura


class Cuentahabiente(Persona):
    __id=""
    __saldo=0

    def __init__(self, id, nombre, monto):
        Persona.__init__(self, nombre)
        self.__id=id
        self.__saldo=monto

    def retirar(self,monto):
        if monto>self.__saldo:
            return False
        else:
            self.__saldo = self.__saldo - monto
            return True

    def depositar(self, monto):
        self.__saldo = self.__saldo + monto



    def __str__(self):
        return "El titular de la cuenta "+ self.__id + " es: " + self.nombre + " y con saldo de: " + str(self.__saldo) + " y tiene una edad de: "+ str(self.getEdad()) + " años."


class Estudiante(Persona):
    pass


class Paciente(Persona):
    pass

