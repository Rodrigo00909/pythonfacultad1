# Las listas pueden ser comparadas como cualquier otra variable:
# La comparacion se realiza ELEMENTO a ELEMENTO

lista1 = [2,3]
lista2 = [1,4]
if lista1 > lista2: # Como compara que el primer elemento de la lista 1 es 2 y el de la lista 2 es 1 ya sabe que la lista1 tiene un primer elemento mas grande entonces da true
    print(True) 
else:
    print(False)
lista3 = [2,3]
lista4 = [2,4]
if lista3 > lista4: # En este caso hay una igualdad en ambos primeros subindices, entonces pasa al segundo y le da la razon del mas grande a la lista 4
    print(True)
else:
    print(False)
lista5 = [2,4,6]
lista6 = [2,4]
if lista5 > lista6:
    print(True)
else:
    print(False)

# Copia de listas: Copiar una lista solo copia LA REFERENCIA AL OBJETO
listaa1 = [1,2,3]
listaa2 = listaa1
listaa2.append(4)
print(listaa1) # 1,2,3,4. El 4 yo se lo agregue a la lista 2 pero como esta es una referencia al objeto lista1 entonces tb se lo suma a la lista1.
#Ambas variables apuntan al mismo objeto en memoria. Una asignacion directa las dos representaran al mismo objeto.

# Si tenemos dudas de que pasa podemos utilizar la funcion id(<objeto>), en este caso el objeto que le pasaremos sera el nombre de la variable que contiene a nuestra lista.
# Devuelve la identidad del objeto y es equivalente a su direccion de memoria.
print(id(listaa1), id(listaa2)) # Daran exactamente el mismo ID 

# Para realizar una verdadera copia de la lista y evitando la caracteristica de la forma directa podemos hacer esto:
# Realizar la copia a traves de una rebanada:
listaa3 = [1,2,3]
listaNueva = listaa3[ : ] # Al no poner ningun subindice, es decir dejar un espacio, el sistema considera que va de inicio a fin es decir toda la lista.
listaNueva.append(4)
print(listaa3, listaNueva, sep=" / ")

# La segunda forma consiste en utilizar la funcion list().
# Si se lo aplicamos a algo iterable que no es una lista como por ejemplo range() lo convierte en lista
# pero al aplicarlo a algo que YA ES una lista conseguimos que se realice una veraddera copia y no una referencia:
listaa4 = [1,2,3]
listaNueva2 = list(listaa4)
listaNueva2.append(6)
print(listaa4, listaNueva2, sep=" / ")

# La otra forma es utilizar el metodo copy()
listaa5 = [1,2,3]
listaNueva3 = listaa5.copy()
listaNueva3.append(8)
print(listaa5, listaNueva3, sep=" / ")
print()
## USO DE FOR CON LISTAS: La instruccion for puede utilizarse para recorrer listas sin necesidad de range() ni de subindices, que debo usarlo en un while por ejemplo.
# En este caso la variable del for no utilizara valores correspondientes a subindices, los valores a recibir van a ser los propios elementos de la lista 
# Ejemplo:
vocales = ["a","e","i","o","u"]
for letra in vocales: #No hay range(), len() nada.
    print(letra, end=" ") # a e i o u
print()
# No neceistamos usar subindices ni range ni len.

# Usando estas cosas de range() y demas, si itero una lista y elimino un elemento me dara un error de rango. usando este metodo se solucionaria.
# Aunque lo mejor en vez de eliminar elementos en la primera: seria recorrer la primera y a medida que encuentro cosas que me interesan las guardo en una segunda lista o variable
# Por ejemplo eliminar elementos repetidos: Lo mejor es recorrer la lista y si encuentro un elemento UNICO lo agrego en una nueva lista auxiliar, sin modificar la primera.

# Borar de una lista de palabras las palabras q se encuentren en una segunda lista: UN TIP: Empezar de atras para adelante (con los numeros negativos) ya de esta manera
# No se corren los valores posteriores, es decir lo que se corre ya lo procese y no lo volvere a usar.

# Puede usarse una rebanada para recorrer la lista parcialmente.
vocales2 = ["a","e","i","o","u"]
for letra in vocales2[1:4]: # Para recorrer una lista en forma parcial es decir partir desde donde yo quiero usamos rebanadas: en este caso ira desde el subindice 1(e) hasta 4(u)
    # pero el ultimo valor no se toma en cuenta.
    print(letra, end=" ") # e i o

