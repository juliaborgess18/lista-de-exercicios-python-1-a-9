nome = ["Julia","Pedro","Karina"]
id = [1,2,3]

resultado_da_lista = zip(nome, id)

for nome, id in resultado_da_lista:
    print(f"{nome}:{id}")

