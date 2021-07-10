import operator
arreglo=[]

archivo=open("records.txt","r") #abrir un archivo en modo lectura
for linea in archivo:
    arreglo.append(linea)       #leer el contenido y guardarlo en una variable
archivo.close()                 #cerrar el archivo

####conversion de lineas en elementos separados#######
user=[]
record=[]
for elemento in arreglo:
    indice1=elemento.index("-")
    indice2=elemento.index("*")
    user.append(elemento[0:indice1])
    record.append(elemento[indice1+1:indice2])


records=dict(zip(user,record))
records_sort = sorted(records.items(), key=operator.itemgetter(1), reverse=True)
print(records_sort)