# Instruccion PASS: No sirve para nada, no ahce nada.
# Para que existe? puede usars en situaciones especiales para evitar errores de sintaxis. Ejemplo si escribimos una funcion pero todavia no sabemos su codigo es decir esta varia
# le ponemos un pass y no me dara error.
def calcularsalario(empleado):
    pass    

# NO USARLO EN IFs: ESTO BAJA PUNTOS
nota=5
recuperan = []
nombre = []
if nota >= 4:
    pass
else: 
    recuperan.append(nombre)

# Esto se podria escribir mejor, de otra forma: Planteando la segunda condicion en el if, y sin else. Osea preguntar al reves:
# Se pregunta si la nota es menor que 4, en ese caso se hace el recuperan.append(nombre) en el if, sin en else

# Funcion MAP: IMPORTANTE
# Nos permite aplicarle otra funcion a todos los elementos de una lista. Y con los resultados que vaya obteniendo construye una nueva lista
# Sintaxis: <lista2> = list(map(<funcion>, <lista1>))
# En este ejemplo: map tomara cada uno de los elementos de lista1 (su segundo parametro) y a cada uno de ellos le aplicará la funcion (primer parametro)
# Al aplicarle la funcion va a tener un resultado x cada elemento de la lista uno.  Y von todo este nuevo grupo de resultados los guarda en la lista2
print()
print()
# Ejemplo: 
numeros2 = [1,2,3,4]
raices = list(map(lambda x:x**(1/2), numeros2)) # Esta funcion calcula la raiz cuadrada de x ( si seria 1/3 seria raiz cubica). Es raiz xq tiene dos **
# Recordar que el parametro de lambda es la variable o lista que esta detras de la coma. 
# Map siempre va acompañado de list xq map no devuelve una lista si no un objeto map.
print(numeros2)
print(raices)

# Esto es lo mismo que hacer todo esto:
# numeros = [1,2,3,4]
# raices = []
# for i in numeros:
#     raices.append(i**(1/2))

# Funcion Filter(). Selecciona algunos elementos de una lista para crear una nueva lista con ellos.
# Los elementos de la lista original que se añaden a la nueva lsita son aquellos que devuelven True al aplicarles una funcion
# La diferencia entre map y filter es que en map podemos utilizar cualquier funcion q nos devuelva un resultado. La lista que nos construye map la arma con los resultados que
# nos devuelvio la funcion luego de ser aplicada a todos los elementos de la lista original. Pero con filter la funcion q le pasamos como parametro NO PUEDE ser cualquier funcion
# Debe ser una funcion q solo devuelva TRUE O FALSE. No puede deolver string, ni nada.
# Filter se queda solamente con los elementos de la lsita original que le devuelvan TRUE al aplicar la funcion. Con esto arma la lista final. Los que dieron false se descartan
# Por ejemplo si queiro los pares, me deja esos. Los otros no.
# Ejemplo:
print()
numeros3 = [0,1,2,3,4,5]
impares = list(filter(lambda x: x%2!=0, numeros3)) # Si el RESTO(%) de un numero X divido por 2 es DISTINTO a 0, de la lista numeros, lo guardo en impares
pares = list(filter(lambda x: x%2==0, numeros3))
print(impares) #[1,3,5] 
print(pares) 
print()


# Listas por comprension: son una manera matematica para crear listas que deriva de la teoria de Conjuntos.
numeraso = 6
cuadrados = [x**2 for x in range(numeraso+1)] #x se multiplica x la potencia de 2 desde el 0 hasta el 6. Obviamente el 6 no se toma en cuenta xq es el ultimo. Por eso el agrego +1
print(cuadrados) #0,1,4,9,16,25
# Sintaxis: <lista> = [<expr for <elem> in <secuencia>]
# la exprecion <expr> representa alguna operacion que se aplica a cada elemento <elem>(o variable) de <secuencia>(range, lista, etc.). El resultado de esta expresion se agregara a <lista> 
# Los corchetes son necesarios para crear la lista. La funcion list() tambien sirve, es decir: <lista> = list(<expr for <elem> in <secuencia>)
# Esto es muy parecido a MAP
print()
# A esta lista por comprension tambien podemos agregarle un IF q permita cuales elementos se agregan ala lista final par ano agregarlos todos.
# Ejemplo
cubospares = list(i**3 for i in range(11) if i**3 %2 == 0) # Potencia de 3 en cada i para cada i en el rango de 11(de 0 a 10). Luego, si la potencia de 3 en i es igual a 0 si lo divido x 2
# Entonces se agrega a la variable. Los demas no. Es decir agregue pares luego de potenciarlos por 3.
print(cubospares) #0,8,64,216......

# Map y filter pueden ser reemplazadas por listas de comprension.