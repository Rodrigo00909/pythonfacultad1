## Uso de parametros por omisión:
# Escribir una función para calcular la raiz n-ésima de un número

def calcularRaiz(radicando, indice=2):
    return radicando ** (1/indice)

#Programa Principal

a = float(input("Ingrese el radicando: "))
r2 = calcularRaiz(a)
r3 = calcularRaiz(a, 3) # Dara error xq ya tengo un indice x defecto
print("Raiz cuadrada:",r2)
print("Raiz cúbica:",r3)