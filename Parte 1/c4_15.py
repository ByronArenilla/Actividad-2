p_esferaA = float(input("Ingrese el peso de la esfera A: "))
p_esferaB = float(input("Ingrese el peso de la esfera B: "))
p_esferaC = float(input("Ingrese el peso de la esfera C: "))
p_esferaD = float(input("Ingrese el peso de la esferac D: "))

if p_esferaA == p_esferaB and p_esferaA == p_esferaC:
    print("D es la esfera diferente")
    if p_esferaD > p_esferaA:
        print("D es la de mayor peso")
    else:
        print("D es la de menor peso")
elif p_esferaA == p_esferaB and p_esferaA == p_esferaD:
    print("C es la esfera diferente")
    if p_esferaC > p_esferaA:
        print("C es la de mayor peso")
    else:
        print("C es la de menor peso")
elif p_esferaA == p_esferaC and p_esferaA == p_esferaD:
    print("B es la esfera diferente")
    if p_esferaB > p_esferaD:
        print("B es la de mayor peso")
    else:
        print("B es la de menor peso")
else:
    print("A es la esfera diferente")
    if p_esferaA > p_esferaB:
        print("A es de mayor peso")
    else:
        print("A es la de menor peso")