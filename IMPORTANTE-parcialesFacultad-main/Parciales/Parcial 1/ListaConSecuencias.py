# Tema 1, ejercicio 2

import random

def separarsecuencias(lista):
    suma = 0
    i = 0
    while i<len(lista):
        if suma+lista[i]>20:
            lista.insert(i,0)
            suma = 0
        else:
            suma = suma + lista[i]
        i = i + 1
    lista.append(0)

# Programa principal
n = int(input("Ingrese la cantidad de elementos de la lista: "))
while n<1:
    print("Tamaño inválido. Debe ser mayor que 0")
    n = int(input("Ingrese la cantidad de elementos de la lista: "))
print()
lista = [random.randint(1, 20) for i in range(n)]
print("Lista original:")
print(*lista)
separarsecuencias(lista)
print("\nLista modificada:")
print(*lista)