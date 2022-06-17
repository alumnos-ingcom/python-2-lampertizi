################
# Tiziano Lamperti  - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.

PRE: dos listas

POST: n° de elementos superpuestos
"""

def find_superposes(lista1,lista2):
    """
    Retorna el n° de elementos superpuestos entre 2 listas
    """
    menor = len(lista1) <= len(lista2)
    count = 0
    spositions = 0
    if menor:
        while count < len(lista1):
            if lista1[count] == lista2[count]:
                spositions = spositions + 1
                count = count + 1
            else:
                count = count + 1
    else:
        while count < len(lista2):
            if lista2[count] ==  lista1[count]:
                spositions = spositions + 1
                count = count + 1
            else:
                count = count + 1
    return spositions

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista1 = str(input("ingrese una oración: "))
    lista2 = str(input("ingrese otra oración: "))
    
    resultado = find_superposes(lista1,lista2)
    print(resultado)

if __name__ == "__main__":
    principal()
