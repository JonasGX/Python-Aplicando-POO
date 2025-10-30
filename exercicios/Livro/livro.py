
class Livro():
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'Resumo da instância Titulo: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}'
    
    @classmethod
    def lista_livros(cls):
        print(f"{'Titulo'.ljust(30)} | {'Autor'.ljust(30)} | {'Ano de Publicação:'.ljust(30)} |{'Disponível'.ljust(30)} ")
        for livro in cls.livros:
            print(f"{livro.titulo.ljust(30)} | {livro.autor.ljust(30)} | {str(livro.ano_publicacao).ljust(30)} | {livro.disponivel} ")

    @property
    def disponivel(self):
        return '✅' if self._disponivel else '❌'
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.livros:
            if ano == livro.ano_publicacao and livro._disponivel:
                livros_disponiveis.append(livro.titulo)
        
        if len(livros_disponiveis) > 0:
            print(f'Livros disponíveis do ano {ano}: {livros_disponiveis}')
        else:
            print(f'Não há livros disponíveis para do ano: {ano}')

        return livros_disponiveis