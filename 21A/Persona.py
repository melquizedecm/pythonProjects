class Persona():
####metodo constructor
    def __init__(self, ine,ciudad,fecha,nombre,tel):
        self.__INE = ine
        self.__ciudadNacimiento = ciudad
        self.__fechaNacimiento = fecha
        self.nombre = nombre
        self.telefono = tel

###metodo string
    def __str__(self):
        return "Nombre: " + self.nombre + "\n Ciudad: " + self.__ciudadNacimiento

##metodos GET y SET
    def getINE(self):
        return self.__INE

    def getCiudad(self):
        return self.__ciudadNacimiento

    def getFecha(self):
        return self.__fechaNacimiento

    def getNombre(self):
        return self.nombre

    def setNombre(self,nuevoNombre):
        self.nombre=nuevoNombre

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, nuevoTelefono):
        self.telefono= nuevoTelefono

#Metodos PROPIOS de la Clase
    def caminar(self):
        return  "Estoy caminando"

    def comer(self):
        return "Estoy comiendo"

    def correr(self):
        return "estoy corriendo"

    def dormir(self):
        return  "Estoy durmiendo"