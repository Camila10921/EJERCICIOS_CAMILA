#determinar si un aprendiz apruab o desaprueba algoritmia,
#sabiendo que aprobara si su promedio de tres calificaciones 
#es mayor o igual a 70; reprueba en caso contratrio
#declaro las variable de la linea 5  a la linea 7 en donde nos pide las calificaciones
calif1=int(input("ingrese la calificación 1: "))
calif2=int(input("ingrese la calificación 2: "))
calif3=int(input("ingrese la calificación 3: "))
#calculamos el promedio
promedio=(calif1+calif2+calif3)/3
#si el promedio es mayor o igual a 70 imprimimos el mensaje de que aprueba "de la linea 11 a la 12"
if promedio>=70:
    print("aprueba algoritmia")
#si el promedio es menor que esto imprimimos el mensaje de que desaprueba "de la linea 14 a la 15"
else:
    print("desaprueba algoritmia")

