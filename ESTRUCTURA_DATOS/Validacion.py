#############################################################
#       INSTITUTO TECNOLOGICO SUPERIOR PROGRESO             #
#       ANA VICTORIA PANANA GARCIA                          #
#       ING. ANIMACION DIGITAL Y EFECTOS VISUALES  2do sem  #
#       POO.  Prof. Melquizedec Moo Medina                  #
#       PROGRAMA: VALIDACION                                #
#############################################################

class Validacion: #Definiendo la clase Validacion

    #Asignacion de atributos
    entero=0
    flotante=0.0
    cadena=""
    dato=""

    def validarEntero(self,dato): #Definicion de metodo entero que verifica que dato se entero
        self.dato=dato
        try:
            if int(dato):
                return int(dato)
            else:
                return False
        except ValueError:
            return False

    # Definicion de metodo que verifica que dato sea flotante
    def validarFlotante(self,dato):
        self.dato=dato
        try:
            if float(dato):
               return True
            else:
               return False
        except:
            return False

    def rangoEntero(self,dato,minimo,maximo):#Definicion de rango entero que verifica si existe dato en un rango minimo,maximo y que todos sean enteros
        dato=self.validarEntero(dato)
        minimo=self.validarEntero(minimo)
        maximo=self.validarEntero(maximo)
        if (dato and minimo and maximo):
            if (dato >= minimo and dato <= maximo):
                return (dato)
        return False

    def validarString(self,dato): #Definicion de un metodo que valide si dato es de tipo cadena
        self.dato=dato
        try:
            if str(dato):
                return str(dato)
            else:
                return False
        except ValueError:
            return False

    def validarCadena(self,dato):  #definicion de un metodo que verifique una entrada de tipo entero y cuente el numero de digitos de la entrada
        dato=self.validarEntero(dato)
        if (dato):
            def cuantos_digitos(n):
                ind = 1
                while n > 9:
                    n = n / 10
                    ind = ind + 1
                print(ind)
        return False

    def validarCalificacion(self,dato):
        try:
            if 0<= float(dato) <=100:
                return dato
            else:
                return False
        except:
            return  False

    def validarRangoFlotante(self,minimo,maximo,dato):
        try:
            if minimo<= float(dato)<=maximo:
                return True
            else:
                return False
        except:
            return False

'''
while True:
    dato=raw_input("Escribe un valor flotante")
    validar=Validacion()
    if validar.validarFlotante(dato):
        print("El valor es flotante")
    else:
        print("El valor no es flotante")
'''