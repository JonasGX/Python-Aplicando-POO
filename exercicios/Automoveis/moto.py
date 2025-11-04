from veiculos import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo
    
    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | status do veiculo: {self._ligado} | tipo: {self._tipo}'