numero = int(input("Digite um número: "))
fatorial = 1

while True:
    if numero == 0:
        break
    fatorial *= numero
    numero = numero - 1

print(fatorial)