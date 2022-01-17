from Funciones import *
mayor=0
numero=int(input("Número primo: "))
while primo(numero):
    print("Suma de los dígitos:",sumaDigitos(numero))
    digito=int(input("Dígito: "))
    print("El",digito,"aparece",frecuencia(numero,digito),"veces")
    if numero > mayor:
        mayor=numero
    numero=int(input("Numero primo: "))
print("Factorial de",mayor,":",factorial(mayor))