#programa para estimular a los alumnos
nombreAlumno=str(input("ingrese su nombre: "))#definimos una variable en la cual pida el nombre del alumno 
pensión=float(input("ingrese el valor de la pensión: "))#definimos una variable en la cual nos pide el valor de la pensión 
nota1=float(input("ingrese su nota de matematicas: "))#definimos una variable en la cual le pide al usuario una nota de matematicas
nota2=float(input("ingrese su nota de castellano: "))#definimios una variable en la cual le pide al usuario una nota de castellano 
nota3=float(input("ingrese su nota de ingles: "))#definimos una variable en la cual le pide al usuario una nota de ingles
promedio=nota1+nota2+nota3/3 #lo que hacemos aca es definir la variable para hacer el procedimiento requerido 
if promedio >=  9: #definimos la función if si el promedio es mayor a 9
    descuento=pensión*0.30 #realizamos la operacion para sacar el porcentaje
    totalDescuento=pensión-descuento #realizamos la operación para restar el descuento de la pension
elif promedio < 9: #definimos la función elif si el promedio es menor a 9
    descuento=pensión*0.10 #realizamos la operación para sacar el porcentaje del iva
    totalDescuento=pensión+descuento #realizamos la operación para sumar la pension con el iva
print("el alumno", nombreAlumno, "con un promedio de", promedio, "tiene un descuento de", descuento, "por lo tanto debera pagar", totalDescuento)#imprimimos la frase que quiero que vea el usuario