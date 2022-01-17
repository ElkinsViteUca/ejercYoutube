anioInicio=int(input("Año Inicial:"))
anioFinal=int(input("Año Final: " ))
for anio in range(anioInicio, anioFinal+1):
    if anio%10==0:
        continue
    if anio%4==0:
        continue
    if anio%100!=0 or anio%400==0:
         print(anio)