lista_de_palavras = []

while True:
    palavra = input('Digite uma palavra (ou q para sair): ')
    
    if palavra.lower() == 'q':
        break 
    
    lista_de_palavras.append(palavra)
    
tamanho_de_cada_palavra_na_lista_de_palavras = map(lambda p:len(p),lista_de_palavras)

for p in tamanho_de_cada_palavra_na_lista_de_palavras:
    print(p)
    