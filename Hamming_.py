def autocompletar(cadena):
    cadena=list(cadena)

    x=posicion=0
    while posicion<len(cadena):
        posicion=2**x
        if posicion<len(cadena):
            cadena.insert(posicion-1,"X")
        else:
            break
        x+=1
    cadena="".join(cadena)
    print(cadena)
    return cadena







cadenaEnviar="1001"
print(autocompletar(cadenaEnviar))
