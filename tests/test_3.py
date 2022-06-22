################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio3 import find_superposes

"""
Se probará la función find_superposes del ejercicio3
"""

def test_superposiciones():
    """
    Se probarán listas,strings, listas c/ints,strings,bools,floats
    """
    # listas de prueba
    lista1 = [1,9,3,2,5,0]
    lista2 = [1,9,5,2,3,0]
    lista9 = [-1,-9,-5,-2,-3,0]
    lista3 = "Hola, Mundo"
    lista4 = ["H","o","r","a",","," ","L","i","n","d","o"]
    lista5 = [True,False,False,True]
    lista6 = [False,False,True,True]
    lista7 = [7.45,7.08,98.223,12.552,5.21,6.2]
    lista8 = [1.0,7.08,98.21,13.07,5.12,0.0]
    # mensajes de error
    mensaje1 = "no calcula listas con n° naturales + el 0"
    mensaje2 = "no calcula entre una lista y un string"
    mensaje3 = "no calcula listas con bools"
    mensaje4 = "no calcula con listas de floats"
    mensaje5 = "no calcula mezclando entre string e int"
    mensaje6 = "no calcula entre ints y floats"
    mensaje7 = "no calcula entre n° positivos y negativos"
    # casos de prueba
    caso1 = find_superposes(lista1,lista2) 
    caso2 = find_superposes(lista3,lista4) 
    caso3 = find_superposes(lista5,lista6) 
    caso4 = find_superposes(lista7,lista8) 
    caso5 = find_superposes(lista2,lista4) 
    caso6 = find_superposes(lista1,lista8) 
    caso7 = find_superposes(lista2,lista9) 
    assert caso1 == (4,[0,1,3,5]),mensaje1
    assert caso2 == (8,[0, 1, 3, 4, 5, 8, 9, 10]),mensaje2
    assert caso3 == (2,[1, 3]),mensaje3
    assert caso4 == (1,[1]),mensaje4
    assert caso5 == (0,[]),mensaje5
    assert caso6 == (2,[0,5]),mensaje6
    assert caso7 == (1,[5]),mensaje7

