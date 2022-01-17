
#video 11
CAPACIDADDM2=4
PORCENTAJEGRADAS=0.2
PORCENTAJEESPECIALES=0.3
PORCENTAJESCOMUNES=0.7

dimensiones=float(input("dimensiones del estadio (en m2):"))
personasengradas=int(input("cantidad de personas que caben en las gradas"))
porcentajescenarios=int(input("porcentajes que ocupa el escenario"))

m2gradas=dimensiones*PORCENTAJEGRADAS
m2escenario=dimensiones*(porcentajescenarios/100)
m2disponibles=dimensiones-m2gradas-m2escenario
personastotales=(m2disponibles*4)+personasengradas
print("caben",personastotales,"personas")
precioentradaespecial=float(input("precio entrada especial:"))
precioentadacomun=float(input("precio entrada comun: "))
print("ingreso total de ventas:",)(personastotales*PORCENTAJEESPECIALES)*precioentradaespecial+(personastotales*PORCENTAJESCOMUNES)*precioentadacomun

