import json

# Crear diccionario con datos personales
mis_datos = {
    "nombre": "Kenson",
    "Pais": "El Salvador",
    "Departamento": "Morazan",
    "Edad":38
}

with open("mis_datos.json", "w", encoding="utf-8") as archivo_json:
    json.dump(mis_datos, archivo_json, ensure_ascii=False, indent=4)

print("Datos personales guardados:")
with open("mis_datos.json", "r", encoding="utf-8") as archivo_json:
    datos_leidos = json.load(archivo_json)
    print(datos_leidos)

datos_leidos["edad"] += 1

with open("mis_datos.json", "w", encoding="utf-8") as archivo_json:
    json.dump(datos_leidos, archivo_json, ensure_ascii=False, indent=4)

print("Datos actualizados:")
with open("mis_datos.json", "r", encoding="utf-8") as archivo_json:
    datos_actualizados = json.load(archivo_json)
    print(datos_actualizados)
