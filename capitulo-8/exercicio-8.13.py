class ContaBancaria:
    def __init__(self,):
        self.saldo = 0
        
    def depositar_conta_bancaria(self, valor):
        self.saldo +=valor 
    
    def sacar_conta_bancaria(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor 
        else:
            print("Não há saldo suficiente para continuar a operação")
    
    def consultar_saldo_conta_bancaria(self):
        return self.saldo 
    
class ContaPoupanca(ContaBancaria):
    def __init__(self, taxa_juros):
        super().__init__()
        self.taxa_juros = taxa_juros
        
    def rendimento_conta_poupanca(self, meses):
        return self.saldo * ((1 + self.taxa_juros)**meses-1)
    
if __name__ == "__main__":
    conta_poupanca = ContaPoupanca(0.005)
    
    conta_poupanca.depositar_conta_bancaria(1000)
    resultado = conta_poupanca.rendimento_conta_poupanca(12)
    print(f"Saldo após 12 meses: R${resultado}")
    
    
    
    