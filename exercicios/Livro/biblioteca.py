from livro import Livro

# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. 
# Crie duas instâncias da classe Livro e imprima essas instâncias.

livro1 = Livro('Grande sertão: veredas', 'Guimarães Rosa', 1996)
livro2 = Livro('Dom Casmurro', 'Machado de Assis', 1996)
livro3 = Livro('O Morro dos Ventos Uivantes', 'Emily Bront', 1847)
livro4 = Livro('As Flores do Mal', 'Chale Baudelaire', 1857)
livro5 = Livro('Em Busca do Tempo Perdido', 'Marcel Prous', 1996)
livro6 = Livro('O Sol Também se Levanta', 'Ernest Hemingway', 1926)
livro7 = Livro('O Som e a Fúria', 'William Faulkner', 1929)


# Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
# Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
livro1.emprestar()
livro5.emprestar()

Livro.lista_livros()

# Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro
# e retorna uma lista dos livros disponíveis publicados nesse ano.
print()
Livro.verificar_disponibilidade(1996)


# Saida...
# Titulo                         | Autor                          | Ano de Publicação:             |Disponível
# Grande sertão: veredas         | Guimarães Rosa                 | 1996                           | ❌ 
# Dom Casmurro                   | Machado de Assis               | 1996                           | ✅
# O Morro dos Ventos Uivantes    | Emily Bront                    | 1847                           | ✅
# As Flores do Mal               | Chale Baudelaire               | 1857                           | ✅
# Em Busca do Tempo Perdido      | Marcel Prous                   | 1996                           | ❌
# O Sol Também se Levanta        | Ernest Hemingway               | 1926                           | ✅
# O Som e a Fúria                | William Faulkner               | 1929                           | ✅

# Livros disponíveis do ano 1996: ['Dom Casmurro']