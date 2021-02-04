"""
3. Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. 
Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) 
se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento 
de la función.

Cantidad de viajes | Valor del pasaje
1 a 20             | Averiguar valor actualizado
21 a 30            | 20% de descuento sobre tarifa máxima
31 a 40            | 30% de descuento sobre tarifa máxima
Más de 40          | 40% de descuento sobre tarifa máxima
"""
def calculargasto(totalviajes):
    """ Recibe el total de viajes que el usuario hizo en el mes para realizar el calculo de su gasto total. Valor del viaje $19 """
    if totalviajes<=20:
        gastototal=totalviajes*19 # En esta variable se guarda el numero de viajes que realizó x 19 (valor del viaje)
    elif totalviajes>20 and totalviajes<=30:
        gastototal=20*19+(totalviajes-20)*(19*0.8) # El descuento es 0.8 porque es %20 y 1 - 0.2 es 0.8. 
        # Los primeros 20 viajes valen 19 (20*19). Resto a viajes -20 para saber si eran 27-28 o etc viajes
        # esta cantidad entre 20 y 30 se multiplica por 19*20% de descuento
    elif totalviajes>30 and totalviajes<=40:
        gastototal=20*19+10*(19*0.8)+(totalviajes-30)*(19*0.7)
    elif totalviajes>40:
        gastototal=20*19+10*(19*0.8)+10*(19*0.7)+(totalviajes-40)*(19*0.6)
    return gastototal

#Programa Principal
v=int(input("Ingrese la cantidad de viajes realizados en el mes: "))
gasto=calculargasto(v)
print("El gasto mensual fue de %2.4f" %gasto)