lista_de_numeros = []

while True:
    numero = input("Digite um numero (ou q para sair): ")
    if numero.lower() == 'q':
        break
    lista_de_numeros.append(int(numero))

lista_de_quadrados = map(lambda x:x**2, lista_de_numeros)
for quadrados in lista_de_quadrados:
    print(quadrados)    