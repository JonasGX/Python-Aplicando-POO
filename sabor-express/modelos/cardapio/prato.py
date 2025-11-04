from modelos.cardapio.item_cardapiio import ItemCardapio


# classe filha
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        # super -> Permite que a classe Prato acesse informações de outra classe
        super().__init__(nome,preco)
        self.descicao = descricao

    def __str__(self):
        return self._nome