# Una cadena de caracteres (string) es un conjunto de 0 o mas caracteres.
# Las constantes de cadena de caracteres pueden encerrarse indistintamente entre comillas simples
# o dobles. p1 = "Lunes" p2 = 'Martes'
# Constantes en cadena: permite utilizar otro tipo de comillas dentro de la cadena
marca = "Mc. Donal´s"
frase = 'Dijo "ya voy" y ya partió'
# Si se utilizan 3 juegos de comillas la cadena retiene el formato dado por el programador y puede
# extenderse por múltiples líneas.

# Secuencias de escape: se utilizan para representar caracteres con significados especiales
# Toda secuencia de escape empieza con una barra invertida : \
# El carácter que se escriba despues de ella establece el significado de la secuencia de escape.

# Ejemplos:
# \n : Salto de linea
# \t : Tabulador
# \' : Comilla simple
# \" : Comilla doble
# \\ : Barra invertida
# \a : Campanilla

print("Lunes\nMartes\nMiércoles") # Lunes
                                    # Martes
                                    # Miércoles

# Cadenas crudas: (raw) se crean escribiendo la tecla r antes de abrir las comillas
ruta = r"c/nuevo/datos.txt"
# En cadena cruda no se interpretan las cadenas de escape

# Listas y cadenas: las cadenas de caracteres y las listas tienen muchas cosas en comun:
# pero tb algunas diferencias. Ambas son secuencias de elementos, es decir iterables que
# pueden ser recorridas por un for

# SIMULITUDES:
# se pueden acceder a cada elemento a traves de un subindice(base 0)
cad = "Lunes"
print(cad[2]) # n

# Tambien pueden manipularse mediante rebanadas:
#Referencia a cad lunes :
subcad = cad[1:3]
print(subcad) # un (0 es L, 1 es u, 2 es n, 3 es e, 4 es s. Pero solo llega hasta u xq el último no se toma en cuenta)

# Pueden ser concatenadas con el operador +
nom = input("Nombre ?: ")
saludo = "Bienvenido" + nom
print(saludo)

#Pueden replicarse mediante el operador *
risa = "ja"
print(risa*5) # jajajajaja

separador = "-" * 80

# Comparten muchas funciones y métodos:

# dia = "Lunes"
# len():print(len(dia)) # 5
# in: if "es" in dia: 
# not in: if "es" not in cad:

# cad2 = "Lunes"
# max(): print(max(cad2)) # u
# min(): print(min(cad2)) # L
# index(): print(cad2.index("es")) # 3
# count(): print(cad2.count("es")) # 1

# DIFERENCIAS: 
# Las listas son mutables, pero las cadenas son INMUTABLES

# Esto significa que no pueden ser modificadas.

# Las funciones y métodos para manipularlas devuelven una nueva cadena, sin alterar la original.

# Debido a que son inmutables, las cadenas carecen del método REVERSE() de las listas,
# Tampoco todos los elemetnos que trabajan in situ como append, pop, remove, clear, sort.

# Para invertir una cadena se puede utilizar la técncia de las rebanadas:
original = "Hola"
invertida = original[ : :-1] # aloH # No tiene subindice de inicio ni de fin pero tiene un incremento de -1 (tercer)
# lo que hace q nos devuelva una copia invertida de la cadena original, guardada en la var invertida
# Es decir con el primer espacio vacio le digo que la rebanada empieza en el subindice 0, al dejar vacio el segundo espacio
# le digo que la rebanada termina con el ultimo caracter de la cadena, y el tercer subindice -1 me dice q la tome
# de atras para adelatne

# Todo cambio que querramos hacer para trabajar sobre una cadena es creando una cadena nueva


## Comparaciones:
# Los strings se pueden comparar como cualquier otra variable. Se utiliza la comparacion ALFABETICA
# Es decir: La palabra que en un diccionario aparezca ANTES se considera MENOR. La que aparezca despues se considera la MAYOR
# Las MAYUSCULAS son MENORES que las MINUSCULAS

## Conversiones:
# No puedo hacer de forma directa la concatenacion un número dentro de un string. Es necesario convertir el numero a STRING
# Esto se consigue con la funcion str(). Sirve para convertir numeros a string y cualquier cosa a un string, hasta una LISTA.
c = 75
mensaje = "Precio: " +str(c) + "dólares"
print(mensaje) # Precio: 75 dólares

