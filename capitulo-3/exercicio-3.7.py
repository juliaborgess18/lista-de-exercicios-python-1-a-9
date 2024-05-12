numeros = []

while True:
    novo_valor = int(input("Digite um valor (0 para sair): "))
    if novo_valor == 0:
        break
    numeros.append(novo_valor)

somatorio = 0
contador = 0
for numero in numeros:
    if numero >= 0:
        somatorio += numero
        contador += 1

print(f"A média dos números positivos é de: {somatorio/contador}")