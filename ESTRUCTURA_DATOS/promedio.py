xz-


print("PROGRAMA PARA CALCULA EL PROMEDIO DE UNA CANTIDAD DE CALIFICACIONES")

##leer la cantidad de calificaciones
n=0
while True:
    print("Escribe la cantidad de Calificaciones a capturar y Presiona ENTER")
    n=input(" (debe ser un numero entero, positivo) :_")
    try:
        if int(n) and int(n)>0:
            break
        else:
            print("Debe ser un numero positivo")
    except ValueError:
        print("Debe ser un numero entero")

##leer las calificaciones
calif=[]
for i in range(0,int(n)):

    while True:
        try:
            print("Escribe una calificacion entre 0 y 100, calificacion[",str(i),"]: _")
            calificacion= float(input())
            if calificacion>=0 and calificacion<=100:
                calif.append(calificacion)
                break
        except ValueError:
            print("Error en la captura de calificacion, Intente de nuevo")

##Indicar si fueron aprobatorias  y calcular promedio
suma=0.0
for i in range(0,int(n)):
    if float(calif[i])>=70:
        print("La calificacion ",i, " fue Aprobatoria: [",calif[i],"]")
    else:
        print("La calificacion ",i, " fue No Aprobatoria: [",calif[i],"]")
    suma=suma+float(calif[i])
promedio= suma/int(n)
print ("El promedio es: ", promedio)



