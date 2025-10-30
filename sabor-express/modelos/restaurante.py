from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    # Metodo construtor: Sempre que acionarmos a classe esse método é chamado
    # o self é apenas um padrão do python, mas pode ser colocado qualquer nomenclatura
    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    # O metodo str retorna a representação textual de acordo com o que é configurado aqui dentro
    # Por padrão ao chamar a classe é retornado um id, exemplo: <__main__.Restaurante object at 0x000001EC6FDFFBB0>
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def lista_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação 0-5'.ljust(25)} |{'Status'.ljust(25)} ")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '✅' if self._ativo else '❌'

    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if self._ativo and len(self._avaliacao) > 0:
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            qtd_notas = len(self._avaliacao)
            media = round(soma_notas / qtd_notas, 1)
            return media

        else:
            return '-'

