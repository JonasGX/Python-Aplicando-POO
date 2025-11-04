from banco.banco import Banco

class Agencia(Banco):
    def __init__(self, nome, enderco, numero):
        super().__init__(nome, enderco)
        self.numero = numero
    
    def __str__(self):
        return f'Banco: {self._nome}, numero: {self.numero}'