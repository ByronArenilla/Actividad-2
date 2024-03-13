from Circulo import Circulo
from Cuadrado import Cuadrado 
from Rectangulo import Rectangulo
from TrianguloRectangulo import TrianguloRectangulo
figura1 = Circulo(2)
figura2 = Rectangulo(1,2)
figura3 = Cuadrado (3)
figura4 = TrianguloRectangulo(3,5)

print(f"El área del círculo es {figura1.calcular_area():.2f} y su perímetro es {figura1.calcular_perimetro():.2f}")
print(f"El área del rectángulo es {figura2.calcular_area()} y su perímetro es {figura2.calcular_perimetro()}")
print(f"El área del cuadrado es {figura3.calcular_area()} y su perímetro es {figura3.calcular_perimetro()}")
print(f"El área del triangulo es {figura4.calcular_area()} y su perímetro es {figura4.calcular_perimetro():.2f}. El triangulo {figura4.determinar_tipo_triangulo()}")
