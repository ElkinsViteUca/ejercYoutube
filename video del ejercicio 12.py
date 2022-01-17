#video numero 12

numero=int(input("N. de cliente:"))
if numero==1000:
    print("Ganaste un premio!")
print("contiúa el programa")

#segundo ejrecicio
a=int(input("Ingresa un némero:"))
b=int(input("Ingrese un número:"))
if a<b:
    print("El primero es menor")
elif b<a:
    print("El segundo es menor")
else:
    print("Son iguales")
    
#tercer ejercicio
dia=input("Dia de la semana: ")
if dia=="lunes":
    print("Oh, no!")
elif dia=="viernes":
    print("¡Ya casi!")
elif dia=="sábado" or dia=="domingo":
    print("Ahora si se puede descansar")
else:
    print("A esperar el fin de semana!")