def abrir_arquivo(arquivo):
    try:
        with open(arquivo, "r") as resultado:
            print(resultado.read()) 
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except IOError:
        print("Arquivo não pode ser lido")
    finally:
        print("E é isso!")
        
nome_do_arquivo = input("Digite o nome do arquivo: ")
abrir_arquivo(nome_do_arquivo)