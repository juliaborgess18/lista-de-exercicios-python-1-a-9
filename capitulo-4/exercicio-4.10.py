import re 

frase = input("Digite uma frase: ")
re_artigos_frase = r'\b(o|a|os|as|um|uma|uns|umas|e|à)\b'
nova_frase = re.sub(re_artigos_frase, "", frase)

print(nova_frase)