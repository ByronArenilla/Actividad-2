import math
class Circulo():
    def __init__(self, radio):
        self.radio = radio  #Atributo que define el radio de un círculo

    
    #Método que calcula el area de un círculo 
    def calcular_area(self):
        return math.pi*math.pow(self.radio,2)
    
    #Método que calcula el perímetro del círculo
    def calcular_perimetro(self):
        return 2*math.pi*self.radio

        
