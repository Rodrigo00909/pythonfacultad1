# 1) Escribir un programa para generar e imprimir una matriz de N x N con números enteros al azar comprendidos entre 1 y 99. El programa debe funcionar para cualquier valor de N,
# el que se ingresa por teclado. Se valorará que el proceso se realice mediante una lista por comprensión anidadas. La matriz debe imprimir diagonal
import random

# Funciones

def generarMatriz(matriz):
    fc = len(matriz)
    for i in range(fc):
        matriz[i][fc-i-1] = random.randint(1,99)

def imprimirMatriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(f"{columna:3}", end="")
        print()

# Programa Principal
n = int(input("Ingrese el tamaño de la matriz, debe ser un número mayor a 0: "))
while n<1:
    print("ERROR: Introduciste un tamaño no válido")
    n = int(input("Ingrese el tamaño de la matriz, debe ser un número mayor a 0: "))
print()
matriz = [[0]*n for fila in range(n)]
#matriz2 = [[random.randint(1,99) for columna in range(n)] for fila in range(n)]
print("Matriz Generada:")
print(matriz)
print("Matriz Ordenada:")
generarMatriz(matriz)
imprimirMatriz(matriz)

