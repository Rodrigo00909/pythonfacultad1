""" Leer un conjunto de números enteros. Calcular su promedio e imprimir aquellos valores leídos que sean mayores que el promedio """
lista = []
n = int(input("Ingrese un numero entero o -1 para terminar: "))
while n != -1:
    lista.append(n)
    n = int(input("Ingrese un numero entero o -1 para terminar: "))
cant = len(lista)
if cant == 0:
    print("No se ingresaron valores")
else:
    prom = sum(lista)/cant
    print("Promedio:",prom)
    for i in range(cant):
        if lista[i] > prom:
            print(lista[i], end=" ")
    print()