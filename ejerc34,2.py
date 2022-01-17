#1
lista=[1,2,3,4]
for elemento in lista:
    print(elemento)
    
#2
articulos={154:["jabón en polvo","limpieza",True],
           248:["talco","cosmética",False],
           199:["cera para pisos","limpieza",True]}
for clave, valor in articulos.items():
    print("Código:",clave)
    print("Descripción: ",valor[0])
    print("Rubro: ",valor[1])
    if valor[2]:
        print("Hay stock")
    else:
        print("Agotado")
    print("---------")
           