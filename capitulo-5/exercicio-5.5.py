def funcao_variavel_x() -> None:
    x = 99
    print(f"O valor de 'X' é {x} dentro da função.")

funcao_variavel_x()
print(f"O valor de 'X' é {x} fora da função.")

# Traceback (most recent call last):
#   File "c:\Users\Igor\Desktop\lista-de-exercicios-python\capitulo-5\exercicio-5.5.py", line 6, in <module>
#     print(f"O valor de 'X' é {x} fora da função.")
#                               ^
# NameError: name 'x' is not defined
# R: A variável 'X' só existe dentro da função 'funcao_variavel_x', por isso ela não pode ser chamada fora do escopo da mesma.