# 3. Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que 
# dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita 
# desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un
# determinado mes y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.

# Cantidad de viajes | Valor del pasaje
# 1 a 20            | Averiguar valor actualizado
# 21 a 30           | 20% de descuento sobre tarifa máxima
# 31 a 40           | 30% de descuento sobre tarifa máxima
# Más de 40         | 40% de descuento sobre tarifa máxima

def calcularGasto(v):
    gastos = 0
    if v <= 20:
        gastos = v*19
    elif v >= 21 and v <= 30:
        gastos = 20*19+(v-20)*(19*0.8)
    elif v >= 21 and v <= 40:
        gastos=20*19+10*(19*0.8)+(v-30)*(19*0.7)
    elif v <= 40:
        gastos=20*19+10*(19*0.8)+10*(19*0.7)+(v-40)*(19*0.6)
    return gastos

#Programa Principal
viajes = int(input("Introduzca el total de viajes realizados en el mes: "))
gastoTotal = calcularGasto(viajes)
print("El total de viajes fue: %2.3f"%gastoTotal)

## Primero realizar una funcion que calcule el gasto de los viajes. Esta recibira como parametro la cantidad de viajes realizados. Se comparará si viajes es menor o igual a 20, xq
## asi lo pide la consigna, se calculara tambien si es mayor que 21 pero menor o igual a 30, tambien se comparara lo mismo pero con 31 a 40, por ultimo se comparara si fueron mas de 40 viajes.
## se creara una varible para calcular los gastos dentro de esta misma funcion. Se le multiplicara por 19 ya que ese fue el valor actualizado del gasto de sube. 
## Esta multiplicacion se hará en el primer comparativo. Para el segundo se querra agregar a la variable de gastos el resultado de 20*19 + (viajes-20)*(19*0.8)
## para el prox sera gasto=20*19+10*(19*0.8)+(viajes-30)*(19*0.7), y para el prox gasto=20*19+10*(19*0.8)+10*(19*0.7)+(viajes-40)*(19*0.6)
## Se devolverá el gasto total
