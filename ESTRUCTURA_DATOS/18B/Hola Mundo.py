class HolaMundo:

    def __init__(self):
        print("Soy el constructor")

    def getDatos(self):
        return "soy el dato a devolver"

class HolaMundo2:

    def obtenerValores(self):
        self.holaMundo1 = HolaMundo()
        self.miVariable=self.holaMundo1.getDatos()

    def getMiVariable(self):
        return  self.miVariable


objeto=HolaMundo2()
objeto.obtenerValores()
variableDatos=objeto.getMiVariable()
print(variableDatos)
