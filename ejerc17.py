corrimiento=int(input("Corriemiento:"))
alfabeto="abcdefghijklmnopqrstuvwxyz"
mensaje=input("Mensaje a encriptar:")
encriptado=""
for caracter in mensaje:
    if caracter.lower() in alfabeto:
        indice=alfabeto.find(caracter.lower())
        indice=(indice+corrimiento)%27
        encriptado+=alfabeto[indice]
    else:
        encriptado+=caracter
print("Mensaje encriptado:",encriptado)
