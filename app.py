tareas = []


def agregar_tarea(titulo):
    if not titulo or not titulo.strip():
        print("Error: el titulo de la tarea no puede estar vacio.")
        return
    tareas.append({"titulo": titulo.strip(), "completada": False})
    print("Tarea agregada.")


def listar_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    for i, tarea in enumerate(tareas, start=1):
        estado = "[X]" if tarea["completada"] else "[ ]"
        print(f"{i}. {estado} {tarea['titulo']}")


def completar_tarea(indice):
    if 1 <= indice <= len(tareas):
        tareas[indice - 1]["completada"] = True
        print("Tarea completada.")
    else:
        print("Numero de tarea invalido.")


def eliminar_tarea(indice):
    if 1 <= indice <= len(tareas):
        eliminada = tareas.pop(indice - 1)
        print(f"Tarea eliminada: {eliminada['titulo']}")
    else:
        print("Numero de tarea invalido.")


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
        elif opcion == "3":
            try:
                num = int(input("Numero de tarea a completar: "))
                completar_tarea(num)
            except ValueError:
                print("Escribe un numero valido.")
        elif opcion == "4":
            try:
                num = int(input("Numero de tarea a eliminar: "))
                eliminar_tarea(num)
            except ValueError:
                print("Escribe un numero valido.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
