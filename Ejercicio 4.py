#Ej. 4. Pedir la cantidad de grados y convertirlos a °C, °F y K.

#ENTRADA DE DATOS
grados_celcius = float(input("Escribir temperatura: "))


#PROCESOS
grados_fahrenheit = (grados_celcius * 1.8) + 32
grados_kelvin = grados_celcius + 273.15

#SALIDA DE DATOS
print("La temperatura es de:", grados_celcius, "°C")
print("La temperatura es de:", round(grados_fahrenheit, 2), "°F")
print("La temperatura es de:", grados_kelvin, "K")