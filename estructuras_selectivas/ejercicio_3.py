#una empresa quiere hacer una compra de varias piezas de la
#misma clase a una fabrica de bolsos
#definimos una variable en la cual pide el monto total de la compra
montoTotal=float(input("ingrese el monto total de la compra: "))
#colocamos el if y definimos si el monto excede de 500000, la empresa pagara un porcentaje, le pedira prestado al banco otro porcentaje y le pedira un credito a la empresa pero la empresa cobra un porcentaje sobre el valro total
#de la linea 7 a la 10
if montoTotal>500000:
    empresa=montoTotal*0.55
    banco=montoTotal*0.30
    credito=montoTotal*0.15+(montoTotal*0.20)
#pero si el valor no es de 500000 la empresa pagara un porcetaje y le pedra un credito, pero de igual modo esa credito va con un iva
#de la linea 13 a la 15
else:
    empresa=montoTotal*0.70
    credito=montoTotal*0.30+(montoTotal*0.20)
#y por ultimo imprimimos un mensaje ne la cual esten todos los datos 
print("monto que pago la propia empresa", empresa, ", el banco le presto", banco, "y un credito con un monto de", credito)
