# VIDEO NUMERO 14
fecha= input ("Fecha(formato 'dia,DD/MM'): ")
fecha=fecha.lower()
diasemana=fecha[0:fecha.find(',')]
dianro=int(fecha[fecha.find(' ')+1:fecha.find('/')])
mesnro=int(fecha[fecha[fecha.find('/')+1:]])
if dianro>31 or mesnro>12:
    print("fecha incorrecta")
else:
    if diasemana in "lunes,martes,miercoles":
       respuesta=input("se tomaron examnes? S/N: ")
       if respuesta.lower()=="s":
           aprobados=int(input("cantidad de aprobados"))
           reprobado=int(input("cantidad de reprobado"))
    elif diasemana == "jueves":
        asistencia=int (input("porcentaje de asistencia"))
        print("asistio la mayoria")
    elif diasemana == "viernes":
        if dianro == 1 and (mesnro==1 or mesnro==7):
            print("asistio la mayoria ")
        else:
            print("no asistio la mayoria")
    elif diasemana == "viernes":
        if dianro ==1 and (mesnro==1 or mesnro ==7):   
            print("comienzo de nuevo ciclo") 
            alumnos=int(input("cantidad de alumnos:"))
            arancel=float(input("arancel:$"))
            print ("ingreso total:$",alumnos*arancel)  
    else:
        print("fecha incorrecta ")
    
print("fin del programa")
    
    