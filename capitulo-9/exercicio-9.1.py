primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

try:
    print(f"Resultado da divisão {primeiro_numero / segundo_numero}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Números inválidos.")