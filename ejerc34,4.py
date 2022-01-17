def empleadoExiste(empleados,nombre):
    for datos in empleados.Values():
        if datos[0]==nombre:
            return True
    return False

empleados={100: ["Jorge Millán","Administración"],
           200: ["Oriana López","Gerencia"],
           300: ["Guadalupe Ríos","RR.HH. "],
           400: ["Lionel Campos","Ventas"]}

nombre=input("Nombre de empleado: ")
if not empleadoExiste(empleados, nombre):
    print("El empleado no se encuentra en la nómina")