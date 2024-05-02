#definimos una variables en la cual nos pide los datos necesarios como lo son el valor de la compra y el color que escogio, de la linea2 a la 3
compra=float(input("ingrese el valor de la compra: "))
color=str(input("ingrese el color que saco: "))
#con la variable if ponemos lo del descuento si es rojo, de la linea 5 a la 6
if color == "rojo":
    descuento=15
#con la variable elif ponemos lo del descuento si es verde, de la linea 8 a la 9
elif color == "verde":
    descuento=20
#con la variable elif ponemos lo del descuento si es diferente, de la linea 11 a la 12
elif color == "diferente":
    descuento=0
#sacamos el valor total a pagar, realizando el procedimiento correspondiente
valorPagar=compra-(compra*descuento/100)
#imprimimos elmensaje con todos los datos correspondientes 
print("el valor de la compra es de", compra, "el color que saco fue", color, "con un descuento de", descuento, "y el valor a pagar es de", valorPagar)