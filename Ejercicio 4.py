import pickle

amigos = ["Luis", "Juan", "Carlos"]

with open("amigos.pkl", "wb") as archivo_pickle:
    pickle.dump(amigos, archivo_pickle)

with open("amigos.pkl", "rb") as archivo_pickle:
    amigos_recuperados = pickle.load(archivo_pickle)
    print("Lista de amigos recuperada:")
    print(amigos_recuperados)

amigos_recuperados.append("María")

with open("amigos.pkl", "wb") as archivo_pickle:
    pickle.dump(amigos_recuperados, archivo_pickle)

with open("amigos.pkl", "rb") as archivo_pickle:
    lista_actualizada = pickle.load(archivo_pickle)
    print("\nLista actualizada:")
    print(lista_actualizada)
