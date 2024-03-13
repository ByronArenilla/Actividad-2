numero_inscripcion = input("Ingrese el número de inscripción: ")
nombres = input("Ingrese su nombre y apellido: ")
patrimonio = int(input("Ingrese su patrimonio: "))
estrato = int(input("Ingrese su estrato social: "))
matricula = 50000

if patrimonio > 2000000 and estrato > 3:
    matricula += matricula*0.03
print(f"El estudiante  con número de inscripción {numero_inscripcion} y nombre {nombres} debe pagar {matricula:.2f}")