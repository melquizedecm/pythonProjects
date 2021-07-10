from ValidacionesClass import *
validar=ValidacionesClass()

while True:
    numeroCalificaciones=raw_input("Escribe la cantidad de calificaciones:")
    if validar.validarEntero(numeroCalificaciones):
        numeroCalificaciones=int(numeroCalificaciones)
        break
calificaciones=[]
suma=0
for i in range(1,numeroCalificaciones+1):
    while True:
        calificacion=raw_input("Escribe la calificacion["+str(i)+"]:")
        if validar.validarEntero(calificacion):
            if validar.validarRangoEntero(0,100,calificacion):
                calificaciones.append(int(calificacion))
                suma+=int(calificacion)
                break
            else:
                print ("Error: el dato no esta en el rango")
        else:
            print("Error: El dato debe ser entero")

for i in range(0,numeroCalificaciones):
    if calificaciones[i]>=70:
        print (str(i)+": "+str(calificaciones[i])+ ": Aprobado")
    else:
        print (str(i)+": " + str(calificaciones[i]) + ": NA")

promedio=suma/numeroCalificaciones
print("El promedio del grupo es: "+ "{0:.2f}".format(promedio))
