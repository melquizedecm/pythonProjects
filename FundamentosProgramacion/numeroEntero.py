num1=float(input())

entero=float("{0:.0f}".format(num1))

if num1==entero:
    print("es entero")
else:
    print("No es entero")