from Funciones import *

pasajeros=[]
ciudades=[]
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino mediante el DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar pais destino mediante DNI")
    print("6. Cantidad de pasajeros que viajan a un país")
    print("7. Salir el programa")
    opcion=int(input("Acción a ejecutar: "))
    if opcion ==1:
        print("Agregar pasajeros")
        pasajeros=agregarPasajeros(pasajeros)
    elif opcion==2:
        print(("Agregar ciudades"))
        ciudades=agregarCiudades(ciudades)
        
    elif opcion==3:
        dni=int(input("DNI: "))
        print("El pasajero viaja a", buscarCiudad(pasajeros,dni))
    
    elif opcion==4:
        ciudad=input("Ciudad: ")
        print("Viajan",cantidadPasajerosCiudad(pasajeros,ciudad),"pasajeros")
    
    elif opcion==5:
        dni=int(input("DNI: "))
        print("Viaja a",buscarPaisDestino(pasajeros,ciudades,dni))
    
    elif opcion==6:
        pais=input("Pais: ")
        print("Viajan",cantidadPasajerosPais(pasajeros,ciudad,pais),"pasajeros")
    
    elif opcion==7:
        break
    else:
        print("Opción inválida")
                
        
        