
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebiba
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Ariba', 'Mexicano')
restaurante_japones = Restaurante('Tai food', 'Japonesa')
restaurante_brasileiro = Restaurante('Brasileirao', 'Brasileira')


bebida_suco = Bebiba('Melancia', 5.00, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')


def main():
    # Restaurante.lista_restaurantes()
    print(bebida_suco)
    print(prato_paozinho)


if __name__ == '__main__':
    main()