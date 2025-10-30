
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Ariba', 'Mexicano')
restaurante_japones = Restaurante('Tai food', 'Japonesa')
restaurante_brasileiro = Restaurante('Brasileirao', 'Brasileira')

restaurante_praca.alternar_estado()
restaurante_japones.alternar_estado()

restaurante_praca.receber_avaliacao('Jubileu Manteiga', 3)
restaurante_praca.receber_avaliacao('Agostinho Carrara', 2)
restaurante_praca.receber_avaliacao('Relampago Marquinhos', 2)
restaurante_japones.receber_avaliacao('Relampago Marquinhos', 4)
restaurante_japones.receber_avaliacao('Jubileu Manteiga', 5)
restaurante_japones.receber_avaliacao('Agostinho Carrara', 5)



def main():
    Restaurante.lista_restaurantes()


if __name__ == '__main__':
    main()