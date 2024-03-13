p_esferaA = float(input("Ingrese el peso de la esfera A: "))
p_esferaB = float(input("Ingrese el peso de la esfera B: "))
p_esferaC = float(input("Ingrese el peso de la esfera C: "))

if p_esferaA > p_esferaB and p_esferaA > p_esferaC:
    print("La esfera A es la de mayor peso")
elif p_esferaB > p_esferaA and p_esferaB > p_esferaC:
    print("La esfera B es la de mayor peso")
elif p_esferaC > p_esferaA and p_esferaC > p_esferaB:
    print("La esfera C es la de mayor peso")
else:
    print("Las esferas tiene pesos iguales")