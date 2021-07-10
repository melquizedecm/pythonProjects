 ### PROGRAMA DE ORDENACION DE DATOS, METODO INSERCION (BURBUJA) ###
class ejemplo:
 ### CREAMOS UNA LISTA EN LA CUAL GUARDAREMOS LOS NUMEROS QUE INGRESEMOS ####
 lista = []

 ### LE PEDIMOS AL USUARIO CUANTOS NUMEROS QUIERE INGRESAR ###
 cantidad = int(input("¿cuantos numeros deseas ingresar?:  "))
 ### SE INICIALIZA LA VARIABLE, PARA ENUMERAR LOS DATOS INGRESADOS ###
 i = 1
 ### PARA INGRESAR LAS NUMEROS, MIENTRAS CUMPLA LA CONDICION ###
 while(cantidad  > 0 ):
 ### EL USUARIO INGRESA LOS NUMEROS ###
    numero = int(input("numero #" + str(i) + ":  "))
 ### APENAS INTRODUCE EL NUMERO, LO AÑADE A LA LISTA ###
    lista.append(numero)
 ### INCREMENTO DE LA VARIABLE i ###
    i = i + 1
 ### DISMINUYE EN UNO LAS CANTIDADES QUE TIENE QUE INGRESAR ###
    cantidad = cantidad - 1


 ### ORDENACION DE LA LISTA ####
 ### RANGO DE LA LISTA i ###
 espacio=0
 for  i in range (0,len((lista))-1,1):
 ### LONGITUD DE LA LISTA INCREMENTADA EN UNO ###
     for j in range(i+1,len(lista),1):
         espacio+=1
 ### COMPARACION DE LOS NUMEROS ###
         espacio+=1
         if lista[i]>lista[j]:
 ### ALMACENA EL ELEMENTO ANTES DE INTERCAMBIAR ###
             aux=lista[i]
 ### HACE EL INTERCAMBIO ###
             lista[i]=lista[j]
             lista[j]=aux
             espacio+=3
 ### SE IMPRIME LA LISTA ###
 print ("lista: ", lista)
 print ("\n\n")
 espacio = int(espacio * 4)
 print(str(espacio * 8) + "bits de memoria\n" + str(espacio) + "bytes de memoria RAM")
