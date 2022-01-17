lista=[1,2,3,4,5,6,7,8,0,9,9,9]

for i in range(len(lista)-1):
    if lista[i]==lista[i+1]:
        print(lista[i])