import operator
jugadores=[]
archivo=open("records.txt", "r") #abrir el archivo como lectura "r"
for linea in archivo:
    jugadores.append(linea)        #leer el archivo y guardarla en la variable contenido
archivo.close()                  #cerrar el archivo
              #utilizar la variable que tiene el contenido

usuario=[]
record=[]
for elemento in jugadores:
    indice1=elemento.index("-")
    indice2=elemento.index("*")
    usuario.append(elemento[0:indice1])
    record.append(elemento[indice1+1:indice2])

records=dict(zip(usuario,record))
records_sort= sorted(records.items(), key=operator.itemgetter(1), reverse=True)
print(records_sort)