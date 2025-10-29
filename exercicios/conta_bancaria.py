class ContaBancaria():
    todos_clientes = []
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
        ContaBancaria.todos_clientes.append(self)
        
    
    def __str__(self):
        return f"""Titular: {self.titular}\nSaldo: R${self.saldo}\nStatus da Conta: {self.ativo_status}\n"""
    
    def clientes():
        print(f"{'Titular'.ljust(25)} | {'Saldo'.ljust(25)} | {'Status da conta'.ljust(25)}")
        for cliente in ContaBancaria.todos_clientes:
            print(f'{cliente.titular.ljust(25)} | {str(cliente.saldo).ljust(25)} | {cliente.ativo_status.ljust(25)}')

    @property
    def ativo_status(self):
        return '✅' if self.ativo else '❌'
    
    def ativar_conta(self):
        self.ativo = not self.ativo

jonas = ContaBancaria('Jonas Gomes', 4500.00)
nicolly = ContaBancaria('Jubileu Pipoca', 1000.00)
joao = ContaBancaria('Batatinha frita 123', 100000.00)
jonas.ativar_conta()
joao.ativar_conta()

ContaBancaria.clientes()

# saida...
# Titular                   | Saldo                     | Status da conta
# Jonas Gomes               | 4500.0                    | ✅
# Jubileu Pipoca            | 1000.0                    | ❌
# Batatinha frita 123       | 100000.0                  | ✅