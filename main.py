# PROYECTO: ANALIZADOR DE COMENTARIOS

comentarios = []

# Funcion para registrar un comentario
def registrar_comentario():
    comentario = input("Escriba el comentario del estudiante: ")
    comentario = comentario.strip()

    if comentario == "":
        print("El comentario no puede estar vacio.")
    else:
        comentarios.append(comentario)
        print("Comentario registrado correctamente.")


# Funcion para mostrar todos los comentarios
def mostrar_comentarios():
    if len(comentarios) == 0:
        print("Todavia no hay comentarios registrados.")
    else:
        print("\n--- COMENTARIOS REGISTRADOS ---")
        for i in range(len(comentarios)):
            print(i + 1, ".", comentarios[i])

# Punto 3: Buscar comentarios que contengan una palabra indicada
def buscar_comentarios(comentarios):
    palabra = input("Ingrese la palabra que desea buscar: ").strip().lower()

    encontrados = [
        (i, comentario)
        for i, comentario in enumerate(comentarios, start=1)
        if palabra in comentario.lower().split()
    ]

    if encontrados:
        print("\nComentarios encontrados:")
        for numero, comentario in encontrados:
            print(f"{numero}. {comentario}")
    else:
        print("No se encontraron comentarios con esa palabra.")


# Punto 4: Mostrar la cantidad de palabras de cada comentario
def contar_palabras(comentarios):
    if not comentarios:
        print("No hay comentarios registrados.")
        return

    print("\nCantidad de palabras por comentario:")
    for numero, comentario in enumerate(comentarios, start=1):
        cantidad = len(comentario.split())
        print(f"Comentario {numero}: {cantidad} palabras")

# Funcion para seleccionar un comentario
def seleccionar_comentario(comentarios):
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
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


# Punto 5: Contar las apariciones de una palabra
# en un comentario seleccionado
def contar_apariciones(comentarios):
    comentario = seleccionar_comentario(comentarios)

    if comentario is None:
        return

    palabra = input("Ingrese la palabra que desea contar: ").strip().lower()

    if palabra == "":
        print("La palabra no puede estar vacia.")
        return

    cantidad = comentario.lower().split().count(palabra)

    print("\n--- RESULTADO DE LA BUSQUEDA ---")
    print("Comentario:", comentario)
    print("Palabra buscada:", palabra)
    print("Cantidad de apariciones:", cantidad)


# Punto 6: Mostrar el resumen de un comentario
# y almacenarlo en una tupla
def mostrar_resumen(comentarios):
    comentario = seleccionar_comentario(comentarios)

    if comentario is None:
        return

    palabra = input("Ingrese la palabra que desea buscar: ").strip().lower()

    if palabra == "":
        print("La palabra no puede estar vacia.")
        return

    cantidad_caracteres = len(comentario)
    cantidad_palabras = len(comentario.split())
    cantidad_apariciones = comentario.lower().split().count(palabra)

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
            buscar_comentarios(comentarios)

        elif opcion == "4":
            contar_palabras(comentarios)

        elif opcion == "5":
            contar_apariciones(comentarios)

        elif opcion == "6":
            mostrar_resumen(comentarios)

        elif opcion == "7":
            print("Gracias por utilizar el analizador de comentarios.")

        else:
            print("Opcion no valida. Intente nuevamente.")


# Ejecucion del programa
menu_principal()
