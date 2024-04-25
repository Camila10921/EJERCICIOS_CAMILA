#variables
compra=int(input("ingrese el valor de la compra: ")) #declaramos la variable del valor de la compra
descuento=int(input("ingrese el descuento: ")) #declaramos la variable del desuento al que adquirio

total_descuento=compra*descuento #declaramos la variale en donde se va a realizar el procedimiento, para solucionar primero multiplicamos el valor de la compra por el descuento
total_compra=compra+total_descuento #declaramos la variable en donde se suma el valor del despuento mas la compra 

print("la compra fue", compra,"con un descuento de", descuento, "y el valor final a pagar es", total_compra)