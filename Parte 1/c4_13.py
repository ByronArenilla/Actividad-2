valor_compra = int(input("Ingrese el valor de la compra: "))
color_bolita = input("Escriba el color de la bolita que le salió: ")
descuento = 0
if color_bolita.lower() == "verde":
    valor_compra = valor_compra*0.9
    descuento = "10%"
elif color_bolita.lower() == "amarillo" or  color_bolita.lower() == "amarilla":
    valor_compra = valor_compra* 0.75
    descuento = "25%"
elif color_bolita.lower() == "azul":
    valor_compra = valor_compra*0.5
    descuento = "50%"
elif color_bolita.lower() == "rojo" or color_bolita.lower() == "roja":
    valor_compra = 0
    descuento = "100%"
elif color_bolita.lower() == "blanco" or  color_bolita.lower() =="blanca":
    valor_compra = valor_compra
    descuento = "0%"

print(f"El valor de su compra es {valor_compra}. Como sacó la bolita {color_bolita}, se le aplicó un descuento del {descuento}")