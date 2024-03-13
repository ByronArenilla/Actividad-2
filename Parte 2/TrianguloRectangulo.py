import math
class TrianguloRectangulo():
    def __init__(self, base, altura):
        #Atributos del triangulo rectángulo
        self.base = base 
        self. altura = altura

    
    #Método para calcular el área de un triangulo rectángulo
    def calcular_area(self):
        return (self.base * self.altura/2)
    
    #Método para calcular hipotenusa
    def calcular_hipotenusa(self):
        return math.pow(self.base*self.base+self.altura*self.altura, 0.5)


    #Método para calcular el perímetro del triángulo
    def calcular_perimetro(self):
        return (self.base + self.altura + self.calcular_hipotenusa())

    #Método para determinas si el triangulo es:
    #Equlátero: sus tres lados son iguales
    #Escaleno: si sus tres lados son todos diferentes
    #isóceles: si dos de sus lados son iguales y el otro es diferente de los demás
        
    def determinar_tipo_triangulo(self):
        if self.base == self.altura and self.base == self.calcular_hipotenusa() and self.altura == self.calcular_hipotenusa:
            return "Es un triangulo equilatero"
        elif self.base != self.altura and self.base != self.calcular_hipotenusa() and self.altura != self.calcular_hipotenusa():
            return "Es un triángulo escaleno"
        else:
            return "Es un triángulo isóceles"
    