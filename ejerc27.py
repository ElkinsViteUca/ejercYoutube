def titulo(cadena):
    nueva=""
    inicioPalabra=True #indica el incicio de una palabra
    for caracter in cadena:
        if not caracter.isalpha():
            nueva=nueva+caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva=nueva+caracter.upper()
                inicioPalabra=False # ya no es el incicio de una palabra
            else:
                nueva=nueva+caracter.lower()
    return nueva    

if __name__ == "__main__": 
    import doctest
    doctest.testmod()
    
    