import math
A = float(input("Ingrese el valor A: "))
B = float(input("Ingrese el valor B: "))
C = float(input("Ingrese el valor C: "))

discriminante = B**2 -4*A*C
if discriminante > 0:
    # Hay dos soluciones reales diferentes
    x1 = (-B+ math.sqrt(discriminante)/ (2*A))
    x2 = (-B - math.sqrt(discriminante)/ (2*A))
    print (f"Solución 1: {x1} - Solución 2: {x2}")
elif discriminante == 0:
    #Una solución real
    x = -B/ (2*A)
    print(f"Solución: {x}")
else:
    #soluciones complejas
    parte_real = -B/ (2*A)
    parte_imaginaria = math.sqrt(abs(discriminante)) / (2*A)
    solucion1 = complex(parte_real, parte_imaginaria)
    solucion2 = complex (parte_real,parte_imaginaria)
    print(f"Solución 1: {solucion1} -  Solución 2: {solucion2}")