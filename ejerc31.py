from Funciones import *

primaria=set()
secundaria=set()
print("Alumnos De Primaria: ")
primaria=cargarNombres(primaria)
print("Alumnos De Secundaria: ")
secundaria=cargarNombres(secundaria)

print("Nombre De Todos Los Alumnos:")
for nombre in primaria & secundaria:
    print(nombre)
    
print("nombres Comunes: ")
for nombre in primaria & secundaria:
    print(nombre)
    
print("Nombre De Primaria Que No Se Repiten En Secundaria")
for nombre in primaria-secundaria:
    print(nombre)