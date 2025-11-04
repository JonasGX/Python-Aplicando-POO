from veiculos import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas
    
    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | status do veiculo: {self._ligado} | qtd portas: {self._portas}'