#variables
sueldo=500000 #declaramos el sueldo fijo
comisiones=700 #declaramos cuanto se cobra por comisión


nombre=str(input("nombre del vendedor: ")) #definimos la variable del nombre del vendedor
ventas=int(input("ingrese el total de comisiones: ")) #definicmos la variable para ingresar el numero de ventas

total_comisiones=ventas*comisiones #declaramos los ejercicios necesarios para resolver el problema, aca multiplicamos las ventas paor la comisiones para asi sacar el valor total de comisiones
total_sueldo=total_comisiones+sueldo #sumamos las comisiones mas el total del sueldo para asi resolver la operación del total del sueldo 

print("el vendedor", nombre, "tiene un sueldo de", sueldo,"durante el mes obtuvo una comisión de", total_comisiones,"y el valor total a pagar es", total_sueldo) #creamos y frase y los procedimientos que se deben realizar 
