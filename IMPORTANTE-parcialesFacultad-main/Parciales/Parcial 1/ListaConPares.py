# Tema 2, ejercicio 2
# 2) Generar una lista con números enteros entre 1 y 100 obtenidos al azar. Luego se solicita leer un número N y buscar en la lista todos los pares de números cuya suma sea
# igual a N imprimiendo una sola vez cada par hallado.

import random

def buscarpares(lista, n):
    listapares = []
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):  # Empezamo desde i+1 para no repetir pares
            if lista[i]+lista[j]==n:
                par = [lista[i], lista[j]]
                if par not in listapares:
                    listapares.append(par)   # Creamos una lista de listas con los pares hallados
    return listapares

# Programa principal
n = int(input("Ingrese la cantidad de elementos de la lista: "))
while n<1:
    print("Tamaño inválido. Debe ser mayor que 0")
    n = int(input("Ingrese la cantidad de elementos de la lista: "))
print()
lista = [random.randint(1, 100) for i in range(n)]
print("Lista original:")
print(*lista)
n = int(input("\nIngrese la suma a buscar: "))
pares = buscarpares(lista, n)
print("\nPares hallados:")
print(*pares)