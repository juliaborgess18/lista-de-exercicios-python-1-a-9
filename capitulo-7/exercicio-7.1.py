nome_de_arquivo = input("Digite o nome do arquivo: ")

with open(nome_de_arquivo, "r") as resultado:
    conteudo = resultado.read()
print(conteudo)