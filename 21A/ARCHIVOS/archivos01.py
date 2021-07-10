import random
nombre=input("Escribe tu nombre")
record=random.randrange(10,100)

archivo=open("records.txt","a")                     #abrir el archivo para escribrir "a"
archivo.write(nombre+"-" + str(record) + "*\n")     #Escribir dentro del archivo
archivo.close()                                     #cerrar el archivo

