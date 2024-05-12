import os 

with open("arquivo_vazio.txt", "a") as resultado:
    solicita_usuario_nome_do_arquivo_para_exclusao = input("Digite o nome do arquivo criado para que o sistema exclua-o: ")

os.remove(solicita_usuario_nome_do_arquivo_para_exclusao)
    