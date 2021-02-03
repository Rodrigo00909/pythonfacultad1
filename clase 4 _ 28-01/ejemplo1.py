# Ejemeplo usando rebanadas
# Obtener sublistas con los primeros y ultimos N elementos  de una lista
# Vamos a crear a partir de un range una lista y luego pidiendole un numero al usuario extraemos esa cantidad de elementos tanto de la IZ como de la DER de la lista.

lista = list(range(10)) #Como range me deja en formato de rango lo convierto a lista. Dará 9 xq no toma el valor final
n = int(input("Cuantos elementos desea tomar: "))
comienzo = lista[ :n] # n elementos del comienzo # Comienzo es igual a la lista con 10 elementos con rebanada que ira desde el inicio hasta n (numero especificado x el usuario)
final = lista[-n: ] # n elementos del final # Comienza en -n (osea 2 negativo en caso de q el usuario puso 2 que en ese caso 10 es -1, 9 es -2 ) hasta el final de la lista
extremos = comienzo + final
print()
print("Lista original:",*lista)
print("Comienzo:",*comienzo)
print("Final:",*final )
print("Comienzo + final:",*extremos)
print("Comienzo y final pero mas bonito:",comienzo, final, sep="-")