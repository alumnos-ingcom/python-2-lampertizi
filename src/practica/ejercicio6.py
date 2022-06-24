################
# Tiziano Lamperti  - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
6. El Cifrado del Cesar
Implementar una funcion que codifique un texto rotandolo
una cantidad de posiciones ajustable.

Implementar la funcion que decodifique el texto rotado una
cantidad de posiciones ajustable.

PRE: n° de rotaciones + texto

POST: texto rotado
"""


def codifica_cesar(cadena, posiciones):
    """
    retorna el string codificado
    """
    # 48 - 57 = 0 al 9
    # 97 - 122 = a - z
    # 65 - 90 = A - Z
    cadena_final = ""
    count = 0
    while count < len(cadena):
        letra = cadena[count]
        if letra.isdigit():
            valor_letra = ord(letra) - ord("0")
            valor_cambiado = chr((valor_letra + posiciones) % 10 + ord("0"))
            cadena_final = cadena_final + valor_cambiado
            count = count + 1
        elif letra.islower():
            valor_letra = ord(letra) - ord("a")
            valor_cambiado = chr((valor_letra + posiciones) % 26 + ord("a"))
            cadena_final = cadena_final + valor_cambiado
            count = count + 1
        elif letra.isupper():
            valor_letra = ord(letra) - ord("A")
            valor_cambiado = chr((valor_letra + posiciones) % 26 + ord("A"))
            cadena_final = cadena_final + valor_cambiado
            count = count + 1
        else:
            if letra == " ":
                cadena_final = cadena_final + letra
                count = count + 1
            else:
                valor_caracter = ord(letra)
                caracter_cambiado = chr(valor_caracter + posiciones)
                cadena_final = cadena_final + caracter_cambiado
                count = count + 1
    return cadena_final


def decodifica_cesar(texto, llave):
    """
    retorna texto codificado en cifrado cesar
    """
    llave = -llave
    resultado = codifica_cesar(texto,llave)
    return resultado

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("cadena a codificar: ")
    corrido = int(input("posiciones a correr: "))
    resultado = codifica_cesar(cadena, corrido)
    print(resultado)
    cadena = input("cadena a decodificar: ")
    corrido = int(input("llave: "))
    resultado = decodifica_cesar(cadena, corrido)
    print(resultado)


if __name__ == "__main__":
    principal()
