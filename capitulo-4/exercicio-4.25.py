import datetime

data_atual = datetime.datetime.now()
dias_adicionais = datetime.timedelta(30)
nova_data = data_atual + dias_adicionais

print(nova_data)