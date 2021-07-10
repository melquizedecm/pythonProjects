semaforo=False
n=1007
for i in range(2,n,1):
    print(n, "/", i)
    residuo=n%i
    print(residuo)
    print("********")
    if residuo==0:
        semaforo=True
        break

if semaforo==True:
    print("no es primo")
else:
    print("Es primo")
