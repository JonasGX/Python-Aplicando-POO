

class Pessoa():
    def __init__(self, nome='', idade=0, profissao=None):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    def aniversario(self):
        self.idade += 1
        print(self.idade)
    
    @property
    def saudacao(self):
        if self.profissao is None:
            return f'Olá, sou {self.nome}!'
        else:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'

# Criando instâncias das classes
jonas = Pessoa('Jonas', 23, 'Data Engineer')
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(jonas)
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
jonas.aniversario()
pessoa1.aniversario()
pessoa3.aniversario()
print()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(jonas)
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(jonas.saudacao)
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)