# 1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
# a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
# teclado.
# b. Ordenar en forma ascendente cada una de las filas de la matriz.
# c. Intercambiar dos filas, cuyos números se reciben como parámetro.
# d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
# e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
# f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
# parámetro.
# g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
# h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
# i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
# j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
# una lista con los números de las mismas.
# NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
# sea el valor ingresado.

#        |Columna 0   |Columna 1  |Columna 2  |Columna 3
# Fila 0 |A[0][0]     |A[0][1]    |A[0][2]    |A[0][3] PARA RELLENAR SE RELLENA TB EN ESTE ORDEN PRIMERO TODA LA FILA 0, LUEGO LA 1 Y ASI CON SUS RESPECTIVAS COLUMNAS
# Fila 1 |A[1][0]     |A[1][1]    |A[1][2]    |A[1][3]
# Fila 2 |A[2][0]     |A[2][1]    |A[2][2]    |A[2][3]

def construirMatriz(filas,columnas):
    """ Construye la matriz desde 0 y la devuelve """
    matriz = []
    for f in range(filas):
        matriz.append([0] * columnas)
    return matriz

def rellenarMatriz(matriz):
    """ Recibe una matriz y la rellena con números introducidos por teclado """
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            n = int(input("Introduzca un número para rellenar: "))
            matriz[f][c] = n

def imprimirMatriz(matriz):
    """ Le da forma de matriz a la matriz recibida """
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

def cambiarColumnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    n1 = int(input("Cúal matriz quiere cambiar?: "))
    n2 = int(input("Por cúal?: "))
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = matriz[f][c][::-1]

# Programa Principal
n = int(input("Ingrese el tamaño de las filas: "))
n2 = int(input("Ingrese el tamaño de las columnas: "))
matriz = construirMatriz(n,n2)
rellenarMatriz(matriz)
imprimirMatriz(matriz)







