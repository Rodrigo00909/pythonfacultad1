### Break: Salir del while sin necesidad de que la condicion se vuelva falsa. Se escribe el break dentro de un if normalmente.
### Cuando usamos break a veces usamos else en un while. El Código de esta clausula solo se ejecuta si el ciclo while termino en forma normal, es decir sin usar el break osea
### xq su condicion se hizo falsa. Que termine de forma anormal seria que usemos el break xq su condicion sigue siendo true pero nosotros lo rompimos.

### DETERMINAR SI UN NUM ES PRIMO O NO (Osea cuando solo es divisible por si mismo y por 1). El numero 5 solo tiene como divisores al 5 y al 1. Es un primo.
## El numero 4 no, xq admite al 4, al 1 y al 2 como divisor

#### Para verificarlo buscamos que no tenga como divisor el mismo 1 o su mismo numero. Se comienza desde el 2 xq el 1 sabemos q es divisor que todos. Se comprueba hasta 1 menos que el numero
### O hasta la raiz cuadrada del mismo numero y seria lo mismo.

## Para probar si el numero 10 es primo comprobaremos los divisores entre 1 y 9. Encontraremos xq si NO primo pero el 11 si, por ejemplo.
n = int(input("Ingrese un num"))
divisor = 2
while divisor < n:
    if n % divisor == 0:
        print(n,"No es numero primo")
        break
    divisor = divisor + 1
else:
    print(n,"es un num primo")


    ## Imprimir los valores 1/x entre -3 y 3