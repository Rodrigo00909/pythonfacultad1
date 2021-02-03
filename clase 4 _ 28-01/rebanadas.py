# Una rebanada (Slice) es una manera de referirse a un grupo de elementos pertenecientes a una lista. Elementos contiguos (elementos q esten uno alado del otro)
# En lugar de usar un solo subindice se utilizan dos o tres, separados por "dos puntos"
# Nos podias referir a la totalidad de la lista o bien a un solo elemento utilizando un subindice. Pero si queremos extraer 2 o 3 o 4 elementos de la lista en especifico?
# La unica manera de hacerlo era utilizar un ciclo y copiemos los elementos que queriamos en una lista nueva. Pero con la tecnica rebanada vamos a poder
# Para rebanadas hacen falta por lo menos 2 sub indices, y se aceptan hasta 3. Para separar a los subindices se utiliza el signo de los 2 puntos :

lista = [7,8,9,10,11,12]
sublista = lista[2:5] # [9,10,11]
print(sublista)
# Nos referimos a una porcion de la lista inicial que empieza en el sub indice 2(9) y sub indice 5 (12) pero no se mostrara este ultimo sub indice xq el valor final en python no cuenta.
# Pero esto no muestra el ultimo elemento. Para que lo hga podria hacer esto:
sublista = lista[2:6]
print(sublista)
print()
# O de esta otra manera:
# Dejar en blanco algunos de los subindices hace que se considere el extremo de la lista:
lista1 = [7,8,9,10,11,12]
lista2 = lista1[3: ] # Desde el 3 hasta el final
lista3 = lista1[ :3] # Desde el inicio hasta el 3
print(lista2) # 10, 11, 12
print(lista3) # 7, 8, 9 

print()
# Podemos poner 3 subindices en una rebanada. Al poner 3 el tercero funciona como incremento. El incremento predeterminado va de a 1(considerando todos uno alado del otro)
# Pero para ir salteando agregamos un incremento:
lista4 = [7,8,9,10,11,12,13,14]
sublista2 = lista4[1:6:2] # va del subindice 1 al 6 pero saltando de a 2
print(*sublista2) # 8 10 12

print()
# Incrementos negativos:
# Al poner un incremento negativo los subindices se toman de atras para adelante. Con esta tecnica podemos invertir una lista
original = [1,2,3,4,5]
invertida = original[ : :-1] #No tiene subindice de inicio ni final. Ante la ausencia de alguno de estos 2 se consideran los extremos: Vamos de inicio a fin es decir toda la lista.
# Al decirle que incremento es -1 nos queda todos los elementos en orden inverso. Crearemos una copia invertida de la lista original
print(invertida)
# No es lo mismo que usar reverse() xq esto crea una nueva lista, el reverse modifica la lista existente

print("Variables:")
# Las rebanadas tambien funcionan en variables. Podriamos usar subindices guardados en variables. 
lista5 = [1,2,3,4,5,6,7,8]
a = 3
b = 5
sublista3 = lista5[a:b+1] # Agregue mas uno para que tome el valor final
print(sublista3)

print()
# Rebanadas nulas: Rebanada que no agarra ningun elemento de la lista. Para crearlo utilizamos el mismo subindice como inicio y fin. El subindice final no esta incluido, recordar.
# Nos sirve para isnertar una lista adentro de otra en un determinado lugar. Si concatenamos una lista con otra, se agrega al final de la lista. 
# Y, para agregarle a una lista algunos elementos especificos de otra lista seria asi:
lista6 = ["a", "b", "c", "d"]
lista6[2:2] = ["X", "Y"] # La x y la y se agregarán en esas posiciones indicadas. Si pondria 2:3 estaria comiendo los lugares desde el 2 al 3 es decir que la C se eliminaria.
print(*lista6, sep=" - ")
# Aunque tambien se podria hacer, en vez de rebanadas nulas, con rebanadas comunes, concatenando porciones de la lista.