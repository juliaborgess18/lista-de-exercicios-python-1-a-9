def read_file(arquivo):
    try:
        with open(arquivo, 'r') as resultado:
            print(resultado.read()) 
    except FileNotFoundError:
        print("Arquivo não existe")
    finally:
        print("E é isso!")

nome_do_arquivo = input("Digite o nome do arquivo: ")
read_file(nome_do_arquivo)