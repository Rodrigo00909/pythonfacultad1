# Numeros al azar: inventa la computadora. Es para factor de azar, criptografia, juegos, etc.
# Esto se hace con el modulo random
import random
# random.randint(<min>, <max>): Devuelve un numero entero al azar dentro del intervalo dado. El intervalo se considera cerrado. Es el unico momento donde el valor final ESTA incluido
# random.random(): devuelve un numero real al azar dentro del intervalo [0,1), es decir comprendido entre 0 y 1.
# Al tener un corchete detras del 0 y un parentesis delante del 1, siguiendo las leyes de matematica, quiere decir que el 0 esta incluido pero el 1 no. Por lo tanto los numeros
# Al azar generados por esta funcion van entre 0 y 0.99999 ... etc

# random.choice(<secuencia>): Devuelve un elemento elegido al azar dentro de una secuencia(lista, rangos, strings, tuplas, etc) pasada como parametro.
# Elige un elemento al azar de dicha secuencia y nos lo devuelve como valor de retorno

opciones = ["Piedra", "Papel", "Tijera"]
seleccion = random.choice(opciones)
print(seleccion)

# Funcion shuffle: random.shuffle(<lista>): Mezcla una lista in situ. Las mecla siguiendo un patron al azar. Puede servir para juegos de cartas

lista = [3,4,5,6]
random.shuffle(lista)
print(lista)