num_lineas=5
blanco=' '
asterico='*'

for fila in range(1,num_lineas):
    for i in range(num_lineas - fila,0,-1):
        print(blanco, end="")
    for cuenta in range(1,2*fila,1):
        print("*", end="")
    print('')
