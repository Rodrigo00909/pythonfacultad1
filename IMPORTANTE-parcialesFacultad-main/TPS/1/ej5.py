"""
5. Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones
de asteriscos, donde la cantidad de filas se recibe como parámetro:
**********              **
**********              ****
**********              ******
**********              ********
**********              **********

"""

def imprimirMatriz(filas):
    """Recibe la cantidad de filas e imprime
    un patrón de asteriscos en forma de matriz"""
    for i in range(filas):
        for j in range(filas * 2):
            print("*", end="")
        print() # Este print reinicia el ciclo, si no seguira todo de corrido


def imprimirEscalera(filas):
    """Recibe la cantidad de filas e imprime
    un patrón de asteriscos en forma de escalera"""
    asteriscos = 2
    for i in range(filas):
        for j in range(asteriscos):
            print("*", end="")
        print()
        asteriscos += 2


# Programa Principal
# Solicitar 1 número entero positivo
cantFilas = int(input("Cantidad de Filas: "))
print()

# Imprimir patrón 1
print("PATRON 1: Matriz")
imprimirMatriz(cantFilas)
print()

# Imprimir patrón 2
print("PATRON 2: Escalera")
imprimirEscalera(cantFilas)