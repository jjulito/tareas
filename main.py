import json
import os

ARCHIVO = "tareas.json"

# Cargar tareas desde archivo JSON
def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return []

# Guardar tareas en archivo JSON
def guardar_tareas(tareas):
    with open(ARCHIVO, "w") as f:
        json.dump(tareas, f, indent=4)

# Mostrar lista de tareas
def mostrar_tareas(tareas):
    if not tareas:
        print("\n No hay tareas registradas.")
        return
    print("\n=== Lista de Tareas ===")
    for i, tarea in enumerate(tareas, 1):
        estado = "(Completada)" if tarea["completada"] else "(Pendiente)"
        print(f"{i}. {tarea['descripcion']} [{estado}]")

# Agregar nueva tarea
def agregar_tarea(tareas):
    descripcion = input("Escribe la nueva tarea: ")
    tareas.append({"descripcion": descripcion, "completada": False})
    guardar_tareas(tareas)
    print("Tarea agregada con éxito.")

# Marcar tarea como completada
def completar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return
    try:
        indice = int(input("Número de tarea a completar: ")) - 1
        tareas[indice]["completada"] = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada.")
    except (ValueError, IndexError):
        print("Número de tarea inválido.")

# Eliminar tarea
def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return
    try:
        indice = int(input("Número de tarea a eliminar: ")) - 1
        tarea = tareas.pop(indice)
        guardar_tareas(tareas)
        print(f"Tarea '{tarea['descripcion']}' eliminada.")
    except (ValueError, IndexError):
        print("Número de tarea inválido.")

# Menú principal
def menu():
    tareas = cargar_tareas()
    while True:
        print("\n=== Gestor de Tareas ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("Saliendo... ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
