################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from practica.ejercicio4 import encontrar_a_fibo
"""
se probará la función que retorna el valor de la suc. de fibonacci pedido
"""

def test_a_fibo():


    """
    se pondrán valores < 2 y muy grandes
    """
    assert encontrar_a_fibo(1) == ValueError, "acepta valores < 2"
    assert encontrar_a_fibo(5) == 3, "no hace bien los calculos"
    assert encontrar_a_fibo(45) == 70140873, "no opera con n° grandes"
