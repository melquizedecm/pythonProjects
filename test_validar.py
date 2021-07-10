
def esTelefono(numero):
    if len(numero)==10:
        senal=0 #0=apagado, 1=encendido
        for letra in numero:
            if ord(letra)<= 47 or ord(letra)>=58:
                senal=1
        if senal==1:
            return False
        if senal==0:
            return True
    else:
        return False

def esMinuscula():
    pass

def esMayuscula():
    pass

def esNumero():
    pass