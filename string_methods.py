def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""
    print(nombre.strip())
    print(nombre.lstrip())
    print(nombre.rstrip())

    print(frase.upper())
    print(frase.lower())
    print(frase.title())

    print(frase.find("gran"))
    print(frase.replace("programacion", "desarrollo"))

    print(frase.count("a"))
    print("Python" in frase)
    print("Java" in frase)

    print(frase[0:6])
    print(frase[0:6:2])
    print(frase[0:6][::-1])

    nombre_sin_espacios = nombre.strip()
    python = frase[0:6]
    print(f"{nombre_sin_espacios} trabaja con {python}")

    print(multilinea)
