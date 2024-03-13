ventas_dep1 = float(input("Ingrese el importe global de las ventas del departamento 1: "))
ventas_dep2 = float(input("Ingrese el importe global de las ventas del departamento 2: "))
ventas_dep3 = float(input("Ingrese el importe global de las ventas del departamento 3: "))

salario = float(input("Ingrese el salario de los vendedores: "))
total_ventas = ventas_dep1 + ventas_dep2 + ventas_dep3

if ventas_dep1 > total_ventas * 0.33:
    salario1 = salario + salario * 0.2
else:
    salario1 = salario

if ventas_dep2 > total_ventas * 0.33:
    salario2 = salario + salario *0.2
else:
    salario2 = salario

if ventas_dep3 > total_ventas * 0.33:
    salario3 = salario + salario *0.2
else:
    salario3 = salario

print(f"""Salario departamento 1: {salario1}
Salario departamento 2: {salario2}
Salario departamento 3 {salario3}""")

