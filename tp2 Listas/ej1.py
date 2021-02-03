# 1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
# a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
# b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
# c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro.
# d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
# auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].

import random

def cargarLista():
    """ Rellena una lista entre los numeros 00 y 99 con 4 digitos. """
    numerosAzar = []
    cantNum = random.randint(00,99) # 1,9
    for i in range(cantNum):
        numerosAzar.append(random.randint(0000,9999)) 
    return numerosAzar

def sumarElem(lista):
    """ Suma el total de una lista """
    lista = sum(lista)
    return lista

def eliminarElem(elemento, lista):
    """ Elemina un elemento ingresado por teclado de la lista. """
    while elemento in lista:
        lista.remove(elemento)
    return lista

def verificacapicua(contenidoLista):
    """ Verifica si una lista es capicua o no. """
    capicua = True
    for i in range(len(contenidoLista)//2):
        if contenidoLista[i] != contenidoLista[(i*-1)-1]:
            capicua = False
            break
    return capicua

#Programa Principal
print("Lista Generada:")
lista = cargarLista()
print(lista)
print("Lista Sumada:")
print(sumarElem(lista))
elem = int(input("Para eliminar un elemento escriba su numero, para salir -1: "))
while elem != -1:
    elemEliminado = eliminarElem(elem, lista)
    if elemEliminado != 0:
        print(f"El elemento {elem} fue eliminado correctamente.")
        print("La nueva lista seria:",lista)
    else:
        print("No fue posible borrar el elemento.")
    elem = int(input("Para eliminar un elemento escriba su numero, para salir -1: "))
escapi = verificacapicua(lista)
if escapi:
    print("La lista es capicúa.")
else:
    print("La lista no es capicúa.")
print("La lista final será la siguiente: ")
print(*lista, sep=" - ")