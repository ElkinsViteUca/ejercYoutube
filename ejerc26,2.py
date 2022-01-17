def lenUltimaPalabra(cadena):
    longitud=len(cadena)
    if longitud==0:
        return 0
    cantidad = 0
    for i in range(longitud):
        if cadena[i]!= " ":
            cantidad=cantidad+1
        else:
            if cadena[i]==" " and i<(longitud-1) and cadena[i+1]!=" ":
                cantidad=0
    return cantidad
            