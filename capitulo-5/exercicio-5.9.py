valor_alvo = 50
lista_vinhos = [
    { 'nome': 'Vinho A', 'valor': 19.90 },
    { 'nome': 'Vinho B', 'valor': 35.99 },
    { 'nome': 'Vinho C', 'valor': 43.59, },
    { 'nome': 'Vinho D', 'valor': 59.00 },
    { 'nome': 'Vinho E', 'valor': 59.95 }
    ]

encontrar_vinho_mais_caro = lambda vinho: vinho['valor'] >= valor_alvo 
resultado = list(filter(encontrar_vinho_mais_caro, lista_vinhos))

print(resultado)

