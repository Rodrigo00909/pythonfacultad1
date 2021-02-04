# Tema 1, ejercicio 1
# 1) Escribir un programa para generar e imprimir una matriz de N x N con números enteros al azar comprendidos entre 1 y 99. El programa debe funcionar para cualquier valor de N,
# el que se ingresa por teclado. Se valorará que el proceso se realice mediante una lista por comprensión anidadas. La matriz debe imprimir diagonal
import random

def generarmatriz(mat):
    n = len(mat)   # Igual cantidad de filas y columnas
    for i in range(n):
        mat[i][n-i-1] = random.randint(1, 99) # Esto hace q la matriz se genere en diagonal: Establece la cantidad de N entre (1,99) en una forma establecida de la matriz creada (en diagonal)

def imprimirmatriz(mat):
    for fila in mat:
        for col in fila:
            print(f"{col:3}", end="") ## Col:3 es el espacio q hay entre columnas, jugar con el numero
        print()

# Programa principal
n = int(input("Ingrese el tamaño de la matriz: "))
while n<1:
    print("Tamaño inválido. Debe ser mayor que 0")
    n = int(input("Ingrese el tamaño de la matriz: "))
print()
# Creamos la matriz directamente con los números al azar usando listas por comprensión anidadas
matriz = [[0]*n for fila in range(n)] # Construye directamente la matriz por N filas y N columnas
generarmatriz(matriz)
imprimirmatriz(matriz)