# PROYECTO: ANALIZADOR DE COMENTARIOS

comentarios = []


# Funcion para procesar un comentario y generar una tupla
def procesar_comentario(comentario):
    comentario = comentario.strip()

    cantidad_caracteres = len(comentario)
    cantidad_palabras = len(comentario.split())

    resumen = (
        comentario,
        cantidad_caracteres,
        cantidad_palabras
    )

    return resumen


# Funcion para registrar un comentario
def registrar_comentario():
    comentario = input("Escriba el comentario del estudiante: ")
    comentario = comentario.strip()

    if comentario == "":
        print("El comentario no puede estar vacio.")
        return

    resumen = procesar_comentario(comentario)
    comentarios.append(resumen)

    print("Comentario registrado correctamente.")


# Funcion para mostrar todos los comentarios
def mostrar_comentarios():
    if len(comentarios) == 0:
        print("Todavia no hay comentarios registrados.")
        return

    print("\n--- COMENTARIOS REGISTRADOS ---")

    for i, resumen in enumerate(comentarios, start=1):
        print(f"{i}. {resumen[0]}")


# Funcion para buscar comentarios por una palabra
def buscar_comentarios():
    if len(comentarios) == 0:
        print("Todavia no hay comentarios registrados.")
        return

    palabra = input("Ingrese la palabra que desea buscar: ")
    palabra = palabra.strip().lower()

    if palabra == "":
        print("La palabra no puede estar vacia.")
        return

    encontrados = 0

    for i, resumen in enumerate(comentarios, start=1):
        comentario = resumen[0]
        palabras = comentario.lower().split()

        if palabra in palabras:
            print(f"{i}. {comentario}")
            encontrados += 1

    if encontrados > 0:
        print("Busqueda exitosa.")
        print("Cantidad de comentarios encontrados:", encontrados)
    else:
        print("No se encontraron comentarios con esa palabra.")


# Funcion para mostrar la cantidad de palabras
# de cada comentario
def contar_palabras():
    if len(comentarios) == 0:
        print("Todavia no hay comentarios registrados.")
        return

    print("\n--- CANTIDAD DE PALABRAS ---")

    for i, resumen in enumerate(comentarios, start=1):
        print(f"Comentario {i}: {resumen[2]} palabras")


# Funcion para seleccionar un comentario
def seleccionar_comentario():
    if len(comentarios) == 0:
        print("Todavia no hay comentarios registrados.")
        return None

    mostrar_comentarios()

    try:
        numero = int(input("Seleccione el numero del comentario: "))

        if numero < 1 or numero > len(comentarios):
            print("El numero del comentario no es valido.")
            return None

        return comentarios[numero - 1]

    except ValueError:
        print("Debe ingresar un numero entero.")
        return None


# Funcion para contar las apariciones de una palabra
def contar_apariciones():
    resumen = seleccionar_comentario()

    if resumen is None:
        return

    comentario = resumen[0]
    palabra = input("Ingrese la palabra que desea contar: ")
    palabra = palabra.strip().lower()

    if palabra == "":
        print("La palabra no puede estar vacia.")
        return

    palabras = comentario.lower().split()
    cantidad = palabras.count(palabra)

    print("\n--- RESULTADO DE LA BUSQUEDA ---")
    print("Comentario:", comentario)
    print("Palabra buscada:", palabra)
    print("Cantidad de apariciones:", cantidad)

    if cantidad > 0:
        print("Busqueda exitosa.")
    else:
        print("La palabra no aparece en el comentario.")


# Funcion para mostrar el resumen de un comentario
def mostrar_resumen():
    resumen_original = seleccionar_comentario()

    if resumen_original is None:
        return

    comentario = resumen_original[0]

    palabra = input("Ingrese la palabra que desea buscar: ")
    palabra = palabra.strip().lower()

    if palabra == "":
        print("La palabra no puede estar vacia.")
        return

    cantidad_caracteres = len(comentario)
    cantidad_palabras = len(comentario.split())
    cantidad_apariciones = comentario.lower().split().count(palabra)

    # Tupla con la informacion del comentario
    resumen = (
        cantidad_caracteres,
        cantidad_palabras,
        cantidad_apariciones
    )

    print("\n--- RESUMEN DEL COMENTARIO ---")
    print("Comentario:", comentario)
    print("Palabra buscada:", palabra)
    print("Numero de caracteres:", resumen[0])
    print("Numero de palabras:", resumen[1])
    print("Apariciones de la palabra:", resumen[2])
    print("Tupla de resumen:", resumen)

    if cantidad_apariciones > 0:
        print("Busqueda exitosa.")
    else:
        print("No se encontraron apariciones de esa palabra.")


# Menu principal del programa
def menu_principal():
    opcion = ""

    while opcion != "7":
        print("\n========== ANALIZADOR DE COMENTARIOS ==========")
        print("1. Registrar un comentario")
        print("2. Mostrar todos los comentarios")
        print("3. Buscar comentarios por una palabra")
        print("4. Mostrar la cantidad de palabras de cada comentario")
        print("5. Contar apariciones de una palabra en un comentario")
        print("6. Mostrar el resumen de un comentario")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_comentario()

        elif opcion == "2":
            mostrar_comentarios()

        elif opcion == "3":
            buscar_comentarios()

        elif opcion == "4":
            contar_palabras()

        elif opcion == "5":
            contar_apariciones()

        elif opcion == "6":
            mostrar_resumen()

        elif opcion == "7":
            print("Gracias por utilizar el analizador de comentarios.")

        else:
            print("Opcion no valida. Intente nuevamente.")


# Ejecucion del programa
menu_principal()
