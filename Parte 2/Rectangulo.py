class Rectangulo():
    def __init__(self,base,altura):
        #Atributos
        self.base = base
        self.altura = altura

    #Método para calcular área de un rectángulo
    def calcular_area(self):
        return self.base * self.altura
    

    #Método para calcular perímetro
    def calcular_perimetro(self):
        return (2*self.base)+(2*self.altura)
    



