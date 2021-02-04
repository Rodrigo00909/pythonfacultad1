# Realizar un cuadrado magico. Escribir un programa para cargar valores en una matriz de N x N, con N ingresado x el usuario o generado al azar, e imprimir un mensaje indicando si se trata
# de un cuadrado magico o no. Si lo es mostrar su suma magica. Imprimir tambien la matriz utilizada.

import random

def imprimirmatriz(mat):
    for f in mat:
        for c in f:
            print("%3d" %c, end="")
        print()
    print()

def determinarcuadradomagico(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    esmagico = True
    # Control de filas
    sumafilas = []
    for fila in matriz:
        sumafilas.append(sum(fila))
    if min(sumafilas)!=max(sumafilas):
        esmagico = False
    # Control de columnas
    sumacolumnas = []
    for c in range(columnas):
        suma = 0
        for f in range(filas):
            suma = suma + matriz[f][c]
        sumacolumnas.append(suma)
    if min(sumacolumnas)!=max(sumacolumnas):
        esmagico = False
    # Diagonales
    principal = 0
    secundaria = 0
    for f in range(filas):
        principal += matriz[f][f]
        secundaria += matriz[f][filas-c+1]
    if principal!=secundaria:
        esmagico = False
    return esmagico

# Programa principal
n = int(input("Ingrese el tamaño de la matriz: "))
print()
# Creamos la matriz ya terminada usando listas por comprensión anidadas
mat = [[random.randint(0,9) for c in range(n)] for f in range(n)]
"""
mat = [ [4,3,8],
        [9,5,1],
        [2,7,6] ]
"""
imprimirmatriz(mat)
if determinarcuadradomagico(mat):
    print("Es un cuadrado mágico")
else:
    print("No es un cuadrado mágico")
