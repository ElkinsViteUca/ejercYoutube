digitosEnLaLinesa=0
cantLineas=0
titulo=input("Título del libro:")
while titulo!="*":
    if titulo == "/":
        cantLineas+=1
        print("Línea completa. Aparecen",digitosEnLaLinesa,"digitos")
        digitosEnLaLinesa=0
    else:
        for caracter in titulo:
            if caracter in "0123456789":
                digitosEnLaLinesa+=1
    titulo=input("Titulo del libro:")
print("Fin. Se leyeron",cantLineas,"Líneas")

        