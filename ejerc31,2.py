def firecciones(ventas):
    domicilios=set()
    for venta in ventas:
        domicilios.add(venta[3])
    return domicilios