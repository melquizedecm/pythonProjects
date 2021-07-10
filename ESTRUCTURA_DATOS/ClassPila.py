from classLista import  *
class Pila:
    cima=None
    base=None
    def __init__(self):
        self.pila=Lista()

    def push(self,data):
        self.pila.agregarNodoDerecho(data)


