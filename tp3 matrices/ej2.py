# 2. Para cada una de las siguientes matrices, desarrollar una función que la genere y
# escribir un programa que invoque a cada una de ellas y muestre por pantalla la
# matriz obtenida. El tamaño de las matrices debe establecerse como N x N, y las
# funciones deben servir aunque este valor se modifique.
# VER PATRON EN TP

def crearmatriz(tamaño):
    """ Crea la matriz G con el tamaño indicado """ 
    matriz = []
    for i in range(tamaño):
        pedacito = []
        for j in range(tamaño):
            pedacito.append(0)
        matriz.append(pedacito)

    return matriz

def espiralMatriz(matriz,tamaño):
    """ Llena la matriz con el método G """
    eskere = 0
    arriba = 0
    derecha = 0
    abajo = 0
    izquierda = 0
    relleno = 1
    paso = 0
    i = 0
    while eskere < (tamaño*2) - 1:
        if paso == 00:
            for j in range(izquierda, tamaño - derecha):
                matriz[i][j] = relleno
                relleno+=1
            paso = 1
            arriba +=1
            i = arriba
        elif paso == 1:
            for j in range(arriba,tamaño-abajo):
                matriz[j][tamaño-i] = relleno
                relleno +=1
            paso = 2
            derecha +=1
            i = derecha
        elif paso == 2:
            for j in range(tamaño-1-derecha,izquierda-1,-1):
                matriz[tamaño-1][j] = relleno
                relleno += 1
            paso = 3
            abajo += 1
            i = abajo
        elif paso == 3:
            for j in range(tamaño-abajo-1,arriba-1,-1):
                matriz[j][i-1] = relleno
                relleno += 1
            paso = 0
            izquierda += 1
            i = izquierda
        eskere += 1

def imprimirmatriz(matriz,size):
    for i in range(size):
        for j in range(size):
            print("|%4d" %matriz[i][j], end="")
        print("|\n")

n = 4
matrix = crearmatriz(n)
espiralMatriz(matrix,n)
print()
print(matrix)
print()
imprimirmatriz(matrix,n)

