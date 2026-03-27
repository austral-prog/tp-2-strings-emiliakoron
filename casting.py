def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    
    precio = input()
    descuento = input()
    cantidad = input()

    precio = float(precio)
    descuento = float(descuento)
    cantidad = int(cantidad)

    precio_con_descuento = precio - (precio * (descuento / 100))
    total = precio_con_descuento * cantidad

    print(precio_con_descuento)
    print(total)
