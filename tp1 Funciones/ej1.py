# 1. Desarrollar una función que reciba tres números positivos y devuelva el mayor de
# los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. 
# No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el
# máximo hallado, o un mensaje informativo si éste no existe.
# Maximo estricto = Que sea el mas grande y unico

# Ejecutar solo 1 programa 
# Programa 1

def mayorPos(a,b,c):
    if a > b:
        if a > c:
            return a
    if b > a:
        if b > c:
            return b
    if c > a:
        if c > b:
            return c
    return -1

# Programa Principal
x = int(input("Ingrese un primer número: "))
y = int(input("Ingrese un segundo número: "))
z = int(input("Ingrese un tercer número: "))
if mayorPos == -1:
    print("No existe un mayor estricto")
else:
    print("El mayor es:",mayorPos(x,y,z))

# -----------------------------

# Programa 2

### Agregar la importancion de randint desde random
## Escribir un array que contenga los 3 numeros fecha. Recorrerlo agregandole la importacion random de randint, con rango de numeros 0 y 10
## Asignar los 3 numeros del array a algunas variables que luego seran trasladados como parametro a la funcion de mayor estricto.
## Agregar una validacion para que si el mayor es -1 entonces diga que no exista un mayor, en caso contrario que diga cual fue el mayor
from random import randint

def mayorEstr(a,b,c):
    if a > b:
        if a > c:
            return a
    if b > a:
        if b > c:
            return b
    if c > a:
        if c > b:
            return c
    return -1

def verificarFecha():
    fechas = []
    for i in range(3): # 3 xq son 3 numeros pos
        fechas.append(randint(0,10))
    a,b,c = fechas

    mayorEstricto = mayorEstr(a,b,c)

    print(fechas)
    if mayorEstricto == -1:
        print("No existe un mayor estricto")
    else:
        print(f"El mayor estricto es {mayorEstricto}")

# Programa Principal
verificarFecha()