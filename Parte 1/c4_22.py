nombre_empleado = input("Ingrese el nombre del empleado: ")
valor_hora = float(input("Ingrese el valor de la hora de trabajo: "))
horas_trabajadas = float(input("Ingrese las horas que trabaja al mes: "))
salario_mesual = valor_hora * horas_trabajadas
if salario_mesual > 450000:
    print (f"Nombre: {nombre_empleado} -  Salario: {salario_mesual}")
else:
    print(f"Nombre: {nombre_empleado}")