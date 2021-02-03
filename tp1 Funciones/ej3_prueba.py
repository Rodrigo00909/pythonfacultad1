def calcularGastoSubte(viajes):
    if viajes<=20:
        gasto=viajes*19
    elif viajes>20 and viajes<=30:
        gasto=20*19+(viajes-20)*(19*0.8)
    elif viajes>30 and viajes<=40:
        gasto=20*19+10*(19*0.8)+(viajes-30)*(19*0.7)
    elif viajes>40:
        gasto=20*19+10*(19*0.8)+10*(19*0.7)+(viajes-40)*(19*0.6)
    return gasto

#Programa principal
v=int(input("Inserte cantidad de viajes realizados en el mes: "))
gasto=calcularGastoSubte(v)
print("El gasto mensual fue de %2.4f" %gasto)