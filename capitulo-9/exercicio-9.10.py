from os import system


def importar_modulo(modulo):
    try: 
        __import__(modulo)
    except ModuleNotFoundError:
        print("O módulo não existe!")
    finally:
        print("Operação finalizada.")
    
nome_do_modulo = input("Digite o nome do módulo: ")
importar_modulo(nome_do_modulo)