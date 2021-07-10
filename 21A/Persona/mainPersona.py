from Persona import *

nombre=input("Escribe tu nombre")
matricula="09201234"
promedio=input("Escribe el promedio")

estudiante1=Estudiante(matricula,nombre)
estudiante1.setPromedio(promedio)


altura=input("escribe la altura de : " + estudiante1.nombre)
estudiante1.setAltura(altura)
print(estudiante1)


