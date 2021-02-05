# 1.Desarrollar un programa que utilice una función para devolver un número entero obtenido al azar comprendido 
# entre A y B, asegurándose que no contenga dígitos repetidos. Los límites A y B se pasan como parámetro entero, 
# y deberán ser intercambiados si A fuera mayor que B. Imprimir por pantalla el número obtenido.
import random

#Funciones
def generarEntero(a,b):
    """ Genera numero entero al azar entre A y B recibidos por parámetro """
    lista = []
    cant = random.randint(5,50)
    for i in range(cant):
        lista.append(random.randint(a,b))
    return lista

def eliminarDuplicados(lista):
    """ Elimina los dígitos repetidos de una lista recibda por parámetro """
    listaNueva = []
    for item in lista:
        if item not in listaNueva:
            listaNueva.append(item)
    return listaNueva
    

#Programa principal
print()
print("Bienvenido al Programa")
print()
a = int(input("Introduzca un número: "))
b = int(input("Introduzca otro número: "))
while a<0 or b<0:
    print("Error. Tamaño incorrecto. El numero debe ser mayor que 0 y 'a' debe ser menor que 'b'")
    a = int(input("Introduzca un número: "))
    b = int(input("Introduzca otro número: "))
if a>b:
    aux = b
    b = a
    a = aux
lista = generarEntero(a,b)
print()
print("La lista generada es:")
print(*lista, sep="-")
print()
listaNueva = eliminarDuplicados(lista)
print("La nueva lista sin repetidos es:")
print(*listaNueva, sep="-")


