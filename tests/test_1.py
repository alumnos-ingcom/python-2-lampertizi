################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio1 import encontrar_par

"""
Se prueba la función encontrar_par del ejercicio1
"""

def test_encontrar_par():


    """
    Se evaluarán valores float,negativos,positivos y neutros
    """
    numero_xl = 89789456415641897421564541564789415648912310
    assert encontrar_par(5) is False, "no detecta naturales impares"
    assert encontrar_par(numero_xl) is True, "no calcula n° 'grandes'"
    assert encontrar_par(-8) is True, "no calcula n° negativos pares"
    assert encontrar_par(-11) is False, "no calcula n° negativos impares"
    assert encontrar_par(10.0) is True, "no calcula floats naturales pares"
    assert encontrar_par(11.5) is False, "no calcula n° con decimales"
