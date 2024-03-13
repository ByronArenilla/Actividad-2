class Cuadrado():
    def __init__(self, lado):
        self.lado = lado #Atributo del cuadrado

    #Método para calcular área
    def calcular_area(self):
        return self.lado*self.lado
    
    #Método para calcular el perímetro
    def calcular_perimetro(self):
        return(4*self.lado)


    