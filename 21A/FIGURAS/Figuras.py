class Figuras:
    def __init__(self):
       self.color=(255,255,255)
       self.area=0

    def cambiarColor(self,nuevoColor):
        self.color=nuevoColor

    def calcularArea(self):
        print("falta definir el tipo de figura")

    def operacionNumeros(self, a=1, b=1):
        if a==int(a) and b==int(b):
            return a+b
        if float(a) and float(b):
            return a*b

class Triangulo(Figuras):
    def __init__(self):
        self.base=0
        self.altura=0

    def calcularArea(self):
        # a=(b x h)/2
        self.area=(self.base * self.altura)/2

class Circulo(Figuras):
    def __init__(self,radio):
        Figuras.__init__(self)
        self.radio=radio

    def calcularArea(self):
        # 3.14159 * r*r
        self.area= 3.14159 * self.radio * self.radio

class Cuadrado(Figuras):
    def __init__(self):
        Figuras.__init__(self)
        self.lado=0

    def calcularArea(self):
        #area= lado*lado
        self.area=self.lado*self.lado

class Rectangulo(Figuras):
    def __init__(self):
        Figuras.__init__(self)
        self.base=0
        self.altura=0


    def calcularArea(self):
        # area = base * altura
        self.area= self.base*self.altura