#variable
nombre=str(input("ingrese el nombre del estudiante: "))
calificación_promedio_actividades=float(input("ingrese la calificación promedio de las actividades: "))
calificación_proyecto_final=float(input("ingrese la calificación del proyecto final: "))
calificación_promedio_evaluaciones=float(input("ingrese la calificación promedio de las evaluaciones parciales: "))
nota_final=(calificación_promedio_actividades*0.3)+(calificación_proyecto_final*0.5)+(calificación_promedio_evaluaciones*0.2)#proceso que se realiza para obtener la nota final
print("la nota final de algoritmia del estudiante", nombre, "es: ", nota_final)
