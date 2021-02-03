# Una matriz es una estructura de datos formada por filas y columnas.

#        |Columna 0   |Columna 1  |Columna 2  |Columna 3
# Fila 0 |A[0][0]     |A[0][1]    |A[0][2]    |A[0][3]
# Fila 1 |A[1][0]     |A[1][1]    |A[1][2]    |A[1][3]
# Fila 2 |A[2][0]     |A[2][1]    |A[2][2]    |A[2][3]

# A[2][0]
# A = Nombre de la matriz
# [2] = Subindice de la fila
# [0] = Subindice de la columna

# Necesitamos dos subindices, uno para el numero de fila y el otro para el numero de columnas. Si yo digo que esta es una matris de 3x4 o [3][4] me refiero que es una 
# matriz ubicada en la fila 3 y columna 4

# Como python no tiene un soporte para la construccion de matrices las vamos a simular. Las simularemos construyendo una LISTA DE LISTAS
# Esto es una lista que no contiene numeros, tampoco palabras. Es una lista que contiene en su interior otras listas. Cada una de estas OTRAS LISTAS se comporta como una fila de nuestra matriz.
# los elementos dentro de estas listas son a su vez listas.
# Ambos subindices (flas y columnas)comienzan desde 0

# Vamos a trabajar con matrices regulares (cuadradas o rectangulares)
# La creacion de la misma se puede hacer en forma estatica o dinamica. 
# Todas las filas tendran la misma cantidad de columnas, y todas las columnas la misma cantidad de filas.

# Primero vamos a crear la matiz con los numeros que se nos ocurra. Una vez que hemos creada la matriz reemplazaremos esos 0 o 1 por los valores que realmente necesitemos.
# De este modo podrmeos trabajar tranquilamente con la matriz

# Hay dos maneras de crearlas (estatica o dinamica)
# Estatica: Es dibujar la matriz dentro de nuestro programa:
matrizEstatica = [ [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0] ]
print(matrizEstatica)
# Hemos creado una matriz de 3x4 (3 filas, 4 columnas)
# Yo tengo que conocer el tamaño de la matriz en el momento que escribo el programa. No lo puedo pedir por escrito. Por eso las dinamicas son mejores, en este caso si se puede preguntar.
print()
# Dinamicas: 
filas = 3
columnas = 4
matrizDinamica = []
for f in range(filas): # Realiza tantas iteraciones como filas necesite
    matrizDinamica.append([0] * columnas) # En cada iteracion agrego una fila ya armada, es decir tomo una lista de un solo 0 [0] y la multiplico x la cantidad de columans. De esta manera
    # repito una lista para hacerla mas grande
print(matrizDinamica)
print()
# Otra alternativa para crear matrices: Usar listas por comprension
filas2 = 3
columnas2 = 4
matrizNueva = [ [0] * columnas2 for i in range(filas2)] 
print(matrizNueva)

# Una vez creada la matriz, la rellenaremos con numeros ingresados a traves del teclado. Luego la imprimiremos por pantalla.
# ambas tareas son realizadas a traves de funciones.
def rellenarmatriz(matriz):
    #Autodetectamos el tamaño de la matriz
    # En otros lenguajes nos tienen que pasar el tamaño de la amtriz xq no sabemos, pero aca si:
    # una matriz es una lista q contiene filas, entonces el len() de la matriz me indica la cantida de filas que contiene
    filas = len(matriz)
    # Para la cantidad de columnas debo agarrar cualquiera de las filas y averiguar su longitud, nuestras matrices sno cuadradas o rectangulares x tanto la longitud de una nos sirve para todas
    # No se cuantas filas tiene mi matriz pero supongo q por lo menos tiene 1. la primera es con el subindice 0: [0] entonces x eso lo ponemos asi:
    columnas = len(matriz[0])
    # Por cada iteracion del for de la F se van a relizar todas las iteraciones del for de la c:
    for f in range(filas): # recorre filas
        for c in range(columnas): # recorre columnas
            # Y en cada iteracion del for de la c le vamos a solicitar al usuario q ingrese un numero guardandolo en la variable n
            n = int(input("Ingrese un número: ")) # 
            matriz[f][c] = n # Esta variable n la guardamos dentro de la matriz, en los lugares de la F(fila) y de la C(columna)
            # Vamos a empezar con fila 0 columna 0, luego fila 0 columuna 1, fila 0 columna 2, fila 0 columna 3
            # Luego viene fila 1 columna 0, fila 1 columna 1 .... y etc etc etc hasta llegar a completar la matriz 3x4. En total el usuario tendra que ingresar 12 numeros
            # Recorda que f y c en su for iteraran en total 12 veces xq 3x4=12 y cada resultado se ira asignando a N y luego pasados a matriz[f][c]
            # De esta manera reemplazamos los 0 de la matriz con los valores que desea el usuario
           
# A veces los datos provienen de otro lado, no es necesario usar los del teclado. Podemos usar matrices con 1 en las diagonales y 0 en otros lugares y asi.
# Algo complejo es cuando se pide rellenar la matriz con un aspecto de espiral (numeros q crecen y se enroscan en la matriz hasta llegar al centro). 

# hay que imprimir una matriz con el aspecto que ella tiene no una larga fila o columna de numeros como esta predeterminada. Queremos una fila debajo de la anterior.
# para eso usamos estos trucos de programacion:
def imprimirmatriz(matriz):
    filas = len(matriz) # Obtenemos cantidad de filas
    columnas = len(matriz[0]) # Obtenemos cantidad de columnas
    for f in range(filas): # Ciclo para filas
        for c in range(columnas): # Ciclo para columnas
            print("%3d" %matriz[f][c], end="") # Tecnica de especificadores de conversion, para q los numeros aparezcan en columna. El end="" es para q los numeros aparezcan uno alado del otro
            # Con esto imprimimos solamente la primera fila xq suponemos que la f todavia vale 0. Al primir toda la columna de la fila 0 salimos del for de la C y nos encontramos con un print
            # que no imprime nada, pero en realidad este print lo que hace es avanzar a la siguiente linea de pantalla ya que no esta dentro del for de la c si no dentro del for de la f
            # Es decir, este print vacio nos permite ir cambiando de renglon de pantalla
        print() 

# Este codigo va dentro del programa principal, despues de haber creado la matriz con cualquiera de las tres alternativas
rellenarmatriz(matrizDinamica) # Le paso como parametro la matriz dinamica que cree antes, pueden ser cualquiera de las 3
imprimirmatriz(matrizDinamica)