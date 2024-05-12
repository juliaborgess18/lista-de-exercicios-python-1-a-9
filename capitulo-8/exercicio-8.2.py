class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area_do_retangulo(self, ) -> float:
        return self.largura * self.altura
        
if __name__ == "__main__":
    retangulo_1 = Retangulo(10,15)
    
    print(retangulo_1.calcular_area_do_retangulo())