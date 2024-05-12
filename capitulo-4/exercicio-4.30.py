import datetime

data_atual = datetime.datetime.now()
mes_atual = data_atual.month

numero_da_semana_atual = data_atual.strftime('%W')
print(numero_da_semana_atual)
