nombre_trabajador = input("Ingrese su nombre: ")
horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
valor_hora = int(input("Ingrese el valor de la hora de trabajo: "))
salario = 0
if horas_trabajadas > 40 and horas_trabajadas <= 48:
    salario = (40*valor_hora)+((horas_trabajadas-40)*2*valor_hora)
elif horas_trabajadas > 48:
    salario = (40*valor_hora)+(8*2*valor_hora)+((horas_trabajadas-48)*3*valor_hora)
else:
    salario = horas_trabajadas * valor_hora


print(f"El salario de {nombre_trabajador} es de {salario}")