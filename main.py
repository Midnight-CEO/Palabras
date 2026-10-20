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
