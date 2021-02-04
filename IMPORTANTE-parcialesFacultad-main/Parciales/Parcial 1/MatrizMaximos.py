# Tema 2, ejercicio 1
# 1) Escribir un programa para generar e imprimir una matriz de N x N con números enteros al azar comprendidos entre 0 y 99. El programa debe funcionar para cualquier valor de N,
# el que se ingresa por teclado. Se valorará que el proceso se realice mediante una lista por comprensión. Luego se solicita imprimir la fila y columna del mayor elemento almacenado en 
# la matriz. Mostar todas las coordenadas que correspondan en caso de estar repetido.

import random

def buscarmaximos(mat):
    n = len(mat)  # Misma cantidad de filas que de columnas
    listamax = []
    mayor = -1
    for f in range(n):
        for c in range(n):
            if mat[f][c]>mayor:
                mayor = mat[f][c]
                listamax.clear()        # Borramos las coordenadas del máximo anterior
                listamax.append([f,c])  # Creamos una lista de listas con las coordenadas del maximo
            elif mat[f][c]==mayor:
                listamax.append([f,c])  # Agregamos otra coordenada porque el máximo está repetido
    return mayor, listamax

def imprimirmatriz(mat):
    for fila in mat:
        for col in fila:
            print(f"{col:3}", end="")
        print()

# Programa principal
n = int(input("Ingrese el tamaño de la matriz: "))
while n<1:
    print("Tamaño inválido. Debe ser mayor que 0")
    n = int(input("Ingrese el tamaño de la matriz: "))
print()
# Creamos la matriz directamente con los números al azar usando listas por comprensión anidadas
matriz = [[random.randint(0,99) for columna in range(n)] for fila in range(n)] # Construye la matriz de N filas por N columnas, con los valores entre 0 y 99
imprimirmatriz(matriz)
maximo, maximos = buscarmaximos(matriz)
print(f"\nEl máximo es {maximo} y se encontró en las coordenadas", end=" ")
print(*maximos, sep=", ")