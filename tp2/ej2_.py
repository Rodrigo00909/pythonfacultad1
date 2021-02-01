# 2. Escribir funciones para:
# a. Generar una lista de 50 números aleatorios del 1 al 100.
# b. Recibir una lista como parámetro y devolver True si la misma contiene algún
# elemento repetido. La función no debe modificar la lista. # recorrer todo el array
# c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
# únicos de la lista original, sin importar el orden.
# Combinar estas tres funciones en un mismo programa.

import random

def generarlistarandom(cant, min, max):
    """Recibe la cantidad de elementos, un mínimo
    y un máximo y devuelve una lista cargada con
    esa cantidad entre ese mínimo y ese máximo"""
    lista = []
    for i in range(cant):
        lista.append(random.randint(min, max))
    return lista

def repetidoTrue(lista):
    """Recibe una lista y devuelve True si
    contiene algún elemento repetido"""
    repetido = False
    for i in range(len(lista)):
        if lista.count(lista[i]) > 1:
            repetido = True
            break
    return repetido

def generarListaSinRepe(lista):
    """Recibe una lista y devuelve una nueva
    sin sus valores repetidos"""
    nuevaLista = []
    for i in range(len(lista)):
        if lista.count(lista[i]) == 1:
            nuevaLista.append(lista[i])
    return nuevaLista

# Programa principal
cantidad = int(input("Ingrese una cantidad: "))
minimo= int(input("Ingrese un mínimo: "))
maximo = int(input("Ingrese un máximo: "))

listaAzar = generarlistarandom(cantidad, minimo, maximo)
print()
print("LISTA GENERADA CON {cantidad} ELEMENTOS ENTRE {minimo} Y {maximo}")
print()
print(*listaAzar)
print()

repetido = repetidoTrue(listaAzar)
if repetido:
    print("La lista posee uno o más elementos repetidos")
else:
    print("La lista no posee elementos repetidos")
print()

sinRepetidos = generarListaSinRepe(listaAzar)

print("LISTA SIN ELEMENTOS REPETIDOS")
print()
print(*sinRepetidos)
