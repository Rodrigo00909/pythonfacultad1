## Lista: Conjunto de elementos agrupados en una sola estructura

# Pueden imprimirse a traves de ciclos while o for.
# Tambien pueden imprimirse asi:

numeros = [1,2,3,4]
print(numeros) # [1,2,3,4]
print(*numeros) # 1 2 3 4 => de esta manera imprimimos sin los corchetes


## Operaciones con lista
# Concatenacion

lista1 = [1,2,3,4]
lista2 = [4,6,7]
lista3 = lista1 + lista2
print(lista3)

# Pueden ser repetidas

listaa1 = [3,4,5]
listaa1 = lista1 * 3
print(listaa1)
listaa2 = [0] * 5
print(listaa2)

# Para agregar elementos a la lista se utiliza append
lista4 = [3,4,5]
lista4.append(6)
print(lista4) #[3,4,5,6]


## Al ser mutables, y ser modificadas podemos alterar su contenido fuera de una funcion a traves del sub indice:
lista = [3,4,5]
lista[1] = 7
print(lista)

## Funcion len()
# Devuelve un entero con la cantidad de elementos que la lista contiene
lista5 = [3,4,5,6]
print(len(lista)) # 4

## Funcion sum()
# Permite obtener la sumatoria de los valores q pertenecen a una lista. La lista solo debe tener numeros para eso, solo numeros.
lista3 = [3,4,5,6]
print(sum(lista3)) # 18

# Funcion max()
# Devuelve el MAYOR de los elementos almacenados en una lista. Para esto la lista tiene que tener elementos homogeneos (TODOS NUMEROS O TODAS CADENAS DE CARACTERES)
lista6 = [4,2,3,7,9]
print(max(lista6)) #9

# Funcion min()
# Devuelve el MENOR de los elementos almacenados en una lista. Para esto la lista tiene que tener elementos homogeneos (TODOS NUMEROS O TODAS CADENAS DE CARACTERES)
listaa6 = [4,2,3,7,9]
print(max(listaa6)) #2

# Funcion list()
# Obtiene una lista a partir de cualqueir otro iterable de python. Es decir, convierte cualquier iterable en una lista. Podemos convertir una tupla, conjunto, diccionario, strings, etc en
# Iterativo. Range devuelve un objeto rango, no una lista. List() devolverá una lista. Para usar a range como lista se utiliza el list para convertirlo a lista y luego usar el range

lista7 = list(range(5))
print(lista7) # [0,1,2,3,4]


# Operador in: 
# Permie verificar la presencia de un elemento. Devuelve True o False
# Tambien existe not in para verificar la ausencia de un elemento
lista8 = [3,4,5,6]
if 4 in lista8:
    print("Hay un 4 en la lista")

## Las listas tienen sub indice positivo y negativo. En esta lista: [1,2,3,4,5,6,7] hay 7 elementos. En positivo seria del 0 al 6. En negativo del -1 al -7, es decir:
## Si quisiera referirme al ultimo elemento de la lista basta con poner -1


## Que es DESEMPAQUETAR? Se refiere a asignar los elementos de una lista a un conjunto de variables
# fecha = [14,12,2019]
# dia, mes, año = fecha

## Las listas tambien se pueden replicar (repetir) mediante el asterisco:
lista010 = [3,4,5]
lista010 = lista1*3
print(lista010) # [3,4,5,3,4,5,3,4,5]
lista020 = [0]*5
print(lista020) # [0,0,0,0,0]


