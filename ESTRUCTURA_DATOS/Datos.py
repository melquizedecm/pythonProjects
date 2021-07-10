#############################################################
#       INSTITUTO TECNOLOGICO SUPERIOR PROGRESO
#       PROGRAMM:  U1ADA04-  clase Datos
#       ING. ANIMACION DIGITAL Y EFECTOS VISUALES  3er.sem
#       POO.  Prof. Melquizedec Moo Medina
#       DATE:  08-SEP-2017
#       DESCRIPTION: contiene el ingreso de datos validados
#############################################################


from Validacion import *

validar=Validacion()

class Datos:
    def solicitarCalificacion(self):
        while True:
            dato=raw_input("Ingresa la calificacion:")
            if validar.validarCalificacion(dato):
                return float(dato)
            else:
                print("Error en la captura")



    def solicitarCalificacionesArreglo(self):
        c = 0
        calificaciones = []
        while True:
            print("calificacion " + str(c) + ":")
            calificaciones.append(self.solicitarCalificacion())
            opcion = raw_input("Deseas Ingresar otra calif? (Si/No): ")
            if opcion == "No":
                return calificaciones
            c += 1
