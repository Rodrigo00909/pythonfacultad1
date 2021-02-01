# Un método es una función que pertence a un objeto 
# Los métodos permiten manipular datos almacenados en el objeto.
# Se escriben luego del nombre del objeto, separados por un punto

#El método append(<elem>) agrega un elemento al final de la lista.

lista = [3,4,5]
lista.append(6)
print(lista) # [3,4,5,6]

#Método insert: Es parecido al append pero con diferencia de que elejimos el lugar.
lista2 = [3,4,5]
lista2.insert(2,9) # El primer parametro => El sub indice / Segundo => El valor del elemento
print(lista2) # [3,4,9,5]

# El método pop(<pos>) elimina y devuelve un elemento de la lista, indentificado por su subindice. Si no le pasamos parametro borra el ultimo elemento de la lista.
# Guarda el elemento qe borramos en una variable, pero si no lo quiero usar entonces no hace falta poner la variable. (lista.pop)

lista3 = [3,4,5]
elemBorrado = lista3.pop(1)
print(elemBorrado) # 4
print(lista3) # [3,5]

# Recordar que -1 hace referencia al ultimo elm de la lista.

# El método remove(<elem>) elimina la primera aparicion de un elemento en la lista identificado por su valor.
# Si el elemento está mas de una vez solo borra la primera, si no hay nada da un error. Se le pone el elemento exacto a borrar.
# Para que no de un error esta bueno poner un IN antes del remove.

lista4 = [3,4,5,4]
lista4.remove(4) # queda [3,4,5]

# Si de casualidad tendria esto:
lista5 = [3,4,4,4,4,4,4,5,7]
print(lista5)
# Y quisiera eliminar todos los 4 deberia ahcer asi:
while 4 in lista5:
    lista5.remove(4)
print(lista5)

# Método index: busca un elemento y devuelve su posicion. Provoca un error si no encuentra
lista6 = [3,4,5]
print(lista6.index(5)) # 2

# Index solo devuelve la priemra posicion es decir que si hay un segundo elemento igual al seleccionado lo ignora, para eso existe esto:
# Tmabien permite elegir la región de búsqueda. Es con dos y con 3 parametros
lista7 = [3,4,5,7,9,11,13,15]
print(lista7.index(5,2)) #Inicio
print(lista7.index(5,2,4)) # Inicio y fin. LLegaria hasta el 3, el 4 queda fuera xq el valor final nunca esta incluido
# El de dos parametros: el primero es el numero o valor a buscar, el 2do parametro indica en que subindice empezamos a buscar.
# Con 3 parametros: El tercer parametro es el indice en el cual queremos terminar la busqueda. El valor final no está incluido
# Lo mas comun es usar index con 2 o 1 parametro.

# Metodo count(<elem>): permite contar cuantas veces se repite un valor dentro de una lista.

lista8 = [3,4,5,3]
print(lista.count(3)) # 2

#Count no da error, si no encuentra devuelve 0

# Método clear() elimina In situ* todos los elementos de la lista 
# Que es *in situ? Se refiere a metodos que modifican una lista SIN CREAR UNA LISTA NUEVA. El método append, pop, remove, etc, trabajan In situ xq modifican una lista sin crear una nueva.

lista9 = [3,4,5]
lista9.clear()
print(lista9)

# Método para dar vuelta una lista: reverse() invierte in situ el orden los elementos de la lista.

lista0 = [3,4,5]
lista0.reverse()
print(lista0) # [5,4,3]

# Método sort() Evita el asqueroso método de ordenamiento. Ordena in situ a una lista.
lista02 = [5,1,7]
lista02.sort()
print(lista02) # [1,5,7]

# Método sort al reves: reverse=True es un parametro que hace que los elementos se ordenen de mayor a menor.
lista03 = [5,1,7]
lista03.sort(reverse=True)
print(lista03) # [7,5,1]

# Parametro key=<clave> permite establecer el criterio de ordenamiento cuando éste no sea el valor del ítem. Es decir: Nos permite crear un criterio de ordenamiento 
# que sea distinto al criterio básico que utiliza python. El valor de los elementos es el criterio de comparacion que utiliza python a la hora de ordenar una lista.
# A veces hay que ordenar una lista segun un atributo que no sea el valor de los elementos.

lista04 = [1,2,3,4,5,6]
lista04.sort(key=lambda x: x%2) # Quiero ordenar primero los numeros pares (2,4,6) y luego los impares. Entonces necesito que si el resto de x y 2 da 0 esten los pares primero
# Si es par devuelve 0, si es impar devuelve 1. Entonces como 0 es mayor que 1 priemro quedarán ordenados los numeros 0 y dp los 1
print("Lista 04",lista04) # [2,4,6,1,3,5]

# Ahora si quisiera hacerlo al reves, la funcion lambda en vez de devolver x%2 devuelva 1-x%2. Entonces si es impar: 1-1=0, si es par 1-0 = 1
lista004 = [1,2,3,4,5,6]
lista004.sort(key=lambda x: 1-x%2)
print("Lista 004", lista004)
# O si no con el reverse true
lista05 = [1,2,3,4,5,6]
lista05.sort(key=lambda x: x%2, reverse=True) 
print("Lista 05",lista05) # [1,3,5,2,4,6]
# El 1- o en otros casos -1 sirve mucho para estos casos. Siempre hay alguna manera matematica para resolver.
# Con un not tampoco se pdoria hacer xq el not cambia el valor de verdad de una condicion o epxresion boleana, y aca no hay eso. Pero ojo puede funcionar.

# Si a len lo aplicamos a un string nos dira cuantas letras tiene xq len siempre es la longitud
# En el metodo sort, si se utilizan funciones incorporadas no es necesario crear funcion lambda

nombres = ['Andres', 'Ariel', 'Juan']
nombres.sort(key=len) #Ordenar lista nombres: Si no le pondriamos el key lo ordenaria de forma alfabetica (primero andres, ariel juan) pero con el key=len le decimos q ordene la lista segun la
#longitud de cada nombre, del menor a mayor
print(nombres) # ['Juan', 'Ariel', 'Andres']
numeros = [3,-2,4,1] # Lista con numeros enteros positivos y negativos
numeros.sort(key=abs) # Si hago un sort sin parametro key me queda primero el -2 que es el mas pequeño, leugo -1, 3, 4. Pero con key=abs (abs = valor absoluto q devuelve el valor positivo
# de un numero, queda -1 -2 3 4 xq los signos no son tenidos en cuenta, solo los valores absolutos de cada numero.)
print(numeros) # [-1,-2,3,4]

