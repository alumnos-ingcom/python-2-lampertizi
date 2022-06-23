################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from practica.ejercicio5 import encuentra_pares

"""
se probará la función que encuentra pares de {}()[]
"""

def test_encuentrapares():
    """
    se probarán strings con letras,simbolos, y combos irregulares de {[()]}
    """
    oracion1 = "(hola)"
    oracion2 = "{{}}}"
    oracion3 = "[{!!!}]"
    assert encuentra_pares("{}") == True, "no calcula bien un solo par"
    assert encuentra_pares(oracion1) == True, "no calcula cuando hay letras"
    assert encuentra_pares(oracion2) == False, "no calcula el cierre"
    assert encuentra_pares(")]{[{") == False, "no calcula cuando hay desorden"
    assert encuentra_pares("[}") == False, "no detecta pares"
    assert encuentra_pares(oracion3) == True, "no detecta cuando hay simbolos"

