def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass
    base = input("Ingrese la base: ")
    altura = input("Ingrese la altura: ")

    base = float(base)
    altura = float(altura)

    area = base * altura
    perimetro = (2 * base) + (2 * altura)
    print(area)
    print(perimetro)
