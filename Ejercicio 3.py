import os
import shutil

archivos_en_directorio = os.listdir()
print("Todos los archivos en el directorio actual:")
print(archivos_en_directorio)

archivos_txt = [archivo for archivo in archivos_en_directorio if archivo.endswith(".txt")]
print("\nArchivos .txt encontrados:")
print(archivos_txt)

directorio_destino = "mis_textos"
if not os.path.exists(directorio_destino):
    os.mkdir(directorio_destino)
    print(f"\nDirectorio '{directorio_destino}' creado.")
else:
    print(f"\nEl directorio '{directorio_destino}' ya existe.")

for archivo in archivos_txt:
    shutil.move(archivo, os.path.join(directorio_destino, archivo))
    print(f"Archivo '{archivo}' movido a '{directorio_destino}'.")

print("\nContenido final del directorio 'mis_textos':")
print(os.listdir(directorio_destino))
