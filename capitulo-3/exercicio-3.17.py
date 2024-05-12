lista=[1, 15, 64, 14, 7, 9, 11, 10, 19, 2]
lista_ordenada = sorted(set(lista))

segundo_menor = lista_ordenada[1]

segundo_maior = lista_ordenada[-2]  

print(f"O Segundo menor valor é: {segundo_menor}.")
print(f"O Segundo maior valor é: {segundo_maior}.")