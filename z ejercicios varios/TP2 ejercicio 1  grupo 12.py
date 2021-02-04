#ejercicio 1 opcion 2 tp2 grupo 12
import random

def generarlistarandom():
    """genera un numero al azar de dos digitos, que es usado como la cantidad de
     numeros que va a contener una lista de numeros al azar de 4 digitos"""
    listarandom = []
    cant = random.randint(10,99)
    for i in range(cant):
        listarandom.append(random.randint(1000,9999))
    return listarandom

def borrarlista (b,c):
    """Borra de la lista b, el elemento c"""
    cantborrar = b.count(c)
    for j in range(cantborrar):
        b.remove(c)
    return cantborrar

def verificacapicua (d):
    """verifica si una lista es capicua."""
    capicua = True
    for k in range(len(d)//2):
        if d[k] != d[(k*-1)-1]:
            capicua = False
            break
    return capicua

#Programa Principal
lista = generarlistarandom()
print("La lista generada es la siguiente: ")
print(lista)
sumatorialista = lambda x: sum(x)
print("Al sumar todos los elementos de la lista, se obtiene como resultado: ",sumatorialista(lista))
borrar = int(input("Ingrese un valor a eliminar o -1 para terminar: "))
while borrar != -1:
    numborrado = borrarlista(lista,borrar)
    if numborrado != 0:
        print("La lista sin el elemento",borrar,"quedo así: ")
        print(lista)
    else:
        print("El numero ingresado",borrar,"no se encontro en la lista")
    borrar = int(input("Ingrese otro valor a eliminar o -1 para terminar: "))
capi = verificacapicua(lista)
if capi:
    print("La lista es capicúa.")
else:
    print("La lista no es capicúa.")
print("La lista final será la siguiente: ")
print(lista)