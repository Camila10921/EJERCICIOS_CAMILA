#calcular el numero de pulsaciones que debe de tener una 
#persona cada 10 segundos de aerobicos
#definimos las variables necesarias como lo son el sexo y la edad de la persona, de la linea 4 a la 5
sexo=str(input("ingrese cual es su sexo: "))
edad=int(input("ingrese su edad: "))
#colocamos el if si es femenino y se realiza el procedimiento para hallar las pulsaciones, de la linea 7 a la 8
if sexo == "femenino":
    pulsaciones=(220-edad)/10
#colocamos el elif si no es femenino y se realiza el procedimiento para hallar las pulsaciones, de la linea 10 a la 11
elif sexo == "masculino":
    pulsaciones=(210-edad)/10
#y por ultimo imprimimos el mensaje que queremos que le usuario vea 
print("una persona", sexo, "tiene", pulsaciones, "por cada 10 segundos de aeróbicos")