#Métodos que SIRVEN PARA TRABAJAR CON CADENAS. recordar q devuelven UNA CADENA NUEVA
# <str>.split([<sep>]): Sirve para particionar o dividir un string en distintos elementos. Sirve para separar las palabras por ejemplo. Le aplicamos el metodo split a la cadena 
# que queremos particionar y le pasamos el caracter que queremos usar como divisor osea el caracter q nos particiona la cadena. En otras palabras,
# Divide <str> en una lista de cadenas, buscando <sep> como separador. Si <sep> se omite, se asumenen los espacios:
frase = "Hola Mundo"
lista = frase.split() # ['Hola', 'Mundo']
fecha = "21/9/2020"
d,m,a = fecha.split('/') 

# Ejemplo: Lo que esta bien:
ola = "Hola   Mundo" #3 espacios
lista1 = ola.split()
print(lista1)
#Lo que está mal:
lista2 = ola.split(' ')
print(lista2) # [Hola, , , Mundo]

#Método join: hace lo contrario que split: construye una nueva cadena a partir de una lista o de un string => <sep>.join(<secuencia>):
# Devuelve un string con los elementos de <secuencia> separados por <sep>. La secuencia puede ser una cadenao una lista de cadenas.
dias = ["lunes", "martes", "jueves"]
dias2 = '-'.join(dias)
print(dias2) #lunes - martes -jueves
# Se le aplica a un separador, no a una variable. La variable se la pasa como parametro.

#Método replace: <str>replace(<vie>,<nue>,[<max>]): 
# Devuelve una cadena neuva reemplazando todas las apariciones de <vie> por <nue>, hasta un máximo de <max> reemplazados. Este último parametro es opcional.
# Si se omite se reemplazantodas las apariciones. No da error si <vie> no existe.
# Entonces, busca la cadena vieja y la reeemplaza por una cadena nueva. El tercer parametro tiene que ser un numero o variable numerica, indica el maximo numero de reemplazos
# que se van a realizar, si no lo ponemos se reemplazan todas las apariciones q se encuentren.
#ejemplo: 
a = "Hoy es un día frío, que frío está!"
b = a.replace("frío", "húmedo") # Reemplazamos frio por húmero, como no hay tercer parametro reemplaza las dos veces q encontro frio
print(b) # Hoy es un día húmero, que húmedo está!
c = a.replace("frío", "húmedo", 1) # Reemplazamos frio por humedo, pero como hay parametro de 1 solo reemplazara el primero q encuentre y nada mas.
print(c) # Hoy es un día húmero, que frío está!

# Copia de cadenas: Siempre copia su referencia - es decir su dirección de memoria - sin importar la técnica que se utilice.
# Esto se relaciona con la copia de listas: Copiar una lista de forma directa lista1 = lista2 no copia nada, solamente crea dos variables que apuntan al mismo objeto en memoria.
# Pero para solucionar eso usabamos algunos trucos para realizar una verdadera copia como la funcion list(), método copy() o usar rebanadas.
# Para string sea lo que sea que hagamos para realizar una verdadera copia no se podrá logar. 
a = "Hola" 
b = a # Copia directa
c = a[ : ] # Copia a traves de una rebanada
d = str(a) # Copia utilizando funcion str() / con lista utilizabamos list
e = a + "" # Concatenar una cadena vacia para ver si sirve
## Cómo saber cuantas variables tuvieron exito o solamente tenemos disintas variables pero con igual referencia?
for i in map(id, [a,b,c,d,e]): # para saberlo usamos la funcion ID que es la funcion q devuelve un número q representa la ubicación de la variable dentro de la memoria.
    # Para no hacer 5 print usamos una mejor tecnica. El for tb sirve para recorrer objetos map sin necesidad de pasarlos a lista. 
    # map aplicaba una funcion a los elementos de una lista. La funcion a aplicar en este caso será ID y la lista la construyo ahi mismo (lista implicita xq no se guarda en una variable)
    # y esta lista contiene el nombre de las 5 varaibles para averiguar su id. Con un for le aplicará el map id a cada uno de esas 5 variables
    # Dara un númeroe igual para las 5 variables. 
    print(i)
# Entonces no pudimos crear una verdadera copia de un string. Esto python lo hace para ahorrar memoria. 
# Esto se debe a que las cadenas son inmutables, por lo que crear copias idénticas sólo desperdiciaría memoria.
