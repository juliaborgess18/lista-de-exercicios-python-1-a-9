def calcular_media_aritmetica_lista(lista):
    try:
        soma_dos_valores_da_lista = sum(lista)
        tamanho_da_lista = len(lista)
        return soma_dos_valores_da_lista / tamanho_da_lista
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    except TypeError:
        print("Foram detectados elementos não numéricos")    

lista_de_numeros_atual = []  
lista_de_numeros_antiga = []  

while True:
    numero = input("Digite um número para ser adicionado na lista ou M para saber a média: ")
    
    lista_de_numeros_antiga = list(map(int, lista_de_numeros_atual))
    lista_de_numeros_atual.append(numero)
        
    if numero.lower() == 'm':
        print(calcular_media_aritmetica_lista(lista_de_numeros_antiga))
        break
    



