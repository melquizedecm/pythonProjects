#############################################################
#       INSTITUTO TECNOLOGICO SUPERIOR PROGRESO
#       PROGRAMM:  U1ADA04
#       ING. ANIMACION DIGITAL Y EFECTOS VISUALES  3er.sem
#       POO.  Prof. Melquizedec Moo Medina
#       DATE:  08-SEP-2017
#       DESCRIPTION:
#############################################################

from Datos import *
datos = Datos()
validar=Validacion()

############## BLOQUE DE SOLICITUD DE DATOS ###############
calificaciones=datos.solicitarCalificacionesArreglo()

############### BLOQUE DE IMPRESION  ###############
sumaCalificaciones=0.0
for c in range(0,len(calificaciones),1):
    if  validar.validarRangoFlotante(0,69,calificaciones[c]):
        print ("{0:.2f}".format(calificaciones[c]) + "No Aprobado ")
    else:
        print ("{0:.2f}".format(calificaciones[c])+ "Aprobo ")
    sumaCalificaciones+=calificaciones[c]

############### CALCULO EM IMPRESION DEL PROMEDIO ###############
promedio=sumaCalificaciones/ len(calificaciones)
print("El promedio del grupo es: " + "{0:.2f}".format(promedio))



