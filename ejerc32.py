contadores={}
alfabeto="abcdefghijklmnopqrstuvwxyz"
for letra in alfabeto+alfabeto.upper():
    contadores[letra]=0
for i in range(3):
    cadena=input("Cadena de caracteres: ")
    for caracter in cadena:
        if caracter.lower() in alfabeto:
            contadores[caracter]+=1

for caracter,cantidad in contadores.items():
    print(caracter,":",cantidad)