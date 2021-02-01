# 1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
# a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
# b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
# c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro.
# d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
# auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].

import random

def generarlistarandom():
    listarandom = []
    cant = random.randint(10,99)
    for i in range(cant):
        listarandom.append(random.randint(1000,9999))
    return listarandom ## cambiar de 1 al 100 en ej2

def borrarlista (b,c):
    cantborrar = b.count(c)
    for j in range(cantborrar):
        b.remove(c)
    return cantborrar

def verificacapicua (d):
    capicua = True
    for k in range(len(d)//2):
        if d[k] != d[(k*-1)-1]:
            capicua = False
            break
    return capicua

#Programa Principal
lista = generarlistarandom()
print("La lista generada es la siguiente: ")
print(lista)
sumatorialista = lambda x: sum(x)
print("Al sumar todos los elementos de la lista, se obtiene como resultado: ",sumatorialista(lista))
borrarElem = int(input("Ingrese un valor a eliminar o -1 para terminar: "))
while borrarElem != -1:
    numborrado = borrarlista(lista,borrarElem)
    if numborrado != 0:
        print(f"Se eliminó el elemento {borrarElem} la lista actualizada es así:: ")
        print(lista)
    else:
        print("El numero ingresado {borrarElem} no se encontro en la lista")
    borrarElem = int(input("Ingrese otro valor a eliminar o -1 para terminar: "))
capi = verificacapicua(lista)
if capi:
    print("La lista es capicúa.")
else:
    print("La lista no es capicúa.")
print("La lista final será la siguiente: ")
print(lista)
