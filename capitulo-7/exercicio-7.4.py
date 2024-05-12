import os

nome_do_arquivo = input("Digite o nome do arquivo: ")
nome = os.path.splitext(nome_do_arquivo)[0]
extensao = os.path.splitext(nome_do_arquivo)[1]
os.rename(nome_do_arquivo, f"renomeado{extensao}")