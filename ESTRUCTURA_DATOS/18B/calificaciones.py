######################################################
########################################################################################
########################################################################################
# Program Name: calificaciones.py
# Authors: Melquizedec Moo Medina
# Description:  Programa que lee una cantidad de calificaciones y calcula el promedio


numeroCalificaciones=0
while True:
    numeroCalificaciones=raw_input("Escribe la cantidad de alumnos:")
    try:
        if int(numeroCalificaciones):
            numeroCalificaciones=int(numeroCalificaciones)
            break
    except ValueError:
        print("Error: ")

suma=0
calificacion=[]  ##INICAILIZO MI ARREGLO

for i in range(0,numeroCalificaciones):
    while True:
        try:
            calificacionAlumno = int(raw_input("Escribe la calificacion ["+str(i)+"]:"))
            calificacion.append(calificacionAlumno)
            if calificacion[i]>=0 and calificacion[i]<=100:
                suma=suma+calificacion[i]
                break
        except ValueError:
            print("Error: ")

promedio=suma/numeroCalificaciones

for i in range(0,numeroCalificaciones):
    if calificacion[i]>=70:
        print("calificacion ["+str(i)+"] es " + str(calificacion[i]) + ": Aprobatorio")
    else:
        print("calificacion [" + str(i) + "] es " + str(calificacion[i]) + ": NA")

    print("El promedio del grupo es: "+ str(promedio))