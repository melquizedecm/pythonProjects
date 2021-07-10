class Figuras:
    def __init__(self):
        self.area=0
        self.color=(255,255,255)#rgb
        self.contorno=0

    def setColor(self):
        pass

    def __str__(self):
        return "El area es: " + str(self.area)

class Circulo(Figuras):
    def __init__(self,radio):
        Figuras.__init__(self) ##cobrar la herencia
        self.radio=radio

    def setRadio(self,radio):
        self.radio=radio

    def calcularArea(self):
        #area=3.14159 *radio *radio
        self.area=3.14159*self.radio*self.radio

class Triangulo(Figuras):
    def __init__(self,base, altura):
        Figuras.__init__(self)
        self.base=base
        self.altura=altura

    def setBase(self,base):
        self.base=base

    def setAltura(self,altura):
        self.altura=altura

    def calcularArea(self):
        self.area=self.base*self.altura/2


