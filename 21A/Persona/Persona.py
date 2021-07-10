class Persona:
    nombre=""
    edad=0
    altura=0
    peso=0

    def __init__(self, nombre):
        self.nombre=nombre

    def setNombre(self,nuevoNombre):
        self.nombre=nuevoNombre

    def setEdad(self,nuevaEdad):
        self.edad=nuevaEdad

    def setAltura(self,nuevaAltura):
        self.altura=nuevaAltura

    def setPeso(self,nuevoPeso):
        self.peso=nuevoPeso

class Estudiante(Persona):
    __matricula=""
    promedio=0

    def __init__(self,matricula, nombre):
        Persona.__init__(self, nombre)
        self.__matricula=matricula

    def setPromedio(self,nuevoPromedio):
        self.promedio=nuevoPromedio

    def setMatricula(self,nuevaMatricula):
        self.__matricula=nuevaMatricula

    def __str__(self):
        return "Nombre: " + self.nombre + " matricula: "+ self.__matricula + " promedio: " + self.promedio

class Paciente(Persona):
    __id=""
    __tipoSangre=""

    def __init__(self, id, nombre, edad, peso, altura, tipoSangre):
        Persona.__init__(self,nombre)
        self.edad=edad
        self.peso=peso
        self.altura=altura
        self.__tipoSangre=tipoSangre
        self.__id=id

class Cuentahabiente(Persona):
    __id=""
    __saldo=0.0

    def __init__(self, nombre, montoInicial):
        Persona.__init__(self,nombre)
        self.__saldo=montoInicial

    def depositar(self, monto):
        self.__saldo=self.__saldo+monto

    def retirar(self,monto):
        if monto<self.__saldo:
            return False
        else:
            self.__saldo=self.__saldo-monto
            return True
