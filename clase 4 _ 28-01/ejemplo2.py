# Ejemplo de matrices sin caca

def rellenarmatriz(matriz):
    """ Rellena una matriz con numeros que fueron tomados por teclado """
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas): 
            n = int(input("Ingrese un número: ")) # 
            matriz[f][c] = n 

def imprimirmatriz(matriz):
    """ Realiza el patrón para imprimir correctamente una matriz """
    filas = len(matriz) 
    columnas = len(matriz[0])
    for f in range(filas): 
        for c in range(columnas): 
            print("%3d" %matriz[f][c], end="") 
        print() 

# Programa principal
filas = 3
columnas = 4
matrizDinamica = []
for f in range(filas): 
    matrizDinamica.append([0] * columnas) 

rellenarmatriz(matrizDinamica)
imprimirmatriz(matrizDinamica)