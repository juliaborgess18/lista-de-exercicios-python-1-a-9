class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo 
        self.autor = autor 
    
    def mostrar_dados_livro(self, ) -> None:
        print(f"{self.titulo} foi escrito por {self.autor}")
        
class LivroFisico(Livro):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self.paginas = paginas
    
    def mostrar_dados(self,) -> None:
        print(f"{self.titulo} foi escrito por {self.autor} e tem {self.paginas} páginas")
    
if __name__ == "__main__":
    livro_fisico = LivroFisico("Pensando como Bill Gates", "Daniel Smith", 221)
    
    livro_fisico.mostrar_dados()