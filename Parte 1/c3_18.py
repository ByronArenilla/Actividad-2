codigo_empleado = "501015"
nombre_empleado = "Byron Arenilla"
horas_trabajadas = 150
valor_hora = 10000
salario_bruto = horas_trabajadas*valor_hora
retefuente =  salario_bruto*0.035
salario_neto = salario_bruto - retefuente

print(f"El trabajador {nombre_empleado} con código {codigo_empleado}, que trabajo {horas_trabajadas} horas, cuyo valor hora es ${valor_hora}. tiene un salario bruto de ${salario_bruto} y un salario neto de ${salario_neto}")