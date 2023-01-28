# Operaciones matemáticas

#Importar una librería o biblioteca de funciones mátematicas
import math

# Entrada de datos
# Declarar o crear dos variables
número_1 = float(input("Escribe un número: "))
número_2 = float(input('Escribe otro número: '))

#CONSTANTE
GRAVEDAD_TIERRA = 9.8
PI = 3.1416

# Procesos (Operaciones o cálculos matemáticos y/o lógicos)
suma = número_1 + número_2
resta = número_1 - número_2
multiplicación = número_1 * número_2
división = número_1 / número_2
potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2)
cuadrado = número_1 ** 2
cubo = pow(número_2,3)
raíz_cuadrada_1 = math.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(9, 1/3)
módulo_residuo_1 = 9 % 2
módulo_residuo_2 = 20 % 6


# Salida de datos
print ("Redondear la suma de constantes es igual a", round(GRAVEDAD_TIERRA + PI, 3))
print("La suma es igual a", suma)
print("La resta es igual a", resta)
print("La multiplicación es igual a", multiplicación)
print("La división es igual a", división)
print("La potencia 1 es igual a", round(potencia_1, 2)) 
print("La potencia 2 es igual a", round(potencia_2, 4))

print('La suma es igual a ' + str(suma)) #CONCATENAR (Unión de dos o más textos) 
print('La resta es igual a ' + str(resta)) #CASTEO: Conversión de un tipo de dato eb otro tipo de dato
print('La multiplicación es igual a ' + str(multiplicación))
print('La división es igual a ' + str(división))
print('La potencia 1 es igual a ' + str(potencia_1)) 
print('La potencia 2 es igual a ' + str(potencia_2))

print(f"La suma es igual a {suma}") #f: Formateo de interpolación de texto
print(f"La resta es igual a {resta}")
print(f"La multiplicación es igual a {multiplicación}")
print(f"La división es igual a {división}")
print(f"La potencia 1 es igual a {potencia_1}") 
print(f"La potencia 2 es igual a {potencia_2}")

print ("El módulo residuo es igua a", módulo_residuo_1)
print ("El módulo residuo es igua a", módulo_residuo_2)