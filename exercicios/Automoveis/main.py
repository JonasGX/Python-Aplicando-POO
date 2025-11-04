from carro import Carro
from moto import Moto

def main():
    uno = Carro('FIAT', 'fiat uno 147', 4)
    lambreta = Moto('Honda', 'Lambreta do grau', 'Casual')
    print(uno)
    print(lambreta)


if __name__ == '__main__':
    main()