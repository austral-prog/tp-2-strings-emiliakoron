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

    # decorativo
    print("=" * 24)
    print("    FICHA DEL ALUMNO")
    print("=" * 24)

    # Nombre limpio
    nombre_limpio = nombre_completo.strip().title()
    print(f"Nombre: {nombre_limpio}")

    # Email en minúsculas
    email_limpio = email.strip().lower()
    print(f"Email: {email_limpio}")

    # Cantidad de caracteres
    cantidad = len(nombre_limpio)
    print(f"Caracteres en nombre: {cantidad}")

    # Iniciales
    pos_espacio = nombre_limpio.find(" ")
    iniciales = nombre_limpio[0] + nombre_limpio[pos_espacio + 1]
    print(f"Iniciales: {iniciales}")

    # Usuario apellido.nombre
    partes = nombre_limpio.split()
    usuario = f"{partes[-1].lower()}.{partes[0].lower()}"
    print(f"Usuario: {usuario}")

    # Email contiene @
    print(f"Email valido: {'@' in email_limpio}")

    # Dominio del email
    dominio = email_limpio[email_limpio.find("@") + 1:]
    print(f"Dominio: {dominio}")

    # Nombre para archivo
    nombre_guion = nombre_limpio.replace(" ", "_")
    print(f"Nombre para archivo: {nombre_guion}")

    # Contar 'a'
    print(f"Cantidad de a: {nombre_limpio.count('a')}")

    # Código secreto
    print(f"Codigo secreto: {nombre_limpio[::-1].upper()}")

    # Notas y cálculos
    n1 = int(nota1)
    n2 = int(nota2)
    n3 = int(nota3)

    suma = n1 + n2 + n3
    promedio = suma / 3
    promedio_entero = suma // 3

    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {int(promedio_entero)}")

    # Cierre decorativo
    print("=" * 24)
