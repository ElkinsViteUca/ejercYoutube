def validar(email):
    caracterBuscado="@"
    emailValido=False
    for c in email:
        if c == caracterBuscado:
            emailValido=True
            break
    return emailValido

#programa principal
dirección=input("Tu email: ")
if validar(dirección):
    print("Dirección válida")
else:
    print("Dirección inválida")        