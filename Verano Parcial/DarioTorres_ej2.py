# 2.Cargar una matriz de N x N elementos con números enteros, ingresados por teclado o generados al azar 
# (desarrollar una sola de estas opciones). El valor de N se ingresa por teclado. Mostrar por pantalla la matriz obtenida. 
# Luego se solicita informar:

# -Valor y ubicación de los elementos mayor y menor de cada fila y columna
# -Valor del menor elemento de la diagonal principal
import random

#Funciones
def imprimirMatriz(matriz):
    """ Imprime la matriz reciba por parámetro """
    for fila in matriz:
        for columna in fila:
            print(f"{columna:3}", end="")
        print()

def mayorElem(matriz):
    """ Devuelve el mayor elemento de una matriz """
    print("Los mayores elementos de cada fila y columna son:")
    for i in range(len(matriz)):
        print(max(elem[i] for elem in matriz))

def menorElem(matriz):
    """ Devuelve el menor elemento de una matriz """
    print("Los menores elementos de cada fila y columna son:")
    for i in range(len(matriz)):
        print(min(elem[i] for elem in matriz))

def diagonalPrincipal(matriz):
    """ Devuelve el menor elemento de la diagonal principal de una matriz """
    diagonalPrin=[]
    for f in range(len(matrizAlAzar)):
        for c in range(len(matrizAlAzar)):
            numero=matrizAlAzar[f][c]
            if [f]==[c]:
                diagonalPrin.append(numero)
    print("El elemento de menor valor de la diagonal principal es:")
    print(min(diagonalPrin))

# Programa Principal
print()
print("Bienvenido al Programa")
print()
n = int(input("Ingrese el tamaño de la matriz. Debe ser mayor que 0: "))
while n<1:
    print("Error. Tamaño incorrecto.")
    n = int(input("Ingrese el tamaño de la matriz. Debe ser mayor que 0: "))
print()

matrizAlAzar = [[random.randint(0,99) for columna in range(n)] for fila in range(n)]
print("Matriz Constuida:")
imprimirMatriz(matrizAlAzar)
print()
mayorElem(matrizAlAzar)
print()
menorElem(matrizAlAzar)
print()
diagonalPrincipal(matrizAlAzar)

    