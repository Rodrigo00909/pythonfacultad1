""" Uso de numeros al azar: para un juego de generala se necesita desarrollar una funcion que simule el lanzamiento de los cinco dados de un cubilete
Escribir un programa para verificar su funcionamiento """
import random

def lanzar_dados(cuantos):
    dados = []
    for i in range(cuantos):
        dados.append(random.randint(1,6)) # Agregar 5 numeros a la lista enteros al azar, comprendidos entre 1 y 6 (solo pueden ser 1,2,3,4,5,6)
    return dados

#Programa Principal
jugada = lanzar_dados(5) # cinco dados
print(jugada)

# EL PROGRAMA PRINCIPAL ES LO QUE VERIFICA EL FUNCIONAMIENTO