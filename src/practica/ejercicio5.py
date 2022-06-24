################
# Tiziano Lamperti  - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Corchetes balanceados
Implementar una función que determine si una cadena con corchetes
está balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra.
El resultado debe ser un valor lógico indicando si esta o no balanceado.

PRE: string con [({

POST: bool indicando si todos los corchetes tienen cierre
"""


def encuentra_pares(string):
    """
    retorna bool indicando si el string tiene cierre o no
    """
    abre = "{[("
    cierra = "}])"
    parentesis = 0
    corche = 0
    llave = 0
    cierra_p = 0
    cierra_c = 0
    cierra_l = 0
    for char in string:
        if char in abre:
            if char == "(":
                parentesis += 1
            elif char == "[":
                corche += 1
            else:
                llave += 1
        elif char in cierra:
            if char == ")":
                cierra_p += 1
            elif char == "]":
                cierra_c += 1
            else:
                cierra_l += 1
        else:
            pass
    resultado = False
    if parentesis == cierra_p:
        if corche == cierra_c:
            if llave == cierra_l:
                resultado = True
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    hilo = str(input("Ingrese cadena de brackets : "))
    resultado = encuentra_pares(hilo)
    print(resultado)


if __name__ == "__main__":
    principal()
