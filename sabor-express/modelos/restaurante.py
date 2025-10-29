class Restaurante:
    restaurantes = []
    # Metodo construtor: Sempre que acionarmos a classe esse método é chamado
    # o self é apenas um padrão do python, mas pode ser colocado qualquer nomenclatura
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    # O metodo str retorna a representação textual de acordo com o que é configurado aqui dentro
    # Por padrão ao chamar a classe é retornado um id, exemplo: <__main__.Restaurante object at 0x000001EC6FDFFBB0>
    def __str__(self):
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def lista_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Ativo'.ljust(25)} ")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

# Instânciando objetos dentro da classe
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana')

Restaurante.lista_restaurantes()
