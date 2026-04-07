def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = int(input())
    descuento = float(input())
    cantidad = int(input())

    precio_desc = precio - descuento
    total = precio_desc * cantidad

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_desc}")
    print(f"Total: {total}")
