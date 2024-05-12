idade = int(input("Insira a sua idade: "))
genero = input("Insira o seu gênero: ")

if idade >= 60 and genero == 'F':
    print("Esta mulher pode aposentar.")
elif idade >= 65 and genero == 'M': 
    print("Esta homem pode aposentar.")
else:
    print("Não pode aposentar.")