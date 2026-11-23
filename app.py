tareas = []


def agregar_tarea(titulo):
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada.")


def listar_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    for i, tarea in enumerate(tareas, start=1):
        estado = "[X]" if tarea["completada"] else "[ ]"
        print(f"{i}. {estado} {tarea['titulo']}")


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS CLI - AYUDA RAPIDA ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            titulo = input("Titulo de la tarea: ")
            agregar_tarea(titulo)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opcion aun no implementada.")


if __name__ == "__main__":
    main()
