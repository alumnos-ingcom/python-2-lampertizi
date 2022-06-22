################
# Tiziano Lamperti  - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Implementar una función que permita obtener el n-esimo termino de la 
sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
PRE: un n° natural mayor a 2

POST: término de la sucesión pedido
"""

def encontrar_a_fibo(num_sucesion):
    """
    retorna el término > 2 de la sucesion de fibonacci que se pide
    """
    if num_sucesion < 2:
        raise ValueError("tiene que ser un n° mayor a 2")
    count = 0
    termino1,termino2 = 0, 1
    lista_numeros = []
    while count < num_sucesion:
        lista_numeros.append(termino1)
        termino_nuevo = termino1 + termino2
        termino1 = termino2
        termino2 = termino_nuevo
        count = count + 1
    return lista_numeros[-1]

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    hasta_donde = int(input("qué termino querés saber? "))
    resultado = encontrar_a_fibo(hasta_donde)
    print(resultado)
    pass

if __name__ == "__main__":
    principal()

