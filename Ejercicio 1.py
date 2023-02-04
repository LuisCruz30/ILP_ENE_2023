#Ej. 1. Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

#ENTRADA DE DATOS
calificación_1 = float(input("Escribir calificación 1: "))
calificación_2 = float(input("Escribir calificación 2: "))
calificación_3 = float(input("Escribir calificación 3: "))


#PROCESOS
suma = calificación_1 + calificación_2 + calificación_3
promedio = suma / 3




#SALIDA DE DATOS
print("El promedio de calificaciones es:", round(promedio, 2))

if (promedio > 6 and promedio <=10):
    print("APROBADO")

elif (promedio == 6):
    print("APENAS APROBADO")

elif (promedio >=0 or promedio < 6):
    print ("REPROBADO")

elif (promedio < 0 or promedio > 10):
    print ("PROMEDIO NO VÁLIDO")