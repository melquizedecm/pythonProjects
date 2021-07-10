### r=read   w=write   a=append

#archivo=open("records.txt","r")  ## "r" es como solo lectura
#contenido=archivo.read()
#print(contenido)

#archivo=open("records.txt","a")  ## "a" es para agregar algo al final de mi archivo de texto
#archivo.write("\nAna")  ## "\n" es para agregar un enter
#archivo.write("\n1000")

#archivo=open("records.txt","w")  ## "w" es para escribir en tu archivo
#archivo.write("\nAngel")       ##solo esta informacion se mostrará en el archivo
#archivo.write("\n5000")

#archivo.close()

###########TENGO UN NUEVO RECORD##################

usuario="BEATRIZ"
nuevoRecord=10000
############# 1. ABRIR ARCHIVO Y OBTENER EL RECORD ANTERIOR##########
archivo=open("records.txt", "r")
nombre=archivo.readline()
recordAnterior=int(archivo.readline())

########### 2. COMPARAR RECORDS ############
if nuevoRecord>recordAnterior:
    ##### SI ES MATO, ESCRIBIR EL NUEVO RECORD ########
    archivo=open("records.txt", "w")
    archivo.write(usuario)
    archivo.write("\n"+str(nuevoRecord))
    archivo.close()