def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass

    gasto = float(input())
    dinero_recibido = int(input())

    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)
    print()
    print("Vuelto")
    print()
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")
