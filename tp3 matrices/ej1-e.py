def trasponer(matriz):
    largo=4
    cont=0
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(cont,largo):
            aux=matriz[f][c]
            matriz[f][c]=matriz[c][f]
            matriz[c][f]=aux
        cont+=1
    return matriz

def imprimirmatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

#Programa Principal

matriz = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
resultado = trasponer(matriz)
imprimirmatriz(resultado)