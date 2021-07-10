class Persona():
    #metodo constructor
    def __init__(self, INE,nombre,ciudad,fecha,edad):
        self.__INE = INE
        self.nombre = nombre
        self.telefono = ""
        self.__ciudadNacimiento = ciudad
        self.__fechaNacimiento = fecha

    ###definir metodos GET Y SET
    def getINE(self):
        return self.__INE

    def getCiudadNacimiento(self):
        return  self.__ciudadNacimiento

    def getFechaNacimiento(self):
        return  self.__fechaNacimiento

    def setTelefono(self,nuevoTelefono):
        self.telefono=nuevoTelefono

    def __str__(self):
        return "Nombre: "+self.nombre +"\nTelefono: " + self.telefono + "\nCiudad: "+ self.__ciudadNacimiento

    def caminar(self):
        pass
    def comer(self):
        pass
    def correr(self):
        pass
    def dormir(self):
        pass

class Personaje():
    pass

class Estudiante():
    pass




