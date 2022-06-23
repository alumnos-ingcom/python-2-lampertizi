################
# Tiziano Lamperti  - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
1. Pares e impares
Escribir una función que retorne True cuando un número entero es par 
y False cuando no lo sea, sin utilizar módulo.
"""

def encontrar_par(numero):


    """
    Retorna un bool indicando si el numero es par o no.
    """
    cuenta1 = numero / 2
    cuenta2 = numero // 2
    return(cuenta2 - cuenta1 == 0)

def principal():


    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("ingrese un n° para saber si es par o no: "))
    salida = encontrar_par(numero)
    print(salida)

if __name__ == "__main__":
    principal()

