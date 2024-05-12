dict_alunos = {}

while True:
    nome_aluno =input("Nome do aluno (ou 'q' para sair): ")
    if nome_aluno.lower() == 'q':
        break  
    nota_aluno = float(input(f"Nota de {nome_aluno}: "))
    dict_alunos[nome_aluno] = nota_aluno   
    
# for nome, nota in dict_alunos.items():
#     print(f"{nome}:{nota}")

alunos_com_nota_superior_a_7 = {nome:nota for nome, nota in dict_alunos.items() if nota > 7}
print(alunos_com_nota_superior_a_7)
    
    

