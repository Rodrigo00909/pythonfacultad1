"""
9. Resolver el siguiente problema diseñando y utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso para poder cargar el camión de reparto.

La empresa cuenta con N camiones, y cada uno puede transportar hasta media tonelada (500 kilogramos).

En un cajón caben 100 naranjas con un peso entre 200 y 300 gramos cada una.

Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como jugo. 

Se solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas 
e informar cuántos cajones se pueden llenar, cuántas naranjas son para jugo y
si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto. 

Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.

Además, se desea saber cuántos camiones se necesitan para transportar la cosecha,
considerando que la ocupación del camión no debe ser inferior al 80%;
en caso contrario el camión no serán despachado por su alto costo.

"""

import random

#Definición de Funciones

def esJugo(peso_naranja):
    if 200<peso_naranja<300:
        return False
    else:
        return True

def cant_cajones(total_a_cajon):
    cajones = 0
    if total_a_cajon >= 100:
        cajones = total_a_cajon // 100
    return cajones
       
def cant_remanentes(total_a_cajon):
    remanentes = 0
    if total_a_cajon > 100:
        remanentes = total_a_cajon % 100
    else:
        remanentes = total_a_cajon

    return remanentes

def cant_camiones(peso):
    cantidad = 0
    peso_maximo_camion = 500 * 1000
    peso_minimo_camion = peso_maximo_camion * 0.8

    while peso >= peso_maximo_camion:
        cantidad += 1
        peso -= peso_maximo_camion
    if peso >= peso_minimo_camion:
        cantidad += 1
    return cantidad

#Programa General

cant_naranjas=int(input("Ingresar la cantidad de naranjas cosechadas:"))
while cant_naranjas < 0:
    cant_naranjas=int(input("Error, el valor no puede ser negativo. Favor de ingresar la cantidad de naranjas cosechadas:"))

total_a_cajon = 0
total_a_jugo = 0
peso_total = 0 
a_cajon = 0
maximo_por_cajon = 100
peso = 0
for i in range(cant_naranjas):
        
    naranja=random.randint(150,350)
   
    if esJugo(naranja):
        total_a_jugo = total_a_jugo + 1
    else:
        total_a_cajon += 1 
        a_cajon +=1
        peso_total += naranja
        if a_cajon == maximo_por_cajon:
            a_cajon = 0 
            peso += peso_total
            peso_total = 0
print("La cantidad de naranjas a cajon son:",total_a_cajon)
print("La cantidad de naranjas a jugo son:",total_a_jugo)
print("La cantidad de cajones es:",cant_cajones(total_a_cajon))
print("La cantidad de remanentes que no entran en cajones pero no son jugo, son:",cant_remanentes(total_a_cajon))
print("La cantidad de camiones es:",cant_camiones(peso))