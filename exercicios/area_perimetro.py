import math

class Circle():
    def __init__(self, diametro):
        self.diametro = diametro
        self.raio = diametro / 2

    def calcula_area(self):
        return f'A area do circulo é: {round(math.pi * (self.raio ** 2))}cm'
    
    def calcular_perimetro(self):
        return f'O perimetro do circulo é: {(2 * math.pi * self.raio):.2f} cm'

circulo1 = Circle(20)

print(circulo1.calcula_area())
print(circulo1.calcular_perimetro())