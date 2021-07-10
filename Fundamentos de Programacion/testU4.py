import random

c=[]
c.append(12)
c.append(3)
c.append(27)
c.append(16)
c.append(4)
c.append(25)
c.append(47)
c.append(76)
c.append(45)
c.append(78)
c.append(3)
c.append(10)

suma=0
for i in range(0,len(c),1):
    suma=suma+c[i]
    print("el valor del vector["+str(i)+"]es : "+str(c[i]))

print(suma/len(c))


aleatorio=random.randrange(0,1000)
print(aleatorio)
