#Trabajo Práctico 2: Listas
#EJERCICIO 2
#Alumno: Matías Santoro
#Grupo 1

#IMPORT
import random

# Funciones
def cargar_lista_al_azar(cant, min, max):
    """Recibe la cantidad de elementos, un mínimo
    y un máximo y devuelve una lista cargada con
    esa cantidad entre ese mínimo y ese máximo"""
    lista = []
    for i in range(cant):
        lista.append(random.randint(min, max))
    return lista

def hay_repetido(lista):
    """Recibe una lista y devuelve True si
    contiene algún elemento repetido"""
    repetido = False
    for i in range(len(lista)):
        if lista.count(lista[i]) > 1:
            repetido = True
            break
    return repetido

def lista_sin_repetidos(lista):
    """Recibe una lista y devuelve una nueva
    sin sus valores repetidos"""
    nueva_lista = []
    for i in range(len(lista)):
        if lista.count(lista[i]) == 1:
            nueva_lista.append(lista[i])
    return nueva_lista

# Programa principal

# Solicitar al usuario una cantidad, un mínimo y un máximo para cargar una lista al azar
cantidad = int(input("Ingrese una cantidad: "))
minimo= int(input("Ingrese un mínimo: "))
maximo = int(input("Ingrese un máximo: "))

# Carga una lista al azar y la imprime
listaAzar = cargar_lista_al_azar(cantidad, minimo, maximo)
print()
print("LISTA GENERADA CON", cantidad,"ELEMENTOS ENTRE", minimo, "Y", maximo)
print()
print(*listaAzar)
print()

# Determina si la lista posee algún valor repetido e imprime el resultado
repetido = hay_repetido(listaAzar)
if repetido:
    print("La lista posee uno o más elementos repetidos")
else:
    print("La lista no posee elementos repetidos")
print()

# Crea una lista con los elementos únicos de la anterior y e imprime el resultado
sin_repetidos = lista_sin_repetidos(listaAzar)

print("LISTA SIN ELEMENTOS REPETIDOS")
print()
print(*sin_repetidos)


## DEL EJ DE FRANCO # while para recorrer la lista para ver su largo. Variable repetida = false. EL while recorre la lista siempre que sea repetido verdadero. Lista i+1