import math
a = 4
b = 5
c = 6
perimetro = a + b + c
s = (a+b+c)/2
area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
print(f"Un triangulo con lados {a},{b},{c} tiene un perímetro de {perimetro}, un semiperímetro {s} y un area {area:.3f}")