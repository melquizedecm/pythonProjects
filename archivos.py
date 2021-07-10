######tengo un nuevo record########
nuevoRecord=14000
######1. Abrir archivo y obtener el record anterior#####
archivo=open("datos.txt","r")
recordAnterior=int(archivo.readline())
archivo.close()

##2. COMPARAR RECORDS
if nuevoRecord>recordAnterior:
    ## SI ES MAYOR ESCRIBIR EL NUEVO RECORD
    archivo=open("datos.txt","w")
    archivo.write(str(nuevoRecord))
    archivo.close()

###r=read, w=Write, a=append