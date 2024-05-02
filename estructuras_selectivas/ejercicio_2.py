#calcular el valor a pagar por la compra de zapatillas.
#si se compran se aplica un descuento del 20% sobre el
#total de la compra y si son menos de tres zapatillas 
#un descuento del 10%
cantZapa=int(input("digite cuantos pares de zapatillas compraste: ")) #declaramos una variable en la cual le pide al usuario la cantidad de zapatillas
valorSindesc=float(input("digite el valor total de la compra: ")) #declaramos una variable en la cual le pide al cliente el valor de la compra
#le colocamos if y si la cantidad de zapatos es mayor o igual a 3 pares el descuento es del 20% "de la linea 8 a la linea 9"
if cantZapa>=3:
    descuento=20
#le colocamos else si son menos y le damos un descuento del 10% "de la linea 11 a la 12"
else:
    descuento=10
#hacemos el procedimeinto correspondiente en la cual sacamos el descuento
valorCondesc=valorSindesc-(valorSindesc*descuento/100)
#imprimimos el valor que quiero que vea el usuario
print("el valor total de su compra es de", valorCondesc)