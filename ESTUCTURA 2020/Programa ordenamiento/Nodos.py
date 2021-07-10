class Nodo:
##METODOS
    refDer=None

##CONSTRUCTOR
    def __init__(self,dato):
        self.dato=int(dato)

    #def __str__(self):##Para que le lea el dato ya que lo lee como cadena de texto
        #return self.dato
##TODOS ESTOS MÉTODOS ES PARA ALMACENAR LOS DATOS DICHOS
    def setDato(self, nuevoDato):
        self.dato=nuevoDato

    def getDato(self):
        return self.dato

    def setRefDer(self,nodo):
        self.refDer=nodo

    def getRefDer(self):
        return self.refDer





