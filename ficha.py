def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    nombre_completo = input()
    email = input()
    nota1 = input()
    nota2 = input()
    nota3 = input()

    #encabezado decorativo
    print("=" * 24)
    print("    FICHA DEL ALUMNO")
    print("=" * 24)

    nombre_limpio = nombre_completo.strip().title()
    print("Nombre: ", nombre_limpio)

    email_limpio = email.strip().lower()
    print("Email: ", email_limpio)

    cantidad = len(nombre_limpio)
    print("Caracteres en nombre: ", cantidad)

    pos_espacio = nombre_limpio.find(" ")
    iniciales = nombre_limpio[0] + nombre_limpio[pos_espacio + 1 ]
    print("Iniciales: ", iniciales)

    nombre_en_partes = nombre_limpio.split()
    usuario = f"{nombre_en_partes[-1].lower()}.{nombre_en_partes[0].lower()}"
    print("Usuario: ", usuario)

    print("Email valido: ", "@" in email_limpio)

    dominio = email_limpio[email_limpio.find("@") + 1:]
    print("Dominio: ", dominio)

    nombre_guion = nombre_limpio.replace(" ", "_")
    print("Nombre para archivo: ", nombre_guion)

    print("Cantidad de a: ", nombre_limpio.count("a"))

    print("Codigo secreto: ", nombre_limpio[::-1].upper())

    n1 = float(nota1)
    n2 = float(nota2)
    n3 = float(nota3)

    suma = n1 + n2 + n3
    promedio = suma / 3
    promedio_entero = suma // 3 

    print("Nota 1: ", n1)
    print("Nota 2 ", n2)
    print("Nota 3", n3)
    print("Suma: ", suma)
    print("Promedio: ", promedio)
    print("Promedio_entero: ", promedio_entero)

    print("="*24)
