macaco = 0
print("Hola")

def myFuncion(parametro):
    """ Documentacion (docstring) """
    variable = parametro
    return print(variable)

nombre = input("Introduce: ")
myFuncion(nombre)

### Las funciones deben estar al inicio del programa. El programa principal debe comenzar despues de la ultima funcion. Este debe empezar con un comentario que lo identifique.
## Cada funcion deberia realizar una sola cosa. Ejemplo: El input que pida algo y el print no deben estar juntos en esta misma funcion.
## No deben leerse ni imprimirse valores dentro de una funcion que realice otra tarea. 
## No hay que salir de una funcion desde el interior de un ciclo. Es decir poner un return dentro de un if o un while. Para salir del ciclo primero ponemos el break y luego de que salimos
## del ciclo ponemos el return sin algun problema. Esto es xq el return sale del ciclo y del return xq retorna algo fuera de la funcion, El break solamente rompera el ciclo.

## La cadena de documentacion (docstring) no es obligatoria, debe especificar que hace la funcion pero no como lo hace. Es un breve resumen.


### Factoriales: Multiplicar todos los numeros enteros positivos de un numero y todos los que esten detras de el:
# Factorial de 4 = 4.3.2.1

def calcularfactorial(n):
    """ Devuelve el factorial de un numero entero positivo """
    fact = 1
    for i in range(1, n+1): ## El valor inicial 1 es para que no arranque desde 0 si no desde 1. El valor final es n+1 xq el valor final del range nunca esta incluido
        fact = fact * i ## Multiplicamos el fact por el i. I va a valer lo que devuelva el range: 1,2,3,4 etc. Vamos a multiplicar los valores fact partiendo de 1 por todos los valores a recorrer
    return fact

# Programa Principal
a = int(input("Ingrese un numero entero: "))
b = calcularfactorial(a)
print("El factorial es",b)


# Funciones incorporadas en python
# Abs() Valor Absoluto
# Len() longitud
# int() Convierte a numero entero
# float() Convierte a numero real
# range() define el rango