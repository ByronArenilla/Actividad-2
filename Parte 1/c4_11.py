a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))
c = int(input("Ingrese otro número entero: "))

if a > b and a > c:
    print(f"El número mayor es {a}")
elif b > a and b > c:
    print(f"El mayor es {b}")
elif c >a and c > b:
    print(f"El mayor es {c}")
else:
    print("Los números son iguales")

