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
