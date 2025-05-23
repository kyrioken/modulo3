import json
import os

archivo_notas = "notas.json"

if not os.path.exists(archivo_notas):
    notas_iniciales = {
        "Juan": [85, 90, 78],
        "María": [92, 88, 95],
        "Pedro": [76, 81, 69]
    }
    with open(archivo_notas, "w", encoding="utf-8") as archivo:
        json.dump(notas_iniciales, archivo, ensure_ascii=False, indent=4)

def cargar_notas():
    with open(archivo_notas, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_notas(notas):
    with open(archivo_notas, "w", encoding="utf-8") as archivo:
        json.dump(notas, archivo, ensure_ascii=False, indent=4)

def ver_todas_las_notas(notas):
    print("\n--- Todas las notas ---")
    for estudiante, calificaciones in notas.items():
        print(f"{estudiante: {calificaciones}")

def añadir_estudiante(notas):
    nombre = input("Nombre del nuevo estudiante: ").strip()
    if nombre in notas:
        print("Ese estudiante ya existe.")
        return
    notas_nuevas = input("Introduce las notas separadas por comas: ")
    lista_notas = [int(nota.strip()) for nota in notas_nuevas.split(",") if nota.strip().isdigit()]
    notas[nombre] = lista_notas
    guardar_notas(notas)
    print(f"Estudiante {nombre} añadido correctamente.")

def buscar_estudiante(notas):
    nombre = input("Nombre del estudiante a buscar: ").strip()
    if nombre in notas:
        print(f"{nombre}: {notas[nombre]}")
    else:
        print("Estudiante no encontrado.")

def menu():
    while True:
        print("\n--- Sistema de Notas ---")
        print("1. Ver todas las notas")
        print("2. Añadir un nuevo estudiante")
        print("3. Buscar estudiante por nombre")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        notas = cargar_notas()
        
        if opcion == "1":
            ver_todas_las_notas(notas)
        elif opcion == "2":
            añadir_estudiante(notas)
        elif opcion == "3":
            buscar_estudiante(notas)
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


menu()
