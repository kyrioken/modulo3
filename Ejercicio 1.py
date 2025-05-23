with open("mi_archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Pizza\n")
    archivo.write("Tacos\n")
    archivo.write("Pupusas\n")

print("Contenido del archivo:")
with open("mi_archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

with open("mi_archivo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Papas fritas\n")

print("Contenido actualizado:")
with open("mi_archivo.txt", "r", encoding="utf-8") as archivo:
    contenido_actualizado = archivo.read()
    print(contenido_actualizado)
