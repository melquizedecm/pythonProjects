tupla = (
11, 11, 2, 9, 5, 9, 4, 8, 18, 8, 10, 5, 14, 19, 10, 9, 16, 17, 5, 8, 6, 5, 19, 18, 2, 10, 16, 5, 2, 13, 7, 13, 18, 5,
14, 15, 8, 15, 5, 8, 16, 14, 16, 3, 1, 3, 8, 2, 19, 17, 8, 5, 13, 15, 2, 17, 4, 6, 8, 20, 15, 10, 11, 14, 5, 19, 8, 14,
5, 16, 18, 12, 9, 18, 10, 4, 8, 5, 4, 18, 16, 7, 8, 16, 8, 2, 16, 17, 7, 2, 6, 7, 17, 1, 14, 3, 13, 8, 17, 11, 11, 2, 9,
5, 9, 4, 8, 18, 8, 10, -7, -6, 19, 10, 9, 16, 17, 5, 8, 6, 22, 23, 18, 0, 6)

#### OBTENER EL MAYOR##
mayor=0
mayorPar=0
menorPar=21
for elemento in tupla:
    #### obtener el mayor###
    if elemento>=mayor:
        mayor=elemento

    ##para obtener el mayor par
    if elemento%2==0 and elemento>=mayorPar:
        mayorPar=elemento

    ####el menor par####
    if elemento%2==0 and elemento<=menorPar:
        menorPar=elemento

print(menorPar)