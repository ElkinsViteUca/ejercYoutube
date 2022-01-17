#Ejercicio 10
 
#programa1
n=input("tu nombre: ")
print("ahora estas en la matrix," , n)

#programa2
costo=float(input("costos de la cena: $"))
servicio= (costo*6.2)/100
propina=costo*0.1
print("costos total de la comida: $", costo+servicio+propina)

#programa3
costo=float(input("costos de la cena: $"))
servicio= (costo*0.062)
propina=costo*0.1
print("costos total de la comida: $", costo+servicio+propina)

#programa 3
dia=int(input("dia de tu nacimiento"))
mes=int(input("mes de tu nacimiento:"))
anio=int(input("año de tu nacimiento: "))
print(dia,"/",mes,"/",anio)

#programa4
fecha=int(input("Fecha en formato DDMMAAA: "))
anio=fecha%10000
dia=fecha//1000000
mes=(fecha//10000)%100
print(dia,"/",mes,"/",anio)

#programa5
fecha=input("Fecha en formato DDMMAAA: ")
dia=fecha[:2]
mes=fecha[2:4]
anio=fecha[4:]
print(dia,"/",mes,"/",anio)



