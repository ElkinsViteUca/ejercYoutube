while True:
    print("Opción 1 - comenzar programa")
    print("Opción 2 - imprimir listado")
    print("Opción 3 - finalizar programa")
    opcion=int(input("Opción elegida:"))
    if opcion==1:
        print("¡Comenzamos!")
    elif opcion==2:
        print("Listado")
        print("Nadia, Esteban, Mariela, Fernanda")
    elif opcion==3:
        print("Hasta la próxima")
        break
    else:
        print("Opciín incorrecta. Debe ingresar 1,2 o 3")