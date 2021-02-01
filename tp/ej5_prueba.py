def imprimirAsteriscosMatriz(filas):
    for i in range(filas):
        for j in range(filas * 2):
            print("*", end="")
        print()


def imprimirAsteriscosEscalera(filas):
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
print("PATRÓN 1")
imprimirAsteriscosMatriz(cantFilas)
print()

# Imprimir patrón 2
print("PATRÓN 2")
imprimirAsteriscosEscalera(cantFilas)