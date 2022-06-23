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
    assert encuentra_pares("{}") is True, "no calcula bien un solo par"
    assert encuentra_pares(oracion1) is True, "no calcula cuando hay letras"
    assert encuentra_pares(oracion2) is False, "no calcula el cierre"
    assert encuentra_pares(")]{[{") is False, "no calcula cuando hay desorden"
    assert encuentra_pares("[}") is False, "no detecta pares"
    assert encuentra_pares(oracion3) is True, "no detecta cuando hay simbolos"
