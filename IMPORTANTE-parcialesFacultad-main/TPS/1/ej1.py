"""
1. Desarrollar una función que reciba tres números positivos y devuelva el mayor de
los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. 
No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, 
invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
"""

def calcularmayor(x, y, z):
    mayor = 0
    if x > y:
        if x > z:
            mayor = mayor + x
    if y > x:
        if y > z:
            mayor = mayor + y
    if z > x:
        if z > y:
            mayor = mayor + z
    if mayor > 0:
        return print(f"El numero {mayor} es el mayor")
    else:
        return print(f"No existe un número mayor")

#Programa Principal
n = int(input("Ingrese el primer número positivo: "))
n2 = int(input("Ingrese el segundo número positivo: "))
n3 = int(input("Ingrese el tercer número positivo: "))
calcularmayor(n,n2,n3)
    
