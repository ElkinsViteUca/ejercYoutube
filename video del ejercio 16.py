total=0
for i in range(101):
    if i%3==0:
        total+=i
print("sumatoria:",total)

########
numero=int(input("numero:"))
f=1
if numero !=0:
    f=f*i
print("factorial:",f)

####

n1=0
n2=1
print(n1)
print(n2)
for i in range (8):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3

#######

sumanegativos=0
sumapositivos=0
cantidadpositivos=0
for i in range (6):
    nro=int(input("numero:"))
    if nro>=0:
        cantidadpositivos+=1
        sumapositivos+=nro
    else:
        sumanegativos+=nro
print("sumatoria de negativos:",sumapositivos/cantidadpositivos)
if cantidadpositivos!=0:
    print("promedio de positivos:",sumapositivos/cantidadpositivos)
else:
    print("no se ingresaron numero positivos")
    
