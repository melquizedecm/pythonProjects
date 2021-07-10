dias =['Lunes','Martes','Miercoles']
valores=['3','10','6']

dia=input("dame el dia")
valor=input("dame el valor")

###validacion
for i in range(len(dia)):
    if dia ==dias[i]:
        if valor==valores[i]:
            "usuario correcto"