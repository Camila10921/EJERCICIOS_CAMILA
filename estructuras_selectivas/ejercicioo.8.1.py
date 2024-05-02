#tomando coo base los resultados obtenidos en un laboratorio de analisis
#clinicos, un medico determina si una persona tiene anemia o no, lo cual
#de su nivel de hemoglobina en la sangre, de su edad y de su sexo
#declaramos variables como lo son el nombre y la edad para asi mismo empezar el procedimiento, de la linea 5 a la 6
nombrePaciente=str(input("ingrese su nombre: "))
mayor12Meses=str(input("¿eres mayor a 12 meses?: "))
#depende de lo que me respondan, se le coloca el if y el elif
if mayor12Meses == "si":
    años=int(input("ingresa cuanto años tienes: "))
elif mayor12Meses == "no":
    meses=int(input("ingresa cuantos meses tienes: "))
#declaramos una variable en la cual pediremos el nivel de hemoglobina 
nivelHemoglobina=float(input("puedes introducir tu nivel de hemoglobina en g%: "))
#declaramos una variable en la cual pediremos el genero al usuario
genero=str(input("ingresar tu genero de nacimiento: "))

#se utilizan las distintas estructuras de acuerdo al proceso
if años<=1:
    rango = (13, 26)
elif años>=2 and años<=6:
    rango = (10, 18)
elif años>=7 and años<=12:
    rango = (11, 15)
elif meses>=2 and meses<=5:
    rango = (11.5, 15)
elif meses>=6 and meses<=10:
    rango = (12.6, 15.5)
elif meses>=11 and meses<=15:
    rango = (13, 15.5)
elif genero.lower() == 'femenino':
    rango = (12, 16)
elif genero.lower() == 'masculino':
    rango = (14, 18)

#si no colocan femenino o masculino colocamos esta variable 
else:
    print("por favor introduce un genero valido")

#y por ultimo imprimimos el resultado
if nivelHemoglobina < rango[0]:
    print ("Eres positivo para anemia")
else:
    print ("Eres negativo para anemia")

