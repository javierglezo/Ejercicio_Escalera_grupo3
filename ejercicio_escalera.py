# Importamos todos los modulos 
import math
import os
import random
import re
import sys

# Definición de la función staircase
def staircase(n):
    # Bucle for que se ejecuta n veces
    for i in range(1, n + 1):
        # Imprime i símbolos '#' en cada línea
        # El valor de i incrementa en 1 en cada iteración, así que cada línea tiene un '#' más que la anterior
        print('#' * i)

# Bloque principal del programa
if __name__ == '__main__':
    # Lee un número entero desde la entrada del usuario
    #n = int(input("Introduzca un numero entero de peldaños para la escalera: "))
    n = int(input("Introduzca un numero entero para definir el tamaño de la escalera: ").strip())
    # Llama a la función staircase con el número leído como argumento
    staircase(n)
