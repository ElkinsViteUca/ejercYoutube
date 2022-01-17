from Funciones import *

socios_activos={1:["Amanda Núñez","17032009",True],2:["Bárbara Molina","17032009",True],3:["Lautaro Campos","17032009",True]}

print("***Cargar socios")
socios_activos=cargarSocios(socios_activos)

print("El club tiene",len(socios_activos),"socios")

print("***Registrar pago de cuotas")
numeros=int(input("Número de socios: "))
socios_activos[numeros][2]=True

print("***Modificando fecha de ingreso...")
socios_activos=modificarFecha(socios_activos,"13032018")

print("***Eliminar socio: ")
nombre=input("nombre y apellido: ")
numero=numeroSocio(socios_activos,nombre)
del socios_activos[numero]

imprimirListado(socios_activos)