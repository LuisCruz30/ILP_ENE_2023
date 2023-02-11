# FUNCIONES/RUTINAS/PROCEDIMIENTOS/MÓDULOS/MÉTODOS.- Tareas o acciones a ejecutar
'''
SINTAXIS:

def Nombre_de_la:Función (Argumentos o Parámetros):
    Contenido de la función
    return (valores) que van a retornar, regresar o devolver la función
'''

# DECLARAR O CREACIÓN DE LAS FUNCIONES
def Sumar (a, b): # Se obtienen o reciben dos parámetros
    suma = a + b
    return suma   # Devolviendo el valor de la suma

def Restar (x, y):
    resta = x - y
    return resta

# INVOCAR O MANDAR A LLAMAR UNA FUNCIÓN
sum = Sumar (10, 3) # Pasar o enviar los valores de los parámetros

# SALIDA DE DATOS
print ("La suma es", sum)
print ("la resta es", Restar (20, 4))