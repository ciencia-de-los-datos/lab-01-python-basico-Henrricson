"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

# try:
#     with open("./data.csv", "r") as archivo:
#         # Lee todas las líneas del archivo
#         datos = archivo.readlines()
# except FileNotFoundError:
#     print("Error: el archivo no existe")


##############


# if clave in diccionario:


############################################################
# Retorne la suma de la segunda columna.
def pregunta_01(datos):

    suma = 0
    for dato in datos:
        dato = dato.split()
        suma = suma + int(dato[1])
    return suma


##############################################################
# Retorne la cantidad de registros por cada letra de la primera columna como la lista
# de tuplas (letra, cantidad), ordendas alfabéticamente.


def pregunta_02(datos):
    conteoLetras = {}
    for dato in datos:
        dato = dato.split()
        letra = dato[0]
        if letra in conteoLetras:
            conteoLetras[letra] += 1
        else:
            conteoLetras[letra] = 1
    conteoOrdenado = sorted(conteoLetras.items(), key=lambda x: x[0])
    return conteoOrdenado
    """


    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """


#####################################################
# Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
# de tuplas (letra, suma) ordendas alfabeticamente.


def pregunta_03(datos):
    suma_por_letra = {}

    for dato in datos:
        letra = dato[0]
        if letra in suma_por_letra:
            suma_por_letra[letra] += int(dato[2])
        else:
            suma_por_letra[letra] = int(dato[2])

    resultado = sorted(suma_por_letra.items(), key=lambda x: x[0])
    return resultado

    """
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """


##############################################################
# La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
# registros por cada mes, tal como se muestra a continuación.
def pregunta_04(datos):
    registroPorMes = {}

    for dato in datos:
        campos = dato.split()
        fecha = campos[2]
        mes = fecha.split("-")[1]
        if mes in registroPorMes:
            registroPorMes[mes] += 1
        else:
            registroPorMes[mes] = 1
    registroPorMesOrdenados = sorted(registroPorMes.items(), key=lambda x: x[0])
    return registroPorMesOrdenados


"""

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
##############################################################
# Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
# letra de la columa 1.


def pregunta_05(datos):

    diccionario = {}

    for dato in datos:
        renglon = dato.split()
        letra = renglon[0]
        columna = int(renglon[1])
        if letra in diccionario:
            diccionario[letra] = (
                max(diccionario[letra][0], columna),  # Valor máximo
                min(diccionario[letra][1], columna),  # Valor mínimo
            )
        else:
            diccionario[letra] = (columna, columna)
    resultado = sorted(diccionario.items(), key=lambda x: x[0])
    resultado = [
        (letra, max_valor, min_valor) for letra, (max_valor, min_valor) in resultado
    ]
    return resultado


"""


    Rta/
    [("A", 9, 2), ("B", 9, 1), ("C", 9, 0), ("D", 8, 3), ("E", 9, 1),]

    """
##############################################################
#    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
#     una clave y el valor despues del caracter `:` corresponde al valor asociado a la
#     clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
#     grande computados sobre todo el archivo.


def pregunta_06(datos):

    min_max_valores = {}

    for line in datos:
        line = line.split()

        for clave_valor in line[4].split(","):
            clave, valor = clave_valor.split(":")
            valor = int(valor)

            if clave in min_max_valores:

                min_max_valores[clave] = (
                    min(min_max_valores[clave][0], valor),
                    max(min_max_valores[clave][1], valor),
                )

            else:

                min_max_valores[clave] = [valor, valor]

    resultado = sorted(min_max_valores.items(), key=lambda x: x[0])
    resultado = [
        (letra, max_valor, min_valor) for letra, (max_valor, min_valor) in resultado
    ]
    return resultado


"""
 

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """


##############################################################
# Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
# valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
# a dicho valor de la columna 2.


def pregunta_07(datos):
    valores_letras = {}

    for line in datos:
        line = line.split()
        clave = line[1]
        letra = line[0]
        if clave in valores_letras:
            valores_letras[clave].append(letra)
        else:
            valores_letras[clave] = [letra]
    resultado = sorted(valores_letras.items(), key=lambda x: x[0])
    return resultado


"""


    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
# Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
# de la segunda columna; la segunda parte de la tupla es una lista con las letras
# (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
# valor de la segunda columna.


def pregunta_08(datos):
    valores_letras = {}

    for line in datos:
        line = line.split()
        clave = line[1]
        letra = line[0]
        if clave in valores_letras:
            if letra not in valores_letras[clave]:
                valores_letras[clave].append(letra)
        else:
            valores_letras[clave] = [letra]

    resultado = sorted(valores_letras.items(), key=lambda x: x[0])
    resultado = [(valor, sorted(letras)) for valor, letras in resultado]
    return resultado


"""


    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """


def pregunta_09(datos):
    diccionario = {}
    for linea in datos:
        linea = linea.split()
        dato = linea[4].split(",")
        for clave_valor in dato:
            clave, valor = clave_valor.split(":")
            if clave in diccionario:
                diccionario[clave] += 1
            else:
                diccionario[clave] = 1
    resultado = sorted(diccionario.items(), key=lambda x: x[0])
    return resultado


"""
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
# Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
# cantidad de elementos de las columnas 4 y 5.


def pregunta_10(datos):
    contenido = []
    for dato in datos:
        dato = dato.split()
        culumna4 = dato[3].split(",")
        columna5 = dato[4].split(",")
        tupla = (dato[0], len(culumna4), len(columna5))
        contenido.append(tupla)
    return contenido


"""
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
# Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
# columna 4, ordenadas alfabeticamente.


def pregunta_11(datos):
    diccionario = {}
    for linea in datos:
        linea = linea.split()
        columna2 = int(linea[1])

        columna4 = linea[3].split(",")
        for letra in columna4:
            if letra in diccionario:
                diccionario[letra] += columna2
            else:
                diccionario[letra] = columna2

    resultado = {k: diccionario[k] for k in sorted(diccionario)}
    return resultado


"""


    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """


#  Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
#  los valores de la columna 5 sobre todo el archivo.


def pregunta_12(datos):
    diccionario = {}
    for linea in datos:
        linea = linea.split()
        dato = linea[4].split(",")
        letra = linea[0]
        suma = sum(int(valor.split(":")[1]) for valor in dato)
        if letra in diccionario:
            diccionario[letra] += suma
        else:
            diccionario[letra] = suma
    resultado = {k: diccionario[k] for k in sorted(diccionario)}
    return resultado


"""
   

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """


# if __name__ == "__main__":

try:

    with open("./data.csv", "r") as archivo:
        # Lee todas las líneas del archivo
        datos = archivo.readlines()
    # print("respuesta 1")
    print(pregunta_01(datos))
    # print("respuesta 2")
    print(pregunta_02(datos))
    # print("respuesta 3")
    print(pregunta_03(datos))
    # print("respuesta 4")
    print(pregunta_04(datos))
    # print("respuesta 5")
    print(pregunta_05(datos))
    # print("respuesta 6")
    print(pregunta_06(datos))
    # print("respuesta 7")
    print(pregunta_07(datos))
    # print("respuesta 8")
    print(pregunta_08(datos))
    # print("respuesta 9")
    print(pregunta_09(datos))
    # print("respuesta 10")
    print(pregunta_10(datos))
    # print("respuesta 11")
    print(pregunta_11(datos))
    # print("respuesta 12")
    print(pregunta_12(datos))
except (
    FileNotFoundError,
    ZeroDivisionError,
    ValueError,
    TypeError,
    IndexError,
) as error:
    print("se produjo un error", error)
