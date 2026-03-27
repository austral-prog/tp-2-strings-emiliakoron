def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    
    precio = int(input())
    descuento = float(input())
    precio_desc = precio - descuento
    total = precio_desc * 3

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_desc}")
    print(f"Total: {total}")
