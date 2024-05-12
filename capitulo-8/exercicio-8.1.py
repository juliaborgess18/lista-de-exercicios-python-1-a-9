class Pessoa:
    def __init__(self, nome, idade) :
        self.nome = nome
        self.idade = idade 

    def mostrar_dados(self, ) -> None:
        print(f"{self.nome}, {self.idade}")
        
if __name__ == "__main__":
    p1 = Pessoa("Júlia",22)
    p2 = Pessoa("Karina",47)

    p1.mostrar_dados()
    p2.mostrar_dados()