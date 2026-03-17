def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    
    gasto = input("Ingrese el gasto: ")
    dinero_recibido = input("Ingrese el dinero recibido: ")

    gasto = float(gasto)
    dinero_recibido = float(dinero_recibido)

    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = round((pesos - vuelto) * 100)

    print(pesos)
    print(centavos)
