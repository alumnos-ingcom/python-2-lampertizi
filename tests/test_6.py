################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio6 import codifica_cesar, decodifica_cesar

"""
se probará las funciones de de/codificacion en cifrado cesar
"""

def test_julio():


    """
    se probarán letrás mayus, minus, y números ; tmb desencriptacion
    como tmb llaves negativas
    """
    t1 = "hola mundo"
    t2 = "HOLA MUNDO"
    t3 = "wxyz"
    t4 = "VamOs dE pasEo"

    r1 = "gnkz ltmcn"
    r2 = "LSPE QYRHS"

    assert codifica_cesar(t1, -1) == "gnkz ltmcn", "no funca con llave negativa"
    assert codifica_cesar(t2, 4) == "LSPE QYRHS", "no funca con mayus"
    assert codifica_cesar(t3, 5) == "bcde", "no funca con valores limite"
    assert codifica_cesar(t4, 14) == "JoaCg rS dogSc", "no funca con mayus + valores limite"

    assert decodifica_cesar(r2, 4) == "HOLA MUNDO", "no funciona el decoder"
    assert decodifica_cesar(r1, -1) == "hola mundo", "no funciona el decoder"
