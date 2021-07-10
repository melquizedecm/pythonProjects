class Datos:

    def leerEnteroPositivo(self,mensaje):
        while True:
            try:
                numero = int(raw_input(mensaje))
                if numero > 0:
                    return numero
                    break
                else:
                    print ("Error no es positivo << "+mensaje+">>")
            except ValueError:
                print ("Error no es 1"
                       "un numero valido <<"+mensaje+">>")

    def leerFlotantePositivo(self,mensaje):
        while True:
            try:
                numero = float(raw_input(mensaje))
                if numero > 0:
                    return numero
                    break
                else:
                    print ("Error, Escribe un valor positivo, <<"+mensaje+">>")
            except ValueError:
                print ("Error al leer el numero, escribe un numero  valido <<"+mensaje+">>")