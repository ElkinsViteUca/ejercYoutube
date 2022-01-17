from Funciones import *

#1
numeros=[]
nro=int(input("NÚMERO: "))
while nro!=0:
    numeros.append(nro)
    nro=int(input("números: "))
    
#2
eliminar=int(input("Número a eliminar: "))
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese numero no esta entre los ingresados")
    
#3
print("Sumatoria de los números: ", sumatoria(numeros))

#4
limite=int(input("Filtrar numero menores a : "))
for n in numerosMenores(numeros,limite):
    print(n)
    
#5
print("Frecuencias: ")
for tupla in frecuencias(numeros):
    print(tupla[0],"aparece",tupla[1],"veces ")

