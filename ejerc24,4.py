from Funciones import *
cantidad=0
mayor=-1
numero=int(input("Número positivo: "))
while numero>=0:
    suma=sumaDigitos(numero)
    if suma>mayor:
        mayor=suma
        n_mayorsuma=numero
    if suma < 10:
        cantidad+=1
        numero=int(input("número positivo: "))
print("Sumatoria de los digitos de ",n_mayorsuma,":",mayor)
print("cantidad co sumatoria menos a 10:", cantidad)