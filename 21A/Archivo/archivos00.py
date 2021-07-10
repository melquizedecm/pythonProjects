import random
nombre=input("Escribe tu nombre")
records= random.randrange(10,100)

archivo=open("records.txt","a") #abrir archivo como escritura
archivo.write(nombre+"-"+str(records)+"*\n")           #escribir el contenido al archivo
archivo.close()                 #cerrar el archivo

