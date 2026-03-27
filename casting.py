def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    
    precio = int(input("Precio: "))
    descuento = float(input("Descuento: "))
    precio_desc = precio - descuento
    total = precio_desc * 3
    print("Precio:", precio)
    print("Descuento:", descuento)
    print("Precio con descuento:", precio_desc)
    print("Total:", total)
