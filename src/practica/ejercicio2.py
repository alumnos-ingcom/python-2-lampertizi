################
# Tiziano Lamperti  - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
2. Estadísticas
Implementar una función que obtenga los máximos, mínimos y promedio de 
una secuencia con números, retornando los valores como una tuple.
Sin utilizar lazos for o las funciones integradas del lenguaje 
que procesan secuencias.
"""

def sacar_stats(tope_de_num):


    """
    Retorna una tupla con la siguiente forma (min,max,promedio)
    """
    assert tope_de_num > 1, "se deben ingresar por lo menos 2 números"
    numeros = []
    para_promedio = 0
    count = 0
    while count < tope_de_num: #se crea lista de  n° + suma para promedio
        numero = int(input("n° a ingresar: "))
        numeros.append(numero)
        para_promedio = para_promedio + numero
        count = count + 1

    count = 0
    cuenta = para_promedio/len(numeros)

    while count < (len(numeros) - 1):
        minimo = numeros[count]
        maximo = numeros[count + 1]

        if maximo < minimo:
            temp = 0
            maximo = temp
            real_maximo = minimo
            real_minimo = temp
            count = count + 1
        elif minimo < maximo:
            real_maximo = maximo
            real_miniom = minimo
            count = count + 1
            continue
    return (real_maximo,real_minimo,cuenta)

def principal():


    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numeros_a_meter = int(input("cuántos n° se ingresarán?: "))
    resultado = sacar_stats(numeros_a_meter)
    print(resultado)

if __name__ == "__main__":
    principal()

