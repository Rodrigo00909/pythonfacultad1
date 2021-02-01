## Las funciones lambda son funciones anonimas. Se escriben en una sola linea de código, guardandolas en una variable la cual siempre que no se pise se podrá volver a usar. 
cuadrado = lambda x: x**2
print(cuadrado(3)) # imprimira 9

# Es lo mismo que hacer esto:

def cuadrado2(x):
    return x**2

#Programa principal 
print(cuadrado2(3))

## Con 2 parametros:

raiz = lambda x,y: x**(1/y) ## **(1/x) es la raiz
a = raiz(25,2) ## En este caso será la raiz cuadrada de 25 osea devolvera 5
print(raiz(8,3)) # imprime 2 xq es la raiz cubica de 8